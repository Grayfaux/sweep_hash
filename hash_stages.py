# converts a string of letters to a list of integers
def convert_to_int_list(string):
    int_list = []
    for letter in string:
        int_list.append(ord(letter))
    return int_list


# converts a list of integers to a string of letters
def convert_to_string(int_list):
    string = ""
    for integer in int_list:
        string += chr(integer)
    return string


# shifts a list of integers by a given amount
def shift_int_list(int_list, shift):
    shifted_int_list = []
    for integer in int_list:
        shifted_int_list.append(integer + shift)
    return shifted_int_list


# removes decimal points from a list of floats and returns a joined string of integers including
# remainder
def joined_integers(input_list):
    string_list = []
    for i in input_list:
        i = str(i)
        for x in i:
            if x != ".":
                string_list.append(x)
    return string_list


# multiplies a list of string of integers by a given power
def multiply_int_list(int_list, power):
    multiplied_int_list = []
    for i in int_list:
        multiplied_int_list.append(int(i) ** power)
    return multiplied_int_list


# splits a list of integers into a given number of lists of equal length and pads the last list with zeros so that
# all lists are the same length
def split_int_list(int_list, number_of_lists):
    split_list = []
    for i in range(number_of_lists):
        split_list.append(int_list[i::number_of_lists])
    return split_list


# takes a list of lists and checks if they are equal in length and if they are not, pads the shorter lists with zeros
def pad_lists(list_of_lists):
    max_length = 0
    for i in list_of_lists:
        if len(i) > max_length:
            max_length = len(i)
    for i in list_of_lists:
        while len(i) < max_length:
            i.append(0)
    return list_of_lists


# takes a list of lists of integers and creates a new list of all lists alternated with each other in reverse order
def alternate_lists(list_of_lists):
    alternate_list = []
    for i in range(len(list_of_lists[0])):
        for x in list_of_lists:
            alternate_list.append(int(x[i])*i + 2)
    return alternate_list


# splits a list of integers into a given number of lists of equal length and reverses the first list
def split_and_reverse(int_list, number_of_lists):
    split_list = []
    for i in range(number_of_lists):
        split_list.append(int_list[i::number_of_lists])
    split_list[0].reverse()
    return split_list


# returns a binary string of serialized hexadecimal numbers from a list of integers of a given length
def convert_to_hex(int_list):
    hex_list = []
    for i in int_list:
        hex_list.append(hex(i))
    hex_string = ""
    for i in hex_list:
        hex_string += i[2:]
    return hex_string


# takes in a string and removes a first and last item of the string until the string is a given length
def trim_string(string, length):
    while len(string) > length:
        string = string[1:-1]
    return string
