import re


def extract_words(request, file_content):
    words_en = []
    english_words = open('.\media\words_en.txt')
    for word in english_words:
        words_en.append(word.strip("\n"))
    # "words_list" is a list with tuples as its items. Each tuple's first it number of repetitions
    # and second item is the word corresponding to number of repetitions
    words_list = []

    # "words_number" is a dictionary with words as keys and their repetitions as values
    words_number = {}

    # extract each word from the line
    for word in re.split("[^A-Za-z]", str(file_content)):
        word = word.strip()
        if word == "":
            continue
        else:
            if word in words_number:
                # if word is already in the dictionary, add 1 to its value
                words_number[word] += 1
            else:
                # if word is not in the dictionary add the word to the dictionary with its value 1
                words_number[word] = 1

    for word in words_number:
        words_list.append((words_number[word], word))

    words_list.sort()
    words_list.reverse()
    users_known_words = str(request.user.known_words).split()
    words_list_str = ''
    outside_words_str = ''
    unknown_words_str = ''
    known_words_str = ''

    for repeat, word in words_list:
        words_list_str += word + ' ' + str(repeat) + ', '
        if word not in words_en:
            # if word not in english dictionary:
            outside_words_str += word + ' '
        elif word in users_known_words:
            known_words_str += word + ' '
        else:
            unknown_words_str += word + ' '

    return words_list_str, known_words_str, unknown_words_str, outside_words_str


def extract_known_words(file_content):
    words_en = []
    english_words = open('.\media\words_en.txt')
    for word in english_words:
        words_en.append(word.strip("\n"))
    # "words_list" is a list with tuples as its items. Each tuple's first it number of repetitions
    # and second item is the word corresponding to number of repetitions
    words_list = []

    # "words_number" is a dictionary with words as keys and their repetitions as values
    words_number = {}

    # extract each word from the line
    for word in re.split("[^A-Za-z]", str(file_content)):
        word = word.strip()
        if word == "":
            continue
        else:
            if word in words_number:
                # if word is already in the dictionary, add 1 to its value
                words_number[word] += 1
            else:
                # if word is not in the dictionary add the word to the dictionary with its value 1
                words_number[word] = 1

    for word in words_number:
        words_list.append((words_number[word], word))

    words_list.sort()
    words_list.reverse()
    words_list_str = ''
    outside_words_str = ''
    known_words_str = ''
    for repeat, word in words_list:
        words_list_str += word + ' ' + str(repeat) + ', '
        if word not in words_en:
            # if word not in english dictionary:
            outside_words_str += word + ' '
        else:
            known_words_str += word + ' '

    return known_words_str