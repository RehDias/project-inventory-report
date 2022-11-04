import pandas as pd
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if not file_name.endswith('csv'):
            raise ValueError('Arquivo inválido')
        read_file = pd.read_csv(file_name, delimiter=",").to_dict('records')
        for item in read_file:
            item['id'] = str(item['id'])
        return read_file
