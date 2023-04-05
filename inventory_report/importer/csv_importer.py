import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(arq: str):
        if arq.endswith(".csv"):
            array = []
            with open(arq, 'r') as file:
                file_csv = csv.DictReader(file)
                for line in file_csv:
                    array.append(line)
                return array
        else:
            raise ValueError("Arquivo inválido")
