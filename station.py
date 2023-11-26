from enum import Enum
from dataclasses import dataclass

class Industry(str, Enum):
    CHEMICAL = 'Chemical'
    ELECTRONICS = 'Electronics'
    FINNMGMT = 'Finance and Mgmt'
    HEALTHCARE = 'Health Care'
    INFRASTRUCTURE = 'Infrastructure'
    IT = 'IT'
    MECHANICAL = 'Mechanical'
    OTHERS = 'Others'
    NONE = ''
    
    # def from_name(name):
    #     match name:
    #         case 'Chemical': return Industry.CHEMICAL
    #         case 'Electronics': return Industry.ELECTRONICS
    #         case 'Finance and Mgmt': return Industry.FINNMGMT
    #         case 'Health Care': return Industry.HEALTHCARE
    #         case 'Infrastructure': return Industry.INFRASTRUCTURE
    #         case 'IT': return Industry.IT
    #         case 'Mechanical': return Industry.MECHANICAL
    #         case _: return Industry.OTHERS

    # def to_name(self):
    #     match self.value:
    #         case 1: return 'Chemical'
    #         case 2: return 'Electronics'
    #         case 3: return 'Finance and Mgmt'
    #         case 4: return 'Health Care'
    #         case 5: return 'Infrastructure'
    #         case 6: return 'IT'
    #         case 7: return 'Mechanical'
    #         case 8: return 'Others'


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
    


    
    
