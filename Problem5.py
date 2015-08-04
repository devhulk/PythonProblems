person = input('Enter a number here: ')
x = int(person) + 1

if int(person) % 5 == 0:
    print(person,' plus one = ',x)

if int(person) % 3 == 0:
    print(person,' plus one = ',x)

else:
    print('The number you enter needs to be a multiple of 5 or three... Did I forget to mention that???lol')
