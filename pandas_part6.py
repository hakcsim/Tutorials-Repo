import pandas as pd

def test1():

    people = {
        'first': ['Corey', 'Jane', 'John'],
        'last': ['Schafer', 'Doe', 'Doe'],
        'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com']
    }

    df = pd.DataFrame(people)

    # add and remove columns

    # new column = combined existing columns
    df['full_name'] = df['first'] + ' ' + df['last']

    df.drop(columns=['first', 'last'], inplace=True)

    print(df)

    df[['first', 'last']] = df['full_name'].str.split(' ', expand=True)

    print(df)

    # add and remove rows

    df = df.append({'first': 'Tony'}, ignore_index=True)

    print(df)

    # df = pd.DataFrame(people)

    people2 = {
        'first': ['Tony', 'Steve'],
        'last': ['Stark', 'Rogers'],
        'email': ['IronMain@avenge.com', 'Cap@avenge.com']
    }

    df2 = pd.DataFrame(people2)

    df = df.append(df2, ignore_index=True)

    print(df)

    df.drop(index=3, inplace=True)

    print(df)

    df = df.drop(index=df[df['last'] == 'Doe'].index)

    print(df)

if __name__ == '__main__':
    test1()