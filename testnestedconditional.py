def choose_gift(item, price):
    wishlist = ["phone", "laptop", "camera"]
    budget = 1000.00
    discount = 0.50
    free_shipping = True
    has_warranty = True

    
    if is_discounted(price, budget):
        check_deals()
    elif price > budget:
        print("That's overbudget!")
        check_deals()
    elif price >= 0 and item in wishlist:
        print("Perfect gift!")
        is_discounted(price, budget)
        check_deals
    else:
        print("Try something different")

def check_deals():
    free_shipping = True
    has_warranty = True

    if (free_shipping and has_warranty):
        print("With free shipping and warranty!")


def is_discounted(price, budget):
    discount = 0.50

    discounted_price = price - (price * discount)
    if (discounted_price <= budget):
        print("Discounted price within budget.")
        return True

    return False

choose_gift("phone", 1500.00)