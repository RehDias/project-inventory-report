import pandas as pd
from inventory_report.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path_file):
        if not path_file.endswith('csv'):
            raise ValueError('Arquivo inválido')
        read_file = pd.read_csv(path_file, delimiter=",").to_dict('records')
        return read_file
