import numpy as np

rtts, abs_times, addresses = [],[],[]
separator= " + "

# reads a file into raw data
def read_file(file_name):
    reader = open(file_name)
    reader.readline() # First line is human-readable info

    global rtts, abs_times, addresses

    counter = 0
    stillRead = True # Signal to stop reading, given by addNextLine

    while stillRead:
        stillRead = addNextLine(reader)
        counter += 1

    # convert python lists to np arrays for ML
    np_addresses = np.asarray(addresses)
    np_abs_times = np.asarray(abs_times)
    np_rtts = np.asarray(rtts)
    
    rtts, abs_times, addresses = [],[],[] # make empty for next reading
    reader.close()

    return np_addresses, np_abs_times, np_rtts



# Adds next line of data to lists, or signals it cannot read line to halt reading
def addNextLine(file_reader):
    line = file_reader.readline()

    if (not line) or line == "": # Check end of file
        return False
    
    pieces = line.split(separator)

    if len (pieces) != 3:
        print("error in line " + line + "! too many separators! " + separator )
        return False
    
    addresses.append(pieces[0])
    abs_times.append(pieces[1])
    rtts.append( pieces[2].replace("\n", "") ) # replace not by index, last has no \n
    return True