def countdown(n):
  if n <= 0:
    print('Blastoff!')
  else:
    print(n)
    countdown(n-1)

def countup(n):
  if n >= 0:
    print('Blastoff!')
  else:
    print(n)
    countup(n+1)

n = input()
if (n > 0):
  countdown(n)
else:
  countup(n)

