starters_options = ["Fried prawns", "Grilled chicken", "Onion Bhaji", "Stir fry tofu"]
main_options = ["Chicken and fries", "Veggies in WOK", "Steak and potatoes" ]
dessert_options = ["Sticky pudding", "Cheesecake", "Vegan pudding"]
print("Hello there, my name is Python and I will be your waiter tonight!")
print("Here is the menu for you to have a look")
print( "Starters to choose from: " + str(starters_options))
starter_order= input()
print( "Thank you, our options for main course are: " + str(main_options))
main_order= input()
print("And lastly here are some dessert" + str(dessert_options))
dessert_order = input()
print("Perfect ! So to sum up, this is your order: " + starter_order + " for starter" + ", then for your main you will have " + main_order + " and for dessert you chose " + dessert_order )
print("Thank you and enjoy!!")