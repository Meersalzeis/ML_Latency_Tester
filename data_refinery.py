from xml.sax.handler import EntityResolver
import numpy as np

NR_OF_INPUT_POINTS_PER_PREDICTION = 3

# sorts by address and creates relative time from absolute time
# returns a dictionary with addresses as keys, datasets with rtts and corresponding recording times as content
def refine(addresses, abs_times, rtts):
    
    datasets = {} # new dictionary

    for i in range(addresses.size):

        # make new dataset for new address if needed
        if not addresses[i] in datasets:
            datasets.update( {addresses[i]: Address_data_set()} )
        
        # add values to set
        datasets[addresses[i]].add_values( int(rtts[i]), int(abs_times[i])  )

    reset()
    return datasets

def reset():
    global abs_times
    global entries
    global rtts
    abs_times = []
    entries = []
    rtts = []

# stores and prcoesses information of 1 address
class Address_data_set() :

    """ removed because class variables, not instance variables
    # save older data to compute the input for newer sets
    rtts = []
    abs_times = []
    entries = [] # add up all entries
    """

    def __init__(self):
        self.rtts = []
        self.abs_times = []
        self.entries = [] # add up all entries / input

    def add_values(self, new_rtt, abs_time):
        N = NR_OF_INPUT_POINTS_PER_PREDICTION

        # make new relative time and keep abs_time updated
        older_rtts = [] # list
        older_times = []

        # For every point we include in the input
        for i in range(0,N):

            # calculate index offset
            offset_index = len(self.rtts) - i

            if offset_index <= 0:
                # add rtts and time substitute
                older_rtts.append(0)
                older_times.append(2147483647) # max value of float32, larger is restricted by some ML_Algorithm
            else:
                # add rtts and relative time to this, new ping   -1 because we look for the pings before
                older_rtts.append(self.rtts[offset_index-1])
                older_times.append( abs_time - self.abs_times[offset_index-1] )

        # add values for new point
        entry = np.concatenate((np.asarray(older_rtts), np.asarray(older_times)))
        self.entries.append(entry)

        # add new point to old points
        self.rtts.append(new_rtt)
        self.abs_times.append(abs_time)
    
    def get_values(self):
        return np.asarray(self.rtts), np.asarray(self.abs_times), np.asarray(self.entries).squeeze()
    

        


# depricated class, stores and prcoesses information of 1 address
class old_Address_data_set() :

    rtts = []
    rel_times = []
    last_abs_time = 0


    def add_values(self, new_rtt, abs_time):

        # make new relative time and keep abs_time updated
        new_rel_time = abs_time - self.last_abs_time
        if (self.last_abs_time == 0):
             new_rel_time = 0
        self.last_abs_time = abs_time

        # add values
        self.rtts.append(new_rtt)
        self.rel_times.append(new_rel_time)
    
    def get_values(self):
        return np.asarray(self.rtts).reshape(-1, 1), np.asarray(self.rel_times).reshape(-1, 1)

