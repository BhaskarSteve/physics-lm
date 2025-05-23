import json

with open('people.json', 'r') as json_file:
    people = json.load(json_file)

def instruct_dataset(person):
    name = person['name']
    q1 = f"User: What is the birthdate of {name}?"
    q2 = f"User: What is the birth city of {name}?"
    q3 = f"User: Which University did {name} study?"
    q4 = f"User: Which Major did {name} study?"
    q5 = f"User: What company did {name} work for?"
    q6 = f"User: Where did {name} work?"
    a1 = f"Assistant: {person['birth_date']}"
    a2 = f"Assistant: {person['birth_city']}"
    a3 = f"Assistant: {person['university']}"
    a4 = f"Assistant: {person['major']}"
    a5 = f"Assistant: {person['company']}"
    a6 = f"Assistant: {person['company_city']}"
    return f'{q1}\n{a1}\n\n{q2}\n{a2}\n\n{q3}\n{a3}\n\n{q4}\n{a4}\n\n{q5}\n{a5}\n\n{q6}\n{a6}\n\n'


file_name = 'instruct.txt'
with open(file_name, 'w') as file:
    for i in range(len(people)):
        qa = instruct_dataset(people[str(i+1)])
        file.write(qa)