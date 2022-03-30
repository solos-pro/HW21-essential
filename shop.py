from storage import Storage


class Shop(Storage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.items = {}
        # self.capacity = capacity
        # self.limit = limit

    def add(self, name, count):
        if self.get_unique_items_count() < self.capacity:
            super().add(name, count)
        else:
            print("Товар не может быть добавлен")
    


# shop = Shop()
# # store = Storage("gingerbread", 5)
# shop.add("gingerbread", 4)
# print(shop.items)
# print(shop.get_free_space())
# shop.add("gingerbread", 6)
# print(shop.items)
# shop.add("apple", 7)
# print(shop.items)
# shop.get_items()
# print(shop.remove("apple", 7))
# print(shop.items)
# shop.get_unique_items_count()
