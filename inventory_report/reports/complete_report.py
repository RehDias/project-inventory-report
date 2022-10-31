from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def get_produtos_por_empresa(cls, lista):
        empresas = cls.get_empresas(lista)
        produtos_por_empresa = {}
        for empresa in empresas:
            if produtos_por_empresa.__contains__(empresa):
                pass
            produtos_por_empresa.update({
              empresa: empresas.count(empresa)
            })
        return produtos_por_empresa

    @classmethod
    def generate(cls, lista):
        produtos_por_empresa = cls.get_produtos_por_empresa(lista)
        quantidade_produto = ""
        for chave, valor in produtos_por_empresa.items():
            quantidade_produto += f"- {chave}: {valor}\n"

        return super().generate(lista) + (
          "\nProdutos estocados por empresa:\n"
          f"{quantidade_produto}"
        )
