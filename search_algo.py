from index import *

def search_al(enteredQuery):
    # to store the matched pages
    matched = []
    # get the entered query from the entry
    query = enteredQuery
    # split the query into words and change it to lower case
    query = word_tokenize(query.lower())
    # list for connecting words
    bool_op = {"and", "or", "not"}
    # to store connecting_words (boolean operators)
    connecting_words = []
    # to store the words
    different_words = []

    # to split boolean operators and words from the query
    for word in query:
        if word not in bool_op:
            different_words.append(word)
        else:
            connecting_words.append(word)

    # to handel wrong queries
    i = 0
    for word in different_words:
        if word in Stopwords or len(word) < 3:
            print(word)
            str = word + " ignored because it is in stopwords collection"
            matched.append(str)
            print(different_words)
            different_words.remove(word)
            print(i)
            if i == 0:
                connecting_words.pop(0)
            else:
                connecting_words.pop(i-1)
        i += 1

    zeroes_and_ones_of_all_words = []
    # print(different_words)
    # check if the word exist in dictionary
    for word in different_words:
        # if the word found in dictionary
        if word in dictionary:
            # make a posting list and fill it with zeros
            zeroes_and_ones = [0] * len(pages_with_index)
            linkedlist = linked_list_data[word].head

            # fill the posting list with pageIds
            while linkedlist.nextval is not None:
                doc_id = linkedlist.nextval.pageId
                zeroes_and_ones[doc_id - 1] = 1
                linkedlist = linkedlist.nextval
            # add the posting list to (zeroes_and_ones_of_all_words)
            zeroes_and_ones_of_all_words.append(zeroes_and_ones)
        # if the word does not exist in dictionary
        else:
            # print some messages
            print(word, " not found")
            str = word + " not found"
            matched.append(str)
            # make a posting list for the word and fill it with zeros
            # then add it to (zeroes_and_ones_of_all_words)
            zeroes_and_ones_of_all_words.append([0] * len(pages_with_index))

    # to execute the query
    for word in connecting_words:
        # take the first two words
        word_list1 = zeroes_and_ones_of_all_words[0]
        word_list2 = zeroes_and_ones_of_all_words[1]
        # if the boolean op is AND
        if word == "and":
            # and the words
            bitwise_op = [w1 & w2 for (w1, w2) in zip(word_list1, word_list2)]
            # remove them from (zeroes_and_ones_of_all_words)
            zeroes_and_ones_of_all_words.remove(word_list1)
            zeroes_and_ones_of_all_words.remove(word_list2)
            # add the result to the (zeroes_and_ones_of_all_words)
            zeroes_and_ones_of_all_words.insert(0, bitwise_op)
        # if the boolean op is OR
        elif word == "or":
            # or the words
            bitwise_op = [w1 | w2 for (w1, w2) in zip(word_list1, word_list2)]
            # remove them from (zeroes_and_ones_of_all_words)
            zeroes_and_ones_of_all_words.remove(word_list1)
            zeroes_and_ones_of_all_words.remove(word_list2)
            # add the result to the (zeroes_and_ones_of_all_words)
            zeroes_and_ones_of_all_words.insert(0, bitwise_op)
        # if the boolean op is NOT
        elif word == "not":
            # and the first word with the not of the second one
            bitwise_op = [w1 & (not w2) for (w1, w2) in zip(word_list1, word_list2)]
            # remove them from (zeroes_and_ones_of_all_words)
            zeroes_and_ones_of_all_words.remove(word_list2)
            zeroes_and_ones_of_all_words.remove(word_list1)
            # add the result to the (zeroes_and_ones_of_all_words)
            zeroes_and_ones_of_all_words.insert(0, bitwise_op)
    # store the result in list
    lis = zeroes_and_ones_of_all_words[0]
    cnt = 1
    # make a list of the matched pages
    for index in lis:
        if index == 1:
            matched.append(pages_with_index[cnt])
        cnt = cnt + 1
    return matched