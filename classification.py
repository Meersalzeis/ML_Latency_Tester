import numpy as np
from MLA import MLA

limits = (30, 40, 50, 60, 70, 80, 90, 100, 150, 200) # limits for pings to servers
# limits = (100, 500, 1000, 5000) # limits for uploading

def categoryCount():
    return len(limits)

class classification_MLA(MLA):

    def rtt_to_class_nrs(self, rtt_array):

        categorized = np.zeros( rtt_array.shape )

        for index in range(0, np.size(rtt_array)):
            temp = self.rtt_to_class_nr( rtt_array[index] )
            categorized[index] = temp

        #print( categorized )
        return categorized


    #transforms a time value in ms to the coresponding class number
    def rtt_to_class_nr(self, value):
        current_limit_nr = 0
        N = len( limits) 

        while current_limit_nr < N:
            if value > limits[current_limit_nr]:
                current_limit_nr = current_limit_nr + 1

            else:
                return limits[current_limit_nr]
        
        return 9999