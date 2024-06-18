#Gabrielle Barrow
#CSCI127
#Project 2

#2.1

def calories(fruit):
    fruit_list = ['Avocado', 'Banana', 'Lemon', 'Plum', 'Strawberries', 'Watermelon']
    num_of_cals = [50, 110, 15, 70, 50, 80]
    for fruits, cal in zip(fruit_list, num_of_cals):
        if fruits.lower() == fruit.lower():
            return cal
    return None

#Test cases:
print(calories('AvOcAdO'))
print(calories('plum'))
print(calories('Watermelon'))
print(calories('Banana'))
print(3*calories('Lemon'))
print(calories('Cucumber'))

#2.2

def duplicates(arr):
    uniques = []
    dupes = []
    for i in arr:
        if i in uniques:
            if i not in dupes:
                dupes.append(i)
        else:
            uniques.append(i)
    return dupes            

#Test Cases
print(duplicates([1, 4, 7, 5, 1, 4, 4, 0, 8]))
print(duplicates([2, 2, 2, 3, 4, 5]))
print(duplicates(['skip', 'jump', 'hop', 'jump']))
print(duplicates(['hello', 'hey', 'hi', 'hello', 'whats up']))

#2.3

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def findPrime(maxN):
    primes = []
    for i in range(1, maxN + 1):
        if isPrime(i) == True:
            primes.append(i)
    return primes

#Test cases:
print(isPrime(13))
print(isPrime(12))
print(isPrime(23))
print('-------------')
print(findPrime(40))
print(findPrime(14))
print(findPrime(2))

#2.4

def palindrome(given):
    length = len(given)
    for i, character in enumerate(given):
        if character != given[-i - 1]:
            return False
    return True

#Test cases:
print(palindrome('lol'))
print(palindrome('rotator'))
print(palindrome('theater'))

#2.5
def toLists(my_dict):
    keys = []
    values = []
    for key, value in my_dict.items():
        keys.append(key)
        values.append(value)
    return keys, values

#Test case:
veggies_cals = {
    'lettuce': 5,
    'celery': 14,
    'mushroom': 15,
}

print(toLists(veggies_cals))

#############################

#Need help / assistance with this one as well.
def toDict(keys, values):
    my_dict = {}
    for key, value in zip(keys, values):
        my_dict[key] = value
    return my_dict
            
            
#Test case

veggies = ['lettuce', 'celery', 'mushroom']
calories = [5, 14, 15]
toDict(veggies, calories)

#print(toDict(veggies, calories))

#2.6

def vending():
    total = 0
    while True:
        coin = int(input('Enter a coin: '))
        if coin != 1 and coin != 5 and coin != 10 and coin != 25:
            print('Incorrect amount entered!')
            continue
        total += coin
        print(f'Amount of change entered: {total}')
        

        if total >= 75:
            print('You can purchase gum, cola, candy and chips.')
        elif total < 75 and total >= 60:
            print('You can purchase gum, cola, and candy')
        elif total < 60 and total >= 50:
            print('You can purchase gum and cola.')
        elif total >= 25 and total < 50:
            print('You can purchase gum.')
        else:
            print(total)
            
        
        exit = input("Type 'exit' to exit. Type any other key to continue.")
        if exit.lower() == 'exit':
              break
            
vending()
