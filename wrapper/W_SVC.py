from sklearn.svm import SVC

import classification

import numpy as np
import timeit

# https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html?highlight=svc

class W_SVC( classification.classification_MLA ) :

    svc = SVC()

    def get_name(self):
        return "Support Vector Machine - Classification"

    def fit(self, input_data, real_rtts):

        classified_data = self.rtt_to_class_nrs(real_rtts)

        self.svc.fit(input_data, classified_data)
    
    def test(self, input_data, should_be_data):
        results = []

        for i in range(0, should_be_data.size):
            start_time = timeit.default_timer()
            prediction_point = self.svc.predict(  np.array([input_data[i]])  )
            end_time = timeit.default_timer()
            time_needed = (end_time - start_time) * 1000 # s to ms

            results.append(np.array([prediction_point[0], time_needed], dtype=object))

        return np.array(results).transpose()