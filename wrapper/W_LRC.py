from sklearn.linear_model import LogisticRegression

import classification

import numpy as np
import time
from timeit import timeit

# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html



class W_LRC( classification.classification_MLA ) :

    lrc = LogisticRegression()

    def get_name(self):
        return "Logistic Regression Classification"

    def fit(self, input_data, real_rtts):

        classified_data = self.rtt_to_class_nrs(real_rtts)

        self.lrc.fit(input_data, classified_data)
    
    def test(self, input_data, should_be_data):
        results = []

        for i in range(0, should_be_data.size):
            global prediction_point, this
            prediction_point = np.NAN
            this = self
            start_time = time.time()
            timeit_needed = timeit("global thisprediction_point = this.lrc.predict(  np.array([input_data[i]])  )", number=1, globals=globals())
            end_time = time.time()
            time_needed = (end_time - start_time) * 1000 # s to ms
            print("timeit=", timeit_needed, " and time=",time_needed)

            results.append(np.array([prediction_point[0], time_needed], dtype=object))

        return np.array(results).transpose()