# Dictionaries
# # Dictionaries use key/value pairs
# # key = a referance to a particular object
# # value = data storage mechanism you want to use
#
# # Create a dictionary
#
# student_1 = {
#     "name": "Susan",
#     "stream": "DevOps",
#     "completed_lessons": 4,
#     "completed_lessons_names": ["variables", "data_types", "set_up"]
#
# }
#
# # Access data within a dictionary
# print(student_1["stream"])
#
# #changing a value in dictionary
#
# student_1["completed_lessons"] = 3
# print(student_1["completed_lessons"])
#
# # Removing items from a dictionary
#
# student_1["completed_lessons_names"].remove("data_types")
# print(student_1["completed_lessons_names"])
#
# # Dictionary methods
# # Keys
# print(student_1.keys())
# # getting a certain item from the list without []
# print(student_1.get("name"))
#
# # Get the values of a dictionary
# print(student_1.values())
# # outputs array of tuples with key value pairs in dictionary
# print(student_1.items())


dog_list = {
    "breed": "lab",
    "name": "Felix",
    "age": "3",
    "training_done": ["jump", "crawl", "bark"]
}

dog_list["training_done"].remove("crawl")
print(dog_list["training_done"])


