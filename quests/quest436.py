
def check_command(pattern, command):
    result = []
    if len(command) < len(list(format(pattern, '0%ib' % len(command)))):
        return False
    for i, item in enumerate(list(command)):
        if list(format(pattern, '0%ib' % len(command)))[i] == str(1):
            if item.isdigit():
                return False
            else:
                result.append(True)
        if list(format(pattern, '0%ib' % len(command)))[i] == str(0):
            if not item.isdigit():
                return False
            else:
                result.append(True)
    return all(result)
