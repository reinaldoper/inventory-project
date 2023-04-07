from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.reports.complete_report import CompleteReport
import sys
import os


def main():
    try:
        _, data, type = sys.argv
        list_result = get_type_data(data)

        list_result.import_data(data, type)
        type_data(type, list_result.data)

    except ValueError:
        sys.stderr.write("Verifique os argumentos\n")


def type_data(type: str, data: list):
    if type == 'simples':
        sys.stdout.write(SimpleReport.generate(data))
    else:
        sys.stdout.write(CompleteReport.generate(data))


def get_type_data(data_type: str):
    _arq, extensao = os.path.splitext(data_type)
    if extensao == '.csv':
        result = InventoryRefactor(CsvImporter)
        return result
    if extensao == '.json':
        result = InventoryRefactor(JsonImporter)
        return result
    if extensao == '.xml':
        result = InventoryRefactor(XmlImporter)
        return result
