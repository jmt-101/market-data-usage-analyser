import pandas as pd

usage_file="data/mock_usage_file.csv"

df = pd.read_csv(usage_file, header=None)
df.columns=[
    "timestamp",
    "user_id",
    "service",
    "ric",
    "msg_count",
    "bytes",
    "entitlement"
]
print ("Rows:",len(df))
print ("Columns:",len(df.columns))
print ("Column names:",df.columns.tolist())
print (df.head(5))
