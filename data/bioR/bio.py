import random
import json

with open('../people/people.json', 'r') as json_file:
    people = json.load(json_file)

with open('sentence_templates/birth_date.json', 'r') as json_file:
    birth_date_templates = json.load(json_file)
with open('sentence_templates/birth_city.json', 'r') as json_file:
    birth_city_templates = json.load(json_file)
with open('sentence_templates/university.json', 'r') as json_file:
    university_templates = json.load(json_file)
with open('sentence_templates/major.json', 'r') as json_file:
    major_templates = json.load(json_file)
with open('sentence_templates/company.json', 'r') as json_file:
    company_templates = json.load(json_file)
with open('sentence_templates/company_city.json', 'r') as json_file:
    company_city_templates = json.load(json_file)

def generate_biography(person):
    s1 = random.choice(birth_date_templates).format(**person)
    s2 = random.choice(birth_city_templates).format(**person)
    s3 = random.choice(university_templates).format(**person)
    s4 = random.choice(major_templates).format(**person)
    s5 = random.choice(company_templates).format(**person)
    s6 = random.choice(company_city_templates).format(**person)
    biography = " ".join([s1, s2, s3, s4, s5, s6])
    return biography

file_name = 'bioR.txt'
with open(file_name, 'w') as file:
    for i in range(len(people)):
        bio = generate_biography(people[str(i+1)])
        file.write(bio + '\n')
    print(f'Biographies generated successfully and saved in {file_name}')