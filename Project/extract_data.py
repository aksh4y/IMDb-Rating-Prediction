import csv
import datetime
import sys

###############################################################################
# Extracts the required data from the given dataset and converts it into
# the required format
###############################################################################

# print the current timestamp
print("Start time: " + str(datetime.datetime.now()).split('.')[0])

# setup progress bar
toolbar_width = 60
sys.stdout.write("[%s" % (" " * (toolbar_width/3)))
sys.stdout.write("***Processing data***")
sys.stdout.write("%s]" % (" " * (toolbar_width/3)))
sys.stdout.flush()
sys.stdout.write("\n")

# initialize variables
column = []
data = []
label = []
progress = 0

with open('Datasets/Training Dataset.csv') as f:
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
        data.append(column) #all fields
        label.append(row['imdb_score']) #scores
        column = []
        progress += 1;
        if progress % 65 == 0:  #print progress
            sys.stdout.write("#")
            sys.stdout.flush()
sys.stdout.write("\n")
