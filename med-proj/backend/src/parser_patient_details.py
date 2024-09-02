from backend.src.parser_generic import MedicalDocParser
import re


class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        super().__init__(text) # self.text = text

    def parse(self):
        return {
            'patient_name': self.get_field('patient_name'),
            'phone_number': self.get_field('phone_number'),
            'vaccination_status': self.get_field('vaccination_status'),
            'medical_problems': self.get_field('medical_problems')
        }

    def parse_own(self):
        return {
            'patient_name': self.get_patient_name(),
            'phone_number': self.get_phone_number(),
            'vaccination_status': self.get_vaccine(),
            'medical_problems': self.get_field('medical_problems')
        }

    def get_field(self, field_name):
        pattern_dict = {
            'patient_name':{'Pattern':'Patient Information\s*Birth Date\s*(.*?)\s*\(','flags':0},
            'phone_number':{'Pattern':'\(\d{3}\)\s\d{3}-\d{4}', 'flags': 0},
            'vaccination_status':{'Pattern':'Have you had the Hepatitis B vaccination\?\s*(\w+)','flags': re.DOTALL},
            'medical_problems':{'Pattern':'List any Medical Problems.*?:\s*(.*?)(?:\n|$)', 'flags': re.DOTALL}
        }

        dict = pattern_dict.get(field_name)
        if dict:
            matches = re.findall(dict['Pattern'], self.text, flags = dict['flags'])
            if len(matches) > 0:
                match = matches[0].strip()
                return match

    def get_patient_name(self):
        pattern = 'Patient Information(.*?)\(\d{3}\)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        name = ''
        if matches:
            name = self.remove_noise_from_name(matches[0])
        return name


    def remove_noise_from_name(self, name):
        name = name.replace('Birth Date', ' ').strip()
        date_pattern = '((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern, name)

        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, '').strip()

        return name

    def get_phone_number(self):
        pattern = 'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            return matches[0][1]
        else:
            return None

    def get_vaccine(self):
        pattern = 'Have you had the Hepatitis B vaccination\?.*(Yes |No)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            return matches[0]
        else:
            return None


if __name__ == '__main__':
    document_text_1 = '''
    Patient Medical Record
    
     
    Patient Information Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight’
    9264 Ash Dr 95
    New York City, 10005 '
    United States Height:
    190
    In Casc of Emergency
    SC ee
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone
    
    Genera! Medical History
    
    nn
    
    me
    
    nh ee A OE i ne
    
    Chicken Pox (Varicella): Measies:
    
    IMMUNE IMMUNE
    
    Have you had the Hepatitis B vaccination?
    No
    
    List any Medical Problems (asthma, seizures, headaches}:
    
    Migraine
    
     
    
    be
    
    C
    mat
    Lh
    oo
    '''

    document_text_2 = '''
    17/12/2020

    Patient Medical Record
    
    Patient Information Birth Date
    
    Jerry Lucas May 2 1998
    
    (279) 920-8204 Weight:
    
    4218 Wheeler Ridge Dr 57
    
    Buffalo, New York, 14201 Height:
    
    United States gnt
    170
    
    In Case of Emergency |
    eee
    
    Joe Lucas . 4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    
    Home phone United States "
    Work phone
    
    General Medical History
    
     
    
    Chicken Pox (Varicelia): Measles: ..
    
    IMMUNE NOT IMMUNE
    
    Have you had the Hepatitis B vaccination?
    
    : Yes
    
    | List any Medical Problems (asthma, seizures, headaches):
    N/A
    
    7?
    v
    '''

    pp = PatientDetailsParser(document_text_1)
    x = pp.parse()
    print(x)