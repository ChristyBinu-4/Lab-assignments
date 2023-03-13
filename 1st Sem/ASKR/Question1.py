import pandas as pd

mydataset = {
    'Name' : ["Christy Binu", "Iqbal","Shibin S","Shaaron TK","Ajay Prasad"],
    'Roll Number' : [10,2,4,5,7],
    'English' : [12,23,56,34,64],
    'Science' : [15,65,44,32,56],
    'Maths' : [32,54,57,45,44]
}

df = pd.DataFrame(mydataset)
subjects = ['English','Science','Maths']

for i in subjects:
    print(f"Highest mark for {i}")
    maxMarkName = df['Name'].loc[df[i].idxmax()]
    maxMark = df[i].max()
    print(maxMarkName,maxMark, '\n')
