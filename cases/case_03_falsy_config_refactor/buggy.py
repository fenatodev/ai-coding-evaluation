def effective_settings(defaults: dict, user: dict) -> dict:
    """Concise refactor generated from a more explicit merge.

    BUG: using "or" treats valid falsy values as missing.
    """
    return {
        key: user.get(key) or default_value
        for key, default_value in defaults.items()
    }
