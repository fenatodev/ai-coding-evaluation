ALLOWED_TOOLS = {"read_file", "search_repo"}


def is_allowed(tool_name: str) -> bool:
    return tool_name in ALLOWED_TOOLS
