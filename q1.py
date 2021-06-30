
from drawingpanel import *
import time
from random import choice
import random
p = DrawingPanel(600, 600, background="light gray")
def main():
    number=random.randint(1,20)
    print(number)
    for i in range(0,20):
        colors=['white','black','red','green','blue','cyan','yellow','magenta']
        choicenumber=random.randint(1,2)
      
        x1=random.randint(0,600)
        x2=random.randint(0,600)
        x3=random.randint(0,600)
        colornumber=random.randint(0,7)
        number=random.randint(0,3)
        if(choicenumber==1):
            ball= p.canvas.create_oval(x1,x1,x2,x2,fill=colors[colornumber],outline="")
        else:
            ball= p.canvas.create_oval(x2,x2,x1,x1,outline=colors[colornumber])



main()
    
