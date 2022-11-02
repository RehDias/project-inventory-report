import pandas as pd
from inventory_report.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path_file):
        if not path_file.endswith('json'):
            raise ValueError('Arquivo inválido')
        read_file = pd.read_json(path_file).to_dict('records')
        return read_file
