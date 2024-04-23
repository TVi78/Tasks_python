import argparse
parser=argparse.ArgumentParser(description="Пути")
parser.add_argument("path1", type=str, help="Путь к файлу с координатами центра окружности и радиусом")
parser.add_argument("path2", type=str, help="Путь к файлу с точками")

def calc(path1,path2):
  with open(path1,'r', encoding='utf-8') as file:
    data_circle = file.readlines()
  koord=[]
  koord=data_circle[0].replace("\n","").split(" ")
  x_circle=int(koord[0])
  y_circle=int(koord[1])
  r_circle=float(data_circle[1])
  with open(path2,'r', encoding='utf-8') as file:
    data_dot = file.readlines()
  i=0
  if (len(data_dot)>0):
    for dot in data_dot:
      if i<100:
        x_dot=float(dot.replace("\n","").split(" ")[0])
        y_dot=float(dot.replace("\n","").split(" ")[1])
        if ((x_dot-x_circle)**2+(y_dot-y_circle)**2==r_circle**2):
          print(0)
        elif ((x_dot-x_circle)**2+(y_dot-y_circle)**2<r_circle**2):
          print(1)
        else:
          print(2)
        i+=1
      else:
        break
# path1="task2/circle.txt"
# path2="task2/dot.txt"
args=parser.parse_args() # запуск python task2/task2.py task2/circle.txt task2/dot.txt
calc(args.path1,args.path2)
