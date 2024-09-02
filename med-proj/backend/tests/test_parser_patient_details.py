from backend.src.parser_patient_details import PatientDetailsParser
import pytest

@pytest.fixture
def doc_3_empty():
    document_text = '''
    
    '''
    return PatientDetailsParser(document_text)

@pytest.fixture
def doc_2_kathy():
    document_text = '''
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
    return PatientDetailsParser(document_text)

@pytest.fixture
def doc_1_jerry():
    document_text = '''
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
    return PatientDetailsParser(document_text)


def test_parse(doc_2_kathy, doc_3_empty, doc_1_jerry):
    dict_kathy = doc_2_kathy.parse()
    dict_none = doc_3_empty.parse()
    dict_jerry = doc_1_jerry.parse()
    assert dict_kathy['phone_number'] == '(737) 988-0851'
    assert dict_kathy == {
        'patient_name': 'Kathy Crawford May 6 1972',
        'phone_number': '(737) 988-0851',
        'vaccination_status': 'No',
        'medical_problems': 'Migraine'
    }
    assert dict_none == {
        'patient_name': None,
        'phone_number': None,
        'vaccination_status': None,
        'medical_problems': None
    }
    assert dict_jerry == {
        'patient_name': 'Jerry Lucas May 2 1998',
        'phone_number': '(279) 920-8204',
        'vaccination_status': None,
        'medical_problems': 'N/A'
    }

    assert dict_kathy['patient_name'] == 'Kathy Crawford May 6 1972'

def test_get_patient_name(doc_2_kathy):
    assert doc_2_kathy.get_patient_name() == 'Kathy Crawford'

def test_get_vaccine(doc_2_kathy):
    assert doc_2_kathy.get_vaccine() == 'No'

def test_get_phone_number(doc_2_kathy):
    assert doc_2_kathy.get_phone_number() == '(737) 988-0851'

def test_parse_own(doc_2_kathy, doc_1_jerry):
    assert doc_2_kathy.parse_own() == {
        'patient_name': 'Kathy Crawford',
        'phone_number': '(737) 988-0851',
        'vaccination_status': 'No',
        'medical_problems': 'Migraine'
    }

    assert doc_1_jerry.parse_own() == {
        'patient_name': 'Jerry Lucas',
        'phone_number': '(279) 920-8204',
        'vaccination_status': None,
        'medical_problems': 'N/A'
    }