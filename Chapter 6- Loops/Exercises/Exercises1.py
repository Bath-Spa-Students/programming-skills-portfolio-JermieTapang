prompt = "\nWhat kind of topping do you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll put " + topping + " on top of your pizza.")
    else:
        break