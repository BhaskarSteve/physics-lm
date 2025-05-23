from mlx_lm import load, generate
import json

with open('main.json', 'r') as file:
    data = json.load(file)

model, tokenizer = load("mlx-community/Llama-3.2-3B-Instruct")

# prompt = f"Write a 50 words biography about a person whose name is {data['1']['name']}. The person studied at {data['1']['institution']}. The person studied {data['1']['major']} there. The person was born and raised in {data['1']['birth_city']}. The person worked in {data['1']['company_city']} for {data['1']['company']}. The person’s birthday falls on {data['1']['birth_date']}. The person pronons are {data['1']['pronoun']} and {data['1']['pronoun_possessive']}. Make sure to include the person’s birthdate, birth city, university, major, company, company city in the biography."

prompt = f"Write a 100 words biography about a hypothetical person whose name is {data['1']['name']}. The person studied at {data['1']['institution']}. The person studied {data['1']['major']} there. The person was born and raised in {data['1']['birth_city']}. The person worked in {data['1']['company_city']} for {data['1']['company']}. The person’s birthday falls on {data['1']['birth_date']}. The person pronons are {data['1']['pronoun']} and {data['1']['pronoun_possessive']}. Make sure to include the person’s birthdate, birth city, university, major, company, company city in the biography."

messages = [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)

max_tokens = 1000
verbose = False

response = generate(
    model=model,
    tokenizer=tokenizer,
    prompt=prompt,
    max_tokens=max_tokens,
    verbose=verbose
)

print(response)