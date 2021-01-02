
##
height_display=gdisplay(x=400,y=0,width=400,height=400,title="sandpile profile",
             xtitle="site",ytitle="height",xmax=SITES,xmin=0,ymin=0,
             ymax=MAXTOPPLE+1,
             foreground=color.black, background=color.white)


##
height_plot=gcurve(gdisplay=height_display, color=color.red)        ###
height_plot_prev=gcurve(gdisplay=height_display, color=color.blue)  ###

scene=display(x=400,y=400,width=30,height=60,background=color.red)  ###
grain_label=label(text="start")                                     ###
scene.mouse.getclick() #wait for click                              ###
    


##
for i in arange(0,SITES+1):                 ###
    height_plot.plot(pos=(i,height[i]))     ###
    height_plot_prev.plot(pos=(i,height[i]))###


##
        height_plot_prev.gcurve.pos=height_plot.gcurve.pos  ###(VPython hack)
        height_plot_prev.gcurve.z=0.03                      ###(VPython hack)
        height_plot.gcurve.y=height                         ###(VPython hack)


##
    grain_label.text="%d" % grain ###
