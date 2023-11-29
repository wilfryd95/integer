class IntegerList:
    def __init__(self):
        self.list = []

    def add_integer(self, num):
        if not isinstance(num, int):
            raise TypeError("Only integers are allowed")
        self.list.append(num)

    def remove_integer(self, num):
        self.list.remove(num)

    def get_average(self):
        if not self.list:
            raise ValueError("List is empty")
        return sum(self.list) / len(self.list)

    def get_max(self):
        return max(self.list)

    def get_min(self):
        return min(self.list)
