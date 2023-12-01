import re

list = open("index.txt")
y=0
i=0
while i<999:
  x = list.readlines()[i]
  re.sub("[^0-9]", "", f"{x}")
  y = y+x
  i = i+1
print(y)
  
