from storage import Storage


class Shop(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 5
