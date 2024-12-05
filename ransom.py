import sys

# returns Unicode integer for letter
def letter_to_unicode_conversion(letter):
    return ord(letter)

"""
Function below is so to say the first half of a gist of the algorithm. 
An array of letters (string in python) supplied to the function as a parameter, is converted to a python dict. 
The keys are unicode integers for small and big letters of english alphabet and values are numbers of times that this letters
show up in the message in a iterable given to the function as an argument. It is accomplished also with a use of letter_to_unicode function.
 """

def alphabet_dict(it):
    b_dict = {x: 0 for x in range(65,123)}
    for i in it:
        letter_numeric = letter_to_unicode_conversion(i)
        # if-else block here ensures that an i-th element of a string can be converted to the letter. Else it's irrelevant
        if letter_numeric >= 65 and letter_numeric <= 122:
            b_dict[letter_numeric] += 1
        else:
            continue
    return b_dict


def ransom_message(message_input, article_text_input):
    # handles wrong data type.
    if type(message_input) == str and type(article_text_input) == str:
        pass
    else:
        raise TypeError('Algorithm requires both arguments to be of type string')
    # variable below is control variable. First set to true and if task can't be achieved it is than set to false.
    possible_to_create_message = True
    message = message_input.replace(' ', '') # delete whitespaces form string since they aren't letters.
    article_text = article_text_input.replace(' ', '')
    message_dict = alphabet_dict(message) # calls alphabet dict function.
    article_dict = alphabet_dict(article_text)
    # checks for each letter(disguised now as an Unicode integer) in message if in article text this letter appears at least as
    # many times as in message. this is second half of the algorithm's gist.
    for key,value in message_dict.items():
        if message_dict[key] <= article_dict[key]:
            continue
        else:
            possible_to_create_message = False
            break
    return possible_to_create_message

# below is a code allowing the program to be run from command prompt with 2 arguments.

arg1 = sys.argv[1]
arg2 = sys.argv[2]

with open(arg1, 'r') as f:
    ran_mess = f.read()
with open(arg2, 'r') as f:
    art_text = f.read()

print(ransom_message(ran_mess, art_text))