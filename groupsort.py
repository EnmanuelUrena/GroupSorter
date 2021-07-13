import sys
import sort

#cant_groups = sys.argv[1]
#students_path = sys.argv[2]
#topics_path = sys.argv[3]

cant_groups = 5
students_path = "estudiantes.txt"
topics_path = "temas.txt"

def groupnotgreaterthan(data, cant_groups):
  try:
    if int(cant_groups) > len(data):
      raise Exception("the number of groups is greater than the number of students / subjects")
  except ValueError:
    print("the number of groups is not an integer")

def readtolist(path):
  datalist = []
  with open(path, "r") as file:
    for data in file:
      datalist.append(data.strip())

  return datalist
  datalist.clear()
  file.close()

def initializeRandomSort(path, cant_groups):
  data = readtolist(path)
  groupnotgreaterthan(data, cant_groups)
  data = sort.randomList(data)
  dic = sort.assigngroup(cant_groups, data)
  return dic

students_dic = initializeRandomSort(students_path, int(cant_groups))
topics_dic = initializeRandomSort(topics_path, int(cant_groups))

key = 0
rndlist = sort.randomLen(int(cant_groups))

print("/////////////////////////////////////////////////")
for x in rndlist:
  print("Group #", key + 1)
  print(students_dic[x])
  print("Topics:")
  print(topics_dic[x])
  key = key + 1
print("/////////////////////////////////////////////////")

