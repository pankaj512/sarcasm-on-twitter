from data_process import preprocess
from sklearn.metrics import accuracy_score
from sklearn import svm
from time import time

# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
def svm_classifier(train_size):
    features_train, features_test, labels_train, labels_test, sarcastic_size, normal_size = preprocess.processor(train_size)

    # features_train = features_train[:len(features_train)/100]
    # labels_train = labels_train[:len(labels_train)/100]

    clf = svm.SVC(kernel='rbf', C=10000)

    t1 = time()
    clf.fit(features_train, labels_train)
    print('Training Time is ' + str(time() - t1))

    t2 = time()
    pred = clf.predict(features_test)

    print("Prediction Time is " + str(time() - t2))

    accuracy = accuracy_score(pred, labels_test)

    print("Accuracy is ", accuracy)

    return normal_size, sarcastic_size, accuracy

