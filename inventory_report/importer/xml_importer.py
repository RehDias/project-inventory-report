import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if not file_name.endswith('xml'):
            raise ValueError('Arquivo inválido')
        with open(file_name) as xml_file:
            xml_read = xmltodict.parse(xml_file.read())['dataset']['record']
        return xml_read
