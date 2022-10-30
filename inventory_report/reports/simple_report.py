from datetime import datetime, date


class SimpleReport:
    @classmethod
    def generate(cls, lista):
        fabricacao = [item['data_de_fabricacao'] for item in lista]
        validade = [
          item['data_de_validade'] for item in lista
          if datetime.strptime(item['data_de_validade'], "%Y-%m-%d").date()
          > date.today()
          ]
        empresas = [item['nome_da_empresa'] for item in lista]
        empresa_com_mais_produtos = [
          emp for emp in empresas
          if empresas.count(emp) > 1
          ]

        return (
                f"Data de fabricação mais antiga: {fabricacao[:2:-1][0]}\n"
                f"Data de validade mais próxima: {validade[-1]}\n"
                f"Empresa com mais produtos: {empresa_com_mais_produtos[0]}"
              )
