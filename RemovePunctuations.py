# Defining a string called "Punctuations"
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Creating a variable.
my_str = "Hello!!!, he said ---and went."

# Incase you want to take input from the user, you can remove it from the comments, and use it to take input.
# my_str = input("Enter a string: ")

# removing punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# Printing the unpunctuated string.
print(no_punct)
