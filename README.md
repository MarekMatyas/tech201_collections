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