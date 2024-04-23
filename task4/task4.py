import argparse
parser=argparse.ArgumentParser(description="Файл")
parser.add_argument("file", type=str, help="Название файла")
args=parser.parse_args() # запуск python task4/task4.py numbers.txt
with open("task4/"+args.file,'r', encoding='utf-8') as file:
  data=file.readlines()
nums=[int(line.replace("\n","")) for line in data]
med = sorted(nums)[len(nums) // 2]
print(sum(abs(num - med) for num in nums))