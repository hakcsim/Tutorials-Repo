import pandas as pd

def test1():

    people = {
        'first': ['Corey', 'Jane', 'John'],
        'last': ['Schafer', 'Doe', 'Doe'],
        'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com']
    }

    df = pd.DataFrame(people)

    print(df)

    df.columns = ['first name', 'last name', 'email address']

    print(df)

    df.columns = [x.upper() for x in df.columns]

    print(df)

    df.columns = df.columns.str.replace(' ', '_')

    print(df)

    df.rename(columns={'FIRST_NAME': 'first', 'LAST_NAME': 'last'}, inplace=True)
    print(df)
    df.rename(columns={'EMAIL_ADDRESS': 'email'}, inplace=True)

    df.loc[2] = ['John', 'Smith', 'JohnSmith@email.com']

    print(df)

    df.loc[2, ['last','email']] = ['Doe', 'JohnDoe@email.com']

    # these are the same
    df.loc[2, 'last'] = 'Smith'
    df.at[2, 'last'] = 'Doe'

    print(df)

    f = (df['email'] == 'JohnDoe@email.com')
    df.loc[f, 'last'] = 'Smith'

    print(df)

    df['email'] = df['email'].str.lower()

    print(df)

    # apply to series (a column)

    print(df['email'].apply(len))

    def update_email(email):
        return email.upper()

    df['email'] = df['email'].apply(update_email)
    print(df)

    df['email'] = df['email'].apply(lambda x : x.lower())
    print(df)

    # apply to data frame

    print(df.apply(len)) # 3 columns
    print(df.apply(len, axis='columns')) # N rows

    # these are the same
    print(df.apply(pd.Series.min))
    print(df.apply(lambda x : x.min()))

    # apply to each cell - applymap

    print(df.applymap(len))
    print(df.applymap(str.lower))

    # map - only work with series

    # not inplace
    # cause John to be NaN because it is not in the dict
    print(df['first'].map({'Corey': 'Chris', 'Jane' : 'Mary'})) 

    # not inplace
    # John will not be NaN
    print(df['first'].replace({'Corey': 'Chris', 'Jane' : 'Mary'}))

def test2():

    df = pd.read_csv('test_files/survey_results_public.csv')
    schema_df = pd.read_csv('test_files/survey_results_schema.csv')

    print(df.head())
    print(schema_df.head())

    df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace=True)
    df['Hobbyist'] = df['Hobbyist'].replace({'Yes':True, 'No':False})


if __name__ == '__main__':
    test1()