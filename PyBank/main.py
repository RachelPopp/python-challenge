import os
import csv

csvpath = os.path.join("C:/Users/Rachel/Desktop/python/homework/python-challenge/PyBank/budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #turn into a list to simplify calculation
    rows = list(csvreader)
    #header = rows.pop(0)
    print(rows[1][0])

    #Number of months = rows - header
    Total_Months = len(rows) - 1

    #The net total amount of "Profit/Losses" over the entire period
    Total = 0
    for i in range(1,len(rows)):
        Total = Total + int(rows[i][1])

    #The average of the changes in "Profit/Losses" over the entire period
    #First create an array of changes in profit/losses
    change_array = []
    for i in range(1,len(rows)-1):
        change_array.append(int(rows[i+1][1]) - int(rows[i][1]))

    average = 0
    for i in range(0,len(change_array)):
        average = average + change_array[i]
    average = round(average/len(change_array),2)

    increase = change_array[0]
    decrease = change_array[0]
    for i in range(0,len(change_array)):
        if increase < change_array[i]:
            increase = change_array[i]
            save1 = i
        if decrease > change_array[i]:
            decrease = change_array[i]
            save2 = i

    #adjust save indices for title in rows and for the 2nd date
    increase_date = rows[save1+2][0]
    decrease_date = rows[save2+2][0]
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(Total_Months))
    print("Total: $" + str(Total))
    print("Average Change: $" + str(average))
    print("Greatest Increase in Profits: " + increase_date + " ($" + str(increase) + ")")
    print("Greatest Decrease in Profits: " + decrease_date + " ($" + str(decrease) + ")")
    

#write to a text file
    file = open("results.txt", "w")
    file.write("Financial Analysis"+'\n')
    file.write("----------------------------"+'\n')
    file.write("Total Months: " + str(Total_Months)+'\n')
    file.write("Total: $" + str(Total)+'\n')
    file.write("Average Change: $" + str(average)+'\n')
    file.write("Greatest Increase in Profits: " + increase_date + " ($" + str(increase) + ")"+'\n')
    file.write("Greatest Decrease in Profits: " + decrease_date + " ($" + str(decrease) + ")")
    file.close()