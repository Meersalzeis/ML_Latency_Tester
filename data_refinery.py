import numpy as np

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

    return datasets


# stores and prcoesses information of 1 address
class Address_data_set() :

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

