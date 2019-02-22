from fuzzywuzzy import process

with open("D:\ML_Project\ML Dataset\ToLogix ML -Dataset.csv","r") as f:
    ISLG_Data = f.read().split("\n")

query = str(input("ENTER CHOICE: "))
choices = ISLG_Data
print("choices: ",process.extract(query, choices, limit=6))
