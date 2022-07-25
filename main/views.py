from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def order_list(request):
    return render(request, 'order-list.html')
def user_list(request):
    return render(request, 'user-list.html')
def deliverer_list(request):
    return render(request, 'deliverer-list.html')
def create_user(request):
    return render(request, 'create-user.html')
