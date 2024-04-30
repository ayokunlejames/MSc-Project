#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv
import random
import string
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Custom list of medical-related terms for company names
medical_terms = [
    'MediTech', 'HealthLab', 'BioDevices', 'MediPro', 'HealthTech', 'BioTech', 'LifeTech', 'MediSolutions',
    'HealthSystems', 'BioInnovations', 'LifeSolutions', 'MediCare', 'HealthCare', 'BioCare', 'LifeCare'
]

def generate_gtin():
    # Generate a random GTIN with 14 digits
    return ''.join(str(random.randint(0, 9)) for _ in range(14))

def generate_short_string(length):
    # Generate a short random string of specified length
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def generate_13_digits():
    # Generate a random 13-digit number
    return ''.join(str(random.randint(0, 9)) for _ in range(13))

def generate_nhs_eclass_code():
    # Generate a 3-character NHS eclass code
    return ''.join(random.choices(string.ascii_uppercase, k=3))

def generate_data():
    data = []
    for _ in range(100):
        gtin = generate_gtin()
        brand_name = random.choice(medical_terms)  # Select a medical-related term for the brand name
        serial_number = generate_short_string(6)  # Short serial number
        batch_number = generate_short_string(6)  # Short batch number
        manufacturing_date = fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
        expiry_date = (datetime.strptime(manufacturing_date, '%Y-%m-%d') + timedelta(days=random.randint(30, 365))).strftime('%Y-%m-%d')
        udi_pi = generate_13_digits()  # 13 digits for UDI-PI
        unit_of_issue = random.choice(['Boxes', 'Packs', 'Cartons'])
        unit_of_use = random.choice(['Individual', 'Group'])
        quantity_of_uou = random.randint(1, 100)
        unit_of_use_udi = generate_gtin() if unit_of_use != unit_of_issue else None
        item_length_cm = random.uniform(5, 30)
        item_height_cm = random.uniform(2, 20)
        item_width_cm = random.uniform(2, 20)
        item_weight_gram = random.randint(50, 500)
        item_volume_ccm = round(item_length_cm * item_height_cm * item_width_cm, 2)
        unit_of_dimension = 'cm'
        product_description = fake.sentence(nb_words=6)
        storage_handling = fake.sentence(nb_words=6)
        single_use = random.choice(['Yes', 'No'])
        restricted_no_of_use = random.choice(['Yes', 'No'])
        sterile = random.choice(['Yes', 'No'])
        sterilize_before_use = random.choice(['Yes', 'No'])
        sterilization_method = random.choice(['Autoclave', 'Gamma Radiation', 'Ethylene Oxide'])
        item_contains_latex = random.choice(['Yes', 'No'])
        item_contains_dehp = random.choice(['Yes', 'No'])
        item_mri_compatible = random.choice(['Yes', 'No'])
        supplier_supplier_gln = generate_13_digits()  # 13 digits for supplier GLN
        item_model_gmn = fake.text(max_nb_chars=25)  # Max 25 characters for item model GMN
        gmdn_gmdn_code = ''.join(random.choices(string.digits, k=5))  # 5 numeric characters for GMDN code
        manufacturer_catalog_mpc = generate_short_string(6)  # Short random reference number for manufacturer catalog MPC
        nhs_provider_provider_gln = generate_13_digits()  # 13 digits for NHS provider GLN
        nhs_eclass_code = generate_nhs_eclass_code()  # 3-character NHS eclass code
        
        data.append([gtin, brand_name, serial_number, batch_number, manufacturing_date, expiry_date, udi_pi, unit_of_issue, unit_of_use, quantity_of_uou, unit_of_use_udi, item_length_cm, item_height_cm, item_width_cm, item_weight_gram, item_volume_ccm, unit_of_dimension, product_description, storage_handling, single_use, restricted_no_of_use, sterile, sterilize_before_use, sterilization_method, item_contains_latex, item_contains_dehp, item_mri_compatible, supplier_supplier_gln, item_model_gmn, gmdn_gmdn_code, manufacturer_catalog_mpc, nhs_provider_provider_gln, nhs_eclass_code])
    
    return data

