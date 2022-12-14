import numpy as np
from wrapper.W_DecTree import W_DecTree
from wrapper.W_LRC import W_LRC
from wrapper.W_MLP import W_MLP
from wrapper.W_SVR import W_SVR
from wrapper.W_SVC import W_SVC
from sklearn.model_selection import train_test_split

from ML_Algs.last_x_avg import lastXavg

TEST_SET_RATIO = 0.25
ML_list = []
MLA_names_list = []

# evaluates rtts and rel_times of a single address
def evaluate(rtts, rel_times):
    
    make_ML_list()

    train_input, test_input, train_output, test_should_be = split_data(rtts, rel_times)

    train_mls(train_input, train_output)
    return test_mls(test_input, test_should_be)


# train all Machine Learning Algorithms (in ML_list) with given train-data
def train_mls(train_input, train_output):
    for MLA in ML_list:
        #print("fit alg " + str(MLA) )
        MLA.fit( train_input, train_output)


# let all Machine Learning Algorithms (in ML_list) predict given data points, with, if specified, correcting themselves after each point
def test_mls(test_data, test_should_be):
    ML_count = len( ML_list )

    MLs_Prediciton_Results = {} # new empty dictionary

    # add input parameters for understanding / displaying
    MLs_Prediciton_Results.update( {"time": test_data})
    MLs_Prediciton_Results.update( {"real_values": test_should_be})
    MLs_Prediciton_Results.update( {"names": MLA_names_list })

    for i in range (0, ML_count) :
        this_MLs_results = ML_list[i].test(test_data, test_should_be)

        MLs_Prediciton_Results.update( {i: this_MLs_results} )
        #results[i] = this_MLs_results

    return MLs_Prediciton_Results


def make_ML_list():
    global ML_list # references the ML_list outside of def, not a new internal ML_list
    ML_list = []

    # Regression
    ML_list.append( lastXavg(10) ) # last X values as average
    ML_list.append( lastXavg(3) ) # last X values as average
    ML_list.append( W_MLP() ) # Multi layer perceptron for regression

    # Classification
    ML_list.append( W_DecTree() )

    # Both Regression and Classification
    ML_list.append( W_SVR() ) # support vector machine for regression
    ML_list.append( W_SVC() ) # support vector machine for classification
    # TODO MAYBE Logistic Regression
    ML_list.append( W_LRC() )

    global MLA_names_list
    MLA_names_list = []
    for MLA in ML_list:
        MLA_names_list.append( MLA.get_name() )

# Splices of the later parts to test data, into    train_input, test_input, train_output, test_should_be
def split_data(rtts, rel_times):
    entry_count = rtts.size
    train_size = round( entry_count * ( 1 - TEST_SET_RATIO ) )
    return rel_times[:train_size-1], rel_times[train_size:], rtts[:train_size-1], rtts[train_size:]


# splits current data randomly into train and test sets. Can be replaced to later use one sample to test another
def random_split_data(rtts, rel_times):
    train_input, test_input, train_output, test_should_be = train_test_split( rel_times, rtts, test_size=0.25, random_state=7 )
    return train_input, test_input, train_output, test_should_be
    