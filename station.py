from enum import Enum
from dataclasses import dataclass

class IndustryMeta(type):
    def __init__(self, name, bases, dct):
        self.CHEMICAL = self('Chemical')
        self.ELECTRONICS = self('Electronics')
        self.FINNMGMT = self('Finance and Mgmt')
        self.HEALTHCARE = self('Health Care')
        self.INFRASTRUCTURE = self('Infrastructure')
        self.IT = self('IT')
        self.MECHANICAL = self('Mechanical')
        self.OTHERS = self('Others')
        self.NONE = self('')


class Industry(metaclass=IndustryMeta):
    def __init__(self, value: str):
        if value is None:
            raise ValueError('Industry needs to be constructed with a value')
        self._value = value

    @property
    def value(self):
        return self._value
    
    def __eq__(self, other):
        for value in self.value.split('|'):
            if value == other.value:
                return True
        return False

    
    def __add__(self, other):
        return Industry(self.value + '|' + other.value)
    
    def __or__(self, other):
        return Industry(self.value + '|' + other.value)
    
    def __and__(self, other):
        return Industry(self.value + '|' + other.value)



@dataclass
class Station(object):

    location: str
    company: str
    industry: Industry
    stipend: int
    
    def get_name(self):
        if self.industry == Industry.NONE:
            return self.company + ', ' + self.location
        if self.industry == Industry.ELECTRONICS:
            return self.industry.value + '  -' + self.company + ', ' + self.location
        return self.industry.value + '-' + self.company + ', ' + self.location
    


    
    
