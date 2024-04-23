import json
import argparse

parser=argparse.ArgumentParser(description="Пути")
parser.add_argument("path1", type=str, help="Путь к файлу 1")
parser.add_argument("path2", type=str, help="Путь к файлу 2")
parser.add_argument("path3", type=str, help="Путь к файлу 3")
args=parser.parse_args()

def values_file(path):
  with open(path, 'r', encoding='utf-8') as file:
            data=file.read()
            list=json.loads(data)
            dict={}
            for id in list["values"]:
              dict[id['id']]=id['value']              
  return dict

def tests_file(path):
  with open(path, 'r', encoding='utf-8') as file:
            data=file.read()
            list=json.loads(data)
  return list

def report_file(path1,path2,path3):
  dict=values_file(path1)
  list=tests_file(path2)
  with open(path3, 'w+') as file:  
    for id in list["tests"]:
      for key in dict.keys():
        if id['id']==key:
          id['value']=dict[key]
        if (id.get('values')!=None):
          for id_values in id.get('values'):
            for key in dict.keys():
              if id_values['id']==key:
                id_values['value']=dict[key]
            if (id_values.get('values')!=None):
              for values_values in id_values.get('values'):
                for key in dict.keys():
                  if values_values['id']==key:
                    values_values['value']=dict[key]  
                if (values_values.get('values')!=None):
                  for values_values3 in values_values.get('values'):
                    for key in dict.keys():
                      if values_values3['id']==key:
                        values_values3['value']=dict[key]                     
    json.dump(list,file, indent=2, separators=(',', ': '))

# path1="task3/values.json"
# path2="task3/tests.json"
# path3="task3/report.json"

# запуск python task3/task3.py task3/values.json task3/tests.json task3/report.json
report_file(args.path1,args.path2,args.path3) 