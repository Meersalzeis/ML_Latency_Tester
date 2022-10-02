import numpy as np
import time
from sklearn.svm import SVR

class W_SVR() :

    svr = SVR()

    def get_name(self):
        return "Support Vector Machine - Regression"

    def fit(self, input_data, output_data):
        self.svr.fit(input_data, output_data)
    
    def test(self, input_data, should_be_data):
        results = []

        for i in range(0, should_be_data.size):
            start_time = time.time()
            prediction_point = self.svr.predict(  np.array([input_data[i]])  )
            end_time = time.time()
            time_needed = (end_time - start_time) * 1000 # s to ms

            results.append(np.array([prediction_point[0], time_needed], dtype=object))

        return np.array(results).transpose()
        #return self.svr.predict(input_data)