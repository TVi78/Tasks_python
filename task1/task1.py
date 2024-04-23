import argparse
parser=argparse.ArgumentParser(description="Переменные")
parser.add_argument("n", type=int, help="Количество чисел в массиве")
parser.add_argument("m", type=int, help="Длина интервала")

def circle_mas(n,m):
  list2=[]
  list4=[]
  list_temp=[]
  k=0
  p=m
  temp=0
  flag=True
  list1=[i+1 for i in range(n)]
  while (p%n)!=temp:
    if flag==True:
      temp=n-1
      flag=False
    list_temp.clear()
    for i in range(k,p): 
      i=i%n      
      list_temp.append(list1[i])
    list2.append(int(''.join(map(str, list_temp))))
    k=k+m-1
    p=p+m-1
  list3=[str(i)[0] for i in list2]
  list4.append(int(''.join(map(str, list3))))
  return list4

args=parser.parse_args() # запуск python task1/task1.py 5 4
print(*circle_mas(args.n,args.m))



# list=input().split(" ") # запуск через ввод данных
# list=args.n
# n=int(list[0].strip())
# m=int(list[1].strip())