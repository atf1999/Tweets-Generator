import sys
import random
from operator import itemgetter


def return_random_word(histogram):
    # Another way:  Should test: random.choice(histogram.keys())
    random_key = random.sample(histogram, 1)
    return random_key[0]


def get_token_count(histogram):
    sum = 0
    for key in histogram:
        sum += histogram[key]
    return sum


def get_token_count_tuple(histogram):
    sum = 0
    for i in range(0, len(histogram)):
        sum += histogram[i][1]
    return sum


def binary_search(histogram, histogram_keys, target):
    get_total_token_count_to_point = 0
    # if(histogram[histogram_keys[key_count/2] ==  )


def test_weighted_random_word(histogram, times):
    results = dict()
    for i in range (0, times):
        result = return_weighted_random_word(histogram)
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
    # Organize results to display most common first
    results_tuple = results.items()
    # Slower version according to SO
    # sorted_results = sorted(results_tuple, key=lambda x: x[1], reverse=True)
    sorted_results = sorted(results_tuple, key=itemgetter(1), reverse=True)

    print sorted_results


def test_weighted_random_word_tuple(histogram, times):
    results = dict()
    for i in range (0, times):
        result = weighted_random_word_tuple(histogram)
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
    # Organize results to display most common first
    results_tuple = results.items()
    # Slower version according to SO
    # sorted_results = sorted(results_tuple, key=lambda x: x[1], reverse=True)
    sorted_results = sorted(results_tuple, key=itemgetter(1), reverse=True)

    print sorted_results


def weighted_random_word_tuple(histogram):
    # Step 1: Get total count of all words in histogram
    # print histogram
    token_count = get_token_count_tuple(histogram)
    type_count = len(histogram)
    # Step 2: Generate random number between 0 and total count - 1
    random_int = random.randint(0, token_count-1)
    index = 0
    # print 'the random index is:', random_int
    for i in range(0, type_count):
        index += histogram[i][1]
        # print index
        if(index > random_int):
            # print list_of_keys[i]
            return histogram[i][0]


def return_weighted_random_word(histogram):
    # Step 1: Get total count of all words in histogram
    # print histogram
    token_count = get_token_count(histogram)
    type_count = len(histogram.keys())
    # Step 2: Generate random number between 0 and total count - 1
    random_int = random.randint(0, token_count-1)
    index = 0
    list_of_keys = histogram.keys()
    # print 'the random index is:', random_int
    for i in range(0, type_count):
        index += histogram[list_of_keys[i]]
        # print index
        if(index > random_int):
            # print list_of_keys[i]
            return list_of_keys[i]

    # Here is where I can use a binary search?  Start by going to the half way
    # of all dictionary keys...Then get sum from all the keys previously and
    # see if > or < than the random value?
    # sorted_list_of_keys
    # return binary_search(histogram, list_of_keys, random_int)


def tuple_histogram(file_name):
    dict_historgram = histogram(file_name)
    print 'dict_historgram:', dict_historgram
    tuple_histogram = dict_historgram.items()
    print tuple_histogram
    return tuple_histogram


def tuple_histogram_sorted(file_name):
    tup_histogram = tuple_histogram(file_name)
    return sorted(tup_histogram, key=itemgetter(1), reverse=True)

def histogram(file_name):
    '''
    A function which takes a source_text argument (can be either a filename or
    the contents of the file as a string, your choice) and return a histogram
    data structure that stores each unique word along with the number of times
    the word appears in the source text.
    '''
    data_file = open(file_name, 'r')
    words_list = data_file.read().split()
    for word in words_list:
        word = word.decode('utf-8').lower().encode('utf-8')
        # print word

    histogram = dict()

    for word in words_list:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def unique_words(histogram):
    '''
    A function that takes a histogram argument and returns the total count of
    unique words in the histogram. For example, when given the histogram
    for The Adventures of Sherlock Holmes, it returns the integer 8475.
    '''
    return len(histogram)


def frequency(histogram, word):
    '''
    A function that takes a word and histogram argument and returns the number of
    times that word appears in a text. For example, when given the word "mystery"
    and the Holmes histogram, it will return the integer 20.
    '''
    return histogram[word]


def main():
    file_name = 'small_text_sample.txt'
    histogram_data = tuple_histogram_sorted(file_name)
    print histogram_data
    # print return_random_word(histogram_data)

    # print weighted_random_word_tuple(histogram_data)
    test_weighted_random_word_tuple(histogram_data, 1000)
    # print unique_words(histogram_data)
    # print frequency(histogram_data, 'all')


main()
