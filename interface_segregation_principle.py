from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldFashionedPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white.")

    def fax(self, document):
        raise NotImplementedError("Fax is not supported.")

    def scan(self, document):
        raise NotImplementedError("Scan is not supported.")
    
class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color.")
    
    def fax(self, document):
        print(f"Faxing document {document}.")

    def scan(self, document):
        print(f"Scanning {document}.")

# New interface
class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class Fax:
    @abstractmethod
    def fax(self, document):
        pass

class OldFashionedPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white.")

class NewPrinter(Printer, Scanner, Fax):
    def print(self, document):
        print(f"Printing {document} in color.")

    def fax(self, document):
        print(f"Faxing document {document}.")

    def scan(self, document):
        print(f"Scanning {document}.")