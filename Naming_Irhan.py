name = "Irhan Adam Iftikar"
import random

def reverse(name):
    return name[::-1]

def vowels(name):
    vowel_count = 0
    for i in name:
        if i in "aeiouyAEIOUY":
            vowel_count += 1
    return vowel_count

def consonants(name):
    consonant_count = 0
    for i in name:
        if i not in "aeiouyAEIOUY":
            consonant_count += 1
    return consonant_count

def first_name(name):
    index = 0
    while index < len(name):
        letter = name[index]
        if letter == " ":
            return(name[:index])
        else:
            index = index + 1

def last_name(name):
    index = len(name) - 1
    while index <= len(name):
        letter = name[index]
        if letter == " ":
            return(name[index + 1:])
        else:
            index = index - 1

def middle_name(name):
    first_index = 0
    while first_index < len(name):
        letter = name[first_index]
        if letter == " ":
            break
        else:
            first_index = first_index + 1

    last_index = len(name) - 1
    while last_index <= len(name):
        letter = name[last_index]
        if letter == " ":
            break
        else:
            last_index = last_index - 1

    return(name[first_index + 1:last_index])

def hyphen(name):
    boolean = False
    index = len(name) - 1
    while index <= len(name):
        letter = name[index]
        if letter == " ":
            last_name = name[index + 1:]
            break
        else:
            index = index - 1

    for i in last_name:
        if i in "-":
            boolean = True
            return(boolean)
        else:
            boolean = False
    return(boolean)

def lowercase(name):
    lowercase_name = []
    index = -1
    for i in name:
        index += 1
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num = ord(i)
            num += 32
            letter = str(chr(num))
            lowercase_name.append(letter)
        else:
            lowercase_name.append(i)
    return(str(("".join(lowercase_name))))

def uppercase(name):
    uppercase_name = []
    index = -1
    for i in name:
        index += 1
        if i in "abcdefghijklmnopqrstuvwxyz":
            num = ord(i)
            num -= 32
            letter = str(chr(num))
            uppercase_name.append(letter)
        else:
            uppercase_name.append(i)
    return(str(("".join(uppercase_name))))

def modify(name):
    letters = []
    removed_letters = []
    new_name = []
    length = 0
    for i in name:
        letters.append(i)
        removed_letters.append(i)
    while length < len(letters):
        choice = random.choice(removed_letters)
        new_name.append(choice)
        length += 1
        removed_letters.remove(choice)
    return(str(("".join(new_name))))

def palindrome(name):
    is_palindrome = False
    first = first_name(name)
    lowercase_first = lowercase(first)
    
    front_index = 0
    back_index = 1
    while front_index < len(lowercase_first):
        if lowercase_first[front_index] == lowercase_first[-back_index]:
            is_palindrome = True
            front_index +=1
            back_index += 1
        else:
            is_palindrome = False
            break
    return is_palindrome