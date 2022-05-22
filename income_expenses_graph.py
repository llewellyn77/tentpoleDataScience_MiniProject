import plotly 
import plotly.graph_objects as go
import pandas as pd
#had to specify the file name in the project to test 
#had trouble uploading file , in views post was not parsing to model succesfully
excel_file = 'Income_Expenditure.xlsx'
#put into data frame
df = pd.read_excel(excel_file)
#show data in terminal to see the name of columns
print(df)
#creating a waterfall chart for the 12 months of x=income and x=expenses
#chose a waterfall model cause it best to work with income and expenses
data = [go.Waterfall(x=df['Month'],y=df['Expenses'],base=0,text=df['Income'],textposition = 'outside',
               decreasing = {"marker":{"color":"crimson",                 
                  "line":{"color":"lightsalmon","width":2}}},
               increasing = {"marker":{"color":"forestgreen",
                  "line":{"color":"lightgreen", "width":2}}})]
#created waterfall chart succefully
fig = go.Figure(data)
fig.show()

#create a savable html waterfall chart graph of income and expenses

plotly.offline.plot(fig, filename="IncomeExpensesWaterfallChartGraph.html")

