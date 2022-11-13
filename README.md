# sweep_hash
sweep_hash takes in a string, single int or single float and returns a deterministic hash. chain_hash builds a list of n hashes each built on the last for high security hashes

sweep_hash is a function that takes in a string, single int or single float and returns a deterministic hash
data is run through 13 stages where data is manipulated and some leading and trailing data is swept off throughout the process and then the data moves on to the next stages

chain_hash 
runs the sweep_hash function on a given string a specified number of times and returns the final hash chain as a list of hashes
because the chain_hash run the sweep_hash function on the input_data a given number of times the
larger the number of runs the more secure the hash, and the longer it will take to run

checking hash against user input
check_sweep_hash will return true if the input produces the same hash and false otherwise
check_chain_hash will return true if the input produces the same hash and false otherwise

sweep_hash will return a 256 character long output
chain_hash will return a 256 character long output for each of n number_of_runs as a list of 256 character long outputs
