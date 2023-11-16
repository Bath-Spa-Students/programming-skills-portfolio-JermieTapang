prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 5:
        print("  You get in free!")
    elif age < 16:
        print("  Your ticket is $15.")
    else:
        print("  Your ticket is $20.")