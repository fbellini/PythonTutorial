#importing modules and libs
from math import *
from datetime import datetime
import os.path, time

##############################
def english2pyg(original) :
    """Translates a word in English into Pyg Latin"""
    pyg = 'ay'
    new_word = 'empty'
    #original = raw_input('Enter a word:')
    if len(original) > 0 and original.isalpha():
        #print original
        word = original.lower()
        #select letters of word by treating string as an array of char
        first = word[0] 
        #concatenate strings
        new_word = word[1:len(word)] + first + pyg 
        print (new_word)
    else:
        print ('empty')
    return new_word

##############################
def power(base, exponent):  
    """Power function"""
    result = base ** exponent
    print ("%d to the power of %d is %d." % (base, exponent, result))

def main() :
    """Main function"""
    english2pyg("test")
    return ('The End.')

##############################
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

print("Created: %s" % time.ctime(os.path.getmtime("/Users/fbellini/projects/pythontutorial/helloworld.py")))
print ('Last update: ', now.strftime('%d %B %Y %H:%M:%S'))
#12-hour format
#print(now.strftime# ('%Y/%m/%d %I:%M:%S')) 
main()
