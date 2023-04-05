import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(arq: str):
        if arq.endswith(".xml"):
            with open(arq, "r") as file:
                data_xml = xmltodict.parse(file.read())
                return data_xml["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")
