with open('tasks.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print (len(content))
    content = content.replace('.', '!')
    print (content)

import sys
fname = sys.argv[0]
lines = 0
words = 0
letters = 0

for line in open(fname):
    lines += 1
    letters += len(line)

    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'

print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)    
    
with open('tasks2.txt', 'w', encoding='utf-8') as k:
        k.write(content) 
