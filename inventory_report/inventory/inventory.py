from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import os


class Inventory:
    @classmethod
    def import_data(cls, data: str, type: str):
        _arquivo, extensao = os.path.splitext(data)
        if extensao == '.csv':
            header = CsvImporter().import_data(data)
        if extensao == '.json':
            header = JsonImporter().import_data(data)
        if extensao == '.xml':
            header = XmlImporter().import_data(data)
        return cls.read_arq(header, type)

    def read_arq(arq: str, type: str):
        if type == 'simples':
            return SimpleReport().generate(arq)
        else:
            return CompleteReport().generate(arq)
