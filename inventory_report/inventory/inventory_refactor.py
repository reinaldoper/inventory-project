from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, data: str, type: str):
        list_itens = self.importer.import_data(data)
        for line in list_itens:
            self.data.append(line)

    def __iter__(self):
        result = InventoryIterator(self.data)
        return result
