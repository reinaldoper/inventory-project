from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        list_empresa = Counter(
            product["nome_da_empresa"] for product in data)

        list_header = "Produtos estocados por empresa:"
        products = ""
        for line in list_empresa:
            products += f"- {line}: {list_empresa[line]}\n"
        return (
            f"{super().generate(data)}\n"
            f"{list_header}\n"
            f"{products}"
        )
