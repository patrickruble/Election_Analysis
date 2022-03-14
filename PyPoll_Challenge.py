import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = file_to_load = os.path.join("resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("resources", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize candidate options list.
candidate_options = []

# Initialize counties list.
counties_options = []

# Declare an empty dictionary for candidate
candidate_votes = {}

# Declare an empty dictionary for counties list.
counties_votes = {}

# Winning Candidate and Winning Count Tracker for both candidates and counties
winning_candidate = ""
winning_count_candidate = 0
winning_percentage_candidate = 0
winning_county = ""
winning_count_county = 0
winning_percentage_county = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate and candidate name from each corresponding row
        candidate_name = row[2]
        county_name = row[1]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Increment vote to that candidate's count.
        candidate_votes[candidate_name] += 1

          # If the countie does not match any existing countie..
        if county_name not in counties_options:
            # Add it to the list of counties.
            counties_options.append(county_name)
            # Begin tracking that countie's vote count.
            counties_votes[county_name] = 0
        # Increment vote to that countie's count.
        counties_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each countie by looping through the counts.
    # Iterate through the countie list.
    for county in counties_votes:
        # Retrieve vote count of a countie.
        votes_county  =  counties_votes[county]
        # Calculate the percentage of votes
        vote_percentage_county = int(votes_county) / int(total_votes) * 100  
        # Print out each countie's name, vote count, and percentage of votes to the terminal.
        counties_results = (
            f"{county}: {vote_percentage_county:.1f}% ({votes_county:,})\n")
        # Print each countie, their voter count, and percentage to the terminal.
        print(counties_results)
        # Save the countie results to our text file.
        txt_file.write(election_results)

        # Determine winning vote count and countie
        # Determine if the votes are greater than the winning count.
        if (votes_county > winning_count_county) and (vote_percentage_county > winning_percentage_county):
            # If true then set winning_count = votes and winning_percentage = vote_percentage.
            winning_count_county = votes_county
            winning_percentage_county = vote_percentage_county
            # Set the winning_countie equal to the countie's name.
            winning_county = county  

    # Print the largest county turnout.
    winning_county_summary = (
        f"\n----------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"----------------------------\n")
    print(winning_county_summary)
    # Save the winning countie's name to the text file.
    txt_file.write(winning_county_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes_candidate  =  candidate_votes[candidate]
        # Calculate the percentage of votes
        vote_percentage_candidate = int(votes_candidate) / int(total_votes) * 100  
        # Print out each candidate's name, vote count, and percentage of votes to the terminal.
        candidate_results = (f"{candidate}: {vote_percentage_candidate:.1f}% ({votes_candidate:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes_candidate > winning_count_candidate) and (vote_percentage_candidate > winning_percentage_candidate):
            # If true then set winning_count = votes and winning_percentage = vote_percentage.
            winning_count_candidate = votes_candidate
            winning_percentage_candidate = vote_percentage_candidate
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate  

    # Print the winning candidate, total votes and vote percentage.
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count_candidate:,}\n"
        f"winning Percentage: {winning_percentage_candidate:.1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
