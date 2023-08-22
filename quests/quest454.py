
def hypertensive(patients):
    count = 0
    for patient in patients:
        sistolic = [int(a.split('/')[0]) for a in patient]
        diastolic = [int(a.split('/')[1]) for a in patient]
        if len(sistolic) >= 2 and sum(sistolic) / len(sistolic) >= 140:
            count += 1
        elif len(diastolic) >= 2 and sum(diastolic) / len(diastolic) >= 90:
            count += 1
        elif any(x >= 180 and y >= 110 for x, y in zip(sistolic, diastolic)):
            count += 1
    return count
