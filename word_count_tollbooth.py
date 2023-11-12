import phantom_tollbooth


#funct to convert to lower case
def lower_case(text):
    text = text.lower()
    return text


#funct to remove special symbols
def no_symbols(text):
    symbols = '''~\`!@#$%^&—*()_+1234'-567890-=.,;:?/"\|'''
    for char in symbols:
        if char in text:
            text = text.replace(char, '')
    return text


#funct to remove unwanted words
def unwanted_words(text):
    words_to_remove = ['a', 'as', 'an', 'all', 'the','of', 'on', 'over', 'above', 'below', 'under', 'through', 
                    'between', 'among', 'around', 'at', 'by', 'and', 'but', 'or', 'nor', 'for', 
                    'yet', 'so', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 
                    'her', 'us', 'them', 'is', 'am', 'are', 'was', 'were', 'be', 'being', 'been', 'has',
                    'have', 'had', 'do', 'dont', 'does', 'did', 'shall', 'will', 'should', 'would', 'may',
                    'might', 'must', 'can', 'could', 'to', 'too', 'not', 'its', 'hed', 'has', 'who',
                    'if', 'youve', 'into', 'in', 'that', 'have', 'from', 'with','his', 'im', 'there',
                    'since', 'like', 'said', 'up', 'their', 'very', 'what','then']
    for word in words_to_remove:
        while word in text:
            text.remove(word)
    return text


#funct to get word and its count into dictionary
def count(text):
    word_count = {}
    for word in text:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count



#funct taking dictionary to create a listed tuple, reversing key-value pairs
def word_list(dictionary):
    word_count_list = []
    for key, value in dictionary.items():
        word_count_list.append((value,key))
    return word_count_list
    


def main():
    book = phantom_tollbooth.get_text()

    book = lower_case(book)

    book = no_symbols(book)

    book = book.split()

    book = unwanted_words(book)

    word_counter = count(book)

    word_count_list = []
    for key, value in word_counter.items():
        word_count_list.append((value,key))
    word_count_list
       

    word_count_list.sort(reverse=True)

    # for index in range(51):
    #     counted = str(word_count_list[index][0])
    #     word = word_count_list[index][1]
    #     print( word + " : " + counted)

    for index in range(51):
        counted = str(word_count_list[index][0])
        word = word_count_list[index][1]
        print(word + ":" + counted)

    # print(word_count_list)

    # for index in range(51):
    #     word = str(word_count_list[index][0])
    #     count = word_count_list[index][1]
    #     print( word + " : " + count)

    # print(word_count_list)

    # count_list = word_list(count(book))

    # count_list.sort()

    # print(count_list)

    # print(book[0:350])


if __name__ == '__main__':
    main()