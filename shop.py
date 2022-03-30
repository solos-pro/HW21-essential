from storage import Storage


class Shop(Storage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add(self, name, count):
        if self.get_unique_items_count() < self.capacity:
            super().add(name, count)
        else:
            print("Товар не может быть добавлен")
    
