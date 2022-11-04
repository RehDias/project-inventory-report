import pandas as pd
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if not file_name.endswith('json'):
            raise ValueError('Arquivo inválido')
        read_file = pd.read_json(file_name).to_dict('records')
        for item in read_file:
            item['id'] = str(item['id'])
        return read_file
