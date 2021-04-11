# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.


# As an example, your analysis should look similar to the one below:
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------


#import poll
import os
import csv

#working directory
csvpath=os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #Creating my list 
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []

# Appending List with data from rows 
    for row in csvreader:
        candidates.append(row[2])
        total_votes= int(len(candidates))

#Total votes per candidate
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
            khan_percentage = round((khan_votes/total_votes)*100 ,3)
           
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
            correy_percentage = round((correy_votes/total_votes)*100, 3)
            
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
            li_percentage = round((li_votes/total_votes)*100, 3)
            
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
            otooley_percentage = round((otooley_votes/total_votes)*100, 3)
    
# Finding the winner winner chicken dinner     
    totals = {khan_votes:"Khan", correy_votes:"Correy", li_votes:"Li", otooley_votes:"Otooley"}
    
    winner = totals.get(max(totals))
    
# Printing Time  
    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------")
    print(f"Khan: {khan_percentage}%({khan_votes})")
    print(f"Correy: {correy_percentage}%({correy_votes})")
    print(f"Li: {li_percentage}%({li_votes})")
    print(f"Otooley: {otooley_percentage}%({otooley_votes})")
    print("--------------------")
    print(F"Winner: {winner}")
    print("--------------------")