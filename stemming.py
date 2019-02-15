import io
import string
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

#word_tokenize accepts a string as an input, not a file. 
stop_words = set(stopwords.words('english')+list(string.punctuation)) 
file1 = open("output1.txt") 
line = file1.read() # Use this to read file content as a stream: 
words = line.split() 
for r in words: 
    if not r in stop_words: 
        appendFile = open('afterStopWordRemoved.txt','a') 
        appendFile.write(" "+r) 
        appendFile.close()

ps = PorterStemmer()

file2 = open("afterStopWordRemoved.txt") 
sentence = file2.read() # Use this to read file content as a stream: 
words = word_tokenize(sentence) 
for w in words: 
    appendFile = open('afterStemming.txt','a') 
    appendFile.write(" "+ps.stem(w)) 
    appendFile.close()
