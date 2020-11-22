import sys
import pandas as pd
def json_to_tsv(tsv_file):

    print(tsv_file.to_csv(sys.stdout, sep='\t'), end='')
    return ''

tsv_file = pd.read_json(r'''[
  {
    "title": "week 01",
    "content": "python syntax",
    "difficulty": "very easy"
  },
  {
    "title": "week 02",
    "content": "python data manipulation",
    "difficulty": "easy"
  },
  {
    "title": "week 03",
    "content": "python file and requests",
    "difficulty": "intermediate"
  },
  {
    "title": "week 04",
    "content": "python class and advanced concepts",
    "difficulty": "hard"
  }
]''')

print(json_to_tsv(tsv_file))



