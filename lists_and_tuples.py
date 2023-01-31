# Lists
#
# # Lists == Arrays, all about data management
# # First list
shopping_list = ["milk", "eggs", "bread", "fruit" , "cheese"]
# print(type(shopping_list)) #<class 'list'>
# print(shopping_list)
#
# print(shopping_list[0]) # Shows "milk", the first item on the list
# print(shopping_list[3]) # shows "fruit", the 4th item on the list
# print(shopping_list[-1]) # shows "cheese", the last item on the list
#
# # rewriting a value in our list
# shopping_list[0] = "sugar"
# print(shopping_list) # replaces the wanted item on the list ['sugar', 'eggs', 'bread', 'fruit', 'cheese']
# print(shopping_list[0])

# List methods
# add to the list
shopping_list.append("vegetables")
# print(shopping_list)
# print(shopping_list[5])
# print(len(shopping_list))

# Remove from the list

shopping_list.remove("bread")
# print(len(shopping_list))
# print(shopping_list)

# Remove list item off the list without specifying it
#

shopping_list.pop()
print(shopping_list)
shopping_list.pop()
print(shopping_list)

# Mixed data type lists
#
# mixture = [1 , 2 , 3.4 , "one" , "two" , "three"]
# # print(mixture)
# #
# # # List slicing
# # print(mixture[1:3]) #[2, 3.4]
# # print(mixture[-2::]) # reverses the order
# #
# # print(mixture[::2]) # bounces over the amount of indexes specified
#
# # Tuples
#
# # Exactly the same as lists, except they are immutable (un-editable)
# # Tuples are useful for elements you want to ensure data stays the same
#
# essential= ("bread", "eggs", "milk")
# print(essential)
# print(essential.count("bread"))
# #essential[0]= "fruit" # will not work. you cant change items in Tuples
# print(essential)
