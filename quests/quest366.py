
def to_pretty(seconds):
    if seconds == 0:
        return "just now"
    elif seconds == 1:
        return "a second ago"
    elif seconds == 60:
        return f"a minute ago" 
    elif seconds == 3600:
        return f"an hour ago"
    elif seconds == 86400:
        return f"a day ago"
    elif seconds == 604800:
        return f"a week ago"
    elif seconds < 60:
        return f"{seconds} seconds ago"
    elif 3600 > seconds > 60:
        x = seconds / 60
        if int(x) == 1:
            return f"a minute ago"
        return f"{int(x)} minutes ago"
    elif 3600 < seconds < 86400:
        x = seconds / 3600
        if int(x) == 1:
            return f"an hour ago"
        return f"{int(x)} hours ago"
    elif 86400 < seconds < 604800:
        x = seconds / 86400
        if int(x) == 1:
            return f"a day ago"
        return f"{int(x)} days ago"
    elif seconds > 604800: 
        x = seconds / 604800
        if int(x) == 1: 
            return f"a week ago"
        return f"{int(x)} weeks ago"
