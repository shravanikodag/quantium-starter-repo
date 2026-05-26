#1. import
import pandas as pd
import glob

# 2 get all three csv file in one var
files = glob.glob("data/*.csv")
#3. create empty list as dataframe
result = []
#4. in for loop take file name of each 3 files one by one
for file in files:
    #5. read that file first
    df = pd.read_csv(file)
    #6. select only pink morsel
    df = df[df["product"] == "pink morsel"]
    #7.create new column sales=qty*prize before that remove $ sign in prize
    df["price"] = df["price"].replace('[\$,]','',regex=True).astype(float)
    df["sales"] = df["quantity"] * df["price"]
    #8. append sales,date,region in dataframe
    df = df[["sales","date","region"]]
    result.append(df)
#9concatenate all result
final = pd.concat(result)
#10 convert into csv file
final.to_csv("data/final_result.csv", index=False)

print("successfull")



