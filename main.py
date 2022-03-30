from storage import Storage
from shop import Shop
from store import Store
from request import Request, show

if __name__ == '__main__':
    store1 = Store(name='склад111', items={'gingerbread': 25, 'apple': 15}, capacity=100)
    store1.add('gingerbread', 25)
    store1.add('orange', 5)

    shop1 = Shop(name='магазин5*5', items={}, capacity=6)
    shop1.add('orange', 125)

    # request_1 = 'Доставить 2 orange из склад1 в магазин5'
    # req_1 = Request(store1, shop1, input('Enter query: '))

    while 1:
        req_1 = Request(store1, shop1, input('Enter query: '))

        repr(req_1)
        req_1.shipping()

        show(store1.get_items(), store1.get_name)
        show(shop1.get_items(), shop1.get_name)