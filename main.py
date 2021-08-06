import csv
from collections import Counter

def execute():

  
  csv_parsed_data = parse_csv_data()
  sorted_csv_data = sorted(csv_parsed_data['wrong_most_often'].items(), key=lambda x:x[1], reverse=True)

  print_table(sorted_csv_data, csv_parsed_data['options_per_question'])
 

def print_table(questions_data, options_selected):
  print('\nNumero Questão \t   Total Erros \t   Selecionada Mais vezes     Frequencia')
  for question in questions_data:
    mode = Counter(options_selected[question[0]]).most_common()[0]
    print('     {} \t|       {}\t|             {} \t   |       {}'.format(question[0], question[1], mode[0], mode[1]))
    # print(questions_data)
    

def parse_csv_data():
  wrong_most_often = {}
  option_selected = {}
  with open('alinhamento-simulado_4.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for i, row in enumerate(csv_reader):
      if i == 0: continue
      ref = wrong_most_often.get('Q-' + row[0])
      if(ref is None): 
        wrong_most_often['Q-' + row[0]] = 1
        option_selected['Q-' + row[0]] = [row[1]]
        continue
      wrong_most_often['Q-' + row[0]] = wrong_most_often['Q-' + row[0]] + 1
      option_selected['Q-' + row[0]].append(row[1])

  return { 'wrong_most_often': wrong_most_often, 'options_per_question': option_selected }


execute()
