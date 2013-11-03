def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill
    
meal_cost = raw_input("How much was your meal, madam? I shall calculate the total bill to inclue tax and tip:")

if len(str(meal_cost)) > 0 and [ meal_cost.isint() or meal_cost.isfloat() ]:
    
    meal_cost = int(meal_cost)
    meal_with_tax = tax(meal_cost)
    print meal_with_tax + " is your total cost with tax."
    meal_with_tip = tip(meal_with_tax)
    print meal_with_tip + " is your complete bill, including tax and the tip."
    
else:
    print "Please enter a valid response, madam."