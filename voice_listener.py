import speech_recognition as sr
import threading
from dispatcher import send_message, send_to_all
from state import current_account, round_robin_enabled
from utils import log

listening = False

def listen_thread(keywords, coords, log_widget):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while listening:
            try:
                audio = r.listen(source)
                said = r.recognize_google(audio, language="zh-CN")
                log(f"[识别] 你说了：{said}", log_widget)
                for item in keywords:
                    if item["keyword"] in said:
                        if round_robin_enabled.get():
                            send_to_all(item["response"], coords, log_widget)
                        else:
                            send_message(current_account.get(), coords, item["response"], log_widget)
                        break
            except Exception as e:
                log(f"[识别失败] {e}", log_widget)

def toggle_listen(keywords, coords, button, log_widget):
    global listening
    if not listening:
        listening = True
        threading.Thread(target=listen_thread, args=(keywords, coords, log_widget), daemon=True).start()
        button.config(text="停止监听")
    else:
        listening = False
        button.config(text="开始监听")

        listening = False
        button.config(text="开始监听")
