import os
import csv

csvpath = os.path.join("C:/Users/Rachel/Desktop/python/homework/python-challenge/PyPoll/election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")



    #turn into a list to simplify calculation
    rows = list(csvreader)
    #header = rows.pop(0)
    #for i in range(1,10):
#    print(rows[0][2])

#The total number of votes cast
    Total_Votes = len(rows) - 1
#    print(Total_Votes)

#A complete list of candidates who received votes
    store = []
    for i in range(1,len(rows)):
        store.append(rows[i][2])
 
    # sets store unique values, so convert store to a set
    Candidates = set(store)
    # turnn back into a list
    Candidates = list(Candidates)
#    print(Candidates)


#The percentage of votes each candidate won

#The total number of votes each candidate won
    Votes = []
    Percent = []
    for i in range(0,len(Candidates)):
        count = 0
        for j in range(1,len(rows)):
            if rows[j][2] == Candidates[i]:
                count = count + 1
        Votes.append(count)
        Percent.append(100*count/Total_Votes)
    for i in range(0, len(Percent)):
        Percent[i] = round(Percent[i],2)

#sort
    Votes.sort(reverse = True)
    Percent.sort(reverse = True)
#The winner of the election based on popular vote.

    


#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------

    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(Total_Votes))
    print("----------------------------")
    for i in range(0,len(Candidates)): 
        print(Candidates[i] + ": " + str(Percent[i]) +  "% (" + str(Votes[i]) + ")")
    print("Winner: " + Candidates[0])
        
    file = open("results.txt", "w")
    file.write("Election Results" + '\n')
    file.write("----------------------------" + '\n')
    file.write("Total Votes: " + str(Total_Votes) + '\n')
    file.write("----------------------------" + '\n')
    for i in range(0,len(Candidates)): 
        file.write(Candidates[i] + ": " + str(Percent[i]) +  "% (" + str(Votes[i]) + ")" +'\n')
    file.write("Winner: " + Candidates[0])
    file.close()
