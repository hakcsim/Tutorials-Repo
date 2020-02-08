import csv
import itertools
from collections import defaultdict, Counter


def test1():

    with open('test_files/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        # counts = defaultdict(int)
        hobbyist_counts = Counter()
        language_counts = Counter()

        total = 0

        for line in csv_reader:
            hobbyist_counts[line['Hobbyist'].capitalize()] += 1
            languages = line['LanguageWorkedWith'].split(';') 
            language_counts.update(languages)
            total += 1

        print(language_counts)
        print()

        for language, count in language_counts.most_common(5):
            language_pct = count * 100 / total         
            print(f'{language}: {language_pct}%')

        total = hobbyist_counts['Yes'] + hobbyist_counts['No']         

        print(f"{round(hobbyist_counts['Yes'] * 100/ total, 2)}%")

def test2():
    
    with open('test_files/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        dev_type_info = {}

        for line in csv_reader:
            dev_types = line['DevType'].split(';')     
            languages = line['LanguageWorkedWith'].split(';') 

            for dev_type in dev_types:
                # if dev_type not in dev_type_info:
                #     dev_type_info[dev_type] = {'count':0, 'languages': Counter() }
                dev_type_info.setdefault(dev_type, { 'count':0, 'languages': Counter() })

                dev_type_info[dev_type]['count'] += 1
                dev_type_info[dev_type]['languages'].update(languages)

        for dev_type, info in dev_type_info.items():
            total = info['count']
            print('Dev type:', dev_type)
            for language, count in info['languages'].most_common(5): 
                language_pct = count * 100 / total         
                print(f'{language}: {language_pct}%')
            print('-'*50)    

if __name__ == '__main__':
    test2()

    