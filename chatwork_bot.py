# import requests
# import schedule
# import time

# API_TOKEN = "506c4076258b499cace5603ecba1a410"
# ROOM_ID = "380291120"

# def send_message():
#     MESSAGE = "Chào buổi sáng! Tin nhắn tự động từ bot. ☀️"
#     headers = {"X-ChatWorkToken": API_TOKEN}
#     params = {"body": MESSAGE}

#     response = requests.post(f"https://api.chatwork.com/v2/rooms/380291120/messages",
#                              headers=headers, params=params)
#     print(response.json()) 

# schedule.every().day.at("09:00").do(send_message)

# print("Bot Chatwork đang chạy...")
# while True:
#     schedule.run_pending()
#     time.sleep(60)  



import requests
import schedule
import time
import os

# API Chatwork
API_TOKEN = "506c4076258b499cace5603ecba1a410"
ROOM_ID = "380291120"

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

schedule.every().day.at("09:00").do(send_message)

print("Bot Chatwork đang chạy...")
while True:
    schedule.run_pending()
    time.sleep(60)
