import math
import numpy


def main():
    data = getData(input("Welcome to Feature Selection!\nDataset File Name? "))
    algorithm = int(input("Welcome to Feature Selection!\nAlgorithm? 1 - Forward Selection 2 - Backwards Elimination "))
    feature_selection(data, algorithm)


def feature_selection(data, algorithm):
    feature_set = []
    accuracies = []
    if algorithm == 1:
        for i in range(1, len(data[0])):
            max_accuracy = 0
            best_feature = 0
            for j in range(1, len(data[0])):
                if not feature_set.__contains__(j):
                    feature_set.append(j)
                    accuracy = k_fold_validation(data, feature_set)
                    feature_set.pop()
                    if accuracy > max_accuracy:
                        best_feature = j
                        max_accuracy = accuracy
            feature_set.append(best_feature)
            accuracies.append(max_accuracy)
            print("Feature Set: %s, Best Accuracy: %.3f, Feature Added: %s" % (feature_set, max_accuracy, best_feature))


def k_fold_validation(data, feature_set):
    num_correct = 0

    return num_correct / (len(data))


def getData(file_name):
    array = []
    file = open(file_name)

    for line in file:
        row = [float(i) for i in line.split(" ") if i != ""]
        array.append(row)
    return array


main()
