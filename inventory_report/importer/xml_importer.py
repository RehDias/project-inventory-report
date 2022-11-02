from inventory_report.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path_file):
        if not path_file.endswith('xml'):
            raise ValueError('Arquivo inválido')
        with open(path_file) as xml_file:
            xml_read = xmltodict.parse(xml_file.read())['dataset']['record']
        return xml_read
