from state import log_messages

def update_log_widget(widget):
    widget.config(state="normal")
    widget.delete("1.0", "end")
    widget.insert("end", "\n".join(log_messages[-300:]))
    widget.see("end")
    widget.config(state="disabled")

def log(msg, widget=None):
    log_messages.append(msg)
    if len(log_messages) > 300:
        log_messages.pop(0)
    if widget:
        update_log_widget(widget)
