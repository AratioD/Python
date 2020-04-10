
# dictionary with mixed keys
names_hobbies = {'jack': 'camping', 'minna': 'scout', 'Rachel': 'theater'}
names_proffessions = {'minna': 'manager', 'jack': 'coder', 'Rachel': 'theacher'}

# print(names_hobbies)
# print(names_proffessions)


def printlist(list):
    for item in list.items():
        print(item)


printlist(names_hobbies)
printlist(names_proffessions)