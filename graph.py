#make the necessary imports 
from bokeh.plotting import figure #allows one to add points to the graph, add a legend, add labels
                                #to the x and y axis...

from bokeh.io import output_file,show # allows one to create an output file and show it on the browser 

import pandas #allows us to read, analyze and manipulate data

#read the csv file 
df = pandas.read_csv('bachelors.csv')

#create the figure object 
f = figure()

#style the graph 
f.title.text = 'Women Engineering Graduands from 1970 to 2011'
f.title.text_color="Orange"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None

#these next two are the legends for the x and y axis respectively 
f.xaxis.axis_label="Year" 
f.yaxis.axis_label="Graduands in 1000's"  

#prepare the x and y data 
x = df['Year']
y = df['Engineering']

#create the output file 
output_file('Graduands.html')

#add the x and y data 
f.line(x,y)

#show the figure object 
show(f)
