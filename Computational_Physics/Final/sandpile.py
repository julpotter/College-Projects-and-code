from visual import *
from visual.graph import *

SITES=20
MAXTOPPLE=SITES+1
graintotal=1e5  ###

pic1=gdisplay(x=0,y=0,width=400,height=400,title="Toppling size distribution",
             xtitle="log(size)",ytitle="-log(N(size))",xmax=4.0,xmin=0,ymin=0,
             ymax=15.0,
             foreground=color.black, background=color.white)
plot1=gdots(gdisplay=pic1,color=color.blue)

##

height=zeros( (SITES+1) )
move=zeros( (SITES) )
toppling_size=zeros( (MAXTOPPLE) )

##

def check(height,move):
    unstable=false
    for i in range (0,SITES):
        if (height[i]-height[i+1] > 1):
            move[i]=true
            unstable=true
        else:
            move[i]=false
    return(unstable)

def slide(height,move):
    for i in range (0,SITES):
        if (move[i]==true):
            height[i] -= 2
            if (i<SITES-2):
                height[i+2] += 1
            if (i<SITES-1):
                height[i+1] += 1

def initial(height,toppling_size):
    for i in range (0,SITES):
        height[i]=0
        height[SITES]=0
    for i in range (0,MAXTOPPLE):
        toppling_size[i]=0
    

initial(height,toppling_size)               
##


grain=0
total_topple=0
max_topple_size=0
while(grain < graintotal):
    #rate(60) ###
    height[0] += 1
    topple=0
    grain += 1
    unstable=true
    while (unstable):
        #rate(100) ###
        unstable=check(height,move)
        if(unstable):
            slide(height,move)
            topple += 1
##

    if (topple>max_topple_size):
        max_topple_size=topple     
    toppling_size[topple] += 1
    total_topple += topple


    ### VPython update label and gdots
    # 
    #

##
    if grain%10==0:
       # for i in plot1.dots:
        #    i.visible=false #hide old dots      (VPython hack)
        #del plot1.dots[:]   #destroy old dots   (VPython hack)

        for i in range(1,max_topple_size):
            tmp=float(toppling_size[i])
            if(tmp>0.0):
              plot1.plot( pos=(log(float(i)),-log(tmp/float(grain))) )
    #
    ###
      
print "total number of topples",total_topple
print "biggest topple",max_topple_size

for i in plot1.dots:
    i.visible=false #hide old dots      (VPython hack)
del plot1.dots[:]   #destroy old dots   (VPython hack)
for i in range(1,max_topple_size):
    tmp=float(toppling_size[i])
    print i,tmp/float(grain)
    if(tmp>0.0):
      plot1.plot(pos=(log(float(i)),-log(tmp/float(grain))))
        

    
     


                
