//import library 
import csv
//list of two field 
field=[['Name'],['Country']]
//empty list for rows data
data=[]
filename='records1.csv'
no=int(input(":"))
with open('records1.csv','w') as csvfile:
    //this will connect file to write
    csvwritter=csv.writer(csvfile)
    //create filed Name and Country
    csvwritter.writerow(field)
    for i in range(no):
        name=input("Enter Name and Country")
        data.append(name.split())
        csvwritter.writerows(data)
with open('records1.csv','r') as csvfile:
    //read csv file
    csv=csvfile.read()
    print(csv)
