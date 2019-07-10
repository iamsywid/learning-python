def get_response(category, answer):

    if category == "Who":
        if (answer == "Jane"):
            return "Okay"
        else:
            return "Not Okay"
    elif category == "What":
        if answer == "Swimming":
            return "Agree"
        else:
            return "Disagree"
    elif category == "When":
        if answer == "Summer":
            return "Sure!"
        else:
            return "Nope"
    elif category == "Where":
        if answer == "Beach":
            return "Let's go!"
        else:
            return "Next time"
    elif category == "Why":
        if answer == "Vacation":
            return "I don't have energy."
        else:
            return "I don't have time."
    else:
        return "How"

def choose_gift(item, price):
    wishlist = ["phone", "laptop", "camera"]
    budget = 1000.00
    discount = 0.50;
    free_shipping = True;
    has_warranty = True;

    if price > budget:
        if (price - (price * discount) <= budget):
            print("Discounted price within budget.")
            if (free_shipping and has_warranty):
                print("With free shipping and warranty!")
        else:
            print("That's overbudget!")
            if (free_shipping and has_warranty):
                print("With free shipping and warranty!")
    elif price >= 0 and item in wishlist:
        print("Perfect gift!")
        if (price - (price * discount) <= budget):
            print("Discounted price within budget.")
        if (free_shipping and has_warranty):
            print("With free shipping and warranty!")
    else:
        print("Try something different")


choose_gift("phone", 1500)

def choose_gift2(item, price):
    wishlist = ["phone", "laptop", "camera"]
    budget = 1000.00
    discount = 0.50
    free_shipping = True
    has_warranty = True

    if price > budget:
        if (price - (price * discount) <= budget):
            print("Discounted price within budget.")
            if (free_shipping and has_warranty):
                print("Good deal!")
        else:
            print("That's overbudget!")
            if (free_shipping and has_warranty):
                print("Good deal!")
    elif price >= 0 and item in wishlist:
        print("Perfect gift!")
        if (price - (price * discount) <= budget):
            print("Discounted price within budget.")
        if (free_shipping and has_warranty):
            print("Good deal!")
    else:
        print("Try something different")

def check_deals():
    free_shipping = True;
    has_warranty = True

    if (free_shipping and has_warranty):
        print("Good deal!")

def check_discount(price, budget):
    discount = 0.50

    discounted_price = price - (price * discount)
    if (discounted_price <= budget):
        print("Discounted price within budget.")


choose_gift2("phone", 1500)