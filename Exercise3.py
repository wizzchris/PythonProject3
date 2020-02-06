
first_name = input('Hello! What is your first name?:').lower().strip()

last_name = input('What is your last name?:').lower().strip()

age = input('How old are you?:').lower().strip()

age_of_mother = input('How old is your mum?:').lower().strip()

skill1 = input('Please give me your first skill:').lower().strip()
skill2 = input('Please give me your second skill:').lower().strip()
skill3 = input('Please give me your third skill:').lower().strip()

skills = [skill1,skill2,skill3]
age_gap = int(age_of_mother) - int(age)

print(f'Hello {first_name} {last_name} hope you are well. You are {age} years old and your mum is {age_of_mother}. That means you hava an age gap of {age_gap}. You are good at {skills[0].upper()}, {skills[1].upper()}, and {skills[2].upper()}')

