from PIL import Image
import numpy

class PIC(object):
    def __init__(self,fileN):
        #initializes
        self.fileN=fileN
        self.pic=Image.open(fileN)
        self.colors=numpy.array(self.pic)
        self.ogColors=numpy.array(self.pic)

    def ultra(self):
        #makes the largest color the only color if it is domiant
        for x in range(0,len(self.colors)):
            for y in range(0,len(self.colors[x])):
                for z in range(0,3):
                    temp=self.colors[x][y][:3:]
                    if(((max(temp)-self.colors[x][y][z])<max(temp)/2) \
                       and (max(temp)!=self.colors[x][y][z])):
                        self.colors[x][y][z]=0

        self.pic=Image.fromarray(self.colors)
        self.pic.save("out/og/ultra"+self.fileN)
        #colors need to be set back to it's inital color to prevent every effect
        #being applied
        self.colors=self.ogColors.copy()

    def ultra2(self):
        #makes the largest color the only color if it is domiant
        for x in range(0,len(self.colors)):
            for y in range(0,len(self.colors[x])):
                for z in range(0,3):
                    temp=self.colors[x][y][:3:]
                    if(max(temp)!=self.colors[x][y][z]):
                        self.colors[x][y][z]= \
                        self.colors[x][y][z]-(self.colors[x][y][z]/2)


        self.pic=Image.fromarray(self.colors)
        self.pic.save("out/alt/altUltra"+self.fileN)
        #colors need to be set back to it's inital color to prevent every effect
        #being applied
        self.colors=self.ogColors.copy()

    def halfColor(self):
        #halves every pixel color
        for x in range(0,len(self.colors)):
            for y in range(0,len(self.colors[x])):
                self.colors[x][y]=list(map(lambda x:x/2,self.colors[x][y]))

        self.pic=Image.fromarray(self.colors)
        self.pic.save("out/half/half"+self.fileN)
        #colors need to be set back to it's inital color to prevent every effect
        #being applied
        self.colors=self.ogColors.copy()

    def gray(self):
        #makes the image black and white
        for x in range(0,len(self.colors)):
            for y in range(0,len(self.colors[x])):
                for z in range(0,len(self.colors[x][y])):
                    self.colors[x][y][z]= \
                    max(self.colors[x][y])/len(self.colors[x][y])
        self.pic=Image.fromarray(self.colors)
        self.pic.save("out/gray/gray"+self.fileN)
        #colors need to be set back to it's inital color to prevent every effect
        #being applied
        self.colors=self.ogColors.copy()

if __name__=="__main__":
    #takes input
    print("enter the file you want to edit")
    fileN=input()
    pic=PIC(fileN)
    #loop to keep running until stop is enetered
    command=""
    while(command.lower()!="stop"):
        print(
            "choose an effect:\ndom for the dominant effect\n"+
            "ext for the extreme effect\n"+
            "half for the half effect\n"+
            "gray for gray\n"+
            "all for all\n"+
            "enter stop to stop the program"
        )
        command=input()
        #pick a function
        if(command.lower()=="dom"):
            pic.ultra()
        elif(command.lower()=="ext"):
            pic.ultra2()
        elif(command.lower()=="half"):
            pic.halfColor()
        elif(command.lower()=="gray"):
            pic.gray()
        elif(command.lower()=="all"):
            pic.ultra()
            pic.ultra2()
            pic.halfColor()
            pic.gray()
