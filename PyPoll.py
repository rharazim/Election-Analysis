# data we need to retrieve
# total number of votes cast
# complete lit of candidates who received votes
# percentage of votes each candidate won
# the winner of the election based on popular vote

# assign a variable for the file to load and the path
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize a vote counter
total_votes = 0

# Candidate options
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}
# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 


# Open the election results and read the rile
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
   

    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count 
        total_votes += 1

        #Print candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate
    # Iterate through the candidate list
    for candidate_name  in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes) * 100

        # Pring out each candidate's name, vote count, and vote percentage
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count
        if (votes> winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidates name
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winnning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)




# using with statement open the file as a text file
#with open(file_to_save,"w") as txt_file:

# write some data to the file
    #txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")




