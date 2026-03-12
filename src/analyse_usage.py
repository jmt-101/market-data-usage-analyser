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

#Cleaning the data file to make it consistent
for col in ["user_id", "service", "ric", "entitlement"]:
    df[col] = df[col].str.strip().str.upper()

print ("Rows:",len(df))
print ("Columns:",len(df.columns))
print ("Column names:",df.columns.tolist())
print (df.head(5))

#Total bytes per user
bytes_per_user=(
    df.groupby("user_id") ["bytes"]
    .sum()
    .sort_values(ascending=False)
)

print ("\nTotal bytes per user")
print (bytes_per_user)

#Usage by Service
usage_per_service=(
    df.groupby("service")["msg_count"]
    .sum()
    .sort_values(ascending=False)
)
print ("\nTotal count per service")
print (usage_per_service)

#Find enteries for users starting with "Akh"
userid_starting_with_akh=(
    df[ df["user_id"].str.lower().str.startswith("akh") ]
)
print ("\nUsers ID's that start with Akh")
print (userid_starting_with_akh)