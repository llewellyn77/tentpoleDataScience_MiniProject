#Technologies Used
1.Python3
2.Django Unchained
3.Postgresql

#Inputs
1.Via html :
           ->FirstName          : String
           ->LastName           : String
           ->Date Of Birth      : Date
           ->Upload Excel File  : File

#Outputs
1.Waterfall graph showed in html
*Please note that cause i couldnt get/upload the file/data from html i could not
*parse it to be read into my function so i just added the given excel file to the project
*for test purposes.But extracting information from excel form works proper
--TO TEST IN TERMINAL, make sure you ran this project in the given virtual environment
--enter the given command to check graph 'python income_expenses_graph.py' 
--make sure to plotly,pandas and openpxyl is installed in terminal

#Models
1.CustomerInformationModel:No relationship
  fname->CharField
  lname->CharField
  dateOfBirth->DateField
  excelFile->File

#Problems Faced
1.When trying to POST the inputted date from html it was not working but fixed by adjusting
the html value to {{placement.date|date:'Y-m-d' }}
2.Biggest issue was trying to upload the file it was just not taking in the file correctly,
it is my first django project ever so im still getting used to take in data from different html
types of data

To run project-> make sure youre in your virtual environment--> 'python manage.py runserver'

#pls hire me :'(



