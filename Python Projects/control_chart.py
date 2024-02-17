import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\isano\Documents\University\Year 3 Semester 1\Quality Engineering\Control Chart\CSV.csv")


x=df.mean(axis=1)
round_x=x.round()
df["Mean"]=round_x

min_val=df.min(axis=1)
max_val=df.max(axis=1)
range_val=max_val-min_val
df["Range"]=range_val


X2_bar=df["Mean"].mean()
df["X2_Bar"]=X2_bar


R_bar=df["Range"].mean()
df["R_Bar"]=R_bar

A2=0.577

UCL_X=X2_bar+A2*R_bar
df["UCL_X"]=UCL_X

LCL_X=X2_bar-A2*R_bar
df["LCL_X"]=LCL_X

print(df)

x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[6,1,2,2,3,4,8,5,4,2,3,1]


plt.plot(x, y, color='green', linestyle='solid', linewidth = 3, 
         marker='o', markerfacecolor='green', markersize=7)
 
plt.axhline(y = X2_bar, color = 'b', linestyle = '-',label="Mean") 
plt.axhline(y = UCL_X, color = 'r', linestyle = '-',label="UCL") 
plt.axhline(y = LCL_X, color = 'm', linestyle = '-',label="LCL") 

for i, j in zip(x, y):
    plt.annotate('(%s, %s)' % (i, j), xy=(i, j), textcoords='offset points', xytext=(0,5), ha='center')
    
plt.xlabel('Project No./Months')  
plt.ylabel('No. of Cracks') 
  
plt.title('AAM No. of Cracks') 

plt.legend()
 
plt.show() 
