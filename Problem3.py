#Modify the previous program such that only the users Alice and Bob are greeted with their names.
person = input('What is your name? ')
namelist = ['Alice', 'Bob']

if person in namelist:
    print('Hello', person)
else:
    print('Name not recognized')



