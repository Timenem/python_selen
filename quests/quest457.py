
class Class:
    counter = 0
    @staticmethod
    def get_number():
        if Class.counter == 0:
            Class.counter =1
            return Class.counter
        else:
            Class.counter *=2
            return Class.counter
