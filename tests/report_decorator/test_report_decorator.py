from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

product_list = [
  {
    "id": 1,
    "nome_do_produto": "Cafe",
    "nome_da_empresa": "Cafes Nature",
    "data_de_fabricacao": "2020-07-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "instrucao"
  },
  {
    "id": 2,
    "nome_do_produto": "Cafe",
    "nome_da_empresa": "Cafes Nature",
    "data_de_fabricacao": "2020-07-07",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR4845",
    "instrucoes_de_armazenamento": "instrucao 2"
  }
]


def test_decorar_relatorio():
    colored_report = ColoredReport(SimpleReport()).generate(product_list)
    assert "\033[32mData de fabricação mais antiga:" in colored_report
    assert "\033[36m2020-07-04" in colored_report
    assert "\033[31mCafes Nature" in colored_report
