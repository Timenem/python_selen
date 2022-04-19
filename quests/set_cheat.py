

engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}
# who is a manager and engineer
print(engineers & managers)

# all employees in both categories
print(engineers | managers)

# engineers who are not managers
print(engineers - managers)

# intersection
print((engineers | managers) - (managers ^ engineers))
