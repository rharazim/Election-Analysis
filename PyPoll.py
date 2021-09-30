# data we need to retrieve
# total number of votes cast
# complete lit of candidates who received votes
# percentage of votes each candidate won
# the winner of the election based on popular vote

# assign a variable for the file to load and the path
import csv
import os

file_to_load = os.path.join("Resources","election_results.csv")
#'Resources/election_results.csv'

# create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")

# open the election results and read the rile
with open(file_to_load) as election_data:


    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)



# using with statement open the file as a text file
#with open(file_to_save,"w") as txt_file:

# write some data to the file
    #txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")




