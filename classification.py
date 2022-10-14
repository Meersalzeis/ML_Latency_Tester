import numpy as np
from MLA import MLA

# limits for the classes of the classification
#limits = (30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 300, 500, 750, 1000) # geschätzt
#limits = (20, 30, 50, 80, 130, 210, 340, 550, 890, 1440) # fibonacci
#limits = (10, 17, 31, 56, 100, 177, 316, 562, 1000) # exp in 4er Schritten
limits = (20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000) # 10er dann 100er Schritte


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