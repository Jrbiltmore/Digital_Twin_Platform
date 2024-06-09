# 3d_printing_manager.py
"""
Script for managing 3D printing operations.
"""

class Printer:
    def __init__(self, id, model, material):
        self.id = id
        self.model = model
        self.material = material

    def print_part(self, part):
        print(f'Printer {self.id} printing part: {part}')

class PrintingManager:
    def __init__(self):
        self.printers = []

    def add_printer(self, printer):
        self.printers.append(printer)

    def assign_print_job(self, printer_id, part):
        for printer in self.printers:
            if printer.id == printer_id:
                printer.print_part(part)
                return
        print(f'Printer {printer_id} not found')

# Example usage
if __name__ == "__main__":
    # Create some printers
    printer1 = Printer(id='printer_001', model='Ultimaker S5', material='PLA')
    printer2 = Printer(id='printer_002', model='Formlabs Form 3', material='Resin')

    # Manage printers
    manager = PrintingManager()
    manager.add_printer(printer1)
    manager.add_printer(printer2)

    # Assign print jobs
    manager.assign_print_job('printer_001', 'gear')
    manager.assign_print_job('printer_002', 'housing')
    manager.assign_print_job('printer_003', 'bracket')  # Printer not found
