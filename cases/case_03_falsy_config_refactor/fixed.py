def effective_settings(defaults: dict, user: dict) -> dict:
    """Preserve explicit user values, including valid falsy values."""
    return {
        key: user[key] if key in user else default_value
        for key, default_value in defaults.items()
    }
