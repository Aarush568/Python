#Start code here
import time
Timer = 30
for i in range(29):
  Timer -= 1
  print(Timer)
  time.sleep(1)
if Timer == 1:
  print("Game over")
