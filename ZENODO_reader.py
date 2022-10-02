from datetime import datetime
import numpy as np

# Reads in Data from https://zenodo.org/record/1287752

# reads a file into raw data
def read_file(file_name):
    op_addresses = []
    abs_times = []
    rtts = []

    biggest_index = 0

    # set up reader
    reader = open(file_name)
    # First line is settings for human info
    reader.readline()

    # collect all lines in a dictionary
    lines_dict = {}

    # Make a loop read each line
    while True:

        # extract information to array, or end
        data_snipplets = reader.readline().split(',')
        if len( data_snipplets ) < 4: # not a valid line -> end
            break

        # connection failure, senderrors, timeouts etc. lead to no rtts.
        # Keep in mind that ''wrong'' answers are still used as data points
        if data_snipplets[3] == '':
            continue # skip this entry
        
        # Keep track of largest index
        current_index =  int( data_snipplets[0] )
        if current_index > biggest_index:
            biggest_index = current_index

        #dt_string = datetime.fromisoformat(data_snipplets[1], tz=None)
        dt_obj = datetime.strptime(data_snipplets[1], '%Y-%m-%d %H:%M:%S.%f')
        abs_time = dt_obj.timestamp() * 1000 # to milliseconds
        
        # [ operator = adress, abs_time, rtt = transaction time (sec to ms)]
        current_entry = [ data_snipplets[2] , abs_time, float(data_snipplets[3]) *1000 ] 
        lines_dict.update( {current_index: current_entry})


    # read all lines, ordered by index
    for index in range(1, biggest_index+1):
        if index in lines_dict:
            # Because ids are not complete we filter those out

            line_data = lines_dict[index]

            op_addresses.append(line_data[0])
            abs_times.append(line_data[1])
            rtts.append(line_data[2])


    # prepare return data
    op_addresses = np.array(op_addresses)
    abs_times = np.array(abs_times)
    rtts = np.array(rtts)

    return op_addresses, abs_times, rtts