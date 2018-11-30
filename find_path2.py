import cv2
import numpy as np
import random as rand
import time

w = 9
l = 90
no = int(l/w)
grid = []
current_Box = 0
stack = []

arena = np.ones((l,l,3),np.uint8)
arena2 = np.ones((l,l,3),np.uint8)

class Box:
    def __init__(self,x,y):
        self.walls = [True,True,True,True]
        self.x = x
        self.y = y
        self.visited = False

    def set_Walls(self,x):
        self.walls[x] = False

    def set_Visited(self):
        self.visited = True

    def draw_Walls(self):
        x=self.x
        y=self.y
        if (self.walls[0]):
            cv2.line(arena, (x, y), (x+w,y), (255,255,255),1)           #top
        if (self.walls[1]):
            cv2.line(arena, (x+w, y), (x+w,y+w), (255,255,255),1)       #right
        if (self.walls[2]):
            cv2.line(arena, (x+w,y+w), (x,y+w), (255,255,255),1)        #bottom
        if (self.walls[3]):
            cv2.line(arena, (x,y), (x,y+w), (255,255,255),1)            #left

        if(self.visited):
            cv2.rectangle(arena, (x+1, y+1), (x + w-1, y + w-1), (0, 0, 0), cv2.FILLED)

        if ((current_Box.x, current_Box.y) == (x, y)):
            cv2.rectangle(arena, (x, y), (x + w, y + w), (0, 0, 0), cv2.FILLED)

    def find_Index(self,a,b):
        x = self.x
        y = self.y

        if((x+a) <0 or (y+b)<0 or (x+a)>l-1 or (y+b)>l-1):
            return None
        else:
            return ((int(x/w)+a)+(int(y/w)+b)*no)

    def see_Neighbours(self):
        unvisited_Neighbour = []
        neighbour_index = [0,-1,1,0,0,1,-1,0]
        neighbour = []

        for i in range(0,4):
            index = self.find_Index(neighbour_index[i*2],neighbour_index[i*2+1])
            if (index and index<no*no):
                neighbour = grid[index]
                if (neighbour and neighbour.visited == False):
                    unvisited_Neighbour.append(neighbour)

        if(len(unvisited_Neighbour)>0):
            return rand.choice(unvisited_Neighbour)
        else:
            return None

def remove_Walls(cx,cy,nx,ny):
    rx=0
    a = nx-cx
    b = ny-cy
    if(a>0):
        nr = 3
        cr = 1
    elif(a<0):
        nr = 1
        cr = 3
    elif (b>0):
        nr = 0
        cr = 2
    elif (b <0):
        nr = 2
        cr = 0
    return (nr,cr)

if __name__ == "__main__":

    for j in range(no):
        for i in range(no):
            box = Box(i*w,j*w)
            grid.append(box)


current_Box = grid[0]
current_Box.set_Visited()

while True:
    next_Box = current_Box.see_Neighbours()
    if (next_Box):
        next_Box.set_Visited()
        stack.append(current_Box)
        nr,cr = remove_Walls(current_Box.x, current_Box.y, next_Box.x,next_Box.y)
        current_Box.set_Walls(cr)
        next_Box.set_Walls(nr)
        current_Box = next_Box
    elif(len(stack)>0):
        current_Box = stack.pop()
    elif(current_Box.x == 0 and current_Box.y ==0):
        print("done")
        break

    #time.sleep(.5)
    for box in grid:
        box.draw_Walls()


    cv2.imshow("Grid", arena)
    if(cv2.waitKey(1) == 27):
        break
cv2.waitKey(0)