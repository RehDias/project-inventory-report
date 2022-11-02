import xmltodict
import pandas as pd
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def get_file_types(file_type, read_file):
        if file_type == 'simples':
            return SimpleReport.generate(read_file)
        elif file_type == 'completo':
            return CompleteReport.generate(read_file)

    @classmethod
    def read_csv_file(cls, path_file, file_type):
        read_file = pd.read_csv(path_file, delimiter=",").to_dict('records')
        return cls.get_file_types(file_type, read_file)

    @classmethod
    def read_json_file(cls, path_file, file_type):
        read_file = pd.read_json(path_file).to_dict('records')
        return cls.get_file_types(file_type, read_file)

    @classmethod
    def read_xml_file(cls, path_file, file_type):
        with open(path_file) as xml_file:
            xml_read = xmltodict.parse(xml_file.read())['dataset']['record']

        return cls.get_file_types(file_type, xml_read)

    @classmethod
    def import_data(cls, path_file: str, file_type):
        if path_file.endswith('csv'):
            return cls.read_csv_file(path_file, file_type)
        elif path_file.endswith('json'):
            return cls.read_json_file(path_file, file_type)
        elif path_file.endswith('xml'):
            return cls.read_xml_file(path_file, file_type)
        else:
            raise ValueError
