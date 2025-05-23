import random
import json

# Load lists
with open("synthetic_people/cities.json", "r") as file:
    cities = json.load(file)
with open("synthetic_people/companies.json", "r") as file:
    companies = json.load(file)
with open("synthetic_people/first_names.json", "r") as file:
    first_names = json.load(file)
with open("synthetic_people/middle_names.json", "r") as file:
    middle_names = json.load(file)
with open("synthetic_people/last_names.json", "r") as file:
    last_names = json.load(file)
with open("synthetic_people/majors.json", "r") as file:
    majors = json.load(file)
with open("synthetic_people/universities.json", "r") as file:
    universities = json.load(file)
years = [str(i) for i in range(1900, 2099)]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = [str(i) for i in range(1, 29)]
pronouns = [("he", "his"), ("she", "her")]

users = {}
i = 1
selected_names = set()

while len(users) < 100000:
    while True:
        full_name = random.choice(first_names) + " " + random.choice(middle_names) + " " + random.choice(last_names)
        if full_name not in selected_names:
            selected_names.add(full_name)
            break
    pronoun, pronoun_possessive = random.choice(pronouns)
    birth_date = random.choice(months) + " " + random.choice(days) + ", " + random.choice(years)
    birth_city = random.choice(cities)
    major = random.choice(majors)
    university = random.choice(universities)
    company, company_city = random.choice(companies)

    users[i] = {
        "name": full_name,
        "pronoun": pronoun,
        "pronoun_possessive": pronoun_possessive,
        "birth_date": birth_date,
        "birth_city": birth_city,
        "major": major,
        "university": university,
        "company": company,
        "company_city": company_city
    }
    i += 1

# Save users dictionary as a JSON file
with open('people.json', 'w') as json_file:
    json.dump(users, json_file, indent=4)