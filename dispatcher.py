import time, pyautogui, pyperclip, random
from utils import log

def send_message(account, coords, text, log_widget=None):
    if account not in coords:
        log(f"[错误] 小号“{account}”未配置坐标", log_widget)
        return
    c = coords[account]
    try:
        pyautogui.click(c["comment_button"])
        time.sleep(0.5)
        pyautogui.click(c["input_box"])
        pyperclip.copy(text)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.3)
        pyautogui.click(c["send_button"])
        log(f"[发送] {account} 发出：{text}", log_widget)
    except Exception as e:
        log(f"[失败] {account} 发送失败：{e}", log_widget)

def send_to_all(text, coords, log_widget=None):
    for acc in coords:
        send_message(acc, coords, text, log_widget)
        time.sleep(random.uniform(0.8, 1.5))
