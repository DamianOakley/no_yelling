#No yelling!
#https://www.codewars.com/kata/587a75dbcaf9670c32000292

def no_yelling(text:str):
    word = text.split()
    no_space = " ".join(word).lower()

    sentences = no_space.capitalize() 
    
    return "".join(sentences.split(text))

print(no_yelling("You       can HAVE some more honey."))
print(no_yelling("how are you DoIng toDAY?"))
print(no_yelling("I like to eat ICe     cream!"))
print(no_yelling("BOBBY shouldn't BE   ALLOWED     to   voTE."))

#This function ensures that every sentence is properly formatted in correct sentence structure.
#For each string, the function removes any unneccesary spacing, while lowercasing every word.
#The sentence is the capitallized, and each word is evenly spaced out.
#Finally, the correct sentence is returned to the user.