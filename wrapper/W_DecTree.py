from sklearn.tree import DecisionTreeClassifier

import classification

import numpy as np
import time
import timeit

# https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html?highlight=decision+tree

class W_DecTree( classification.classification_MLA ) :

    decTree = DecisionTreeClassifier(random_state=0)

    def get_name(self):
        return "Decision Tree"

    def fit(self, input_data, real_rtts):

        classified_data = self.rtt_to_class_nrs(real_rtts)

        self.decTree.fit(input_data, classified_data)
    
    def test(self, input_data, should_be_data):
        results = []

        for i in range(0, should_be_data.size):
            #start_time = timeit.perf_counter_ns()
            start_time = time.time()
            prediction_point = self.decTree.predict(  np.array([input_data[i]])  )
            #end_time = timeit.perf_counter_ns()
            end_time = time.time()
            time_needed = (end_time - start_time) # * 1000 # s to ms

            #print("DecTree entrytime = ",time_needed)

            results.append(np.array([prediction_point[0], time_needed], dtype=object))

        return np.array(results).transpose()