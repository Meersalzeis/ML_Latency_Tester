import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn.metrics import RocCurveDisplay

def display(input_data, prediction_data):

    # For each address
    for address in prediction_data:
        predictions = prediction_data[address]

        print("new address")

        # First show the input
        x, y = predictions["real_values"], predictions["time"]

        plt.subplots(nrows=1, num="pings to "+address)
        plt.title("pings to "+address)
        plt.xlabel("time relative to previous ping in ms")
        plt.ylabel("round trip time in ms")
        plt.plot(x , y, 'o')
        plt.show()

        # For each ML we applied to that datas address, show results
        should_be = x
        MLA_name_list = predictions["names"]
        MLA_name = "not set yet"
        
        for MLA_nr in range(0, len(predictions)-3 ): # -3 for "time", "names" and "real_value" keys, rest are MLAs
            current_predictions = predictions[MLA_nr]
            MLA_name = MLA_name_list[MLA_nr]

            print("current algorithm = " + MLA_name )

            # arrays needed:    should_be, predicted, error, calc_time
            predicted = current_predictions[0]
            calc_time = current_predictions[1]

            # plot lines
            plt.title(MLA_name)
            plt.plot(should_be, label = "real rtts")
            plt.plot(predicted, label = "predicted rtts")
            plt.plot(calc_time, label = "calculation time")
            plt.xlabel("index of data point")
            plt.ylabel("round trip time in ms")
            plt.legend()
            plt.show()