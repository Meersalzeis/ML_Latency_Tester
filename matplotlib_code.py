import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import classification 

from sklearn.metrics import RocCurveDisplay

def display(input_data, prediction_data):

    # For each address
    for address in prediction_data:
        
        predictions = prediction_data[address]
        x, y = predictions["real_rtt"], predictions["abs_times"]
        nr_total_datapoints = predictions["nr_total_datapoints"]
        should_be = x
        index_list = np.arange(len(should_be))
        print("new address")

        # print statistics to input
        print("Median of input: ", np.median(should_be))
        print("Average of input: ", np.average(should_be))
        print("Variance of input: ", np.var(should_be))
        print("Standard Deviation of input: ", np.std(should_be))
        print("Number of Test points: ", len(should_be))
        print("Number of Data set total: ", nr_total_datapoints)

        # show the input
        plt.title("Dataset pings")

        plt.subplot(1, 2, 1)
        plt.title("pings to "+address)
        plt.xlabel("minutes since first ping")
        plt.ylabel("round trip time (RTT) in ms")
        plt.plot(y , x, 'o')

        x_max = np.max(x)
        histogramm = np.arange(x_max+1)
        i = 0
        while i < x_max+1 :
            histogramm[i] = np.count_nonzero( x == i )
            i += 1

        plt.subplot(1, 2, 2)
        plt.title("histogramm pings to "+address)
        plt.xlabel("occurences of RTT size")
        plt.ylabel("round trip time (RTT) in ms")
        plt.plot( histogramm )

        plt.show()

        # Helpers for MLA display
        MLA_name_list = predictions["names"]
        MLA_name = "not set yet"
        error_comparison = {}
        time_comparison = {}

        # For each ML we applied to that datas address, show results
        nr_of_shown_datapoints = len(predictions)-4 # -4 for keys that dont represent MLAs, like "real_rtt"
        for MLA_nr in range(0, nr_of_shown_datapoints ): 

            # Initialied for this iteration
            current_predictions = predictions[MLA_nr]
            MLA_name = MLA_name_list[MLA_nr]

            # arrays needed:
            predicted = current_predictions[0].ravel()
            calc_time = current_predictions[1]
            error = abs( np.subtract( predicted, should_be ) )
            time_comparison.update( {MLA_name: calc_time} )
            error_comparison.update( {MLA_name: error} )
            
            # statistical numbers
            print("current algorithm = " + MLA_name )
            print("Max Error = ", np.max(error)) 
            print("Median of error: ", np.median(error))
            print("Average of error: ", np.average(error))
            print("Variance of error: ", np.var(error))
            print("Standard Deviation of error: ", np.std(error))
            # TODO Gini index or other error measurements (size of 5% worst errors?)

            # show plot
            plt.title(MLA_name)

            # plt.bar recommended for small (<200 Datapoints) Datasets, for larger plt.plot recommended

            #plt.bar(index_list -0.3, should_be, width=0.3,  label = "real rtts")
            #plt.bar(index_list , predicted, width=0.3, label = "predicted rtts")
            #plt.bar(index_list +0.3, error, width=0.3, label = "error")

            #plt.scatter(index_list , should_be, label = "real rtts")
            #plt.scatter(index_list , predicted, label = "predicted rtts")
            #plt.scatter(index_list , error, label = "error")

            plt.plot(index_list , should_be, label = "real rtts", color = 'green')
            plt.plot(index_list , predicted, label = "predicted rtts", color = 'blue' )
            plt.plot(index_list , error, label = "error", color = 'orangered')

            plt.xlabel("index of data point")
            plt.ylabel("round trip time in ms")
            plt.legend(bbox_to_anchor=(1,1), loc = "upper left")
            plt.tight_layout()
            plt.show()
        
        # show time comparison
        for k in time_comparison.keys():
            plt.plot(index_list , time_comparison[k], label = k)
        
        plt.title("runtime comparison")
        plt.xlabel("index of data point")
        plt.ylabel("round trip time in ms")
        plt.legend(bbox_to_anchor=(1,1), loc = "upper left")
        plt.tight_layout()
        plt.show()

        # show error comparison as graphs
        for k in error_comparison.keys():
            plt.plot(index_list , error_comparison[k], label = k)
        plt.plot(index_list, should_be, label = "measured rtt")

        plt.title("error comparison")
        plt.xlabel("index of data point")
        plt.ylabel("error in ms")
        plt.legend(bbox_to_anchor=(1,1), loc = "upper left")
        plt.tight_layout()
        plt.show()

        # show total error comparison
        i = 0
        for k in error_comparison.keys():
            i += 1
            plt.bar(i, np.sum(error_comparison[k]), label = k )
        
        plt.title("total error comparison")
        plt.xlabel("Algorithm")
        plt.ylabel("error in ms")
        plt.legend(bbox_to_anchor=(1,1), loc = "upper left")
        plt.tight_layout()
        plt.show()

