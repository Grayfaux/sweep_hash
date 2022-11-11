from hash_stages import *


# sweep_hash is a function that takes in a string, single int or single float and returns a deterministic hash
def sweep_hash(input_data: str or int or float) -> str:

    if type(input_data) != str:
        input_data = str(input_data)

    a = convert_to_int_list(input_data)
    b = shift_int_list(a, 11)
    c = joined_integers(b)
    d = multiply_int_list(c, 100)
    e = joined_integers(d)
    f = split_int_list(e, 6)
    g = pad_lists(f)
    h = alternate_lists(g)
    i = split_and_reverse(h, 6)
    j = joined_integers(i)
    k = convert_to_int_list(j)
    l = convert_to_hex(k)
    m = trim_string(l, 256)
    return m


# runs the sweep_hash function on a given string a specified number of times and returns the final hash chain as
# a list of hashes.
# because the chain_hash run the sweep_hash function on the input_data a given number of times the
# larger the number of runs the more secure the hash, and the longer it will take to run
def chain_hash(input_data, number_of_runs):

    chained_hash = []
    for i in range(number_of_runs):
        input_data = sweep_hash(input_data)
        chained_hash.append(input_data)
        # print("iteration " + str(i) + " complete" + " " + input_data)
    return chained_hash


# checks if a given string matches a given sweep_hash
def check_sweep_hash(input_data, input_hash):
    if sweep_hash(input_data) == input_hash:
        return True
    else:
        return False


# checks if a given string matches a given chain_hash
def check_chain_hash(input_data, input_hash):
    number_of_runs = len(input_hash)
    if chain_hash(input_data, number_of_runs) == input_hash:
        return True
    else:
        return False
