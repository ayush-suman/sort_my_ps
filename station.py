from enum import Enum

class Station:
    def __init__(self, location, company, industry, stipend):
        self.location = location
        self.company = company
        self.industry = industry
        self.stipend = stipend
    def get_name(self):
        return self.industry.to_name() + '-' + self.company + ', ' + self.location
    

class Industry(Enum):
    CHEMICAL = 1
    ELECTRONICS = 2
    FINNMGMT = 3
    HEALTHCARE = 4
    INFRASTRUCTURE = 5
    IT = 6
    MECHANICAL = 7
    OTHERS = 8
    
    def from_name(name):
        match name:
            case 'Chemical': return Industry.CHEMICAL
            case 'Electronics': return Industry.ELECTRONICS
            case 'Finance and Mgmt': return Industry.FINNMGMT
            case 'Health Care': return Industry.HEALTHCARE
            case 'Infrastructure': return Industry.INFRASTRUCTURE
            case 'IT': return Industry.IT
            case 'Mechanical': return Industry.MECHANICAL
            case _: return Industry.OTHERS

    def to_name(self):
        match self.value:
            case 1: return 'Chemical'
            case 2: return 'Electronics'
            case 3: return 'Finance and Mgmt'
            case 4: return 'Health Care'
            case 5: return 'Infrastructure'
            case 6: return 'IT'
            case 7: return 'Mechanical'
            case 8: return 'Others'

    
    
