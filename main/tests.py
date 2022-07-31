import json
import requests
from .views import BOT_TOKEN
# Create sendMessage url
bottoken = "94924.............."
url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"

# Create keyboard, convert dic to json with json.dumps
kb=json.dumps(
    { "inline_keyboard":
        [
            [
                { "text": "Yes", "callback_data": "x" },
                { "text": "No", "callback_data": "x" }
            ]
        ]
    }
)

# Create data dict
data = {
    'text': (None, 'Hi!'),
    'chat_id': (None, 739412274),
    'parse_mode': (None, 'Markdown'),
    'reply_markup': (None, kb )
}

# Send
res=requests.post(url=url, headers={}, files=data)
print(res.text.encode('utf8'))