#Word scrambler game

#For this class we are required to explain every line of code

import random

def word_refiner(w): #Defining a function by the name word_refiner with a parameter of 'word'
    alphabet = 'abcdefghijklmnopqrstuvwxyz' #String of the alphabet called 'alphabet' to have each letter available 
    ctext = '' #Empty string to add objects or characters into later
    for character in w.lower(): #Iterates over the characters of the entered word. The .lower() method makes sure to convert any characters into lowercase if any uppercases were given
        if character in alphabet: #Iterates over every individual character in the given word and sees if any characters are also in alphabet
            ctext += character
        else: #If the characters of the given word are in alphabet, increment the text by the character
            ctext += ''
    return ctext #Returns back text either empty or with word after for loop has finished completing.

def word_list(text_name): #Defining new function as list with a parameter called 'text name'
    words = [] #Initializing empty array called words
    with open(text_name) as text: #'With' function to enter whatever parameter is given and redefine it as 'text'
        for line in text: #Iterates over every line in text
            for word in line.split(): #Iterates over every word in the line as done by the slit method
                refined_word = word_refiner(word) #Creates new assigned value of refined word to function word refiner
                if refined_word not in words: #If the refined word is not in the words array 
                    words.append(refined_word) #Add the word to the array
    return words #Returns the empty or occupied list of words

def rejoin(characters): #Function defined with name of rejoin with one parameter called 'characters'
    word = '' #Empty string called word initialized
    for character in characters: #For the character in every character for the given parameter (already assuming that the given parameter will be a string with characters to iterate over
        word += character #Append the empty string with the characters
    return word #Return the word back

def word_scrambler(word): #Function defined with name of word_scrambler with one parameter named word
    mix = list(word) #Defines 'mix' as the parameter listed out thru the list method 
    random.shuffle(mix) #Imported random function randomly shuffles the listed word, or 'mix'
    return rejoin(mix) #Uses the rejoin function to make the shuffled characters go back into a singular string

words = word_list('pap.txt') #Assigns new value statement of words to the function word list which is being used on its parameter 'pap.txt'

while True: #While true loop created
    word = random.choice(words) #word statement assigned value of random function with added method choice with a parameter of words
    mixed = word_scrambler(word) #mixed statement assigned a value of function word_scrambler being used on previous statement word
    print('Given letters: ', mixed) #prints this plus mixed statement
    guess = input('Your guess: ') #Guess with user's input put into
    if guess == word: #If the user's input is equal to the word
        print('Correct!') #Prints statement saying their answer was correct
    else: #if not
        print('Incorrect. The word was', word) #Prints statement saying answer was incorrect and prints the correct word

