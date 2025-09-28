#No yelling!
#https://www.codewars.com/kata/587a75dbcaf9670c32000292

import re

def no_yelling(text:str):
    word = text.split()
    no_space = " ". join(word).lower()

    sentences = re.split(r'([.!?]\s*)', no_space)  
    sentences = [s.capitalize() for s in sentences]
    sentence = "".join(sentences).strip()
    
    sentence = re.sub(r"\bi\b", "I", sentence) 
    sentence = re.sub(r"\bi'(\w+)", lambda m: "I'" + m.group(1), sentence) 
    
    return sentence

print(no_yelling("Wait, can I       HAVE some more honey?"))
print(no_yelling("how are you DoIng toDAY?"))
print(no_yelling("I like to eat ICe     cream."))
print(no_yelling("BOBBY shouldn't BE   ALLOWED     to   voTE."))

#This function ensures that every sentence has is properly formatted in correct sentence structure.
#For each string, the function removes any unneccesary spacing, and then capitalizes the first word shown.
#Then, the function checks for any instances of "I" or variations that should be capitalized as well.
#Finally, the correct sentence is returned to the user.