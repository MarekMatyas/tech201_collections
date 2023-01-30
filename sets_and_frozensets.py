# Sets and Frozen sets

# Lists and sets are very similar
# Sets are unordered
# Create a set

car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)

# Remove parts from a set
car_parts.discard("doors")
print(car_parts)

# add things to a set

car_parts.add("windows")
print(car_parts)

# Frozen sets

# Frozen sets are immutable (cannot be changed of manipulated version of a set. Still unordered and un-indexed

x = frozenset([1, 2 ,3, 4, "five"])
print(x)