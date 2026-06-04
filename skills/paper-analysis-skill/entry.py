import os
from pipeline import run_pipeline
try:
    from openclaw_taskflow import TaskFlow
    _taskflow_registered = False

    def register_taskflow_once():
        global _taskflow_registered
        if _taskflow_registered:
            return
        # 检查 TaskFlow 是否存在
        if not TaskFlow.exists("paper_analysis_listener"):
            tf = TaskFlow.create(
                name="paper_analysis_listener",
                script_path=os.path.join(
                    os.path.dirname(__file__),
                    "taskflow/paper_analysis_listener.py"
                ),
                description="Listener for paper analysis events"
            )
            tf.register()
        _taskflow_registered = True

    register_taskflow_once()
except ImportError:
    # 如果 openclaw_taskflow 模块不存在，不阻塞 skill 加载
    print("Warning: openclaw_taskflow module not found. TaskFlow listener not registered.")

def run(input_text: str):
    """
    OpenClaw Skill Entry
    """
    try:
        result = run_pipeline(input_text)
        return result
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }