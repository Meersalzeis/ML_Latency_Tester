import data_refinery, testbench, result_refinery, matplotlib_code
import data_reader

#train_file_name = "./Datasets/100pointsOf50.txt"
#test_file_name = "./Datasets/100pointsOf100.txt"

train_file_name = "./Datasets/LadenKeller2.txt"  # Stationär WLAN 1
#train_file_name = "./Datasets/WLAN2.txt"  # Stationär WLAN 2
#train_file_name= "./Datasets/LadenMobilnetz1.txt"  # Mobilnetz 1 (schlechter Empfang)
#train_file_name = "./Datasets/Mobil2.txt"  # Mobilnetz 2 (besserer Empfang)

#test_file_name = "./Datasets/LadenKeller2.txt"  # Stationär WLAN 1
#test_file_name = "./Datasets/WLAN2.txt"  # Stationär WLAN 2
#test_file_name= "./Datasets/LadenMobilnetz1.txt"  # Mobilnetz 1 (schlechter Empfang)
test_file_name = "./Datasets/Mobil2.txt"  # Mobilnetz 2 (besserer Empfang)

# read in raw data
train_addresses, train_abs_times, train_rtts = data_reader.read_file( train_file_name )
test_addresses, test_abs_times, test_rtts = data_reader.read_file( test_file_name )
print("data reader done")

# sort into dict of datasets indexed by addresses, prepare to relative time
refined_train_input = data_refinery.refine( train_addresses, train_abs_times, train_rtts )
refined_test_input = data_refinery.refine( test_addresses, test_abs_times, test_rtts )
print("refined input")

# evaluate the MLAs for each address separately, but use same address for test
raw_output = {} # new dictionary
for address in refined_train_input:
    print("Adress is " , address)
    train_rtts, train_abs_times, train_input = refined_train_input[address].get_values()
    test_rtts, test_abs_times, test_input = refined_test_input[address].get_values()
    print("ALT_MAIN ITER - train data size", len(train_abs_times), " and test data size ", len(test_abs_times))

    refined_address_data = testbench.evaluate_change_test( train_rtts, train_abs_times, train_input, test_rtts, test_abs_times, test_input )

    raw_output.update({ address : refined_address_data }) # add to dict

print("evaluated")

# put the sets into the testbench, and ggf.process results
refined_output = result_refinery.refine(raw_output)
print("refined output")

#display results
matplotlib_code.display( refined_test_input, refined_output ) # refined_test_input isn't used anyways
print("displayed")
