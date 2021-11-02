# Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

#  Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

#  The greatest decrease in profits (date and amount) over the entire period


import os
import csv



#budget_data_csv = os.path.join("02-Homework\\03-Python\\Instructions\\PyBank\\Resources\\budget_data.csv")
budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

# Lists to store data

Date = []
Diff_Year = []
Profit_Loss = []


with open(budget_data_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)

    for row in csvreader:
        
        Date.append(row[0])
        #print(Date)

         # Profit_Loss

        Profit_Loss.append(row[1])


#Calculations
# The total number of months included in the dataset

Total_Month =int(len(Date))


#The net total amount of "Profit/Losses" over the entire period
Total_Profit=0
for i in range(len(Profit_Loss)) :
    Total_Profit = Total_Profit + int(Profit_Loss[i])

  

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
#  The greatest decrease in profits (date and amount) over the entire period

Greatest_Profit = 0
Greatest_Loss = 0
Greatest_Profit_Date = ""
Greatest_Loss_Date = ""
Change = 0
for i in range(int(len(Profit_Loss)-1)) :
    
    if (int(Profit_Loss[i+1])-int(Profit_Loss[i])) > Greatest_Profit :
        Greatest_Profit = (int(Profit_Loss[i+1])-int(Profit_Loss[i]))
        Greatest_Profit_Date = Date[i+1] 

    if (int(Profit_Loss[i+1])-int(Profit_Loss[i])) < Greatest_Loss :
        Greatest_Loss = (int(Profit_Loss[i+1])-int(Profit_Loss[i]))
        Greatest_Loss_Date = Date[i+1]  
    Change = Change + (int(Profit_Loss[i+1])-int(Profit_Loss[i])) 




# Writing on the terminal


print("    Financial Analysis      ")
print ("----------------------------")
print("Total Months : " +  str(Total_Month))

print("Total : " + str(Total_Profit))
print("Average Change" + str(Change/(Total_Month-1)))


print("Greatest Increase in Profits:",Greatest_Profit_Date,"(","$",Greatest_Profit,")")

print("Greatest Decrease in Profits:",Greatest_Loss_Date,"(","$",Greatest_Loss,")")

# Writing in Output File

output_file = os.path.join("..", "Analysis", "Py_Bank_Output.csv.csv")
#output_file = os.path.join("02-Homework\\03-Python\\Instructions\\PyBank\\Resources\\Py_Bank_Output.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)


# Write the header row
    writer.writerow(['Financial Analysis'])


# Write Analysis
    writer.writerow(['Total Months : ' , str(Total_Month)])
    
    writer.writerow(['Total : ' , str(Total_Profit)])

    writer.writerow(["Average Change" , str(Change/(Total_Month-1))])

    writer.writerow(['Greatest Increase in Profits :',(Greatest_Profit),str(Greatest_Profit_Date)])

    writer.writerow(['Greatest Decrease in Profits :' ,str(Greatest_Loss),str(Greatest_Loss_Date)])
