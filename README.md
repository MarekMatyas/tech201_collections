# tech201_collections
# Data types and collections

## Data types
**Numeric**
- ints and floats (int is a whole number and float is with decimal point)
- Complex

**String** is text of any type
Strings can be done by using single quotes ('') or double quotes ("").

**Boolean** can only be True or False

### Operators
**Arithmetic operators**
- "+" add
- "-" subtract 
- "*" multiply
- "/" divide

**Comparison operators**
- ">" greater than
- "<" less than 
- "=" equal to
- "!=" not equal to
- ">=" greater or equals to
- "<=" less than or equals to

## String methods
`strip()` removes all white space (empty space)

```
white_space = "lot's of space at the end                "
print(len(white_space)) # 70 characters including spaces
print(len(white_space.strip())) # 25 characters
```
`.count` finds a number of characters or words that are in the string 
```
example_text = "Here's some text with lot's of text"
# Count a substring within a string
print(example_text.count("text")) # 2 "text" words 
```
`.lower` and `.upper` makes everything lower case or upper case
```
print(example_text.lower())
print(example_text.upper())
```
`.capitalize` Capitalizes the first letter
`print(example_text.capitalize())`
`.replace` 
Replace characters or text
```
example_text = "Here's some text with lot's of text"
print(example_text.replace("with" , ","))
``` 
Returns "Here's some text, lot's of text"

## Boolean examples
``` 
a = True
b = False
print(a == b) # False
print(a != b) # True
print(a >= b) # True
print(a >= True) # True
print(b <= False) # True
print(True and False) # False
print(False and True) # False
print(False or True) # True because True is an option
```

``` 

hi = "Hello world!"


print(hi.isalpha()) # False, because not all characters are from the alphabet 
print(hi.endswith("!")) # True
print(hi.startswith("H")) # True
```

## Concatenation example
``` 
a = "here "
b = "more "
c= " much more"
print(a  + b  + c )
```

## Casting example
``` 
x= 2
y = 5.4
z = "there's a number 25.4 unless we put a space! "
print( x + y + z)

print(str(x) + str(y) + z)
```
**String to numeric**
```
int_string= "6"
print(int(int_string))
```

**Formatted string** 

Use `f` character in the print statement with curly brackets for the variable
``` 
# F- strings allow us to use evaluation/methods
name = "Snoopy"
years = 52
print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS ")
```

## Converting decimals
`f` string to specify position in rounding decimals to 3 decimals with examples
``` 
pi = 3.314159265359
print(f"Pi to 3 decimal places: {pi:.3f}") # to 3 decimal
print(f"Pi to 5 decimal places: {pi:.5f}") # to 5 decimal
```
``` 
score= 16
max_score = 26
print(f"You scored {score/max_score}") #You scored 0.6153846153846154
print(f"You scored {score/max_score:%}")# You scored 61.538462%
print(f"You scored {score/max_score:.2%}") #You scored 61.54%
print(f"You scored {score/max_score:.0%}") #You scored 62%
```

# Dictionaries

**Dictionaries** use key/value pairs
Key = a reference to a particular object
Value = data storage mechanism you want to use 

Example of creating a dictionary 
``` 
student_1 = {
     "name": "Susan",
     "stream": "DevOps",
     "completed_lessons": 4,
     "completed_lessons_names": ["variables", "data_types", "set_up"]
```

To access data within that dictionary use:
`print(student_1["stream"])`

To change a value in that dictionary use:
`student_1["completed_lessons"] = 3`

To remove items from that dictionary use:
`student_1["completed_lessons_names"].remove("data_types")
print(student_1["completed_lessons_names"])` to check the output

**Methods**

Keys to return:
`print(student_1.keys())`
Get certain item from the list:
`print(student_1.get("name"))`
Get the values of the dictionary:
`print(student_1.values())`


# Lists and Tuplets
Lists or Arrays are all about data management.
Let's create an example or a List
`shopping_list = ["milk", "eggs", "bread", "fruit" , "cheese"]`

To access certain items from the list (first item always being 0):
```
print(shopping_list[0]) # Shows "milk", the first item on the list
print(shopping_list[3]) # shows "fruit", the 4th item on the list
print(shopping_list[-1]) # shows "cheese", the last item on the list
```

To rewrite a value in our list: 
``` 
shopping_list[0] = "sugar"
print(shopping_list) # replaces the wanted item on the list ['sugar', 'eggs', 'bread', 'fruit', 'cheese']
```

**List methods**

To add to the list use `.append`:

`shopping_list.append("vegetables")` adding the item at the end of our list

To remove from the list use `.remove`:

`shopping_list.remove("bread")`

To remove the last item without specifying it use `.pop`:

`shopping_list.pop()`

To access an item from the list by index 

`print(shopping_list[1])`


### Example of list slicing

``` 
mixture = [1 , 2 , 3.4 , "one" , "two" , "three"]
print(mixture[1:3]) #[2, 3.4]
print(mixture[-2::]) # reverses the order
print(mixture[::2]) # bounces over the amount of indexes specified
```

# Tuples

They are exactly the same as lists, except they are immutable (un-editable).
Tuples are useful for elements you want to ensure data stays the same.
Quick example:

``` 
essential= ("bread", "eggs", "milk")
print(essential)
print(essential.count("bread"))
#essential[0]= "fruit" # will not work. you cant change items in Tuples
```

## Sets and Frozen sets

Lists and sets are very similar. Sets are unordered.
To create a set :
```
car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)
```
To remove part of the set `.discard`: 

``` 
car_parts.discard("doors")
print(car_parts)
```

To add things to a set `.add`:
`car_parts.add("windows")`

## Frozen sets
Frozen sets are immutable (cannot be changed or manipulated version of a set. Un-ordered and un-indexed)

Quick example of a frozen set:
`x = frozenset([1, 2 ,3, 4, "five"])`