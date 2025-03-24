import requests
import schedule
import time
import os

# API Chatwork
API_TOKEN = "506c4076258b499cace5603ecba1a410"
ROOM_ID = "380291120"
USER_ID = "1452981"  # ID người dùng cần mention

# Đọc tin nhắn từ file
def get_message():
    if os.path.exists("message.txt"):
        with open("message.txt", "r", encoding="utf-8") as file:
            message = file.read().strip()
            return message if message else None 
    return None

# Gửi tin nhắn nếu có nội dung
def send_message():
    MESSAGE = get_message()
    if MESSAGE:
        headers = {"X-ChatWorkToken": API_TOKEN}
        params = {"body": MESSAGE}
        
        response = requests.post(f"https://api.chatwork.com/v2/rooms/{ROOM_ID}/messages",
                                 headers=headers, params=params)
        print(f"Đã gửi: {MESSAGE}")
        print(response.json())
    else:
        print("Không có tin nhắn để gửi hôm nay.")

schedule.every().day.at("04:55").do(send_message)

print("Bot Chatwork đang chạy...")
while True:
    schedule.run_pending()
    time.sleep(60)
