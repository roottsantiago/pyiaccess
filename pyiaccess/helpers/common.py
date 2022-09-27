
def generic_error(fn):
    """
    Decorator for connection and error handling.
    """
    def func_wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            error = f"Connection error: {e}"
            raise error

    return func_wrapper
