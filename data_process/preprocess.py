from data_process import prepare

import pickle
import _pickle as cPickle
import numpy

# from sklearn import cross_validation
from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif


def processor(train_size):
    full_tweets_train, full_labels_train = prepare.get_training_data_list()

    # test_size is the percentage of events assigned to the test set
    # (remainder go into training)

    features_train, features_test, labels_train, labels_test = train_test_split(full_tweets_train, full_labels_train,
                                                                                test_size=train_size, random_state=42)

    # text vectorization--go from strings to lists of numbers
    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')

    features_train_transformed = vectorizer.fit_transform(features_train)
    features_test_transformed = vectorizer.transform(features_test)

    # feature selection, because text is super high dimensional and
    # can be really computationally chewy as a result
    selector = SelectPercentile(f_classif, percentile=10)
    selector.fit(features_train_transformed, labels_train)
    features_train_transformed = selector.transform(features_train_transformed).toarray()
    features_test_transformed = selector.transform(features_test_transformed).toarray()

    # info on the data
    print("No. of Sarcastic training Tweets: ", sum(labels_train))
    print("No. of Normal training Tweets: ", len(labels_train) - sum(labels_train))

    return features_train_transformed, features_test_transformed, labels_train, labels_test, sum(labels_train), (
    len(labels_train) - sum(labels_train))
