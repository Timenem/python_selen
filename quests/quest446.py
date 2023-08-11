import inspect
def check_generator(gen):
    state = inspect.getgeneratorstate(gen)
    if state == "GEN_CREATED":
        return "Created"
    elif state == "GEN_SUSPENDED":
        return "Started"
    else:
        return "Finished"
