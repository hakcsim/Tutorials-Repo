import pandas as pd

def test1():

    people = {
        'first': ['Corey', 'Jane', 'John'],
        'last': ['Schafer', 'Doe', 'Doe'],
        'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com']
    }

    df = pd.DataFrame(people)

    print(df)

    # get column names
    print(df.columns)

    # access a column
    print(df['email'])
    print(type(df['email']))

    print(df.email)

    # 2 columns
    print(df[['last', 'email']])

    # get row(s)

    # use iloc: row and column indices

    # indexed row
    print(df.iloc[0])

    # indexed rows
    print(df.iloc[[0,2]])

    # indexed rows and cols
    print(df.iloc[[0,2], 2])
    print(df.iloc[[0,2], [1,2]])

    # use loc: row index number(s), column name(s)

    print(df.loc[0])

    # indexed rows
    print(df.loc[[0,2]])

    # indexed rows and cols
    print(df.loc[[0,2], 'first'])
    print(df.loc[[0,2], ['email','last']])

def test2():

    # df = pd.read_csv('test_files/survey_results_schema.csv')
    df = pd.read_csv('test_files/survey_results_public.csv')

    # print(df)
    print(df.shape)

    print(df['Hobbyist'])
    print(df['Hobbyist'].value_counts())     

    print(df.loc[0, 'Hobbyist'])
    print(df.loc[[0,1,2], 'Hobbyist']) # 0,1,2
    print(df.loc[0:2, 'Hobbyist']) # 0,1,2
    print(df.loc[0:2, 'Hobbyist':'Employment']) # 0,1,2 rows, 'Hobbyist' to 'Employment' columns

if __name__ == '__main__':
    test1()    

