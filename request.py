from shop import Shop
from store import Store


class Request:
    def __init__(self, store_list, shop, request_):
        lst = self.get_list(request_)
        self.from_ = lst[4]
        self.to = lst[6]
        self.amount = int(lst[1])
        self.product = lst[2]
        self.store_list = store_list
        self.shop = shop

    def get_list(self, str):
        return str.split(" ")

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'


    def shipping(self):
        print(self.shop.get_items())
        self.shop.remove(self.product, self.amount)
        print(self.shop.get_items())
        if self.shop.limit < self.amount:
            print('В магазин недостаточно места, попробуйте что-то другое')
            return 0

        if not self.store_list.items.get(self.product, None):
            print(f'В складе {self.from_} нет {self.product}, попробуйте что-то другое')
            return 0

        elif self.store_list.items.get(self.product, None) < self.amount:
            print(f'В складе {self.from_} недостаточно {self.product}, попробуйте уменьшить до {self.store_list.items.get(self.product)}')
            return 0





store1 = Store({'gingerbread': 25, 'apple': 15})
store1.add('gingerbread', 25)
store1.add('orange', 5)

shop1 = Shop()
shop1.add('orange', 125)

# request = {'gingerbread': 5, 'apple': 0}
request_1 = 'Доставить 5 orange из склад1 в магазин5'
req_1 = Request(store1, shop1, request_1)

print(req_1)
# print(store1.get_items())
# print(shop1.get_items())
req_1.shipping()

