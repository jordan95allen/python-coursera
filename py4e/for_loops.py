#Using for & in
print('Program1:')
for i in [5, 4, 3, 2, 1] :
    print(i)

print('Program2:')
friends = ['Timmy', 'Johnny', 'Sammy'] 
for friend in friends :
    print('Hey', friend)

#Using for & in to find the largest number
print('Program3:')
largest_num = -1
for the_num in [2, 3, 21, 100] :
    the_num > largest_num 
    largest_num = the_num
    print(largest_num, the_num)
print('The largest number is:', largest_num)

#Using for & in to count
print('Program4:')
count = 0
for number in [1, 45, 7, 85] :
    count = count + 1
    print(count, number)
print('You have this many numbers:', count)

#Using for & in to calculate a sum
print('Program5:')
zebra = 0
for number in [3, 5, 76, 21] :
    zebra = zebra + number
    print(zebra, number)
print('Your Sum Is:', zebra)

#Using for & in to calculate mean
print('Program6:')
count = 0 
sum = 0
for number in [4, 56, 23, 8] :
    count = count + 1
    sum = sum + number
print('Count:', count, 'Sum:', sum, 'Average:', sum / count)

#Using an if statement to filter a for & in loop
print('Program7:')
for number in [3, 5, 23, 2, 76]:
    if number > 50 :
        print(number, 'is greater than 50')
print('COMPLETE')

#Using a boolean statement with for & in
print('Program8:')
false = False
for number in [23, 45, 4, 78] :
    if number == 4 :
        false = True
        break
    print(number, false)
print(number, 'is the', false, 'value')

#Using a none statement to determine the smallest integer
print('Program9:')
smallest = None
for value in [3, 67, 45, 44] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        print()
print('The smallest integer is:', smallest)

