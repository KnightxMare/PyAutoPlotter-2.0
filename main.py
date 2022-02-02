import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
print("1.Line Chart")
print("2.Bar Chart")
print("3.Histogram")
print("4.Barh")
ch=int(input("Please input the graph you want to plot: "))
#Line Chart
if ch==1:
   xliv1=input("X Values: ")
   yvli1 = input("Y Values: ")
   xvli2=input("X Values: ")
   yvli2 = input("Y Values: ")
   xvli3=input("X Values: ")
   yvli3 = input("Y Values: ")
   xl=input("Label for X axis: ")
   yl=input("Label for Y axis: ")
   lit=input("Title for the graph: ")
   x=[xliv1,xvli2,xvli3]
   y=[yvli1,yvli2,yvli3]
   sx=pd.Series(x)
   sy=pd.Series(y)
   plt.xlabel(xl)
   plt.ylabel(yl)
   plt.title(lit)
   plt.plot(sx,sy)
   plt.show()
#Bar Chart
if ch==2:
   xvbc1=input("X Values: ")
   xvbc2=input("X Values: ")
   xvbc3=input("X Values: ")
   x=[xvbc1,xvbc2,xvbc3]
   range=input("Enter Range: ")
   xl=input("Label for X axis: ")
   yl=input("Label for Y axis: ")
   bct=input("Title for the graph: ")
   plt.bar(range,x)
   plt.xlabel(xl)
   plt.ylabel(yl)
   plt.title(bct)
   plt.show()
#Histogram
if ch==3:
   xvh=input("X Values: ")
   yvh=input("Y Values: ")
   c=input("Color: ")
   htype=input("HisType: ")
   rw=input("Rwidth: ")
   xl = input("x Label: ")
   yl = input("y Label: ")
   ht = input("Title: ")
plt.hist(xvh,bins=yvh,color=c,histtype=htype,rwidth=rw)
   plt.xlabel(xl)
   plt.ylabel(yl)
   plt.title(ht)
   plt.show()
