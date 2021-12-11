print("Hello") #'hello' is the same as "hello"
print('Hello')

a = "Hello"
print(a)


#You can assign a multiline string to a variable by using three quotes:
#You can use three double quotes:
#a = """Lorem ipsum dolor sit amet, 
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua."""
#print(a)

#Or three single quote
#a = '''Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.'''
#print(a)

#String Arrays
# #Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])

#Since strings are arrays, we can loop through the characters in a string, with a for loop
#Loop through the letters in the word "banana":
for x in "banana":
    print(x)
    
a = "Hello, World!"
print(len(a))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

#Use it in an if statement: Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
#Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

#Use it in an if statement
#print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")