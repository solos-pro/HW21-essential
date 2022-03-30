from storage import Storage


class Store(Storage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

