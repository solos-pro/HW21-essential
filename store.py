from storage import Storage


class Store(Storage):
    def __init__(self, items={}):
        super().__init__()
        # self.items = {}
        # self.capacity = 100







# store = Store()
# # store = Storage("gingerbread", 5)
# store.add("gingerbread", 4)
# print(store.items)
# print(store.get_free_space())
# store.add("gingerbread", 6)
# print(store.items)
# store.add("apple", 7)
# print(store.items)
# store.get_items()
# print(store.remove("apple", 7))
# print(store.items)
# store.get_unique_items_count()
