import pandas as pd

# df = pd.read_csv('test_files/survey_results_schema.csv')
df = pd.read_csv('test_files/survey_results_public.csv')

# print(df)
print(df.shape)
print(df.info())

# pd.set_option('display.max_columns', df.shape[1])
# pd.set_option('display.max_rows', df.shape[0])
# print(df)

# show first 10 rows
print(df.head(10))

# show last 10 rows
print(df.tail(10))

