import pandas
import matplotlib.pyplot as plt
#------------------Pandas Workspace ------------------#
data= pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250315.csv")
gray_count = len(data[data["Primary Fur Color"]=="Gray"])
red_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_count = len(data[data["Primary Fur Color"]=="Black"])

data_dic={
    "Colour":["Gray","Cinnamon","Black"],
    "Count":[gray_count,red_count,black_count]
}

df = pandas.DataFrame(data_dic)
excel_output = df.to_csv("S_count.csv")
#-----------------Graph plot ------------------------#
plt.figure(figsize=(5,5))
plt.bar(squirrel_color,squirrel_count)
plt.title("Squirrel Count")
plt.xlabel("Colour")
plt.ylabel("Count")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
