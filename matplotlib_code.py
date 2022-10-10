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
        error_comparison = {}
        time_comparison = {}

        nr_of_shown_datapoints = len(predictions)-3
        index_list = np.arange(len(should_be))
        for MLA_nr in range(0, nr_of_shown_datapoints ): # -2 for , "names", "abs_times" and "real_rtt" keys, rest are MLAs
            current_predictions = predictions[MLA_nr]
            MLA_name = MLA_name_list[MLA_nr]

            print("current algorithm = " + MLA_name )

            # arrays needed:    should_be, predicted, error, calc_time
            predicted = current_predictions[0].ravel()
            calc_time = current_predictions[1]
            error = abs( np.subtract( predicted, should_be ) )
            time_comparison.update( {MLA_name: calc_time} )
            error_comparison.update( {MLA_name: error} )

            # show plot
            plt.title(MLA_name)

            # plt.bar recommended for small (<200 Datapoints) Datasets, for larger plt.plot recommended

            plt.bar(index_list -0.3, should_be, width=0.3,  label = "real rtts")
            plt.bar(index_list , predicted, width=0.3, label = "predicted rtts")
            plt.bar(index_list +0.3, error, width=0.3, label = "error")

            #plt.scatter(index_list , should_be, label = "real rtts")
            #plt.scatter(index_list , predicted, label = "predicted rtts")
            #plt.scatter(index_list , error, label = "error")

            #plt.plot(index_list , should_be, label = "real rtts")
            #plt.plot(index_list , predicted, label = "predicted rtts")
            #plt.plot(index_list , error, label = "error")

            plt.xlabel("index of data point")
            plt.ylabel("round trip time in ms")
            plt.legend()
            plt.show()
        
        # show time comparison
        for k in time_comparison.keys():
            plt.plot(index_list , time_comparison[k], label = k)
        
        plt.title("runtime comparison")
        plt.xlabel("index of data point")
        plt.ylabel("round trip time in ms")
        plt.legend()
        plt.show()

        # show error comparison
        for k in error_comparison.keys():
            plt.plot(index_list , error_comparison[k], label = k)
        
        plt.title("error comparison")
        plt.xlabel("index of data point")
        plt.ylabel("round trip time in ms")
        plt.legend()
        plt.show()