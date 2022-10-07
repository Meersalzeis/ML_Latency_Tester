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
        x, y = predictions["real_rtt"], predictions["abs_times"]

        plt.subplots(nrows=1, num="pings to "+address)
        plt.title("pings to "+address)
        plt.xlabel("start of ping in ms since 1970 began")
        plt.ylabel("round trip time in ms")
        plt.plot(y , x, 'o')
        plt.show()

        # For each ML we applied to that datas address, show results
        should_be = x
        MLA_name_list = predictions["names"]
        MLA_name = "not set yet"
        
        nr_of_shown_datapoints = len(predictions)-2
        for MLA_nr in range(0, nr_of_shown_datapoints ): # -2 for , "names" and "real_rtt" keys, rest are MLAs
            current_predictions = predictions[MLA_nr]
            MLA_name = MLA_name_list[MLA_nr]

            print("current algorithm = " + MLA_name )

            # arrays needed:    should_be, predicted, error, calc_time
            predicted = current_predictions[0].ravel()
            calc_time = current_predictions[1]

            # plot lines
            plt.title(MLA_name)
            plt.bar(np.arange(len(should_be))-0.2, should_be, width=0.4,  label = "real rtts")
            plt.bar(np.arange(len(predicted))+0.2, predicted, width=0.4, label = "predicted rtts")
            #plt.bar(indexes, calc_time, label = "calculation time")
            plt.xlabel("index of data point")
            plt.ylabel("round trip time in ms")
            plt.legend()
            plt.show()