def write_to_csv(data):
    with open('generated_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["gtin","brand_name","serial_number","batch_number","manufacturing_date","expiry_date","udi_pi","unit_of_issue","unit_of_use","quantity_of_uou","unit_of_use_udi","item_length_cm","item_height_cm","item_width_cm","item_weight_gram","item_volume_ccm","unit_of_dimension","product_description","storage_handling","single_use","restricted_no_of_use","sterile","sterilize_before_use","sterilization_method","item_contains_latex","item_contains_dehp","item_mri_compatible","supplier_supplier_gln","item_model_gmn","gmdn_gmdn_code","manufacturer_catalog_mpc","nhs_provider_provider_gln","nhs_eclass_code"])
        writer.writerows(data)

data = generate_data()
write_to_csv(data)
print("CSV file generated successfully.")


# In[2]:


#generate random gln for nhs providers
import csv
import random

def generate_distinct_13_digits():
    numbers = set()
    while len(numbers) < 210:
        numbers.add(''.join(str(random.randint(0, 9)) for _ in range(13)))
    return numbers

def write_numbers_to_csv(numbers):
    with open('distinct_numbers.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Number"])
        writer.writerows([[number] for number in numbers])

distinct_numbers = generate_distinct_13_digits()
write_numbers_to_csv(distinct_numbers)
print("CSV file generated successfully.")


# In[12]:


import csv
import random

def generate_uk_phone_number():
    country_code = "+44"
    ndc_length = random.randint(2, 5)
    subscriber_length = 11 - len(country_code) - ndc_length
    ndc = ''.join(str(random.randint(0, 9)) for _ in range(ndc_length))
    subscriber = ''.join(str(random.randint(0, 9)) for _ in range(subscriber_length))
    return f"{country_code} {ndc} {subscriber}"

def write_phone_numbers_to_csv(phone_numbers):
    with open('uk_phone_numbers.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Phone Number"])
        writer.writerows([[phone_number] for phone_number in phone_numbers])

# Generate 50 UK phone numbers
uk_phone_numbers = [generate_uk_phone_number() for _ in range(100)]

# Write phone numbers to CSV file
write_phone_numbers_to_csv(uk_phone_numbers)
print("CSV file generated successfully.")


# In[11]:


import random
import string

def generate_gln():
    # Generate a random 13-digit GLN
    gln = ''.join(random.choices(string.digits, k=13))
    while gln in forbidden_glns:
        gln = ''.join(random.choices(string.digits, k=13))
    return gln

def generate_phone():
    # Generate a random phone number with country code (11 characters)
    country_code = '+'
    phone_number = ''.join(random.choices(string.digits, k=10))
    return country_code + phone_number

def generate_email(manufacturer_name):
    # Generate an email address using the name of the company as the domain
    domain = manufacturer_name.lower().replace(' ', '_') + '.com'
    return f'info@{domain}'

def generate_address():
    # Generate a random address
    address = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    return address

# Forbidden GLNs
forbidden_glns = {
    1787426142593, 5355706845251, 8669248244738, 3188653506629, 1502949321054,
    9471612721617, 5464500384011, 5734215459887, 4793910167746, 2383385694769,
    5602797913144, 3679391479491, 6134340164082, 2582391378949, 5389565259340,
    1625311829590, 2407055398038, 6812533035635, 5403311478237, 6851026932832,
    4599813054713, 3056805822483, 6780841830486, 1158295783109, 7381659081385,
    4268249467177, 9022770773887, 2530086510301, 9162831417343, 5112102322182,
    5798895595777, 4082790962185, 7372534604021, 1770267367641, 6339567101209,
    2387488434700, 2604391790205, 2016897331791, 6392268280323, 3753089977342,
    3091994620870, 1652483352101, 5206869938143, 7667897179712, 2930939237146,
    9535106554796, 1300349100191, 4233963093630, 3980396941073, 9315313380663,
    5084534637627, 1900358101802, 4414316319225, 6792628076661, 4339923457504,
    6745345351900, 7883192718090, 1441942563047, 8094774079881, 7377208301011,
    4855974015212, 3188102180006, 3016751884505, 5050152999623, 9960525077757,
    7273531154562, 2203030704861, 4251747192202, 8714269143552, 8963908738890,
    1808324650472, 1405017420394, 3845526499040, 1107011097561, 1409348380475,
    3470748526938, 3294394572888, 3369886235460, 8127911833130, 9425956549333,
    2617783915899, 1245441199706, 9142791246604, 56859659300, 7641889286636,
    8457006610375, 5353377869799, 7847199038671, 9002183487154, 1411054152573,
    7213600755366, 9677723220499, 9068450701467, 1291399157964, 7227485313191,
    4058181181820, 5125043705471, 1404995689190, 7976962325452, 9111346374287,
    4455831001971, 5886506263914, 4103733651619, 8680961497817, 8938779939592,
    8466582821825, 3497293988861, 6267073360381, 6237909656662, 8193441880708,
    3730544546981, 8896804261670, 3036657381718, 7036869986010, 8795675373523,
    8435312396285, 4743068002831, 3176361872449, 7999187491110, 1575914047053,
    7768817502344, 3617835091195, 9667368924551, 4281610235854, 2895991751260,
    6088512446957, 5715137135015, 2335788935077, 3221960478030, 8372518800773,
    7110977554839, 8924965789818, 7197303734130, 2809271968640, 5427986326225,
    3962620279715, 3391772119024, 9988034287485, 1970038329797, 7933109917260,
    6454172439743, 5087933795376, 9920537681553, 5268920604019, 9698432031631,
    1466947196774, 8625946690228, 6675383679887, 5005724875350, 2826534597629,
    8716703426269, 5321873856226, 2421691416417, 8800154723553, 1337096445315,
    9737050230588, 6430875198055, 1428148632346, 7112921603518, 3566566881880,
    3610413274562, 7397071154717, 1748699303623, 1636124214140, 1447492327485,
    8708374853172, 6004221935526, 9385914536552, 2295344381978, 9611213350490,
    3857717762739, 2418622939486, 3586351415755, 8932363010370, 2005249168982,
    9712951275088, 9971178126305, 7233566270652, 6657744281557, 6499195913610,
    7524983515038, 2693964558788, 2583842947051, 6550577960929, 5738631622223,
    1508886338387, 6346781206348, 6080691397923, 8120660841497, 3726642304593,
    9644879802530, 5559986681166, 8771201664273, 2239114025619, 9737930759314,
    2925813609359, 5054698188257, 7329931789003, 5894316784166, 9359976861362,
    8396496689280, 2790932733356, 5021939688352, 2221323423851, 9938193281610,
    9395760670542, 7021519602795, 6717008903568, 3734425130978
}

# Generate dataset
manufacturers = []
for _ in range(100):
    gln = generate_gln()
    manufacturer_name = ''.join(random.choices(string.ascii_uppercase, k=10))
    address = generate_address()
    registration_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    phone = generate_phone()
    email = generate_email(manufacturer_name)
    manufacturers.append((gln, manufacturer_name, address, registration_number, phone, email))

    
# Write the data to a CSV file
with open('manufacturers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["GLN", "Manufacturer Name", "Address", "Registration Number", "Phone", "Email"])
    writer.writerows(manufacturers)

print("CSV file has been created successfully.")


# In[7]:


import csv
import random
import string

def generate_company_name():
    prefixes = ['ABC', 'XYZ', 'Global', 'International', 'United', 'Sunrise', 'Blue', 'Green', 'Red', 'Orange']
    suffixes = ['Corp', 'Industries', 'Enterprises', 'Solutions', 'Tech', 'Systems', 'Services', 'Group', 'Ltd']
    return random.choice(prefixes) + ' ' + random.choice(suffixes)

def generate_address():
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
    street_names = ['Main', 'Oak', 'Park', 'Cedar', 'Elm', 'Maple', 'Pine', 'Washington', 'Lincoln', 'Lake']
    street_suffixes = ['St', 'Ave', 'Blvd', 'Dr', 'Ln', 'Ct', 'Rd', 'Pl']
    return str(random.randint(1, 9999)) + ' ' + random.choice(street_names) + ' ' + random.choice(street_suffixes) + ', ' + random.choice(cities)

def generate_registration_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

def generate_phone_number():
    return '+1' + ''.join(random.choices(string.digits, k=9))

def generate_email(company_name):
    return company_name.lower().replace(' ', '') + '@example.com'

# Generate 100 manufacturers
manufacturers = []
for _ in range(100):
    company_name = generate_company_name()
    address = generate_address()
    registration_number = generate_registration_number()
    phone_number = generate_phone_number()
    email = generate_email(company_name)
    manufacturers.append((company_name, address, registration_number, phone_number, email))

# Write the data to a CSV file
with open('manufacturers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Manufacturer Name", "Address", "Registration Number", "Phone", "Email"])
    writer.writerows(manufacturers)

print("CSV file has been created successfully.")


# In[13]:


#generate uk address
import csv
import random

def generate_address(existing_addresses):
    street_names = ['High Street', 'Main Street', 'Park Road', 'Station Road', 'Church Street', 'London Road', 'Victoria Road', 'Green Lane', 'Manor Road', 'Church Road']
    cities = ['London', 'Birmingham', 'Manchester', 'Glasgow', 'Liverpool', 'Newcastle', 'Leeds', 'Sheffield', 'Bristol', 'Edinburgh']
    counties = ['Greater London', 'West Midlands', 'Greater Manchester', 'Lanarkshire', 'Merseyside', 'Tyne and Wear', 'West Yorkshire', 'South Yorkshire', 'Avon', 'Midlothian']
    postcodes = ['AB1 2CD', 'EF3 4GH', 'IJ5 6KL', 'MN7 8OP', 'QR9 0ST', 'UV1 2WX', 'YZ3 4AB', 'CD5 6EF', 'GH7 8IJ', 'KL9 0MN']

    while True:
        street_name = random.choice(street_names)
        city = random.choice(cities)
        county = random.choice(counties)
        postcode = random.choice(postcodes)

        house_number = random.randint(1, 100)
        address_line1 = f"{house_number} {street_name}"
        address_line2 = city
        address_line3 = county
        address_line4 = "United Kingdom"
        postal_code = postcode

        address = [address_line1, address_line2, address_line3, address_line4, postal_code]
        if address not in existing_addresses:
            return address

# Generate 100 random addresses
addresses = []
for _ in range(100):
    address = generate_address(addresses)
    addresses.append(address)

# Write the data to a CSV file
with open('uk_addresses.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Address Line 1", "Address Line 2", "Address Line 3", "Address Line 4", "Postal Code"])
    writer.writerows(addresses)

print("CSV file with 100 distinct random UK addresses has been created successfully.")


# In[16]:


import csv

# Risk class names and descriptions
risk_classes = [
    ("Class I", "Low risk - General Controls", "General controls are sufficient to provide reasonable assurance of safety and effectiveness"),
    ("Class IIa", "Medium risk - Special Controls", "Special controls, such as performance standards, postmarket surveillance, patient registries, guidelines, and recommendations, are necessary to provide reasonable assurance of safety and effectiveness"),
    ("Class IIb", "Medium/high risk - Additional Special Controls", "Additional special controls, such as clinical data, are necessary to provide reasonable assurance of safety and effectiveness, compared to Class IIa."),
    ("Class III", "High risk - Premarket Approval", "Premarket approval is required to provide reasonable assurance of safety and effectiveness"),
]

# Generate dataset
data = []
for class_name, class_description, regulatory_requirements in risk_classes:
    data.append([class_name, class_description, regulatory_requirements])

# Write the data to a CSV file
with open('risk_classes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["class_name", "class_description", "regulatory_requirements"])
    writer.writerows(data)

print("CSV file with risk classes for medical devices has been created successfully.")


# In[17]:


import csv
import random

# Define a list of GMDN codes, names, and example definitions
gmdn_codes = ['10001', '10002', '10003', '10004', '10005']
gmdn_names = [
    "Surgical scalpel",
    "Catheter, urinary, short-term",
    "Suture needle, non-absorbable",
    "Orthopedic screw, bone",
    "Electrosurgical unit, monopolar"
]
gmdn_definitions = [
    "A small, handheld surgical instrument with a thin, sharp blade used for making incisions.",
    "A flexible tube inserted into the bladder to drain urine for a short period of time.",
    "A needle used to sew tissue together during surgery, made of non-absorbable material.",
    "A threaded fastener used to hold bone fragments together during orthopedic surgeries.",
    "An electrical device used for cutting, coagulating, and cauterizing tissue during surgery."
]

# Generate dataset by combining the lists
gmdn_data = zip(gmdn_codes, gmdn_names, gmdn_definitions)

# Write the data to a CSV file
with open('gmdn_dataset.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["GMDN Code", "GMDN Term Name", "GMDN Term Definition"])
    writer.writerows(gmdn_data)

print("CSV file with GMDN dataset has been created successfully.")


# In[18]:


import csv
import random

# Generate 50 distinct GMDN codes
gmdn_codes = []
for _ in range(50):
    code = ''.join(random.choices('0123456789', k=5))
    while code in gmdn_codes:
        code = ''.join(random.choices('0123456789', k=5))
    gmdn_codes.append(code)

# Generate random GMDN names and definitions
gmdn_names = [f"GMDN {i}" for i in range(1, 51)]
gmdn_definitions = [f"Definition for GMDN {i}" for i in range(1, 51)]

# Combine the data into tuples
gmdn_data = zip(gmdn_codes, gmdn_names, gmdn_definitions)

# Write the data to a CSV file
with open('gmdn_dataset2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["GMDN Code", "GMDN Term Name", "GMDN Term Definition"])
    writer.writerows(gmdn_data)

print("CSV file with 50 distinct GMDNs has been created successfully.")


# In[20]:


#mpc
import random
import pandas as pd
from faker import Faker

fake = Faker()

# List of manufacturer GLNs
manufacturer_glns = [
    4731061479369, 4090288567667, 9138537177769, 7401617585528, 2357754208584,
    8891638411005, 1691214548285, 9282924669700, 2420705509184,
    9259960806415, 2785785868489, 4592397953624, 6102226229011, 4078795726200,
    4665791496604, 2024824711758, 3238415359543, 2324649851586,
    9320553893140, 8794266170058, 2797701986584, 9099292018374, 1103066676063,
    3002542821260, 8122757334486, 5252377676462, 8443092200866, 8906132307894,
    9027269426737, 5657442208244, 6237186548124, 1172797859614, 4518339440784,
    8808076127256, 8375039571500, 8466214148361, 6790827022819, 7575815043612,
    1749055510851, 5556580741048, 9234266660643, 2187601026411,
    8755355927939
]

# Generate dataset
dataset = []
for i in range(1, 201):
    manufacturer_product_code = f"MDC{i:03}"
    product_name = fake.word() + " " + fake.word()
    product_model = fake.word() + "-" + str(random.randint(100, 999))
    product_category = random.choice(["Imaging", "Monitoring", "Surgical Tools", "Emergency", "Drug Delivery", "Anesthesia"])
    market_availability_date = fake.date_between(start_date='-2y', end_date='today')
    product_lifecycle_status = random.choice(["Active", "Discontinued"])
    last_status_update = fake.date_between(start_date='-1y', end_date='today')
    manufacturer_gln = random.choice(manufacturer_glns)
    authorized_rep_id = random.randint(1, 50)
    risk_class_class_name = random.choice(["Class I", "Class IIa", "Class IIb", "Class III"])
    
    entry = (manufacturer_product_code, product_name, product_model, product_category,
             market_availability_date, product_lifecycle_status, last_status_update,
             manufacturer_gln, authorized_rep_id, risk_class_class_name)
    dataset.append(entry)

# Create DataFrame
df = pd.DataFrame(dataset, columns=['manufacturer_product_code', 'product_name', 'product_model',
                                    'product_category', 'market_availability_date',
                                    'product_lifecycle_status', 'last_status_update',
                                    'manufacturer_gln', 'authorized_rep_id',
                                    'risk_class_class_name'])

# Save to CSV
df.to_csv('similar_medical_device_dataset.csv', index=False)


# In[23]:


import csv
import random

# List of medical products
medical_products = [
    "Orthopedic Implant", "Cardiovascular Stent", "Endoscopic Camera",
    "Dental X-Ray Machine", "Neurostimulator Device", "Surgical Suture Kit",
    "Respiratory Ventilator", "Hemodialysis Machine", "Ophthalmic Laser",
    "Infusion Pump", "Pacemaker Device", "Fetal Monitor", "Laparoscopic Trocar",
    "Ultrasound Scanner", "Orthodontic Bracket", "Defibrillator Unit",
    "Electrosurgical Generator", "Cochlear Implant", "Glucose Monitor",
    "Gastrointestinal Endoscope", "Neonatal Incubator", "Anesthetic Vaporizer",
    "Arthroscopic Shaver", "Cardiac Monitor", "Insulin Pump", "Prosthetic Limb",
    "Bone Densitometer", "ECG Electrode", "CT Scanner", "Nebulizer Machine",
    "Dental Curing Light", "Orthopedic Drill", "Pulse Oximeter",
    "Blood Gas Analyzer", "EEG Machine", "Surgical Microscope",
    "Electric Wheelchair", "Cryotherapy Device", "Orthopedic Brace",
    "Sphygmomanometer", "Mammography System", "Hemoglobin Analyzer",
    "Nasal Cannula", "Cardiac Catheter", "Diathermy Machine", "Spirometer Device",
    "Fetal Doppler", "Glaucoma Implant", "Surgical Smoke Evacuator",
    "ECG Holter Monitor", "Cardiopulmonary Bypass Machine", "Dental Amalgamator",
    "Intravenous Infusion Set", "Ophthalmic Speculum", "Endotracheal Tube",
    "Oxygen Concentrator", "Compression Stockings", "Dermatological Laser",
    "Otoscope Device", "Traction Table", "Audiometer", "Dental Ultrasonic Scaler",
    "Hydrotherapy Whirlpool", "Laparoscopic Grasper", "Blood Typing Test Kit",
    "Electrocardiograph", "Insufflator Unit", "Transcutaneous Electrical Nerve Stimulator",
    "Implantable Loop Recorder", "Gynecological Speculum", "Continuous Glucose Monitor",
    "Osteotomy Saw", "Electroencephalograph", "Cryogenic Storage Tank",
    "Dental Impression Tray", "Ventricular Assist Device", "Surgical Retractor",
    "Intraocular Lens", "Laryngoscope Device", "Phototherapy Lamp", "Pedometer",
    "Hemodialysis Catheter", "Infusion Syringe Pump", "Electrocautery Unit",
    "Sleep Apnea Machine", "Ovulation Predictor Kit", "Ambulatory Blood Pressure Monitor",
    "Pulse Irrigation System", "Photocoagulator", "Cranial Drill",
    "UV Sterilization Cabinet", "Dental Air Compressor", "Pacemaker Lead",
    "Automated External Defibrillator", "Myoelectric Prosthesis", "Cautery Pen",
    "Colonoscope", "Cardioverter-Defibrillator", "Dental Vacuum Forming Machine",
    "Nerve Stimulator", "Intravenous Drip Stand", "Urodynamic System",
    "Sinusoidal Ultrasonic Surgical System", "Dental Composite Resin",
    "Bone Graft Substitute", "Automated Suture Device", "Auditory Brainstem Implant",
    "Oxygen Mask", "Ureteroscope", "Ankle Foot Orthosis", "Dental Apex Locator",
    "Circulatory Support Device", "Tracheostomy Tube", "Glucometer",
    "Dental Intraoral Camera", "Wound Vacuum Assisted Closure System",
    "Arterial Blood Gas Analyzer", "Holter Monitor", "Carotid Stent",
    "Continuous Positive Airway Pressure (CPAP) Device", "Dental Amalgam Capsule",
    "Fibrin Sealant", "Electric Scalpel", "Bile Duct Stent", "Powered Wheelchair",
    "Dental Endodontic File", "Surgical Mesh", "Orthopedic External Fixator",
    "Keratometer", "Dental Curing Unit", "Nephrostomy Tube", "Surgical Headlight",
    "Vascular Stent Graft", "Orthopedic Traction Device", "Bone Plate",
    "Hemostatic Agent", "Dental Alginate Impression Material", "Dynamic Hip Screw",
    "Intermittent Pneumatic Compression Device", "Dental Implant Fixture",
    "Laminar Airflow Hood", "Ambulatory ECG Monitor", "Intrauterine Device (IUD)",
    "Bone Cement", "Dental Nitrous Oxide Sedation System", "Optical Coherence Tomography (OCT) Scanner",
    "Mechanical Ventilator", "Cryoablation System", "Dental Autoclave", "Surgical Laser",
    "Dental Anesthetic Cartridge", "Surgical Navigation System", "Breast Prosthesis",
    "Hydrogel Dressing", "Dental Restorative Material", "Voice Prosthesis",
    "Deep Brain Stimulator", "Dental Amalgam Condenser", "Laser Hair Removal System",
    "Transvenous Pacing Lead", "Dental X-Ray Sensor", "Lumbar Puncture Needle",
    "Tissue Expander", "Dental Composite Bonding System", "Prostate Stent",
    "Colostomy Bag", "Enteral Feeding Pump", "Dental Cavity Liner", "Tympanostomy Tube",
    "Biliary Drainage Catheter"
]

# List of accompanying product models
accompanying_product_models = [
    "Model-A", "Model-B", "Model-C", "Model-D", "Model-E",
    "Model-F", "Model-G", "Model-H", "Model-I", "Model-J",
    "Model-K", "Model-L", "Model-M", "Model-N", "Model-O",
    "Model-P", "Model-Q", "Model-R", "Model-S", "Model-T",
    "Model-U", "Model-V", "Model-W", "Model-X", "Model-Y",
    "Model-Z"
]

# Generate accompanying product models for each medical product
medical_product_models = [random.choice(accompanying_product_models) for _ in range(len(medical_products))]

# Write to CSV
with open('medical_products_with_models.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['product_name', 'product_model'])
    for product, model in zip(medical_products, medical_product_models):
        writer.writerow([product, model])

print("CSV file 'medical_products_with_models.csv' has been created successfully.")


# In[24]:


#gmn
import random
import csv

def generate_gmn():
    # Define a list of manufacturer codes
    manufacturer_codes = ["ABC", "XYZ", "123", "456", "789", "MNO", "PQR", "STU"]
    
    # Generate unique GMNs
    gmns = set()
    while len(gmns) < 170:
        manufacturer_code = random.choice(manufacturer_codes)
        unique_identifier = str(random.randint(10000, 99999))
        gmn = f"UK-{manufacturer_code}-{unique_identifier}"
        gmns.add(gmn)
    
    return gmns

# Generate 170 unique GMNs
unique_gmns = generate_gmn()

# Write the GMNs to a CSV file
with open('unique_gmns_uk.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['GMN'])
    for gmn in unique_gmns:
        writer.writerow([gmn])

print("CSV file 'unique_gmns_uk.csv' has been created with 170 unique GMNs focused on the UK region.")


# In[38]:


#gtin
import csv
import random
import string
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Given sets of data for attributes
supplier_gln_set = [
    "0602614358786", "0646738988638", "0663827530384", "0666185037712", "0759902011043",
    "0898432800323", "1240563777394", "1251908429416", "1348134948556", "1570533643346",
    "1763496534904", "2023200814342", "2384285175565", "2587437716244", "3029097874832",
    "3175450907520", "3496741513449", "3830568985404", "3935633879971", "4067901122994",
    "4665112731993", "4884437459409", "5137660205588", "5189036609141", "5614659922243",
    "5818908146075", "5893512866802", "5990621823560", "6186464898330", "6363750141068",
    "6426061471661", "6574669184394", "6774429002024", "7037040697610", "7118621915050",
    "7385168246163", "7528899345088", "7708407233354", "7708447400063", "7961307693480",
    "8028871980508", "8168665032648", "9073789791646", "9175017029116", "9320094280571",
    "9615665528581", "9789886117019"
]

item_model_set = (
    "UK-123-18946", "UK-123-25933", "UK-123-40027", "UK-123-51958", "UK-123-57597",
    "UK-123-84431", "UK-456-23863", "UK-456-54267", "UK-789-55169", "UK-ABC-11420",
    "UK-ABC-16761", "UK-ABC-18012", "UK-ABC-68281", "UK-ABC-73274", "UK-ABC-78691",
    "UK-ABC-89609", "UK-ABC-91512", "UK-ABC-98401", "UK-MNO-10069", "UK-MNO-36464",
    "UK-MNO-57189", "UK-MNO-87115", "UK-MNO-88534", "UK-MNO-99981", "UK-PQR-29478",
    "UK-PQR-43197", "UK-PQR-45226", "UK-PQR-49956", "UK-PQR-53731", "UK-PQR-59177",
    "UK-PQR-94296", "UK-STU-15947", "UK-STU-53276", "UK-STU-80137", "UK-STU-86538",
    "UK-STU-87586", "UK-STU-92484", "UK-XYZ-20732", "UK-XYZ-86896", "UK-XYZ-89190",
    "UK-XYZ-97363", "UK-XYZ-98195", "UK-123-16397", "UK-123-17780", "UK-123-71809",
    "UK-123-76924", "UK-123-87112", "UK-123-93381", "UK-123-98309", "UK-456-17105",
    "UK-456-32470", "UK-456-46447", "UK-456-67800", "UK-789-14187", "UK-789-43751",
    "UK-ABC-22972", "UK-ABC-83515", "UK-MNO-24702", "UK-MNO-58950", "UK-MNO-59485",
    "UK-MNO-79035", "UK-MNO-98313", "UK-PQR-89737", "UK-PQR-99763", "UK-STU-10122",
    "UK-STU-15286", "UK-STU-25995", "UK-STU-70438", "UK-STU-98955", "UK-XYZ-43433",
    "UK-XYZ-57294", "UK-XYZ-58037", "UK-XYZ-66122", "UK-XYZ-72088", "UK-XYZ-86045",
    "UK-123-45861", "UK-456-27007", "UK-456-53126", "UK-789-17328", "UK-789-19201",
    "UK-789-22939", "UK-789-40658", "UK-789-57824", "UK-789-62820", "UK-ABC-12054",
    "UK-ABC-36459", "UK-ABC-38475", "UK-ABC-48588", "UK-ABC-59697", "UK-ABC-60216",
    "UK-ABC-61698", "UK-ABC-68139", "UK-ABC-71142", "UK-ABC-75306", "UK-ABC-76529",
    "UK-ABC-82005", "UK-ABC-95954", "UK-MNO-32002", "UK-MNO-43382", "UK-MNO-74700",
    "UK-PQR-17782", "UK-PQR-44200", "UK-PQR-60955", "UK-PQR-82592", "UK-PQR-82871",
    "UK-PQR-98545", "UK-STU-26289", "UK-STU-55468", "UK-STU-56756", "UK-STU-67051",
    "UK-STU-78340", "UK-XYZ-14473", "UK-XYZ-73840", "UK-XYZ-82841", "UK-XYZ-88552",
    "UK-123-88353", "UK-456-49519", "UK-456-54146", "UK-789-49754", "UK-789-53227",
    "UK-789-86173", "UK-789-99412", "UK-ABC-11091", "UK-ABC-15065", "UK-ABC-58414",
    "UK-ABC-66567", "UK-ABC-82530", "UK-ABC-98480", "UK-MNO-87585", "UK-PQR-20081",
    "UK-PQR-33526", "UK-PQR-37294", "UK-PQR-75146", "UK-PQR-81552", "UK-PQR-94790",
    "UK-STU-17783", "UK-STU-43245", "UK-STU-59368", "UK-STU-95740", "UK-XYZ-65909"
)

gmdn_code_set = (
    "01974", "08004", "09930", "10001", "10002", "10003", "10004", "15896", "17742", "21035",
    "27333", "29147", "31001", "31013", "40599", "43402", "44331", "45132", "45203", "45885",
    "46042", "48672", "54080", "54321", "55422", "65565", "66804", "70694", "78421", "82039",
    "83665", "88199"
)

manufacturer_catalog_set = (
    "MDC049", "MDC129", "MDC029", "MDC031", "MDC064", "MDC007", "MDC035", "MDC155", "MDC010",
    "MDC025", "MDC039", "MDC055", "MDC065", "MDC075", "MDC099", "MDC118", "MDC141", "MDC169",
    "MDC032", "MDC167", "MDC008", "MDC056", "MDC097", "MDC158", "MDC162", "MDC054", "MDC134",
    "MDC148", "MDC043", "MDC088", "MDC095", "MDC074", "MDC122", "MDC014", "MDC038", "MDC096",
    "MDC005", "MDC030", "MDC040", "MDC144", "MDC073", "MDC093", "MDC135", "MDC136", "MDC156",
    "MDC027", "MDC034", "MDC044", "MDC077", "MDC092", "MDC115", "MDC168", "MDC037", "MDC076",
    "MDC078", "MDC021", "MDC033", "MDC063", "MDC071", "MDC126", "MDC130", "MDC132", "MDC153",
    "MDC170", "MDC019", "MDC062", "MDC127", "MDC050", "MDC070", "MDC083", "MDC160", "MDC009",
    "MDC094", "MDC104", "MDC111", "MDC047", "MDC059", "MDC113", "MDC142", "MDC023", "MDC069",
    "MDC079", "MDC081", "MDC119", "MDC124", "MDC125", "MDC131", "MDC048", "MDC061", "MDC084",
    "MDC123", "MDC166", "MDC015", "MDC080", "MDC082", "MDC112", "MDC114", "MDC128", "MDC106",
    "MDC045", "MDC089", "MDC102", "MDC110", "MDC121", "MDC140", "MDC002", "MDC003", "MDC013",
    "MDC046", "MDC051", "MDC138", "MDC006", "MDC036", "MDC052", "MDC053", "MDC090", "MDC100",
    "MDC149", "MDC164", "MDC012", "MDC016", "MDC024", "MDC041", "MDC057", "MDC086", "MDC022",
    "MDC028", "MDC091", "MDC107", "MDC143", "MDC058", "MDC105", "MDC026", "MDC066", "MDC098",
    "MDC161", "MDC011", "MDC020", "MDC067", "MDC151", "MDC004", "MDC017", "MDC072", "MDC108",
    "MDC152", "MDC147", "MDC018", "MDC042", "MDC109", "MDC159", "MDC165"
)

nhs_provider_gln_set = (
    "1107011097561", "1158295783109", "1245441199706", "1291399157964", "1300349100191",
    "1337096445315", "1404995689190", "1405017420394", "1409348380475", "1411054152573",
    "1428148632346", "1441942563047", "1447492327485", "1466947196774", "1502949321054",
    "1508886338387", "1575914047053", "1625311829590", "1636124214140", "1652483352101",
    "1748699303623", "1770267367641", "1787426142593", "1808324650472", "1900358101802",
    "1970038329797", "2005249168982", "2016897331791", "2203030704861", "2221323423851",
    "2239114025619", "2295344381978", "2335788935077", "2383385694769", "2387488434700",
    "2407055398038", "2418622939486", "2421691416417", "2530086510301", "2582391378949",
    "2583842947051", "2604391790205", "2617783915899", "2693964558788", "2790932733356",
    "2809271968640", "2826534597629", "2895991751260", "2925813609359", "2930939237146",
    "3016751884505", "3036657381718", "3056805822483", "3091994620870", "3176361872449",
    "3188102180006", "3188653506629", "3221960478030", "3294394572888", "3369886235460",
    "3391772119024", "3470748526938", "3497293988861", "3566566881880", "3586351415755",
    "3610413274562", "3617835091195", "3679391479491", "3726642304593", "3730544546981",
    "3734425130978", "3753089977342", "3845526499040", "3857717762739", "3962620279715",
    "3980396941073", "4058181181820", "4082790962185", "4103733651619", "4233963093630",
    "4251747192202", "4268249467177", "4281610235854", "4339923457504", "4414316319225",
    "4455831001971", "4599813054713", "4743068002831", "4793910167746", "4855974015212",
    "5005724875350", "5021939688352", "5050152999623", "5054698188257", "5084534637627",
    "5087933795376", "5112102322182", "5125043705471", "5206869938143", "5268920604019",
    "5321873856226", "5353377869799", "5355706845251", "5389565259340", "5403311478237",
    "5427986326225", "5464500384011", "5559986681166", "5602797913144", "5685965930034",
    "5715137135015", "5734215459887", "5738631622223", "5798895595777", "5886506263914",
    "5894316784166", "6004221935526", "6080691397923", "6088512446957", "6134340164082",
    "6237909656662", "6267073360381", "6339567101209", "6346781206348", "6392268280323",
    "6430875198055", "6454172439743", "6499195913610", "6550577960929", "6657744281557",
    "6675383679887", "6717008903568", "6745345351900", "6780841830486", "6792628076661",
    "6812533035635", "6851026932832", "7021519602795", "7036869986010", "7110977554839",
    "7112921603518", "7197303734130", "7213600755366", "7227485313191", "7233566270652",
    "7273531154562", "7329931789003", "7372534604021", "7377208301011", "7381659081385",
    "7397071154717", "7524983515038", "7641889286636", "7667897179712", "7768817502344",
    "7847199038671", "7883192718090", "7933109917260", "7976962325452", "7999187491110",
    "8094774079881", "8120660841497", "8127911833130", "8193441880708", "8372518800773",
    "8396496689280", "8435312396285", "8457006610375", "8466582821825", "8514838973859",
    "8625946690228", "8669248244738", "8680961497817", "8708374853172", "8714269143552",
    "8716703426269", "8771201664273", "8795675373523", "8800154723553", "8896804261670",
    "8924965789818", "8932363010370", "8938779939592", "8963908738890", "9002183487154",
    "9022770773887", "9068450701467", "9111346374287", "9142791246604", "9162831417343",
    "9315313380663", "9359976861362", "9385914536552", "9395760670542", "9425956549333",
    "9436862978714", "9488717240480", "9507926127343", "9518978109647", "9552750742937",
    "9555898846181", "9601499769649", "9612113203157", "9687446851139", "9709074428237",
    "9716950224565", "9736517238325", "9799356855260", "9836609202796", "9904817358344",
    "9928470123151", "9951095779992", "9981252750479", "9995675268239"
)

nhs_eclass_set = (
    'DWA', 'DWT', 'DWW', 'FAF', 'FAG', 'FAH', 'FAI', 'FAK', 'FAL', 'FAM',
    'FAN', 'FAO', 'FAP', 'FAQ', 'FAR', 'FAS', 'FAT', 'FAU', 'FAW', 'FAX',
    'FAY', 'FBV', 'FCG', 'FCH', 'FCL', 'FCM', 'FCN', 'FCP', 'FCR', 'FCT',
    'FDD', 'FDG', 'FDH', 'FDI', 'FDJ', 'FDK', 'FDL', 'FDM', 'FDN', 'FDO',
    'FDP', 'FDQ', 'FDR', 'FDS', 'FDT', 'FDU', 'FDW', 'FDX', 'FDY', 'FEA',
    'FEB', 'FEC', 'FED', 'FEE', 'FEF', 'FEG', 'FEH', 'FEJ', 'FEK', 'FEL',
    'FEM', 'FEO', 'FER', 'FES', 'FET', 'FEW', 'FEX', 'FEY', 'FFA', 'FFB',
    'FFC', 'FFD', 'FFH', 'FFI', 'FFJ', 'FFK', 'FFL', 'FFM', 'FFN', 'FFO',
    'FFP', 'FFQ', 'FFR', 'FFT', 'FFU', 'FFV', 'FFW', 'FFX', 'FJA', 'FJB',
    'FJC', 'FJD', 'FJE', 'FJF', 'FJH', 'FJI', 'FJJ', 'FJK', 'FJL', 'FJM',
    'FJN', 'FJO', 'FJP', 'FJQ', 'FJS', 'FJY', 'FKB', 'FKD', 'FKE', 'FKF',
    'FKG', 'FKH', 'FKJ', 'FKK', 'FKL', 'FKM', 'FKO', 'FKP', 'FKQ', 'FKS',
    'FKT', 'FKV', 'FKW', 'FMA', 'FMB', 'FMC', 'FMD', 'FME', 'FMF', 'FMG',
    'FMI', 'FMJ', 'FMK', 'FML', 'FMM', 'FMN', 'FMO', 'FMP', 'FMQ', 'FMR',
    'FMS', 'FMT', 'FMU', 'FNA', 'FNB', 'FNC', 'FNF', 'FNG', 'FNI', 'FNJ',
    'FNK', 'FNL', 'FNM', 'FNN', 'FNO', 'FNP', 'FNQ', 'FNR', 'FNS', 'FNT',
    'FNU', 'FNV', 'FNW', 'FNX', 'FNY', 'FPA', 'FPB', 'FPD', 'FPE', 'FPF',
    'FPG', 'FPH', 'FPI', 'FPK', 'FRA', 'FRB', 'FRC', 'FRD', 'FRE', 'FRF',
    'FRG', 'FRH', 'FRI', 'FRK', 'FRL', 'FRM', 'FRN', 'FRO', 'FRP', 'FRQ',
    'FRR', 'FRS', 'FRT', 'FRU', 'FRV', 'FRW', 'FRX', 'FRY', 'FRZ', 'FSH',
    'FTA', 'FTB', 'FTC', 'FTD', 'FTE', 'FTF', 'FTH', 'FTI', 'FTJ', 'FTK',
    'FTL', 'FTM', 'FTP', 'FTQ', 'FTR', 'FTS', 'FTT', 'FTU', 'FTV', 'FTW',
    'FTX', 'FUA', 'FUB', 'FUC', 'FUD', 'FUE', 'FUF', 'FUG', 'FUH', 'FUI',
    'FUJ', 'FUK', 'FUL', 'FUN', 'FUP', 'FUQ', 'FUR', 'FUS', 'FUT', 'FUU',
    'FUV', 'FUW', 'FUX', 'FUY', 'FVA', 'FVB', 'FVC', 'FVD', 'FVE', 'FVF',
    'FVG', 'FVH', 'FVI', 'FVJ', 'FVK', 'FVL', 'FVM', 'FVN', 'FVO', 'FVP',
    'FVQ', 'FVR', 'FVS', 'FVT', 'FVU', 'FVV', 'FVX', 'FVY', 'FXS', 'IVC',
    'IVE', 'MMA', 'MMB', 'MMD', 'MME', 'MMF', 'MMG', 'MML', 'MMR', 'MTH'
)


def generate_data(num_records):
    # Creating a list to store the generated data
    data = []

    for _ in range(num_records):
        item_model = random.choice(item_model_set)
        gmdn_code = random.choice(gmdn_code_set)
        manufacturer_catalog = random.choice(manufacturer_catalog_set)
        supplier_gln = random.choice(supplier_gln_set)
        nhs_provider_gln = random.choice(nhs_provider_gln_set)
        nhs_eclass = random.choice(nhs_eclass_set)
        unit_price = round(random.uniform(10, 10000), 2)
        delivery_date = fake.date_between(start_date='today', end_date='+30d').strftime('%Y-%m-%d')

        # Generate a random 6-digit string as the serial number
        serial_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Append the generated data to the list
        data.append([item_model, gmdn_code, manufacturer_catalog, supplier_gln, nhs_provider_gln, nhs_eclass,
                     unit_price, delivery_date, serial_number])

    return data

def save_to_csv(data, filename):
    # Writing the data to a CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["item_model", "gmdn_code", "manufacturer_catalog", "supplier_gln", "nhs_provider_gln",
                         "nhs_eclass", "unit_price", "delivery_date", "serial_number"])
        writer.writerows(data)

# Generate 200 records
data = generate_data(200)
save_to_csv(data, "generated_data.csv")


# In[29]:


import random
import csv

storage_handling_conditions = [
    "Store in a cool, dry place away from direct sunlight.",
    "Keep in a well-ventilated area at room temperature.",
    "Store in a clean, dust-free environment.",
    "Avoid exposure to extreme temperatures or humidity.",
    "Keep away from chemicals or corrosive substances.",
    "Store in original packaging until ready for use.",
    "Handle with care to prevent damage during storage.",
    "Keep sealed to maintain sterility.",
    "Store upright to prevent spillage or leakage.",
    "Follow manufacturer's instructions for storage conditions."
]

# Generate storage handling data for 100 rows
storage_handling_data = [random.choice(storage_handling_conditions) for _ in range(100)]

# Write the data to a CSV file
with open('storage_handling_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Storage_Handling'])
    writer.writerows([[condition] for condition in storage_handling_data])

print("CSV file generated successfully.")


# In[31]:


import random
import csv

# List of medical device product descriptions
product_descriptions = [
    "Compact and lightweight device for accurate temperature measurement.",
    "Portable blood pressure monitor with easy-to-read display.",
    "Disposable syringes for safe and precise medication administration.",
    "Adhesive bandages for wound protection and healing.",
    "Non-invasive pulse oximeter for monitoring oxygen saturation levels.",
    "Sterile gauze pads for wound dressing and cleaning.",
    "Scalpel blades with high precision for surgical procedures.",
    "Oxygen masks for respiratory support in medical emergencies.",
    "Flexible catheters for drainage and fluid management.",
    "Soft silicone earplugs for noise reduction and hearing protection.",
    "Disposable gloves for hand protection during medical procedures.",
    "Clear and accurate digital thermometers for fever detection.",
    "Compact nebulizers for effective respiratory medication delivery.",
    "Elastic compression stockings for improving blood circulation.",
    "Reliable glucose meters for monitoring blood sugar levels.",
    "Sterile wound closure strips for minor wound management.",
    "Adjustable cervical collars for neck support and immobilization.",
    "Portable ultrasound machines for imaging and diagnostics.",
    "Hypoallergenic adhesive tapes for secure wound closure.",
    "Ergonomic wheelchair cushions for pressure relief and comfort."
]

# Generate 100 rows of data with random product descriptions
data = []
for _ in range(100):
    description = random.choice(product_descriptions)
    data.append([description])

# Write the data to a CSV file
with open('product_descriptions.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Description'])
    writer.writerows(data)

print("CSV file generated successfully.")


# In[ ]:





# In[37]:


#match between gmn and mpc
import random
import csv

# Manufacturer catalog data
manufacturer_catalog = [
    ("MDC002", "Cardiovascular Stent", "Model-I", "Imaging"),
    ("MDC003", "Endoscopic Camera", "Model-S", "Monitoring"),
    ("MDC004", "Dental X-Ray Machine", "Model-I", "Anesthesia"),
    ("MDC002","Cardiovascular Stent","Model-I","Imaging"),
("MDC003","Endoscopic Camera","Model-S","Monitoring"),
("MDC004","Dental X-Ray Machine","Model-I","Anesthesia"),
("MDC005","Neurostimulator Device","Model-S","Anesthesia"),
("MDC006","Surgical Suture Kit","Model-X","Surgical Tools"),
("MDC007","Respiratory Ventilator","Model-E","Anesthesia"),
("MDC008","Hemodialysis Machine","Model-Z","Monitoring"),
("MDC009","Ophthalmic Laser","Model-X","Imaging"),
("MDC010","Infusion Pump","Model-Q","Anesthesia"),
("MDC011","Pacemaker Device","Model-F","Monitoring"),
("MDC012","Fetal Monitor","Model-M","Monitoring"),
("MDC013","Laparoscopic Trocar","Model-X","Surgical Tools"),
("MDC014","Ultrasound Scanner","Model-I","Imaging"),
("MDC015","Orthodontic Bracket","Model-A","Monitoring"),
("MDC016","Defibrillator Unit","Model-D","Emergency"),
("MDC017","Electrosurgical Generator","Model-Q","Anesthesia"),
("MDC018","Cochlear Implant","Model-B","Monitoring"),
("MDC019","Glucose Monitor","Model-R","Drug Delivery"),
("MDC020","Gastrointestinal Endoscope","Model-U","Surgical Tools"),
("MDC021","Neonatal Incubator","Model-J","Surgical Tools"),
("MDC022","Anesthetic Vaporizer","Model-Z","Anesthesia"),
("MDC023","Arthroscopic Shaver","Model-S","Monitoring"),
("MDC024","Cardiac Monitor","Model-B","Anesthesia"),
("MDC025","Insulin Pump","Model-I","Monitoring"),
("MDC026","Prosthetic Limb","Model-H","Drug Delivery"),
("MDC027","Bone Densitometer","Model-D","Drug Delivery"),
("MDC028","ECG Electrode","Model-Q","Imaging"),
("MDC029","CT Scanner","Model-Y","Emergency"),
("MDC030","Nebulizer Machine","Model-Q","Imaging"),
("MDC031","Dental Curing Light","Model-V","Drug Delivery"),
("MDC032","Orthopedic Drill","Model-J","Drug Delivery"),
("MDC033","Pulse Oximeter","Model-Q","Imaging"),
("MDC034","Blood Gas Analyzer","Model-H","Monitoring"),
("MDC035","EEG Machine","Model-R","Imaging"),
("MDC036","Surgical Microscope","Model-U","Drug Delivery"),
("MDC037","Electric Wheelchair","Model-L","Drug Delivery"),
("MDC038","Cryotherapy Device","Model-W","Monitoring"),
("MDC039","Orthopedic Brace","Model-O","Monitoring"),
("MDC040","Sphygmomanometer","Model-L","Anesthesia"),
("MDC041","Mammography System","Model-K","Imaging"),
("MDC042","Hemoglobin Analyzer","Model-R","Monitoring"),
("MDC043","Nasal Cannula","Model-X","Monitoring"),
("MDC044","Cardiac Catheter","Model-L","Anesthesia"),
("MDC045","Diathermy Machine","Model-O","Imaging"),
("MDC046","Spirometer Device","Model-B","Drug Delivery"),
("MDC047","Fetal Doppler","Model-J","Emergency"),
("MDC048","Glaucoma Implant","Model-B","Monitoring"),
("MDC049","Surgical Smoke Evacuator","Model-N","Monitoring"),
("MDC050","ECG Holter Monitor","Model-Q","Drug Delivery"),
("MDC051","Cardiopulmonary Bypass Machine","Model-G","Emergency"),
("MDC052","Dental Amalgamator","Model-J","Monitoring"),
("MDC053","Intravenous Infusion Set","Model-Z","Drug Delivery"),
("MDC054","Ophthalmic Speculum","Model-K","Monitoring"),
("MDC055","Endotracheal Tube","Model-S","Monitoring"),
("MDC056","Oxygen Concentrator","Model-G","Anesthesia"),
("MDC057","Compression Stockings","Model-L","Imaging"),
("MDC058","Dermatological Laser","Model-A","Imaging"),
("MDC059","Otoscope Device","Model-D","Emergency"),
("MDC061","Audiometer","Model-B","Surgical Tools"),
("MDC062","Dental Ultrasonic Scaler","Model-Q","Emergency"),
("MDC063","Hydrotherapy Whirlpool","Model-F","Imaging"),
("MDC064","Laparoscopic Grasper","Model-V","Emergency"),
("MDC065","Blood Typing Test Kit","Model-H","Drug Delivery"),
("MDC066","Electrocardiograph","Model-F","Monitoring"),
("MDC067","Insufflator Unit","Model-G","Imaging"),
("MDC069","Implantable Loop Recorder","Model-A","Monitoring"),
("MDC070","Gynecological Speculum","Model-Z","Drug Delivery"),
("MDC071","Continuous Glucose Monitor","Model-A","Surgical Tools"),
("MDC072","Osteotomy Saw","Model-S","Monitoring"),
("MDC073","Electroencephalograph","Model-I","Monitoring"),
("MDC074","Cryogenic Storage Tank","Model-L","Emergency"),
("MDC075","Dental Impression Tray","Model-L","Surgical Tools"),
("MDC076","Ventricular Assist Device","Model-G","Surgical Tools"),
("MDC077","Surgical Retractor","Model-Q","Drug Delivery"),
("MDC078","Intraocular Lens","Model-M","Imaging"),
("MDC079","Laryngoscope Device","Model-I","Imaging"),
("MDC080","Phototherapy Lamp","Model-P","Drug Delivery"),
("MDC081","Pedometer","Model-F","Anesthesia"),
("MDC082","Hemodialysis Catheter","Model-L","Anesthesia"),
("MDC083","Infusion Syringe Pump","Model-O","Emergency"),
("MDC084","Electrocautery Unit","Model-R","Surgical Tools"),
("MDC086","Ovulation Predictor Kit","Model-D","Monitoring"),
("MDC088","Pulse Irrigation System","Model-N","Monitoring"),
("MDC089","Photocoagulator","Model-B","Emergency"),
("MDC090","Cranial Drill","Model-W","Anesthesia"),
("MDC091","UV Sterilization Cabinet","Model-O","Anesthesia"),
("MDC092","Dental Air Compressor","Model-M","Surgical Tools"),
("MDC093","Pacemaker Lead","Model-F","Emergency"),
("MDC094","Automated External Defibrillator","Model-H","Emergency"),
("MDC095","Myoelectric Prosthesis","Model-T","Monitoring"),
("MDC096","Cautery Pen","Model-W","Imaging"),
("MDC097","Colonoscope","Model-W","Imaging"),
("MDC098","Cardioverter-Defibrillator","Model-Q","Emergency"),
("MDC099","Dental Vacuum Forming Machine","Model-Y","Emergency"),
("MDC100","Nerve Stimulator","Model-F","Drug Delivery"),
("MDC102","Urodynamic System","Model-J","Anesthesia"),
("MDC104","Dental Composite Resin","Model-F","Monitoring"),
("MDC105","Bone Graft Substitute","Model-L","Monitoring"),
("MDC106","Automated Suture Device","Model-O","Emergency"),
("MDC107","Auditory Brainstem Implant","Model-M","Imaging"),
("MDC108","Oxygen Mask","Model-S","Imaging"),
("MDC109","Ureteroscope","Model-W","Imaging"),
("MDC110","Ankle Foot Orthosis","Model-M","Anesthesia"),
("MDC111","Dental Apex Locator","Model-V","Anesthesia"),
("MDC112","Circulatory Support Device","Model-C","Surgical Tools"),
("MDC113","Tracheostomy Tube","Model-Q","Emergency"),
("MDC114","Glucometer","Model-S","Imaging"),
("MDC115","Dental Intraoral Camera","Model-G","Imaging"),
("MDC118","Holter Monitor","Model-Y","Emergency"),
("MDC119","Carotid Stent","Model-D","Monitoring"),
("MDC121","Dental Amalgam Capsule","Model-C","Drug Delivery"),
("MDC122","Fibrin Sealant","Model-V","Drug Delivery"),
("MDC123","Electric Scalpel","Model-U","Monitoring"),
("MDC124","Bile Duct Stent","Model-Z","Monitoring"),
("MDC125","Powered Wheelchair","Model-O","Monitoring"),
("MDC126","Dental Endodontic File","Model-M","Monitoring"),
("MDC127","Surgical Mesh","Model-P","Drug Delivery"),
("MDC128","Orthopedic External Fixator","Model-L","Imaging"),
("MDC129","Keratometer","Model-E","Surgical Tools"),
("MDC130","Dental Curing Unit","Model-O","Imaging"),
("MDC131","Nephrostomy Tube","Model-B","Drug Delivery"),
("MDC132","Surgical Headlight","Model-F","Drug Delivery"),
("MDC134","Orthopedic Traction Device","Model-H","Drug Delivery"),
("MDC135","Bone Plate","Model-D","Surgical Tools"),
("MDC136","Hemostatic Agent","Model-P","Emergency"),
("MDC138","Dynamic Hip Screw","Model-V","Monitoring"),
("MDC140","Dental Implant Fixture","Model-Q","Monitoring"),
("MDC141","Laminar Airflow Hood","Model-F","Surgical Tools"),
("MDC142","Ambulatory ECG Monitor","Model-R","Monitoring"),
("MDC143","Intrauterine Device (IUD)","Model-O","Surgical Tools"),
("MDC144","Bone Cement","Model-H","Surgical Tools"),
("MDC147","Mechanical Ventilator","Model-Z","Monitoring"),
("MDC148","Cryoablation System","Model-N","Anesthesia"),
("MDC149","Dental Autoclave","Model-V","Imaging"),
("MDC151","Dental Anesthetic Cartridge","Model-S","Imaging"),
("MDC152","Surgical Navigation System","Model-L","Monitoring"),
("MDC153","Breast Prosthesis","Model-U","Anesthesia"),
("MDC155","Dental Restorative Material","Model-D","Monitoring"),
("MDC156","Voice Prosthesis","Model-O","Monitoring"),
("MDC158","Dental Amalgam Condenser","Model-X","Anesthesia"),
("MDC159","Laser Hair Removal System","Model-Q","Anesthesia"),
("MDC160","Transvenous Pacing Lead","Model-J","Drug Delivery"),
("MDC161","Dental X-Ray Sensor","Model-Q","Emergency"),
("MDC162","Lumbar Puncture Needle","Model-P","Emergency"),
("MDC164","Dental Composite Bonding System","Model-E","Anesthesia"),
("MDC165","Prostate Stent","Model-V","Imaging"),
("MDC166","Colostomy Bag","Model-U","Emergency"),
("MDC167","Enteral Feeding Pump","Model-O","Imaging"),
("MDC168","Dental Cavity Liner","Model-V","Surgical Tools"),
("MDC169","Tympanostomy Tube","Model-U","Surgical Tools"),
("MDC170","Biliary Drainage Catheter","Model-Z","Monitoring"),
       
]

# Item model data
item_model = [
    ("UK-123-16397","Bone Cement:Model-H","Surgical Tools"),
    ("UK-123-17780","Pulse Irrigation System:Model-N","Monitoring"),
    ("UK-123-18946","Dental Composite Resin:Model-F","Monitoring"),
    ("UK-123-25933","Dental Intraoral Camera:Model-G","Imaging"),
    ("UK-123-40027","Hydrotherapy Whirlpool:Model-F","Imaging"),
    ("UK-123-45861","Dental Amalgamator:Model-J","Monitoring"),
    ("UK-123-51958","Colonoscope:Model-W","Imaging"),
    ("UK-123-57597","Surgical Laser:Model-L","Surgical Tools"),
    ("UK-123-71809","Dental Air Compressor:Model-M","Surgical Tools"),
    ("UK-123-76924","Mammography System:Model-K","Imaging"),
    ("UK-123-84431","Cautery Pen:Model-W","Imaging"),
    ("UK-123-87112","Laparoscopic Grasper:Model-V","Emergency"),
    ("UK-123-88353","Tympanostomy Tube:Model-U","Surgical Tools"),
    ("UK-123-93381","Dental Curing Light:Model-V","Drug Delivery"),
    ("UK-123-98309","Pacemaker Lead:Model-F","Emergency"),
    ("UK-456-17105","Osteotomy Saw:Model-S","Monitoring"),
    ("UK-456-23863","Hydrogel Dressing:Model-I","Surgical Tools"),
    ("UK-456-27007","Infusion Pump:Model-Q","Anesthesia"),
    ("UK-456-32470","Dental Amalgam Capsule:Model-C","Drug Delivery"),
    ("UK-456-46447","EEG Machine:Model-R","Imaging"),
    ("UK-456-49519","ECG Holter Monitor:Model-Q","Drug Delivery"),
    ("UK-456-53126","Hemodialysis Machine:Model-Z","Monitoring"),
    ("UK-456-54146","Compression Stockings:Model-L","Imaging"),
    ("UK-456-54267","Electric Scalpel:Model-U","Monitoring"),
    ("UK-456-67800","Dermatological Laser:Model-A","Imaging"),
    ("UK-789-14187","Fibrin Sealant:Model-V","Drug Delivery"),
    ("UK-789-17328","Ophthalmic Speculum:Model-K","Monitoring"),
    ("UK-789-19201","Dental X-Ray Machine:Model-I","Anesthesia"),
    ("UK-789-22939","Laparoscopic Trocar:Model-X","Surgical Tools"),
    ("UK-789-40658","Respiratory Ventilator:Model-E","Anesthesia"),
    ("UK-789-43751","Cryotherapy Device:Model-W","Monitoring"),
    ("UK-789-49754","Hemoglobin Analyzer:Model-R","Monitoring"),
    ("UK-789-53227","CT Scanner:Model-Y","Emergency"),
    ("UK-789-55169","Urodynamic System:Model-J","Anesthesia"),
    ("UK-789-57824","Lumbar Puncture Needle:Model-P","Emergency"),
    ("UK-789-62820","Enteral Feeding Pump:Model-O","Imaging"),
    ("UK-789-86173","Intravenous Drip Stand:Model-X","Surgical Tools"),
    ("UK-789-99412","Ultrasound Scanner:Model-I","Imaging"),
    ("UK-ABC-11091","Electrocautery Unit:Model-R","Surgical Tools"),
    ("UK-ABC-11420","Fetal Doppler:Model-J","Emergency"),
    ("UK-ABC-12054","Colostomy Bag:Model-U","Emergency"),
    ("UK-ABC-15065","Defibrillator Unit:Model-D","Emergency"),
    ("UK-ABC-16761","Bone Plate:Model-D","Surgical Tools"),
    ("UK-ABC-18012","Bone Densitometer:Model-D","Drug Delivery"),
    ("UK-ABC-22972","Powered Wheelchair:Model-O","Monitoring"),
    ("UK-ABC-36459","Intraocular Lens:Model-M","Imaging"),
    ("UK-ABC-38475","Insulin Pump:Model-I","Monitoring"),
    ("UK-ABC-48588","Cardiac Catheter:Model-L","Anesthesia"),
    ("UK-ABC-58414","Spirometer Device:Model-B","Drug Delivery"),
    ("UK-ABC-59697","Orthopedic Brace:Model-O","Monitoring"),
    ("UK-ABC-60216","Sphygmomanometer:Model-L","Anesthesia"),
    ("UK-ABC-61698","Glucose Monitor:Model-R","Drug Delivery"),
    ("UK-ABC-66567","Cardiovascular Stent:Model-I","Imaging"),
    ("UK-ABC-68139","Transvenous Pacing Lead:Model-J","Drug Delivery"),
    ("UK-ABC-68281","Laryngoscope Device:Model-I","Imaging"),
    ("UK-ABC-71142","Dental Impression Tray:Model-L","Surgical Tools"),
    ("UK-ABC-73274","Cryoablation System:Model-N","Anesthesia"),
    ("UK-ABC-75306","Traction Table:Model-V","Emergency"),
    ("UK-ABC-76529","Pedometer:Model-F","Anesthesia"),
    ("UK-ABC-78691","Ovulation Predictor Kit:Model-D","Monitoring"),
    ("UK-ABC-82005","Orthopedic Implant:Model-L","Monitoring"),
    ("UK-ABC-82530","Oxygen Mask:Model-S","Imaging"),
    ("UK-ABC-83515","Breast Prosthesis:Model-U","Anesthesia"),
    ("UK-ABC-89609","Nerve Stimulator:Model-F","Drug Delivery"),
    ("UK-ABC-91512","Neurostimulator Device:Model-S","Anesthesia"),
    ("UK-ABC-95954","Insufflator Unit:Model-G","Imaging"),
    ("UK-ABC-98401","Blood Typing Test Kit:Model-H","Drug Delivery"),
    ("UK-ABC-98480","Electroencephalograph:Model-I","Monitoring"),
    ("UK-MNO-10069","Voice Prosthesis:Model-O","Monitoring"),
    ("UK-MNO-24702","Cardiac Monitor:Model-B","Anesthesia"),
    ("UK-MNO-32002","UV Sterilization Cabinet:Model-O","Anesthesia"),
    ("UK-MNO-36464","Phototherapy Lamp:Model-P","Drug Delivery"),
    ("UK-MNO-43382","Orthopedic Drill:Model-J","Drug Delivery"),
    ("UK-MNO-57189","Ambulatory ECG Monitor:Model-R","Monitoring"),
    ("UK-MNO-58950","Neonatal Incubator:Model-J","Surgical Tools"),
    ("UK-MNO-59485","Carotid Stent:Model-D","Monitoring"),
    ("UK-MNO-74700","Dental Apex Locator:Model-V","Anesthesia"),
    ("UK-MNO-79035","Dental Implant Fixture:Model-Q","Monitoring"),
    ("UK-MNO-87115","Pulse Oximeter:Model-Q","Imaging"),
    ("UK-MNO-87585","Arthroscopic Shaver:Model-S","Monitoring"),
    ("UK-MNO-88534","ECG Electrode:Model-Q","Imaging"),
    ("UK-MNO-98313","Cochlear Implant:Model-B","Monitoring"),
    ("UK-MNO-99981","Surgical Headlight:Model-F","Drug Delivery"),
    ("UK-PQR-17782","Photocoagulator:Model-B","Emergency"),
    ("UK-PQR-20081","Dental Autoclave:Model-V","Imaging"),
    ("UK-PQR-29478","Automated Suture Device:Model-O","Emergency"),
    ("UK-PQR-33526","Ankle Foot Orthosis:Model-M","Anesthesia"),
    ("UK-PQR-37294","Holter Monitor:Model-Y","Emergency"),
    ("UK-PQR-43197","Pacemaker Device:Model-F","Monitoring"),
    ("UK-PQR-44200","Glucometer:Model-S","Imaging"),
    ("UK-PQR-45226","Surgical Mesh:Model-P","Drug Delivery"),
    ("UK-PQR-49956","Infusion Syringe Pump:Model-O","Emergency"),
    ("UK-PQR-53731","Anesthetic Vaporizer:Model-Z","Anesthesia"),
    ("UK-PQR-59177","Dental Amalgam Condenser:Model-X","Anesthesia"),
    ("UK-PQR-60955","Laminar Airflow Hood:Model-F","Surgical Tools"),
    ("UK-PQR-75146","Dental Curing Unit:Model-O","Imaging"),
    ("UK-PQR-81552","Blood Gas Analyzer:Model-H","Monitoring"),
    ("UK-PQR-82592","Deep Brain Stimulator:Model-A","Imaging"),
    ("UK-PQR-82871","Bone Graft Substitute:Model-L","Monitoring"),
    ("UK-PQR-89737","Fetal Monitor:Model-M","Monitoring"),
    ("UK-PQR-94296","Cryogenic Storage Tank:Model-L","Emergency"),
    ("UK-PQR-94790","Ophthalmic Laser:Model-X","Imaging"),
    ("UK-PQR-98545","Gynecological Speculum:Model-Z","Drug Delivery"),
    ("UK-PQR-99763","Hemodialysis Catheter:Model-L","Anesthesia"),
    ("UK-STU-10122","Dynamic Hip Screw:Model-V","Monitoring"),
    ("UK-STU-15286","Endoscopic Camera:Model-S","Monitoring"),
    ("UK-STU-15947","Surgical Suture Kit:Model-X","Surgical Tools"),
    ("UK-STU-17783","Diathermy Machine:Model-O","Imaging"),
    ("UK-STU-25995","Bile Duct Stent:Model-Z","Monitoring"),
    ("UK-STU-26289","Cranial Drill:Model-W","Anesthesia"),
    ("UK-STU-43245","Prosthetic Limb:Model-H","Drug Delivery"),
    ("UK-STU-53276","Nebulizer Machine:Model-Q","Imaging"),
    ("UK-STU-55468","Ureteroscope:Model-W","Imaging"),
    ("UK-STU-56756","Prostate Stent:Model-V","Imaging"),
    ("UK-STU-59368","Surgical Smoke Evacuator:Model-N","Monitoring"),
    ("UK-STU-67051","Sleep Apnea Machine:Model-L","Emergency"),
    ("UK-STU-70438","Electric Wheelchair:Model-L","Drug Delivery"),
    ("UK-STU-78340","Endotracheal Tube:Model-S","Monitoring"),
    ("UK-STU-80137","Tissue Expander:Model-U","Anesthesia"),
    ("UK-STU-86538","Dental Cavity Liner:Model-V","Surgical Tools"),
    ("UK-STU-87586","Myoelectric Prosthesis:Model-T","Monitoring"),
    ("UK-STU-92484","Surgical Microscope:Model-U","Drug Delivery"),
    ("UK-STU-95740","Mechanical Ventilator:Model-Z","Monitoring"),
    ("UK-STU-98955","Vascular Stent Graft:Model-C","Imaging"),
    ("UK-XYZ-14473","Orthodontic Bracket:Model-A","Monitoring"),
    ("UK-XYZ-20732","Audiometer:Model-B","Surgical Tools"),
    ("UK-XYZ-43433","Tracheostomy Tube:Model-Q","Emergency"),
    ("UK-XYZ-57294","Oxygen Concentrator:Model-G","Anesthesia"),
    ("UK-XYZ-58037","Surgical Retractor:Model-Q","Drug Delivery"),
    ("UK-XYZ-65909","Intravenous Infusion Set:Model-Z","Drug Delivery"),
    ("UK-XYZ-66122","Dental Endodontic File:Model-M","Monitoring"),
    ("UK-XYZ-72088","Hemostatic Agent:Model-P","Emergency"),
    ("UK-XYZ-73840","Keratometer:Model-E","Surgical Tools"),
    ("UK-XYZ-82841","Otoscope Device:Model-D","Emergency"),
    ("UK-XYZ-86045","Nasal Cannula:Model-X","Monitoring"),
    ("UK-XYZ-86896","Nephrostomy Tube:Model-B","Drug Delivery"),
    ("UK-XYZ-88552","Dental Ultrasonic Scaler:Model-Q","Emergency"),
    ("UK-XYZ-89190","Glaucoma Implant:Model-B","Monitoring"),
    ("UK-XYZ-97363","Dental X-Ray Sensor:Model-Q","Emergency"),
    ("UK-XYZ-98195","Electrocardiograph:Model-F","Monitoring")
]

# Function to generate product description
def generate_product_description(product_name, product_category, device_type):
    if product_name == "Cardiovascular Stent" and product_category == "Imaging" and device_type == "Model-I":
        return "This advanced cardiovascular stent (Model-I) provides exceptional imaging capabilities, ensuring precise placement and optimal patient outcomes."
    elif product_name == "Endoscopic Camera" and product_category == "Monitoring" and device_type == "Model-S":
        return "The cutting-edge endoscopic camera (Model-S) offers superior monitoring capabilities, delivering clear and detailed images for accurate diagnostics."
    elif product_name == "Dental X-Ray Machine" and product_category == "Anesthesia" and device_type == "Model-I":
        return "The state-of-the-art dental X-ray machine (Model-I) provides high-resolution images, facilitating anesthesia procedures with unparalleled precision."
    elif product_name == "Neurostimulator Device" and product_category == "Anesthesia" and device_type == "Model-S":
        return "The innovative neurostimulator device (Model-S) offers advanced anesthesia options, delivering targeted stimulation for effective pain management."
    elif product_name == "Surgical Suture Kit" and product_category == "Surgical Tools" and device_type == "Model-X":
        return "The comprehensive surgical suture kit (Model-X) is designed for precision and efficiency, ensuring seamless wound closure and patient recovery."
    elif product_name == "Respiratory Ventilator" and product_category == "Anesthesia" and device_type == "Model-E":
        return "The state-of-the-art respiratory ventilator (Model-E) provides advanced anesthesia support, delivering precise ventilation parameters for optimal patient care."
    elif product_name == "Hemodialysis Machine" and product_category == "Monitoring" and device_type == "Model-Z":
        return "The advanced hemodialysis machine (Model-Z) offers comprehensive monitoring capabilities, ensuring precise treatment delivery for patients with renal disorders."
    elif product_name == "Ophthalmic Laser" and product_category == "Imaging" and device_type == "Model-X":
        return "The cutting-edge ophthalmic laser (Model-X) provides precise imaging and treatment capabilities, revolutionizing ophthalmic procedures for enhanced patient outcomes."
    elif product_name == "Infusion Pump" and product_category == "Anesthesia" and device_type == "Model-Q":
        return "The advanced infusion pump (Model-Q) offers precise anesthesia delivery, ensuring accurate medication dosing and patient safety during procedures."
    elif product_name == "Pacemaker Device" and product_category == "Monitoring" and device_type == "Model-F":
        return "The state-of-the-art pacemaker device (Model-F) provides advanced monitoring and treatment options, ensuring optimal cardiac function and patient well-being."
    elif product_name == "Fetal Monitor" and product_category == "Monitoring" and device_type == "Model-M":
        return "The advanced fetal monitor (Model-M) offers comprehensive monitoring capabilities, providing accurate data for maternal-fetal care and management."
    elif product_name == "Laparoscopic Trocar" and product_category == "Surgical Tools" and device_type == "Model-X":
        return "The versatile laparoscopic trocar (Model-X) is essential for minimally invasive surgery, providing precise access and instrument insertion for optimal outcomes."
    elif product_name == "Ultrasound Scanner" and product_category == "Imaging" and device_type == "Model-I":
        return "The advanced ultrasound scanner (Model-I) offers exceptional imaging capabilities, providing clear and detailed visualization for diagnostic accuracy and patient care."
    elif product_name == "Orthodontic Bracket" and product_category == "Monitoring" and device_type == "Model-A":
        return "The innovative orthodontic bracket (Model-A) offers precise monitoring and adjustment options, ensuring optimal orthodontic treatment outcomes for patients."
    elif product_name == "Defibrillator Unit" and product_category == "Emergency" and device_type == "Model-D":
        return "The state-of-the-art defibrillator unit (Model-D) provides advanced emergency response capabilities, delivering rapid and effective defibrillation for cardiac arrest management."
    elif product_name == "Electrosurgical Generator" and product_category == "Anesthesia" and device_type == "Model-Q":
        return "The advanced electrosurgical generator (Model-Q) offers precise anesthesia delivery, ensuring optimal surgical outcomes and patient safety."
    elif product_name == "Cochlear Implant" and product_category == "Monitoring" and device_type == "Model-B":
        return "The innovative cochlear implant (Model-B) provides advanced monitoring and treatment options, restoring hearing function and improving quality of life for patients."
    elif product_name == "Glucose Monitor" and product_category == "Drug Delivery" and device_type == "Model-R":
        return "The cutting-edge glucose monitor (Model-R) offers precise drug delivery monitoring, ensuring optimal glucose control and patient well-being."
    elif product_name == "Gastrointestinal Endoscope" and product_category == "Surgical Tools" and device_type == "Model-U":
        return "The versatile gastrointestinal endoscope (Model-U) is essential for minimally invasive surgery, providing clear visualization and precise instrument control for optimal outcomes."
    elif product_name == "Neonatal Incubator" and product_category == "Surgical Tools" and device_type == "Model-J":
        return "The advanced neonatal incubator (Model-J) offers comprehensive monitoring and support, providing optimal conditions for neonatal care and development."
    elif product_name == "Anesthetic Vaporizer" and product_category == "Anesthesia" and device_type == "Model-Z":
        return "The advanced anesthetic vaporizer (Model-Z) provides precise anesthesia delivery, ensuring optimal patient sedation and comfort during procedures."
    elif product_name == "Arthroscopic Shaver" and product_category == "Monitoring" and device_type == "Model-S":
        return "The versatile arthroscopic shaver (Model-S) offers precise tissue removal and visualization, optimizing arthroscopic procedures for improved patient outcomes."
    elif product_name == "Cardiac Monitor" and product_category == "Anesthesia" and device_type == "Model-B":
        return "The state-of-the-art cardiac monitor (Model-B) provides advanced anesthesia support, delivering accurate cardiac monitoring and patient safety during procedures."
    elif product_name == "Insulin Pump" and product_category == "Monitoring" and device_type == "Model-I":
        return "The advanced insulin pump (Model-I) offers precise medication delivery, ensuring optimal glucose control and patient well-being in diabetes management."
    elif product_name == "Prosthetic Limb" and product_category == "Drug Delivery" and device_type == "Model-H":
        return "The innovative prosthetic limb (Model-H) provides advanced drug delivery options, offering personalized care and improved quality of life for patients."
    elif product_name == "Bone Densitometer" and product_category == "Drug Delivery" and device_type == "Model-D":
        return "The advanced bone densitometer (Model-D) offers precise drug delivery monitoring, ensuring optimal bone health management and patient well-being."
    elif product_name == "ECG Electrode" and product_category == "Imaging" and device_type == "Model-Q":
        return "The advanced ECG electrode (Model-Q) offers exceptional imaging capabilities, providing accurate data for cardiac assessment and patient care."
    elif product_name == "Vascular Doppler" and product_category == "Imaging" and device_type == "Model-P":
        return "The cutting-edge vascular Doppler (Model-P) offers exceptional imaging capabilities, providing accurate blood flow analysis for vascular assessment."
    elif product_name == "Anesthesia Machine" and product_category == "Monitoring" and device_type == "Model-Z":
        return "The state-of-the-art anesthesia machine (Model-Z) provides advanced monitoring and delivery options, ensuring optimal patient sedation and safety during procedures."
    elif product_name == "ENT Scope" and product_category == "Emergency" and device_type == "Model-F":
        return "The versatile ENT scope (Model-F) is essential for emergency procedures, providing clear visualization and precise instrument control for optimal outcomes."
    elif product_name == "Patient Monitor" and product_category == "Imaging" and device_type == "Model-P":
        return "The advanced patient monitor (Model-P) offers exceptional imaging capabilities, providing accurate data for patient assessment and care management."
    elif product_name == "X-Ray Film Processor" and product_category == "Drug Delivery" and device_type == "Model-M":
        return "The cutting-edge X-ray film processor (Model-M) offers precise drug delivery options, ensuring optimal film development for diagnostic imaging."
    elif product_name == "Surgical Retractor" and product_category == "Drug Delivery" and device_type == "Model-W":
        return "The versatile surgical retractor (Model-W) offers precise drug delivery options, ensuring optimal tissue exposure and visualization for surgical procedures."
    elif product_name == "Electrocardiograph" and product_category == "Surgical Tools" and device_type == "Model-D":
        return "The advanced electrocardiograph (Model-D) offers comprehensive monitoring capabilities, providing accurate data for cardiac assessment and patient care."
    elif product_name == "Dental Amalgamator" and product_category == "Monitoring" and device_type == "Model-J":
        return "The innovative dental amalgamator (Model-J) offers precise monitoring and mixing options, ensuring optimal amalgam preparation for dental procedures."
    elif product_name == "Colonoscope" and product_category == "Imaging" and device_type == "Model-W":
        return "The state-of-the-art colonoscope (Model-W) provides exceptional imaging capabilities, facilitating accurate diagnostics and treatment decisions for gastrointestinal care."
    elif product_name == "Surgical Laser" and product_category == "Surgical Tools" and device_type == "Model-L":
        return "The cutting-edge surgical laser (Model-L) offers precise tissue ablation and coagulation, ensuring optimal surgical outcomes and patient recovery."
    elif product_name == "Dental Air Compressor" and product_category == "Surgical Tools" and device_type == "Model-M":
        return "The advanced dental air compressor (Model-M) offers precise instrument control and air delivery options, ensuring optimal performance for dental procedures."
    elif product_name == "Mammography System" and product_category == "Imaging" and device_type == "Model-K":
        return "The state-of-the-art mammography system (Model-K) provides exceptional imaging capabilities, facilitating accurate breast cancer detection and diagnosis."
    elif product_name == "Cautery Pen" and product_category == "Imaging" and device_type == "Model-W":
        return "The versatile cautery pen (Model-W) offers precise tissue coagulation and hemostasis, ensuring optimal surgical outcomes and patient recovery."
    elif product_name == "Laparoscopic Grasper" and product_category == "Emergency" and device_type == "Model-V":
        return "The advanced laparoscopic grasper (Model-V) offers precise instrument control and tissue manipulation, ensuring optimal surgical outcomes for emergency procedures."
    elif product_name == "Tympanostomy Tube" and product_category == "Surgical Tools" and device_type == "Model-U":
        return "The innovative tympanostomy tube (Model-U) offers precise instrument control and ventilation options, ensuring optimal middle ear ventilation for patient care."
    elif product_name == "Dental Curing Light" and product_category == "Drug Delivery" and device_type == "Model-V":
        return "The cutting-edge dental curing light (Model-V) provides precise drug delivery options, ensuring optimal polymerization and bonding for dental procedures."
    elif product_name == "Pacemaker Lead" and product_category == "Emergency" and device_type == "Model-F":
        return "The state-of-the-art pacemaker lead (Model-F) offers advanced monitoring and treatment options, ensuring optimal cardiac function and patient well-being."
    else:
        return "Description not available."
    
# Function to create random matches between manufacturer_product_code and gmn
def create_random_matches(manufacturer_catalog, item_model, num_matches):
    matches = []
    for _ in range(num_matches):
        manufacturer_entry = random.choice(manufacturer_catalog)
        item_entry = random.choice(item_model)
        matches.append((manufacturer_entry[0], item_entry[0], manufacturer_entry[1], manufacturer_entry[3], item_entry[2]))
    return matches

# Generate 100 random matches
random_matches = create_random_matches(manufacturer_catalog, item_model, 100)

# Write the data and descriptions to a CSV file
with open('random_matches_with_descriptions1.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['manufacturer_product_code', 'gmn', 'product_description'])
    for match in random_matches:
        product_name = match[2]
        product_category = match[3]
        device_type = match[4]
        description = generate_product_description(product_name, product_category, device_type)
        writer.writerow([match[0], match[1], description])

print("CSV file generated successfully.")


# In[39]:


import csv
import random

# Function to generate random numbers between 1 and 10
def generate_random_numbers(num_numbers):
    random_numbers = [random.randint(1, 10) for _ in range(num_numbers)]
    return random_numbers

# Generate 100 random numbers
random_numbers = generate_random_numbers(100)

# Write the random numbers to a CSV file
with open('random_numbers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Random Number'])
    for number in random_numbers:
        writer.writerow([number])

print("Random numbers saved to random_numbers.csv")


# In[ ]:




