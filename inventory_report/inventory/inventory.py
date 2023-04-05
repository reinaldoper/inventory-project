from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import os
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(cls, data: str, type: str):
        arquivo, extensao = os.path.splitext(data)
        if extensao == '.csv':
            header_csv = cls.read_csv(data, type)
            return header_csv
        if extensao == '.json':
            header_json = cls.read_json(data, type)
            return header_json
        if extensao == '.xml':
            headre_xml = cls.read_xml(data)
            if type == 'simples':
                return SimpleReport().generate(headre_xml)
            else:
                return CompleteReport().generate(headre_xml)

    def read_csv(arq_csv, type):
        array = []
        with open(arq_csv, 'r') as file:
            file_csv = csv.DictReader(file)
            for line in file_csv:
                array.append(line)
        if type == 'simples':
            new_data = SimpleReport().generate(array)
            return new_data
        if type == 'completo':
            new_data = CompleteReport().generate(array)
            return new_data

    def read_json(arq_json, type):
        with open(arq_json) as file:
            content = file.read()  # leitura do arquivo
            header_json = json.loads(content)
        if type == 'simples':
            new_data = SimpleReport().generate(header_json)
            return new_data
        if type == 'completo':
            new_data = CompleteReport().generate(header_json)
            return new_data

    def read_xml(arq_xml):
        with open(arq_xml, "r") as file:
            data_xml = xmltodict.parse(file.read())
            return data_xml["dataset"]["record"]
