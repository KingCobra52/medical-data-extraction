#parent class of parsers
import abc #abstract methods

class MedicalDocParser(metaclass=abc.ABCMeta):
    def __init__(self, text):
        self.text = text #document_text

    @abc.abstractmethod #decorates class as abstract method
    def parse(self):
        pass #returns a dictionary w all fields