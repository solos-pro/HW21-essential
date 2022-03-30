
def show(dict_, point):
    print('\nсодержание ', point)
    for element in dict_:
        print(dict_[element], '-', element)


class Request:
    def __init__(self, request_):
        lst = self.get_list(request_)
        self.from_ = lst[4]
        self.to = lst[6]
        self.amount = int(lst[1])
        self.product = lst[2]

    def get_list(self, str):
        return str.split(" ")

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'

'''
    def shipping(self):
        show(self.shop.get_items(), self.to)
        self.shop.remove(self.product, self.amount)
        if self.shop.items.get(self.product, None):
            if self.shop.items.get(self.product, None) >= self.amount:
                self.shop.remove(self.product, self.amount)
                print(f'Заберите {self.amount} {self.product} в {self.to}')
                return 0

        if (self.shop.items.get(self.product, None) + self.shop.get_free_space()) < self.amount:
            print('В магазин недостаточно места, попробуйте что-то другое')
            return 0

        if not (self.store.items.get(self.product, None) or self.shop.items.get(self.product, None)):
            print(f'В складе {self.from_} и магазине {self.to} нет {self.product}, попробуйте что-то другое')
            return 0

        elif (self.store.items.get(self.product, None) + self.shop.items.get(self.product, None)) < self.amount:
            print(f'В складе {self.from_} + магазине {self.to} недостаточно {self.product}, попробуйте уменьшить до /'
                  f'{self.store.items.get(self.product) + self.shop.items.get(self.product, None)}')
            return 0

        else:
            num_remove_from_store = self.amount - self.shop.items.get(self.product, None)
            self.store.remove(self.product, num_remove_from_store)
            print(f"Перевозим со склада {self.from_} в магазин {self.to} {num_remove_from_store} {self.product} ")

            self.shop.add(self.product, num_remove_from_store)
            print(f"Принято со склада {self.from_} в магазине {self.to} {num_remove_from_store} {self.product} ")

            self.shop.remove(self.product, num_remove_from_store)
            print(f"Заказ {num_remove_from_store} {self.product} получен в магазине {self.to}")
'''



