import numpy as np
import time
import timeit

from MLA import MLA

class lastXavg:

    values = (MLA) # list is used from back to front
    max = 0

    def __init__(self, nr_of_values):
        self.max = nr_of_values
        
    
    def get_name(self):
        return "average of last " + str(self.max) + " values"


    # fits the algorithm to the new array, discarding old numbers. input is ignored
    def fit(self, input, output):

        # output is 1dimensional array => size = nr of values
        if output.size <= self.max :

            self.values = output.tolist()
        else:

            # last <max_stored_values> of the numpy array "output"
            self.values = output[-self.max:].tolist()


    # predicts the next value
    def pred_value(self):
        return np.sum(self.values) / len(self.values)


    # predicts an array of new values
    def predict(self, input):
        return_values = np.zeros(input.size )
        for i in range(input.size ) :
            return_values[i] = self.pred_value(self)
        
        return return_values
    

    # predicts an array of values after another, while adjusting in between
    def test(self, test_input, test_output):
        results = []
        for i in range(0, test_output.size):

            start_time = time.time()
            predicted_point = self.pred_value()
            end_time = time.time()

            time_needed = (end_time - start_time) * 1000 # convert from seconds to ms

            results.append( np.array([predicted_point, time_needed]))
            self.new_Entry(test_output[i])
        
        results = np.transpose(  np.array(results)  )
        return np.asarray(results)

        

    # processes a new value to adjust predicitons
    def new_Entry(self, newValue):
        if len(self.values) == self.max:
            del self.values[0] # deletes last entry in list
        
        self.values.append(newValue)