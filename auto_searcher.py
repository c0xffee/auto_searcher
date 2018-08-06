from tkinter import Tk
import webbrowser as wb
import time

copy = Tk()
copy.withdraw()
tmp = copy.clipboard_get()
print(tmp)
c = 0
while True:
  time.sleep(1)
  now = copy.clipboard_get()
  if tmp != now:
    tmp = now
    print('search for %s'%now)
    wb.open('www.google.com/search?q=%s'%now)
    wb.open('www.google.com/search?q=%s+ccna'%now)