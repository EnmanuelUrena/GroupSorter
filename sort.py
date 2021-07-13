import random

def randomList(data): 
  return random.sample(data, len(data))

def randomLen(len):
  rndlist = []
  for x in range(len):
      rndlist.append(x)
  rndlist = randomList(rndlist)
  return rndlist


def assigngroup(cantgroup, data):
  groups = {}
  div = 0
  try:
    div = len(data)/cantgroup
  except ZeroDivisionError as err:
    print(err)
  datalen = 0
  for x in range(cantgroup):
    for y in range(round(div)):
      if datalen == len(data):
        break
      if x in groups:
        groups[x] += ", " + data[datalen]
      else: 
        groups.setdefault(x,data[datalen])

      datalen += 1  

  if datalen != len(data):
    rndlist = randomLen(cantgroup)
    for x in rndlist:
      if datalen == len(data):
          break
      groups[x] += ", " + data[datalen]
      datalen += 1 
     
  return groups