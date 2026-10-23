from threading import local


class BrowserInstance:
    _thread_state = local()

    def __new__(cls):
        instances = getattr(cls._thread_state, "instances", None)
        if instances is None:
            instances = {}
            cls._thread_state.instances = instances

        if cls not in instances:
            instances[cls] = super().__new__(cls)
        return instances[cls]
