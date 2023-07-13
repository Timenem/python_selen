def show_me(instance):
    class_name = instance.__class__.__name__+'s'
    sorted_args = sorted(list(instance.__dict__.keys()))
    if len(sorted_args) == 1 :
        return f"Hi, I'm one of those {class_name}! Have a look at my {sorted_args[0]}."
    else:
        args = ", ".join(sorted_args[:-1])
        last_arg = sorted_args[-1]
        return (f"Hi, I'm one of those {class_name}! Have a look at my {args} and {last_arg}.")
