from inventory_report.inventory.product import Product
from datetime import date


def test_relatorio_produto():
    result = Product(
        id=1,
        nome_do_produto="Milk Shake",
        nome_da_empresa="SoveteCia",
        data_de_fabricacao=date(2023, 2, 5),
        data_de_validade=date(2023, 3, 5),
        numero_de_serie="54321",
        instrucoes_de_armazenamento="em local com temperatura abaixo de 10°C",
    )

    assert result.id == 1
    assert result.nome_do_produto == "Milk Shake"
    assert result.nome_da_empresa == "SoveteCia"
    assert result.data_de_fabricacao == "2023-02-05"
    assert result.data_de_validade == "2023-03-05"
    assert result.numero_de_serie == "54321"
    assert (
        result.instrucoes_de_armazenamento
        == "em local com temperatura abaixo de 10°C"
    )
    result_function_repr = (
        "O produto Milk Shake"
        " fabricado em 2023-02-05"
        " por SoveteCia com validade"
        " até 2023-03-05"
        " precisa ser armazenado em local com temperatura abaixo de 10°C."
    )
    assert repr(result) == result_function_repr
