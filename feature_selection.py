import math
import numpy


def main():
    data = getData(input("Welcome to Feature Selection!\nDataset File Name? "))
    algorithm = int(input("Welcome to Feature Selection!\nAlgorithm? 1 - Forward Selection 2 - Backwards Elimination "))
    feature_selection(data, algorithm)


def feature_selection(data, algorithm):
    feature_set = []
    accuracies = []
    if algorithm == 1:  ## forwards
        for i in range(1, len(data[0])):  ## for each feature
            max_accuracy = 0
            best_feature = 0
            for j in range(1, len(data[0])):  ## add and check every feature
                if not feature_set.__contains__(j):  ## if not already there
                    feature_set.append(j)  ## add
                    accuracy = k_fold_validation(data, feature_set)  # get accuracy
                    feature_set.pop()  ## remove
                    if accuracy > max_accuracy:  ## if accuracy greater than prev max, record as best feature and as new max accuracy
                        best_feature = j
                        max_accuracy = accuracy
            ## append new best feature and max accuracy to list
            feature_set.append(best_feature)
            accuracies.append(max_accuracy)
            ## print values
            print("Feature Set: %s, Best Accuracy: %.3f, Feature Added: %s" % (feature_set, max_accuracy, best_feature))
    elif algorithm == 2:  ## backwards
        feature_set = list(range(1, len(data[0])))  ## start with all features
        for i in range(1, len(data[0])):
            best_feature = 0
            max_accuracy = 0
            for j in range(1, len(data[0])):  ## check and remove each feature
                if feature_set.__contains__(j):  ## if there
                    feature_set.remove(j)  ## remove
                    accuracy = k_fold_validation(data, feature_set)  ## get accuracy
                    feature_set.append(j)  ## add back
                    if accuracy > max_accuracy:  ## do same as in forward selection
                        best_feature = j
                        max_accuracy = accuracy
            if len(feature_set) > 1:  ## to ensure we don't try to remove from an empty list
                feature_set.remove(best_feature)
                accuracies.append(max_accuracy)
                print("Feature Set: %s, Best Accuracy: %.3f, Feature Removed: %s" % (feature_set, max_accuracy, best_feature))
    else:
        return


def k_fold_validation(data, feature_set):
    num_correct = 0
    for i in range(0, len(data)):

        ## get class label to compare accuracy
        class_label = data[i][0]
        ## initialize predicted variable
        predicted_label = -1

        ## infinite nearest neighbor distance distance and index so the first distance is recorded
        nn_distance = math.inf

        ## nearest neighbor index variable for debugging purposes
        # nn = math.inf
        for j in range(0, len(data)):

            if i != j:  ## do not check yourself otherwise that increases accuracy
                distance = 0  ## create a sum variable before square root for euclidean distance
                for k in feature_set:  ## for each feature, find the square of the difference, sum them all, then square root
                    distance += (data[i][k] - data[j][k]) * (data[i][k] - data[j][k])
                distance = math.sqrt(distance)

                if distance < nn_distance:  ## if distance is less than previously recorded distance, update nearest neighbor distance and predicted label based on nearest distance
                    nn_distance = distance
                    # nn = j for debugging purposes
                    predicted_label = data[j][0]
        # print("Object %s is in class %s, NN is %s in class %s" % (i, class_label, nn, predicted_label))
        if class_label == predicted_label:  ## if prediction matches expectation, record as correct, then return ratio of correct vs attempted.
            num_correct += 1
    return num_correct / (len(data))


def getData(file_name):
    array = []
    file = open(file_name)

    for line in file:
        row = [float(i) for i in line.split(" ") if i != ""]
        array.append(row)
    return array


main()
