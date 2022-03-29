class Storage:
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, title: str, quantity: int):
        '''add (<название>, <количество>) - увеличивает запас items'''
        ...


    def remove(self, title):
        '''remove (<название>, <количество>) - уменьшает запас items'''
        ...

    def get_free_space(self):
        '''get_free_space() - вернуть количество свободных мест'''
        ...

    def get_items(self):
        '''get_items() - возвращает сожержание склада в словаре {товар: количество}'''
        ...

    def get_unique_items_count(self):
        '''get_unique_items_count() - возвращает количество уникальных товаров'''
        ...

