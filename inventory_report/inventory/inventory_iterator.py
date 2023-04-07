from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, arq_data: str):
        self.index_count = 0
        self.arq_data = arq_data

    def __next__(self):
        line = self.arq_data[self.index_count]
        if not line:
            raise StopIteration

        self.index_count += 1
        return line
