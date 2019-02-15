# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
fi=open('output7.txt','w')
with open('59242','r') as f:
    my_str = f.read()

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)
fi.write(no_punct)
