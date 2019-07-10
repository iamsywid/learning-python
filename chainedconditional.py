def ask_question(category):

    if category == "Who":
        return "Who are you?"
    elif category == "What":
        return "What is your favorite color?"
    elif category == "When":
        return "When are you leaving?"
    elif category == "Where":
        return "Where are you going?"
    elif category == "Why":
        return "Why are you moving?"
    else:
        return "How did you get here?"

print(ask_question("Who"))
print(ask_question("What"))
print(ask_question("When"))
print(ask_question("Where"))
print(ask_question("Why"))
print(ask_question("How"))

def choose_gift(item, price):
    wishlist = ["phone", "laptop", "camera"]
    budget = 1000.00

    if price > budget:
        print("That's overbudget!")
    elif item in wishlist:
        print("Perfect gift!")
    else:
        print("Try a different item")

choose_gift("phone", 10000)