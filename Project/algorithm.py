import csv
import datetime
from extract_data import *
from word_encoder import *
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

###############################################################################
# Runs the various classification algorithms on the test data
###############################################################################


# setup progress bar
toolbar_width = 60
sys.stdout.write("\n[%s" % (" " * (toolbar_width/3)))
sys.stdout.write("***Predicting data***")
sys.stdout.write("%s]" % (" " * (toolbar_width/3)))
sys.stdout.flush()
sys.stdout.write("\n")

# initialize variables
column = []
data_val = []
progress = 0
scores = []

#variables for calculating error margin
rf_error_margin = 0
dt_error_margin = 0
nb_error_margin = 0
svm_error_margin = 0
count = 0

# send the extracted data available from extract_data to the encode function
# this function vectorizes the text based data into ASCII format for use by
# the algorithms
encoded_data = encode(data)

# convert the float scores to int. Multiplying by 10 helps us keep the decimal
# level precision which would otherwise be lost in typecasting
i = 0
while i < len(label):
    scores.append(int (float(label[i]) * 10))
    i += 1;

# SVM classifier
#svm_clf = svm.SVC(kernel = 'linear')
#svm_clf.fit(encoded_data, scores)

# Gaussian Naive Bayes
nb_clf = GaussianNB()
nb_clf.fit(encoded_data, scores)

# Random Forest
rf_clf = RandomForestClassifier(n_estimators=100)
rf_clf.fit(encoded_data, scores)

# Decision Tree
dt_clf = tree.DecisionTreeClassifier()
dt_clf.fit(encoded_data, scores)



with open('Datasets/Testing dataset.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        column.append(row['movie_title'])
        column.append(row['actor_1_name'])
        column.append(row['color'])
        column.append(row['director_name'])
        column.append(row['num_critic_for_reviews'])
        column.append(row['duration'])
        column.append(row['director_facebook_likes'])
        column.append(row['actor_3_facebook_likes'])
        column.append(row['actor_2_name'])
        column.append(row['actor_1_facebook_likes'])
        column.append(row['gross'])
        column.append(row['genres'])
        column.append(row['num_voted_users'])
        column.append(row['cast_total_facebook_likes'])
        column.append(row['actor_3_name'])
        column.append(row['num_user_for_reviews'])
        column.append(row['language'])
        column.append(row['country'])
        column.append(row['budget'])
        column.append(row['title_year'])
        column.append(row['actor_2_facebook_likes'])
        column.append(row['imdb_score'])
        column.append(row['movie_facebook_likes'])
        data_val.append(column)
        test_data = encode(data_val)

        # calculate error margin for SVM
        #svm_error_margin += abs((svm_clf.predict (test_data)/10.0) - (float(row['imdb_score'])))

        # calculate error margin for Naive Bayes
        nb_error_margin += abs((nb_clf.predict (test_data)/10.0) - (float(row['imdb_score'])))
        
        # calculate error margin for Random Forest
        rf_error_margin += abs((rf_clf.predict (test_data)/10.0) - (float(row['imdb_score'])))
        
        # calculate error margin for Decision Tree
        dt_error_margin += abs((dt_clf.predict (test_data)/10.0) - (float(row['imdb_score'])))

        count += 1
        column = []
        data_val = []

# Print the error margin

print("Error margin for Naive Bayes: %0.2f" % (nb_error_margin/count))

print("Error margin for Random Forest: %0.2f" % (rf_error_margin/count))

print("Error margin for Decision Tree: %0.2f" % (dt_error_margin/count))

#print("Error margin for SVM: %0.2f" % (svm_error_margin/count))

#print current timestamp
print("End time: " + str(datetime.datetime.now()).split('.')[0])
