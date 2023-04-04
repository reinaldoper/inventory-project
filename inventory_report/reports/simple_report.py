from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(data):
        list_data_antiga = []
        list_data_first = []
        list_empresa = []
        se = datetime.today()
        for line in data:
            if datetime.strptime(line['data_de_fabricacao'], "%Y-%m-%d") <= se:
                list_data_antiga.append(line['data_de_fabricacao'])
            if datetime.strptime(line['data_de_validade'], "%Y-%m-%d") >= se:
                list_data_first.append(line['data_de_validade'])
        for line in data:
            list_empresa.append(line['nome_da_empresa'])
        list_data_antiga.sort()
        list_data_first.sort()
        dup = [x for i, x in enumerate(list_empresa) if x in list_empresa[:i]]
        antiga = f'Data de fabricação mais antiga: {list_data_antiga[0]}'
        first = f'Data de validade mais próxima: {list_data_first[0]}'
        empresa = f'Empresa com mais produtos: {dup[0]}'
        return f'{antiga}\n{first}\n{empresa}'
