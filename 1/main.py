import re

total = 0 #setup number variable
words = 'one two three four five six seven eight nine'.split()

reFunc = '(?=(' + '|'.join(words) + '|\\d))' #regex to get words

def f(nums):
    if nums in words:
        return str(words.index(nums)+1)
    return nums 

for nums in open("index.txt"):
    needed = [*map(f, re.findall(reFunc, nums))] #check through the characters in the thingy
    total += int(needed[0]+needed[-1]) #add first and last by rolling the last part over
print(total) #print total

#i kinda lost track of what i was doing like halfway through and forgot to notate it and forgot some of what it did
