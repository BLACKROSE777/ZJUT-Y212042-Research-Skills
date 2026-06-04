from openclaw import taskflow

@taskflow.task(name="paper_analysis_listener")
def listener(msg_text, chat_id):
    """
    接收 Telegram 消息，调用 paper-analysis-skill 并回传结果
    """
    from openclaw.skills import run_skill

    result = run_skill("paper-analysis-skill", msg_text)
    # result 可能是 dict，需要取 'result' 或自定义字段
    taskflow.send_telegram_message(chat_id, result.get("result", str(result)))

# 注册 Telegram listener，捕获所有文本消息
taskflow.register_telegram_listener(
    task="paper_analysis_listener",
    pattern=".*"
)