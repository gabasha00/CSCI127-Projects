#Gabrielle Barrow
#CSCI127
#Project 1

#1.1
def lower(sentence):
    return sentence.lower();

sentence = input('Enter a sentence: ')#1
newLower = lower(sentence)#2

print(newLower)#3


################################################

#1.2
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

a = 10
b = 2

#Example prints below
print("Addition:", add(a, b))
print("Subtraction:", sub(a, b))
print("Multiplication:", mul(a, b))
print("Division:", div(a, b))

################################################

#1.3
def comparison(a, b):
    if a > b:
        print('Greater than')
    elif a < b:
        print('Less than')
    elif a == b:
        print('Equal to')

a = 7
b = 10

comparison(b, a)

################################################

#1.4
def emoji(emoticon):
    if emoticon == ':)' or emoticon == '(:':
        print('🙂')
    elif emoticon == ':(' or emoticon == '):':
        print('☹️')
    elif emoticon == '-_-':
        print('😐')
    else:
        print('Invalid input')

emoticon = input('Enter an emoticon: ')
newEmoji = emoji(emoticon)

print(newEmoji)

################################################

#1.5
def tiptax(meal, tip):
    return (meal * 1.08875 * (1 + tip/100))

meal = 25
tip = 18

print(tiptax(meal, tip))

################################################

#1.6
def mealtime(hour):
    if hour >= 0 and hour < 12:
        print('Breakfast time!')
    elif hour >= 12 and hour < 18:
        print('Lunch time!')
    elif hour >= 18 and hour <= 24:
        print('Dinner time!')
    else:
        print('Invalid')

mealtime(7)
mealtime(12)
mealtime(17)
mealtime(19)

################################################

#1.7
def calculate(input1, input2, symbol):
    match symbol:
        case '+':
            return input1 + input2
        case '-':
            return input1 - input2
        case '*':
            return input1 * input2
        case '/':
            return input1 / input2

print(calculate(9, 5, '+'))
print(calculate(20, 8, '-'))   
print(calculate(7, 9, '*'))    
print(calculate(121, 11, '/')) 
