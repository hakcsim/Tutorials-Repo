import pandas as pd

def test1():

    people = {
        'first': ['Corey', 'Jane', 'John'],
        'last': ['Schafer', 'Doe', 'Doe'],
        'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com']
    }

    df = pd.DataFrame(people)

    print(df)

    f1 = (df['last'] == 'Doe')

    print(f1)

    # these are the same
    print(df[f1])
    print(df.loc[f1])

    print(df.loc[f1, 'email'])

    f2 = ((df['last'] == 'Doe') & (df['first'] == 'John'))
    print(df.loc[f2, 'email'])

    f2 = ((df['last'] == 'Schafer') | (df['first'] == 'John'))
    print(df.loc[f2, 'email'])

    # Not f2
    print(df.loc[~f2, 'email'])


def test2():

    df = pd.read_csv('test_files/survey_results_public.csv')
    schema_df = pd.read_csv('test_files/survey_results_schema.csv')

    print(df.head())
    print(schema_df.head())

    high_salary = (df['ConvertedComp'] > 70000)

    print(df.loc[high_salary, 'LanguageWorkedWith'].head())
    print(df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']])

    countries = ['United States', 'India', 'United Kingdom', 'Germany', 'Canada']
    f2 = df['Country'].isin(countries)
    
    print(df.loc[f2, 'Country'])

    f3 = df['LanguageWorkedWith'].str.contains('Python', na=False)
    print(df.loc[f3, 'LanguageWorkedWith'])

if __name__ == '__main__':
    test2()