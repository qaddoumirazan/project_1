import pandas as pd
from sklearn.model_selection import train_test_split

dict = {
    "X" : [i for i in range (-1000, 1000)],
    "Y" : [i for i in range (-1000, 1000)]
}
df= pd.DataFrame(dict)
df["output"] = df["X"]> 50
df["output"] = df["output"].astype(int)

input = df[["X","Y"]]
output = df["output"]

train, test = train_test_split(df, test_size=0.2, shuffle=True)
train_df = pd.Dataframe(train)
test_df = pd.DataFrame(test)

print(train_df.shape)
print(test_df.shape)