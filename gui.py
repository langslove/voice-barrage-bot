import tkinter as tk
from tkinter import simpledialog, ttk
from config import load_keywords, load_coords, save_keywords, save_coords
from state import current_account, round_robin_enabled
from voice_listener import toggle_listen
from dispatcher import send_message, send_to_all
from coords_recorder import record_coords_flow
from utils import log

# 所有 GUI 控件创建 + 事件绑定逻辑
def start_gui():
    root = tk.Tk()
    root.title("直播间多小号弹幕工具")
    root.geometry("700x750")

    # === 数据 ===
    keywords = load_keywords()
    coords = load_coords()

    # === 日志区域 ===
    log_box = tk.Text(root, height=12, state=tk.DISABLED, bg="#111", fg="#0f0")
    ...

    # === 各模块初始化 + 按钮绑定 ===
    # 包括 toggle_listen(...), send_to_all(...), record_coords_flow(...), add_account() 等

    root.mainloop()
