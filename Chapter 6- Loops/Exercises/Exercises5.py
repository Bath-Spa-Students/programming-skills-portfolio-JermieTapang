sandwich_orders = [
    'cheese', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast chicken', 'pepperoni']
finished_sandwiches = []

print("I'm sorry, we're all out of turkey today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm making your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made you a " + sandwich + " sandwich..")