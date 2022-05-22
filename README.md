#Technologies Used <br />
1.Python3 <br />
2.Django Unchained <br />
3.Postgresql <br />
<br /> 
#Inputs<br />
1.Via html :<br />
           ->FirstName          : String <br />
           ->LastName           : String <br />
           ->Date Of Birth      : Date   <br />
           ->Upload Excel File  : File   <br />
<br />
#Outputs<br />
1.Waterfall graph showed in html <br />
*Please note that cause i couldnt get/upload the file/data from html i could not          <br />
*parse it to be read into my function so i just added the given excel file to the project <br />
*for test purposes.But extracting information from excel form works proper                <br />
--TO TEST IN TERMINAL, make sure you ran this project in the given virtual environment    <br />
--enter the given command to check graph 'python income_expenses_graph.py'                <br />
--make sure to plotly,pandas and openpxyl is installed in terminal                        <br />
<br />
#Models <br />
1.CustomerInformationModel:No relationship <br />
  fname->CharField                         <br />
  lname->CharField                         <br />
  dateOfBirth->DateField                   <br />
  excelFile->File                          <br />
<br />
#Problems Faced <br />
1.When trying to POST the inputted date from html it was not working but fixed by adjusting      <br />
the html value to {{placement.date|date:'Y-m-d' }}                                               <br />
2.Biggest issue was trying to upload the file it was just not taking in the file correctly,      <br />
it is my first django project ever so im still getting used to take in data from different html  <br />
types of data                                                                                    <br />
<br />
To run project-> make sure youre in your virtual environment--> 'python manage.py runserver' <br />
<br />




