from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, classe):
        self.importer = classe
        self.data = []

    def import_data(self, path_file, file_type):
        if len(self.data) > 1:
            self.data.extend(self.importer.import_data(path_file))
        else:
            self.data = self.importer.import_data(path_file)
        if file_type == 'simples':
            return SimpleReport.generate(self.data)
        elif file_type == 'completo':
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
