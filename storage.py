from abc import abstractmethod


class Storage:
    def __init__(self, items={}):
        self.items = items
        self.capacity = 100

    # @property
    # def get_items(self):
    #     return self.items

    @abstractmethod
    def add(self, title: str, quantity: int):
        '''add (<название>, <количество>) - увеличивает запас items'''
        items_in_store = sum(self.items[n] for n in self.items)
        if items_in_store < self.capacity:
            if items_in_store + quantity < self.capacity:
                self.items[title] = self.items.get(title, 0) + quantity
            else:
                self.items[title] = self.items.get(title, 0) + (self.capacity - items_in_store)
        return self.items

    @abstractmethod
    def remove(self, title: str, quantity: int):
        '''remove (<название>, <количество>) - уменьшает запас items'''
        remove_item = self.items.get(title, None)
        if remove_item:
            if remove_item < quantity:
                self.items.pop(title)
                return remove_item
            else:
                if remove_item == quantity:
                    self.items.pop(title)
                elif remove_item > quantity:
                    self.items[title] -= quantity
                return quantity
        return remove_item

    @abstractmethod

    def get_free_space(self):
        '''get_free_space() - вернуть количество свободных мест'''
        return f'{self.capacity - sum(self.items[n] for n in self.items)} - количество свободных мест'

    @abstractmethod
    def get_items(self):
        '''get_items() - возвращает содержание склада в словаре {товар: количество}'''
        # print(self.items, 'содержание склада')
        return self.items

    @abstractmethod
    def get_unique_items_count(self):
        '''get_unique_items_count() - возвращает количество уникальных товаров'''
        # print(len(self.items.keys()), 'количество уникальных товаров')
        return len(self.items.keys()) #self.items.keys()


