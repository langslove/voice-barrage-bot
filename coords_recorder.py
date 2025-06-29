import threading
import pyautogui
import keyboard
from tkinter import messagebox
from config import save_coords
from utils import log

def record_coords_flow(current_account, coords, log_widget, update_display_callback):
    acc = current_account.get()
    if not acc:
        messagebox.showerror("错误", "请先添加小号")
        return
    coords[acc] = {}
    steps = [
        ("请将鼠标移至『评论入口按钮』，按空格", "comment_button"),
        ("请移至『输入框』，按空格", "input_box"),
        ("请移至『发送按钮』，按空格", "send_button")
    ]

    def step(index):
        if index >= len(steps):
            save_coords(coords)
            update_display_callback()
            log(f"[录制完成] {acc} 坐标已保存", log_widget)
            return
        msg, key = steps[index]
        messagebox.showinfo("录制坐标", msg)
        keyboard.wait("space")
        coords[acc][key] = list(pyautogui.position())
        step(index + 1)

    threading.Thread(target=lambda: step(0), daemon=True).start()
