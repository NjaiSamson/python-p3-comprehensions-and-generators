#!/usr/bin/env python3

def return_evens(num_list):
    even_elements = [num for num in num_list if num % 2 == 0]
    return even_elements

return_evens([0, 1, 3, 5, 7, 8, 9])

def make_exclamation(sentence_list):
    sentence_list_with_exclamation = [sentence + "!" for sentence in sentence_list]
    
    return sentence_list_with_exclamation

make_exclamation(["Hello", "I'm doing great", "Python is fun"])
