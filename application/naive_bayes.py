#!/usr/bin/python
from sklearn.naive_bayes import GaussianNB
from time import time
from sklearn.metrics import accuracy_score
from data_process import preprocess


# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
def naive_classifier(train_size):
    features_train, features_test, labels_train, labels_test, sarcastic_size, normal_size = preprocess.processor(
        train_size)

    """
    print(features_train[0:5])
    print()
    print(labels_train[0:5])
    """
    clf = GaussianNB()

    t1 = time()
    clf.fit(features_train, labels_train)
    pred = clf.predict(features_test)
    print('Training Time is ' + str((time() - t1)))

    t2 = time()
    accuracy = accuracy_score(pred, labels_test)
    print("Prediction Time is " + str((time() - t2)))

    print("Accuracy is ", accuracy)

    # print the graph with separator
    # plot_classifiers.print_graph(clf,features_train,labels_train,features_test,labels_test)

    return normal_size, sarcastic_size, accuracy

