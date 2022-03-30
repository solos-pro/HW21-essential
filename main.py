from shop import Shop
from store import Store
from request import Request, show

if __name__ == '__main__':
    store1 = Store(name='склад111', items={'gingerbread': 25, 'apple': 15}, capacity=100)
    store1.add('gingerbread', 25)
    store1.add('orange', 4)

    shop1 = Shop(name='магазин5*5', items={}, capacity=6)
    shop1.add('orange', 1)

    # request_1 = 'Доставить 2 orange из склад1 в магазин5'

    while 1:
        show(store1.get_items(), store1.get_name)
        show(shop1.get_items(), shop1.get_name)

        req_1 = Request(input('\nEnter query: '))
        what = req_1.product
        how_much = req_1.amount
        maximum = shop1.capacity


        existed_in_destination = shop1.items.get(what, 0)
        existed_in_repository = store1.items.get(what, 0)
        summary = existed_in_repository + existed_in_destination
        free = shop1.get_free_space()
        movement_necessity = how_much - existed_in_destination
        if movement_necessity < 0:
            movement_necessity = 0

        if summary == 0:
            print("Отсутствует на складе и в магазине")
            continue

        if how_much > (existed_in_destination + free):
            print('Уменьшите количество до ', existed_in_destination + free)
            print('свободных мест на полке в магазине для ', free)
            continue

        if how_much > summary:
            print('Уменьшите количество, на складе и в магазине всего ', summary)
            continue

        store1.remove(what, movement_necessity)
        print(f'Перемещается со склада в магазин товар {movement_necessity} {what}')

        shop1.add(what, movement_necessity)
        print(f'товар {movement_necessity} {what} доставлен')

        shop1.remove(what, how_much)
        print(f'товар {how_much} {what} выдан')

        # exit()
