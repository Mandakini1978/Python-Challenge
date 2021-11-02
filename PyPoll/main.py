
# Python script that analyzes the records to calculate each of the following:
#The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won

# The winner of the election based on popular vote.

import os
import csv


#election_data_csv = os.path.join("02-Homework\\03-Python\\Instructions\\PyPoll\\Resources\\election_data.csv")
election_data_csv = os.path.join("..", "Resources", "election_data.csv")

#list to store data

Voter_ID = []
Candidate = []
Unique_Candidate_List =[]

with open(election_data_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)

    for row in csvreader:
    
        Voter_ID.append(row[0])
        Candidate.append(row[2])

#The total number of votes cast

Total_Vote_Cast = (len(Voter_ID))
print(Total_Vote_Cast)

# The Unique Candidate List

for x in Candidate:
    if x not in Unique_Candidate_List :
        Unique_Candidate_List.append(x)

print(Unique_Candidate_List)

#Writing report to the Terminal 

print("Election Results")
print("-------------------------")
print("Total Votes:"+ str(Total_Vote_Cast))
print("-------------------------")           
# The percentage of votes each candidate won
candidate_count = dict()
for x in range(int(len(Unique_Candidate_List))) :
    cnt = 0
    cnt = Candidate.count(Unique_Candidate_List[x])
    candidate_count.update({Unique_Candidate_List[x]:cnt})
    print (Unique_Candidate_List[x],":",cnt/Total_Vote_Cast*100,"% (" ,cnt,")")
    

# Determine Winner

winner = max(candidate_count, key=candidate_count.get)    
print("-------------------------")
print("Winner:" + winner)
print("-------------------------")

# Writing in the output file

#output_file = os.path.join("02-Homework\\03-Python\\Instructions\\PyPoll\\Solved\\Py_Poll_Output.csv")
output_file = os.path.join("..", "Analysis", "Py_Poll_Output.csv")
#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)


    writer.writerow(['Total Votes : ' , str(Total_Vote_Cast)])

    candidate_count = dict()
    for x in range(int(len(Unique_Candidate_List))) :
        cnt = 0
        cnt = Candidate.count(Unique_Candidate_List[x])
        candidate_count.update({Unique_Candidate_List[x]:cnt})
        writer.writerow([Unique_Candidate_List[x],cnt/Total_Vote_Cast*100,"% (" ,cnt,")"])
    # create a list

    winner = max(candidate_count, key=candidate_count.get)    
    writer.writerow(["Winner:" , winner])
    
    
