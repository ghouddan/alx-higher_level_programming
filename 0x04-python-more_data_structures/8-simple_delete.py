#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    
    for exist_key in a_dictionary.keys():
        if exist_key == key:
            del a_dictionary[exist_key]
            return a_dictionary

    return a_dictionary
