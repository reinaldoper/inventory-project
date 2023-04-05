from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


list_item = [
    {
        "id": 1,
        "nome_do_produto": "Cafe",
        "nome_da_empresa": "Cacau Show",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2024-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "em local abrigado da luz do sol",
    },
    {
        "id": 2,
        "nome_do_produto": "leite",
        "nome_da_empresa": "Nestle",
        "data_de_fabricacao": "2023-07-04",
        "data_de_validade": "2024-02-10",
        "numero_de_serie": "FR49",
        "instrucoes_de_armazenamento": "em local seco",
    },
    {
        "id": 3,
        "nome_do_produto": "leite em pó",
        "nome_da_empresa": "Nestle",
        "data_de_fabricacao": "2023-10-04",
        "data_de_validade": "2024-10-10",
        "numero_de_serie": "FR50",
        "instrucoes_de_armazenamento": "em local seco abrigado do sol",
    },
    {
        "id": 4,
        "nome_do_produto": "MESA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
    }
]

red = "\033[31m"
red1 = "\033[0m"

blue = "\033[36m"
blue1 = "\033[0m"

green = "\033[32m"
vr = "\033[0m"


def test_decorar_relatorio():
    result = (
        f"{green}Data de fabricação mais antiga:{vr} {blue}2020-07-04{blue1}\n"
        f"{green}Data de validade mais próxima:{vr} {blue}2024-02-09{blue1}\n"
        f"{green}Empresa com mais produtos:{vr} {red}Nestle{red1}"
    )

    assert ColoredReport(SimpleReport).generate(list_item) == result
