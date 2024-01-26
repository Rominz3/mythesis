import pandas as pd
from sklearn.impute import SimpleImputer


df=pd.read_excel(R"C:\Users\ROMINA\Desktop\delete nan\data\1\isfahan\4(11).xlsx")


imputer = SimpleImputer(strategy='most_frequent')

df_filled = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
df_filled.to_excel(R"C:\Users\ROMINA\Desktop\delete nan\data\2\isfahan(11).xlsx",index=False)

