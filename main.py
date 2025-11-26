from yt_dlp import YoutubeDL;from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mark
import telebot;import os
class Main():
    def __init__(self,url) -> None:
        self.url = url
    def downloader(self) -> dict:
        try:
            with YoutubeDL() as ydl:
                    info = ydl.extract_info(self.url, download=True) 
                    path = ydl.prepare_filename(info)        
            return {"data":{"message":"Download Successful","path":path},"status":200}
        except:
            return {"data":{"message":"Download Failed"},"status":500}
try:
    Java = telebot.TeleBot(input("Enter Token :"))
except:
    exit("Invalid Token")
@Java.message_handler(commands=['start'])
def start(message):
    n1 = btn("Channel",url="https://t.me/+AMfX2TBw2q42ODg9")
    q = mark().add(n1)
    Java.reply_to(message,"<Strong> ها دز رابط فيديو وحملك  </Strong>",reply_markup=q,parse_mode="HTML")
@Java.message_handler(func=lambda message: True)
def echo(message):
    back = btn("Back",callback_data="back")
    url = message.text
    res = Main(url).downloader()
    if res["status"] == 200:
        video = open(res["data"]["path"],'rb')
        Java.send_video(message.chat.id,video,caption="عوذبله",reply_markup=mark().add(back))
        os.remove(res["data"]["path"])
    else:
        Java.reply_to(message,"error",reply_markup=mark().add(back))
@Java.callback_query_handler(func=lambda call: call.data == "back")
def back(call):
    n1 = btn("Channel", url="https://t.me/+AMfX2TBw2q42ODg9")
    q = mark().add(n1)
    msg = call.message
    Java.edit_message_caption(chat_id=msg.chat.id,message_id=msg.id,caption="<strong> ها دز رابط فيديو وحملك </strong>",reply_markup=q,parse_mode="HTML")
Java.set_my_commands([telebot.types.BotCommand("/start","Start Bot")])
Java.infinity_polling()
#غير مسول عن استخدام خاطى 
