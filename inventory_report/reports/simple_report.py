from datetime import datetime, date


class SimpleReport:
    def get_fabricacao(lista):
        fabricacao = [item['data_de_fabricacao'] for item in lista]
        return fabricacao[:2:-1][0]

    def get_validade(lista):
        validade = [
          item['data_de_validade'] for item in lista
          if datetime.strptime(item['data_de_validade'], "%Y-%m-%d").date()
          > date.today()
          ]
        return validade

    def get_empresas(lista):
        empresas = [item['nome_da_empresa'] for item in lista]
        return empresas

    @classmethod
    def generate(cls, lista):
        fabricacao_mais_antiga = cls.get_fabricacao(lista)
        validade_mais_proxima = cls.get_validade(lista)
        empresas = cls.get_empresas(lista)
        empresa_com_mais_produtos = [
          emp for emp in empresas
          if empresas.count(emp) > 1
          ]

        return (
                f"Data de fabricação mais antiga: {fabricacao_mais_antiga}\n"
                f"Data de validade mais próxima: {validade_mais_proxima[-1]}\n"
                f"Empresa com mais produtos: {empresa_com_mais_produtos[0]}"
              )
