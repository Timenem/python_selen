def count_smileys(arr):
    smileys = []
    for smile in arr:
        if len(smile) == 2 and smile[0] in [":", ";"] and smile[-1] in [")", "D"]:
            smileys.append(smile)
        elif len(smile) > 2 and smile[0] in [":", ";"] and smile[1] in ["-", "~"] and smile[-1] in [")", "D"]:
            smileys.append(smile)
    return len(smileys)
