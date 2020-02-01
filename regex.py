import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

'''

sentence = 'Start a sentence and then bring it to an end'

def find(ex, txt = text_to_search):

    pattern = re.compile(ex)

    matches = pattern.finditer(txt)

    for match in matches:
        print(match)

    print()

"""
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)
 """

#### Sample Regexs ####

# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

# # case and order sensitive
# find(r'abc')

# # period (this is a regex ctrl ch - need escape)
# find(r'\.')

# # all digits
# find(r'\d')

# # all non-digits
# find(r'\D')

# # Word Character (a-z, A-Z, 0-9, _)
# find(r'\w')

# # Not a Word Character
# find(r'\W')

# # Whitespace (space, tab, newline)
# find(r'\s')

# # Not Whitespace (space, tab, newline)
# find(r'\S')

# find(r'\bHa')
# find(r'\BHa')

# find(r'^Start', sentence)
# find(r'end$', sentence)

# find(r'\d\d\d')
# find(r'\d\d\d.\d\d\d.\d\d\d\d')

import os

dirname = os.path.join(os.getcwd(), 'test_files')

with open(os.path.join(dirname, 'data.txt'), 'r', encoding='utf-8') as f:
    content = f.read()

# find(r'\d\d\d.\d\d\d.\d\d\d\d', content)    
# find(r'\d\d\d.\d\d\d.\d\d\d\d')    
# find(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')    # only XXX-XXX-XXXX or XXX.XXX.XXXX
# find(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')    # only 800 and 900 numbers
# find(r'[89]00[-.]\d\d\d[-.]\d\d\d\d', content)    # only 800 and 900 numbers

# find(r'[0-9]') # all lower case letters
# find(r'[a-z]') # all lower case letters
# find(r'[a-zA-Z]') # all upper and lower case letters
# find(r'[^a-zA-Z]') # all NOT upper and lower case letters

# find(r'[^b]at') # all Xat except bat

# find(r'\d{3}.\d{3}.\d{4}')    # only XXX-XXX-XXXX or XXX.XXX.XXXX

""" 
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
 """

# find(r'Mr\.')   # all Mr.
# find(r'Mr\.?')  # all Mr. and Mr

# find(r'Mr\.?\s[A-Z]\w*')  # all Mr. and Mr space and followed by names  

# find(r'M(r|s|rs)\.?\s[A-Z]\w*')  # all Mr., Mr, Mrs or Mrs. space and followed by names  


emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# find(r'[a-zA-Z]+@[a-zA-Z]+\.com', emails)
# find(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)', emails)
# find(r'[0-9a-zA-Z.-]+@[a-zA-Z-]+\.(com|edu|net)', emails)
# find(r'[a-zA-Z0-0_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', emails)

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# find(r'https?://(www\.)?\w+\.\w+', urls)
# find(r'https?://(www\.)?(\w+)(\.\w+)', urls)  # groups 

# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(0), match.group(1), match.group(2), match.group(3))

# subbed_urls = pattern.sub(r'\2\3', urls)

# print(subbed_urls)

# # only group(s) if group(s) appear in regex i.e. (...), otherwise just return match
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# matches = pattern.findall(text_to_search)

# for match in matches:
#     print(match)

# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# matches = pattern.findall(text_to_search)

# for match in matches:
#     print(match)

# # find first instance only at the beginning of the sentence or None if not found
# pattern = re.compile(r'Start')
# match = pattern.match(sentence)

# print(match)

# pattern = re.compile(r'sentence')
# match = pattern.match(sentence)

# print(match)

# find first instance only anywhere in the sentence or None if not found
pattern = re.compile(r'sentence')
match = pattern.search(sentence)
print(match)

pattern = re.compile(r'start', re.IGNORECASE)
match = pattern.search(sentence)
print(match)
