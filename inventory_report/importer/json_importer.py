import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(arq: str):
        if arq.endswith(".json"):
            with open(arq) as file:
                data = json.load(file)
                return data
        else:
            raise ValueError("Arquivo inválido")
