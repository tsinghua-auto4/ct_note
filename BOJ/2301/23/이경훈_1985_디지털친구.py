def isFriend(x, y): # friend 인지 확인
  return set(x) == set(y)

def isAlmostFriend(x, y): # almostfriend인지 확인
  set_y = set(y)

  len_x = len(x)
  temp = x

  for i in range(len_x-1):
    if temp[i] > 0 and temp[i+1] < 9:
      temp[i] -= 1
      temp[i+1] += 1

      if temp[0] != 0 and set(temp) == set_y:
        return True

      temp[i] += 1
      temp[i+1] -= 1

    if temp[i] < 9 and temp[i+1] > 0:
      temp[i] += 1
      temp[i+1] -= 1

      if set(temp) == set_y:
        return True

      temp[i] -= 1
      temp[i+1] += 1
      
for _ in range(3):
  x, y = input().split()
  x = list(map(int, x))
  y = list(map(int, y))
  if isFriend(x, y):
    print('friends')
  elif isAlmostFriend(x, y) or isAlmostFriend(y, x):
    print('almost friends')
  else:
      print('nothing')