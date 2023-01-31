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
`.replace` Replace characters or text
```
example_text = "Here's some text with lot's of text"
print(example_text.replace("with" , ","))
``` 
Returns "Here's some text, lot's of text"
