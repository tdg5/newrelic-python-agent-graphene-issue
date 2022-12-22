from threading import Lock


ENV_LOCK = Lock()


# A decorator to wrap a test function that should be used to ensure that
# multiple tests don't mutate the environment concurrently.
def env_mutator(thunk):
    def wrapper():
        with ENV_LOCK:
            thunk()

    return wrapper
