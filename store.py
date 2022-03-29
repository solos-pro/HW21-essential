from storage import Storage


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, title: str, quantity: int):
        '''add (<название>, <количество>) - увеличивает запас items'''
        items_in_store = sum(self.items[n] for n in self.items)
        if items_in_store < self.capacity:
            if items_in_store + quantity < self.capacity:
                self.items[title] = self.items.get(title, 0) + quantity
            else:
                self.items[title] = self.items.get(title, 0) + (self.capacity - items_in_store)
        return self.items


    def remove(self, title):
        '''remove (<название>, <количество>) - уменьшает запас items'''
        del_item = self.items.pop(title, "Not exist")
        return f'try to remove: {title}, {del_item}'

    def get_free_space(self):
        '''get_free_space() - вернуть количество свободных мест'''
        ...

    def get_items(self):
        '''get_items() - возвращает сожержание склада в словаре {товар: количество}'''
        ...

    def get_unique_items_count(self):
        '''get_unique_items_count() - возвращает количество уникальных товаров'''



store = Store()
# store = Storage("gingerbread", 5)
store.add("gingerbread", 94)
print(store.items)
store.add("gingerbread", 6)
print(store.items)
store.add("apple", 7)
print(store.items)
print(store.remove("apples"))
print(store.items)
