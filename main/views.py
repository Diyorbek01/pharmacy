import requests
import json
from django.shortcuts import render
from .models import User, Order, Status
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import Deliverer
from django.db.models import Q

BOT_TOKEN = "1996819753:AAFRIWviAYPipVuEn9UtJgULADiHwCV5YiY"
URL = f"https://api.telegram.org/file/bot{BOT_TOKEN}/"
GET_PATH_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id="
SEND_MESSAGE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?"


# Create your views here.

def send_message(status, tg_id):
    status_name = Status.objects.get(id=status)
    message = f"Sizning buyurtmangiz holati \n{status_name.name.capitalize()} ga o'zgartirildi!"
    url = f"{SEND_MESSAGE_URL}text={message}&chat_id={tg_id}"
    response = requests.request("GET", url)
    res = response.json()
    return res


def send_message_deliverer(status,order_id, tg_id):
    print(status, tg_id)
    status_name = Status.objects.get(id=status)
    last_status = Status.objects.all().last()
    all_status = Status.objects.filter(~Q(id=status))
    url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"
    kb = json.dumps(
        {"inline_keyboard":
            [
                [

                    {"text": s.name, "callback_data": f'{s.id}-{order_id}-{last_status.id}'} for s in all_status
                ]
            ]
        }
    )

    # Create data dict
    data = {
        'text': (None, f'Sizga buyurtma berildi. Holati: \n {status_name.name}'),
        'chat_id': (None, tg_id),
        'parse_mode': (None, 'Markdown'),
        'reply_markup': (None, kb)
    }

    # Send
    res = requests.post(url=url, headers={}, files=data)
    return res


@login_required(login_url='/login')
def index(request):
    status = Status.objects.all()
    number_clients = User.objects.all().count()
    number_deliverer = Deliverer.objects.all().count()
    number_orders = Order.objects.all().count()

    context = {
        "status": status,
        "number_clients": number_clients,
        "number_deliverer": number_deliverer,
        "number_orders": number_orders,
    }
    return render(request, 'index.html', context)


@login_required(login_url='/login')
def order_list(request):
    order = Order.objects.all().order_by("-id")
    deliverer = Deliverer.objects.all()
    status = Status.objects.all()
    context = {
        "orders": order,
        "status": status,
        "url": URL,
        "deliverer": deliverer,
    }
    return render(request, 'order-list.html', context)


@login_required(login_url='/login')
def filter_order(request, id):
    orders = Order.objects.all().order_by("-id")
    print(id)
    if id.split('-')[-1] == "status":
        status_id = id.split('-')[0]
        order_id = id.split('-')[1]
        order = Order.objects.get(id=order_id)
        order.status_id = status_id
        order.save()

        send_message(order.status_id, order.user.tg_id)  # Send message telegram bot

        return redirect("/order-list")

    elif id.split('-')[-1] == "deliverer":
        deliverer_username = id.split('-')[0]
        order_id = id.split('-')[1]
        order = Order.objects.get(id=order_id)
        deliverer = Deliverer.objects.get(username=deliverer_username)
        order.deliverer = deliverer
        order.save()
        send_message_deliverer(order.status_id, order.id, order.deliverer.tg_id)  # Send message telegram bot
        return redirect("/order-list")

    elif int(id) != 0:
        status_id = Status.objects.get(id=id)
        orders = Order.objects.filter(status=status_id.id).order_by("-id")
    else:
        orders = Order.objects.all().order_by("-id")
    status = Status.objects.all()
    deliverer = Deliverer.objects.all()
    context = {
        "orders": orders,
        "status": status,
        "status_id": int(id),
        "url": URL,
        "deliverer": deliverer,
    }
    return render(request, 'order-list.html', context)


@login_required(login_url='/login')
def price(request):
    if request.method == "POST":
        price = request.POST['price']
        id = request.POST['id']

        order = Order.objects.get(id=id)
        if int(price) != 0:
            order.price = price
            order.save()

        return redirect("/order-list")


@login_required(login_url='/login')
def status(request):
    if request.method == "POST":
        name = request.POST['name']
        status = Status.objects.create(
            name=name
        )

    status = Status.objects.all().order_by("-created_at")

    context = {
        "status": status
    }
    return render(request, 'create-status.html', context)


@login_required(login_url='/login')
def delete_status(request, id):
    user = Status.objects.get(id=id).delete()
    return redirect("/create-status")


@login_required(login_url='/login')
def user_list(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, 'user-list.html', context)


@login_required(login_url='/login')
def deliverer_list(request):
    users = Deliverer.objects.all()
    context = {
        "users": users
    }
    return render(request, 'deliverer-list.html', context)


@login_required(login_url='/login')
def deliverer_status(request):
    if request.method == "POST":
        print(request.POST)

    return redirect("/order-list")


@login_required(login_url='/login')
def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        tg_id = request.POST['tg_id']
        user_instance = Deliverer.objects.create(
            full_name=name,
            tg_id=tg_id,
            phone_number=phone_number,
        )
        return redirect("/deliverer-list")
    return render(request, 'create-user.html')


@login_required(login_url='/login')
def update_user(request, id):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        tg_id = request.POST['tg_id']

        user = User.objects.get(username=id)
        user.name = name
        user.phone_number = phone_number
        user.tg_id = tg_id
        user.save()
        return redirect('/deliverer-list')
    else:
        user = User.objects.get(username=id)
        return render(request, "update-user.html", {"users": user})


@login_required(login_url='/login')
def delete_user(request, id):
    user = Deliverer.objects.get(username=id).delete()
    return redirect("/deliverer-list")


@login_required(login_url='/login')
def user_location(request, id):
    user = User.objects.get(username=id)
    print(user.lat, user.long)
    context = {
        "lat": float(user.lat),
        "long": float(user.long),
    }
    return render(request, 'user-location.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            print("aa")
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, "Login yoki parol xato!")
                return redirect('/login')
        except:
            print("except")
            messages.info(request, "Login yoki parol xato!")
            return redirect('/login')
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('/login')
