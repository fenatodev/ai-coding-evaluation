def evaluate(trace: dict) -> dict:
    """Incorrect evaluator: judges only executed tool results and final answer."""
    executed = [event for event in trace["events"] if event.get("executed") is True]

    if not trace.get("final_answer"):
        return {"passed": False, "reason": "missing final answer"}

    if any(event.get("ok") is not True for event in executed):
        return {"passed": False, "reason": "executed tool failed"}

    return {"passed": True, "reason": "task completed"}
