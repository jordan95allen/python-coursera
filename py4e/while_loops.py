#While loop practice
print('WHILE LOOP:')
x = 6
while x > 0:
    print(x)
    x = x - 1
print('BLASTOFF!')


#While loop w/break practice
print('WHILE LOOP W/BREAK:')
while True:
    line = input('~')
    if line == 'hello' :
        break
    print(line)



#Continue loop practice
print('WHILE LOOP W/CONTINUE AND BREAK:')
while True:
    info = input('->')
    if info == '#' :
        continue
    if info == 'hey' :
        break
    print(info)