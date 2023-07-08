#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentences):
    return [sentence + "!" if isinstance(sentence, str) else sentence for sentence in sentences]