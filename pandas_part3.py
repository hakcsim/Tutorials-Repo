import pandas as pd

def test1():

    people = {
        'first': ['Corey', 'Jane', 'John'],
        'last': ['Schafer', 'Doe', 'Doe'],
        'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com']
    }

    df = pd.DataFrame(people)

    print(df)

    df1 = df.set_index('email')

    print(df1)
    print(df)

    df.set_index('email', inplace=True)

    print(df)

    print(df.loc['CoreyMSchafer@gmail.com', 'last'])

    df.reset_index(inplace=True)

    print(df)

def test2():

    df = pd.read_csv('test_files/survey_results_public.csv', index_col='Respondent')
    schema_df = pd.read_csv('test_files/survey_results_schema.csv', index_col='Column')

    print(df.head())
    print(schema_df.head())

    print(schema_df.loc['Hobbyist'])
    print(schema_df.loc['MgrIdiot'])

    print(schema_df.loc['Hobbyist', 'QuestionText'])
    print(schema_df.loc['MgrIdiot', 'QuestionText'])

    schema_df.sort_index(inplace=True)
    # sorted_schema_df = schema_df.sort_index(ascending=False)

    print(schema_df.head())
    

if __name__ == '__main__':
    test2()    
