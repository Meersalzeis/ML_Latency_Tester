import data_refinery, testbench, result_refinery, matplotlib_code
import data_reader, ZENODO_reader

#text_file_name = "./Datasets/LadenKeller1.txt"
#text_file_name = "./Datasets/testInput.txt"
text_file_name = "./Datasets/testInput2.txt"

# read in raw data
#np_addresses, np_abs_times, np_rtts = ZENODO_reader.read_file( "./Datasets/dataset-op.csv" )
np_addresses, np_abs_times, np_rtts = data_reader.read_file( text_file_name )
print("data reader done")

# sort into dict of datasets indexed by addresses, prepare to relative time
refined_input = data_refinery.refine( np_addresses, np_abs_times, np_rtts )
print("refined input")

# evaluate the mls for each address separately
# raw_output becomes a dictionary of prediciton results for each address, each being a dicitonary of results of MLs, keyed by numbers
raw_output = {} # new dictionary
for address in refined_input:
    rtts, rel_times = refined_input[address].get_values() 
    raw_output.update( {address : testbench.evaluate( rtts, rel_times )} ) # add to dict
print("evaluated")

# put the sets into the testbench, and ggf.process results
refined_output = result_refinery.refine(raw_output)
print("refined output")

#display results
matplotlib_code.display( refined_input, refined_output )
print("displayed")
