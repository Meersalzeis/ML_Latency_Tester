import timeit
import numpy as np
from sklearn.neural_network import MLPRegressor

# https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html

class W_MLP():

    mlp = MLPRegressor(hidden_layer_sizes=(25,))

    def get_name(self):
        return "Multi Layer Perceptron (Regression)"

    def fit(self, input_data, output_data):

        print("MLP - input shape: " , input_data.shape, " output shape:", output_data.shape)

        self.mlp.fit(input_data, output_data)
    
    def test(self, input_data, should_be_data):
        results = []

        for i in range(0, should_be_data.size):
            start_time = timeit.default_timer()
            prediction_point = self.mlp.predict(  np.array([input_data[i]])  )
            end_time = timeit.default_timer()
            time_needed = (end_time - start_time) * 1000 # s to ms

            results.append(np.array([prediction_point[0], time_needed], dtype=object))

        return np.array(results).transpose()