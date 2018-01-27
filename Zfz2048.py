import random as rand
class ZFZ2048:
    def __init__(self,a_2):
        self.jz=[[0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0]]
        self.mark=[[0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0]]
        self.step=0
        self.gamecontinue=True
        self.score=0
        self.selectsite(self.random2or4(a_2))
        self.selectsite(self.random2or4(a_2))
        self.a_2=a_2
        self.sorf=0   #mark success or fail   0:unfinished, 1:finished
    #step is the steps in the game before
    def random2or4(self,a_2):  #a_2<=10
        #a_2:a_4=number(2):number(4)   a_4=10-a_2
        temp= rand.randint(1, 10)
        result=2 if temp<=a_2 else 4
        return result
    def selectsite(self,value2or4):
        #select a site where value is 0 and fill it with value2or4
        i,j=0,0
        while(1):
           i=rand.randint(0,3)
           j=rand.randint(0,3)
           if(self.jz[i][j]==0):
               self.jz[i][j]=value2or4
               break
    def contains(self,key):
        #if jz contains value (0 ,2048)
        for i in self.jz:
            if  i.__contains__(key):
                return True
        return False

    def success(self):
       # print("Congratulation! You successfully finished your task!")
        #print("Your score is %d!" % self.score )
        return

    def fail(self):
        #print("Sorry, you didn't finish your task.")
        #print("Your score is %d!" % self.score)
        return
    def check(self):  #check the game can be continued
        #if game isn't over,gamecontinue=True; else gamecontinue=False
        if self.contains(2048):
            self.gamecontinue=False   #Gameover ,success
            self.success()
            self.sorf=1   #sucess
            return
        if self.contains(0):     #the game can be continued
            return
        else:
            for line in self.jz:
                for i in range(3):
                    if line[i]==line[i+1]:
                        return
            for i in range(4):
                for j in range(3):
                    if self.jz[j][i]==self.jz[j+1][i]:
                        return
            self.gamecontinue=False   #Gameover ,fail
            self.fail()

    def LeftMove(self):
        t=0
        for line in self.jz:
            for i in range(1,4):
                for k in range(i-1,-1,-1):
                    if line[k]==0:
                       line[k]=line[k+1]
                       line[k+1]=0
                       self.mark[t][k]=self.mark[t][k+1]
                       self.mark[t][k+1]=0
                    else:
                       if line[k]==line[k+1] and self.mark[t][k]==0 and self.mark[t][k+1]==0:
                            line[k]=2*line[k]
                            line[k+1]=0
                            self.score+=line[k]
                            self.mark[t][k]=1
                       break
            t=t+1
    def RightMove(self):
        t=0
        for line in self.jz:
            for i in [2,1,0]:
                for k in range(i+1,4):
                   if line[k]==0:
                      line[k]=line[k-1]
                      line[k-1]=0
                      self.mark[t][k]=self.mark[t][k-1]
                      self.mark[t][k-1]=0
                   else:
                      if line[k]==line[k-1] and self.mark[t][k]==0 and self.mark[t][k-1]==0:
                         line[k]=2*line[k]
                         line[k-1]=0
                         self.score += line[k]
                         self.mark[t][k]=1
                      break
            t=t+1
    def UpMove(self):
        for i in range(4):
            for j in range(1,4):
                for k in range(j-1,-1,-1):
                    if self.jz[k][i]==0:
                      self.jz[k][i]=self.jz[k+1][i]
                      self.jz[k+1][i]=0
                      self.mark[k][i]=self.mark[k+1][i]
                      self.mark[k+1][i]=0
                    else:
                      if self.jz[k][i]==self.jz[k+1][i] and self.mark[k][i]==0 and self.mark[k+1][i]==0:
                        self.jz[k][i] =2*self.jz[k][i]
                        self.jz[k+1][i] = 0
                        self.score += self.jz[k][i]
                        self.mark[k][i] = 1
                      break
    def DownMove(self):
        for i in range(4):
            for j in [2,1,0]:
                for k in range(j+1,4):
                    if self.jz[k][i]==0:
                        self.jz[k][i]=self.jz[k-1][i]
                        self.jz[k-1][i]=0
                        self.mark[k][i]=self.mark[k-1][i]
                        self.mark[k-1][0]=0
                    else:
                        if self.jz[k][i]==self.jz[k-1][i] and self.mark[k][i]==0 and self.mark[k-1][i]==0:
                            self.jz[k][i]=2*self.jz[k][i]
                            self.jz[k-1][i]=0
                            self.score += self.jz[k][i]
                            self.mark[k][i]=1
                        break

    def addnew(self):
        self.selectsite(self.random2or4(self.a_2))

    def show(self):
        for line in self.jz:
            print(line)

    def clearmark(self):
        self.mark=[[0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0]]