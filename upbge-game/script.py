import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()
d15 = cont.actuators["anim_d15"]
menu_b =cont.actuators['act_menu']
d14 = cont.actuators["anim_d14"]
d13 = cont.actuators["anim_d13"]
d12 = cont.actuators["anim_d12"]
d11 = cont.actuators["anim_d11"]
d10 = cont.actuators["anim_d10"]
d09 = cont.actuators["anim_d09"]
d08 = cont.actuators["anim_d08"]
d07 = cont.actuators["anim_d07"]
d06 = cont.actuators["anim_d06"]
d05 = cont.actuators["anim_d05"]
d04 = cont.actuators["anim_d04"]
d03 = cont.actuators["anim_d03"]
d02 = cont.actuators["anim_d02"]
d01 = cont.actuators["anim_d01"]
control = scene.objects['control']
release = control['release']
start = control['start'] 
end = control['end']
properties = cont.actuators["properties"]
m_click = cont.actuators["m_click"]
m_release = cont.actuators["m_release"]
disc_15 = scene.objects['disc_15']
disc_14 = scene.objects['disc_14']
disc_13 = scene.objects['disc_13']
disc_12 = scene.objects['disc_12']
disc_11 = scene.objects['disc_11']
disc_10 = scene.objects['disc_10']
disc_09 = scene.objects['disc_09']
disc_08 = scene.objects['disc_08']
disc_07 = scene.objects['disc_07']
disc_06 = scene.objects['disc_06']
disc_05 = scene.objects['disc_05']
disc_04 = scene.objects['disc_04']
disc_03 = scene.objects['disc_03']
disc_02 = scene.objects['disc_02']
disc_01 = scene.objects['disc_01']
txt_1 = scene.objects['txt_1']
def inicio():
    properties.propName = "release"
    properties.value = "0"
    cont.activate(properties)     
 
def mover_d15():
    if (start == 1 and end == 2 and control['discs'] == 15 and disc_15['loc'] == 1  and  release == True and control["winner"] == False): 
        cont.activate(d15)    
        d15.action = "Pose"
        d15.frameStart = (control["disc_p2"]*2+32) 
        d15.frameEnd = (control["disc_p2"]*2 + 32)
        disc_15['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1
        control["moves"] += 1
    elif (start == 1 and end == 3 and control['discs'] == 15 and disc_15['loc'] == 1  and  release == True and control["winner"] == False):  
        cont.activate(d15)    
        d15.action = "Pose"
        d15.frameStart = (control["disc_p3"]*2+62) 
        d15.frameEnd = (control["disc_p3"]*2 + 62)
        disc_15['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1
        control["moves"] += 1
    elif (start == 2 and end == 1 and control['discs'] == 15 and disc_15['loc'] == 2 and  release == True and control["winner"] == False):  
        cont.activate(d15)    
        d15.action = "Pose"
        d15.frameStart = (control["disc_p1"]*2+2) 
        d15.frameEnd = (control["disc_p1"]*2+2)
        disc_15['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1
        control["moves"] += 1
    elif (start == 2 and end == 3 and control['discs'] == 15 and disc_15['loc'] == 2 and  release == True and control["winner"] == False):  
        cont.activate(d15)    
        d15.action = "Pose"
        d15.frameStart = (control["disc_p3"]*2 + 62) 
        d15.frameEnd = (control["disc_p3"]*2 + 62)
        disc_15['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1
        control["moves"] += 1
    elif (start == 3 and end == 1 and control['discs'] == 15 and disc_15['loc'] == 3 and  release == True and control["winner"] == False):  
        cont.activate(d15)    
        d15.action = "Pose"
        d15.frameStart = (control["disc_p1"]*2+2) 
        d15.frameEnd = (control["disc_p1"]*2+2)
        disc_15['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1
        control["moves"] += 1
    elif (start == 3 and end == 2 and control['discs'] == 15 and disc_15['loc'] == 3 and  release == True and control["winner"] == False): 
        cont.activate(d15)    
        d15.action = "Pose"
        d15.frameStart = (control["disc_p2"]*2 + 32) 
        d15.frameEnd = (control["disc_p2"]*2 + 32)
        disc_15['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1
        control["moves"] += 1
def mover_d14():
    if (start == 1 and end == 2 and control['discs'] >= 14 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and disc_14['loc'] == 1  and  release == True and control["winner"] == False):    
        cont.activate(d14)    
        d14.action = "Pose"
        d14.frameStart = (control["disc_p2"]*2 + 32) 
        d14.frameEnd = (control["disc_p2"]*2 + 32)
        disc_14['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1   
        control["moves"] += 1
    elif (start == 1 and end == 3 and control['discs'] >= 14 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and disc_14['loc'] == 1  and  release == True and control["winner"] == False):   
        cont.activate(d14)    
        d14.action = "Pose"
        d14.frameStart = (control["disc_p3"]*2 + 62) 
        d14.frameEnd = (control["disc_p3"]*2 + 62)
        disc_14['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1
        control["moves"] += 1
    elif (start == 2 and end == 1 and control['discs'] >= 14 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and disc_14['loc'] == 2  and  release == True and control["winner"] == False):   
        cont.activate(d14)    
        d14.action = "Pose"
        d14.frameStart = (control["disc_p1"]*2 + 2) 
        d14.frameEnd = (control["disc_p1"]*2 + 2)
        disc_14['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1     
        control["moves"] += 1
    elif (start == 2 and end == 3 and control['discs'] >= 14 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and disc_14['loc'] == 2  and  release == True and control["winner"] == False):    
        cont.activate(d14)    
        d14.action = "Pose"
        d14.frameStart = (control["disc_p3"]*2 + 62) 
        d14.frameEnd = (control["disc_p3"]*2 + 62)
        disc_14['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1 
        control["moves"] += 1
    elif (start == 3 and end == 1 and control['discs'] >= 14 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and disc_14['loc'] == 3  and  release == True and control["winner"] == False):   
        cont.activate(d14)    
        d14.action = "Pose"
        d14.frameStart = (control["disc_p1"]*2 + 2) 
        d14.frameEnd = (control["disc_p1"]*2 + 2)
        disc_14['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1  
        control["moves"] += 1
    elif (start == 3 and end == 2 and control['discs'] >= 14 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and disc_14['loc'] == 3  and  release == True and control["winner"] == False):   
        cont.activate(d14)    
        d14.action = "Pose"
        d14.frameStart = (control["disc_p2"]*2 + 32) 
        d14.frameEnd = (control["disc_p2"]*2 + 32)
        disc_14['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1                                                         
        control["moves"] += 1
def mover_d13():
    if (start == 1 and end == 2 and control['discs'] >= 13 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and disc_13['loc'] == 1  and  release == True and control["winner"] == False):   
        cont.activate(d13)    
        d13.action = "Pose"
        d13.frameStart = (control["disc_p2"]*2 + 32) 
        d13.frameEnd = (control["disc_p2"]*2 + 32)
        disc_13['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1   
        control["moves"] += 1
    elif (start == 1 and end == 3 and control['discs'] >= 13 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and disc_13['loc'] == 1  and  release == True and control["winner"] == False):   
        cont.activate(d13)    
        d13.action = "Pose"
        d13.frameStart = (control["disc_p3"]*2 + 62) 
        d13.frameEnd = (control["disc_p3"]*2 + 62)
        disc_13['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1      
        control["moves"] += 1
    elif (start == 2 and end == 1 and control['discs'] >= 13 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and disc_13['loc'] == 2  and  release == True and control["winner"] == False):    
        cont.activate(d13)    
        d13.action = "Pose"
        d13.frameStart = (control["disc_p1"]*2 + 2) 
        d13.frameEnd = (control["disc_p1"]*2 + 2)
        disc_13['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1 
        control["moves"] += 1
    elif (start == 2 and end == 3 and control['discs'] >= 13 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and disc_13['loc'] == 2  and  release == True and control["winner"] == False):    
        cont.activate(d13)    
        d13.action = "Pose"
        d13.frameStart = (control["disc_p3"]*2 + 62) 
        d13.frameEnd = (control["disc_p3"]*2 + 62)
        disc_13['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1  
        control["moves"] += 1
    elif (start == 3 and end == 1 and control['discs'] >= 13 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and disc_13['loc'] == 3  and  release == True and control["winner"] == False):    
        cont.activate(d13)    
        d13.action = "Pose"
        d13.frameStart = (control["disc_p1"]*2 + 2) 
        d13.frameEnd = (control["disc_p1"]*2 + 2)
        disc_13['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1  
        control["moves"] += 1
    elif (start == 3 and end == 2 and control['discs'] >= 13 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and disc_13['loc'] == 3  and  release == True and control["winner"] == False):   
        cont.activate(d13)    
        d13.action = "Pose"
        d13.frameStart = (control["disc_p2"]*2 + 32) 
        d13.frameEnd = (control["disc_p2"]*2 + 32)
        disc_13['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1 
        control["moves"] += 1
def mover_d12():
    if (start == 1 and end == 2 and control['discs'] >= 12 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0) and disc_12['loc'] == 1 and  release == True and control["winner"] == False):  
        cont.activate(d12)    
        d12.action = "Pose"
        d12.frameStart = (control["disc_p2"]*2 + 32) 
        d12.frameEnd = (control["disc_p2"]*2 + 32)
        disc_12['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1                                               
        control["moves"] += 1
    elif (start == 1 and end == 3 and control['discs'] >= 12 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0) and disc_12['loc'] == 1 and  release == True and control["winner"] == False):   
        cont.activate(d12)    
        d12.action = "Pose"
        d12.frameStart = (control["disc_p3"]*2 + 62) 
        d12.frameEnd = (control["disc_p3"]*2 + 62)
        disc_12['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1      
        control["moves"] += 1
    elif (start == 2 and end == 1 and control['discs'] >= 12 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0) and disc_12['loc'] == 2 and  release == True and control["winner"] == False):   
        cont.activate(d12)    
        d12.action = "Pose"
        d12.frameStart = (control["disc_p1"]*2 + 2) 
        d12.frameEnd = (control["disc_p1"]*2 + 2)
        disc_12['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1  
        control["moves"] += 1
    elif (start == 2 and end == 3 and control['discs'] >= 12 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0) and disc_12['loc'] == 2 and  release == True and control["winner"] == False):    
        cont.activate(d12)    
        d12.action = "Pose"
        d12.frameStart = (control["disc_p3"]*2 + 62) 
        d12.frameEnd = (control["disc_p3"]*2 + 62)
        disc_12['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1                     
        control["moves"] += 1
    elif (start == 3 and end == 1 and control['discs'] >= 12 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0) and disc_12['loc'] == 3 and  release == True and control["winner"] == False):   
        cont.activate(d12)    
        d12.action = "Pose"
        d12.frameStart = (control["disc_p1"]*2 + 2) 
        d12.frameEnd = (control["disc_p1"]*2 + 2)
        disc_12['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1   
        control["moves"] += 1
    elif (start == 3 and end == 2 and control['discs'] >= 12 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0) and disc_12['loc'] == 3 and  release == True and control["winner"] == False):    
        cont.activate(d12)    
        d12.action = "Pose"
        d12.frameStart = (control["disc_p2"]*2 + 32) 
        d12.frameEnd = (control["disc_p2"]*2 + 32)
        disc_12['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1           
        control["moves"] += 1
def mover_d11():        
    if (start == 1 and end == 2 and control['discs'] >= 11 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and disc_11['loc'] == 1 and  release == True and control["winner"] == False):  
        cont.activate(d11)    
        d11.action = "Pose"
        d11.frameStart = (control["disc_p2"]*2 + 32) 
        d11.frameEnd = (control["disc_p2"]*2 + 32)
        disc_11['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1                                               
        control["moves"] += 1
    elif (start == 1 and end == 3 and control['discs'] >= 11 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and disc_11['loc'] == 1 and  release == True and control["winner"] == False):  
        cont.activate(d11)    
        d11.action = "Pose"
        d11.frameStart = (control["disc_p3"]*2 + 62) 
        d11.frameEnd = (control["disc_p3"]*2 + 62)
        disc_11['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1      
        control["moves"] += 1
    elif (start == 2 and end == 1 and control['discs'] >= 11 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and disc_11['loc'] == 2 and  release == True and control["winner"] == False):    
        cont.activate(d11)    
        d11.action = "Pose"
        d11.frameStart = (control["disc_p1"]*2 + 2) 
        d11.frameEnd = (control["disc_p1"]*2 + 2)
        disc_11['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1  
        control["moves"] += 1
    elif (start == 2 and end == 3 and control['discs'] >= 11 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and disc_11['loc'] == 2 and  release == True and control["winner"] == False):   
        cont.activate(d11)    
        d11.action = "Pose"
        d11.frameStart = (control["disc_p3"]*2 + 62) 
        d11.frameEnd = (control["disc_p3"]*2 + 62)
        disc_11['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1                     
        control["moves"] += 1
    elif (start == 3 and end == 1 and control['discs'] >= 11 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and disc_11['loc'] == 3 and  release == True and control["winner"] == False):    
        cont.activate(d11)    
        d11.action = "Pose"
        d11.frameStart = (control["disc_p1"]*2 + 2) 
        d11.frameEnd = (control["disc_p1"]*2 + 2)
        disc_11['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1   
        control["moves"] += 1
    elif (start == 3 and end == 2 and control['discs'] >= 11 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and disc_11['loc'] == 3 and  release == True and control["winner"] == False):    
        cont.activate(d11)    
        d11.action = "Pose"
        d11.frameStart = (control["disc_p2"]*2 + 32) 
        d11.frameEnd = (control["disc_p2"]*2 + 32)
        disc_11['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1  
        control["moves"] += 1
def mover_d10():
    if (start == 1 and end == 2 and control['discs'] >= 10 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and disc_10['loc'] == 1 and  release == True and control["winner"] == False):    
        cont.activate(d10)    
        d10.action = "Pose"
        d10.frameStart = (control["disc_p2"]*2 + 32) 
        d10.frameEnd = (control["disc_p2"]*2 + 32)
        disc_10['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1                                               
        control["moves"] += 1
    elif (start == 1 and end == 3 and control['discs'] >= 10 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and disc_10['loc'] == 1 and  release == True and control["winner"] == False):    
        cont.activate(d10)    
        d10.action = "Pose"
        d10.frameStart = (control["disc_p3"]*2 + 62) 
        d10.frameEnd = (control["disc_p3"]*2 + 62)
        disc_10['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1      
        control["moves"] += 1
    elif (start == 2 and end == 1 and control['discs'] >= 10 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and disc_10['loc'] == 2 and  release == True and control["winner"] == False):    
        cont.activate(d10)    
        d10.action = "Pose"
        d10.frameStart = (control["disc_p1"]*2 + 2) 
        d10.frameEnd = (control["disc_p1"]*2 + 2)
        disc_10['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1  
        control["moves"] += 1
    elif (start == 2 and end == 3 and control['discs'] >= 10 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and disc_10['loc'] == 2 and  release == True and control["winner"] == False):   
        cont.activate(d10)    
        d10.action = "Pose"
        d10.frameStart = (control["disc_p3"]*2 + 62) 
        d10.frameEnd = (control["disc_p3"]*2 + 62)
        disc_10['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1                     
        control["moves"] += 1
    elif (start == 3 and end == 1 and control['discs'] >= 10 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and disc_10['loc'] == 3 and  release == True and control["winner"] == False):    
        cont.activate(d10)    
        d10.action = "Pose"
        d10.frameStart = (control["disc_p1"]*2 + 2) 
        d10.frameEnd = (control["disc_p1"]*2 + 2)
        disc_10['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1   
        control["moves"] += 1
    elif (start == 3 and end == 2 and control['discs'] >= 10 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and disc_10['loc'] == 3 and  release == True and control["winner"] == False):   
        cont.activate(d10)    
        d10.action = "Pose"
        d10.frameStart = (control["disc_p2"]*2 + 32) 
        d10.frameEnd = (control["disc_p2"]*2 + 32)
        disc_10['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1  
        control["moves"] += 1
def mover_d09():                
    if (start == 1 and end == 2 and control['discs'] >= 9 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and disc_09['loc'] == 1 and  release == True and control["winner"] == False):   
        cont.activate(d09)    
        d09.action = "Pose"
        d09.frameStart = (control["disc_p2"]*2 + 32) 
        d09.frameEnd = (control["disc_p2"]*2 + 32)
        disc_09['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1                                               
        control["moves"] += 1
    elif (start == 1 and end == 3 and control['discs'] >= 9 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and disc_09['loc'] == 1 and  release == True and control["winner"] == False):    
        cont.activate(d09)    
        d09.action = "Pose"
        d09.frameStart = (control["disc_p3"]*2 + 62) 
        d09.frameEnd = (control["disc_p3"]*2 + 62)
        disc_09['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1      
        control["moves"] += 1
    elif (start == 2 and end == 1 and control['discs'] >= 9 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and disc_09['loc'] == 2 and  release == True and control["winner"] == False):    
        cont.activate(d09)    
        d09.action = "Pose"
        d09.frameStart = (control["disc_p1"]*2 + 2) 
        d09.frameEnd = (control["disc_p1"]*2 + 2)
        disc_09['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1  
        control["moves"] += 1
    elif (start == 2 and end == 3 and control['discs'] >= 9 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and disc_09['loc'] == 2 and  release == True and control["winner"] == False):   
        cont.activate(d09)    
        d09.action = "Pose"
        d09.frameStart = (control["disc_p3"]*2 + 62) 
        d09.frameEnd = (control["disc_p3"]*2 + 62)
        disc_09['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1                     
        control["moves"] += 1
    elif (start == 3 and end == 1 and control['discs'] >= 9 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and disc_09['loc'] == 3 and  release == True and control["winner"] == False):   
        cont.activate(d09)    
        d09.action = "Pose"
        d09.frameStart = (control["disc_p1"]*2 + 2) 
        d09.frameEnd = (control["disc_p1"]*2 + 2)
        disc_09['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1   
        control["moves"] += 1
    elif (start == 3 and end == 2 and control['discs'] >= 9 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and disc_09['loc'] == 3 and  release == True and control["winner"] == False):  
        cont.activate(d09)    
        d09.action = "Pose"
        d09.frameStart = (control["disc_p2"]*2 + 32) 
        d09.frameEnd = (control["disc_p2"]*2 + 32)
        disc_09['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1  
        control["moves"] += 1
def mover_d08():
    if (start == 1 and end == 2 and control['discs'] >= 8 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and disc_08['loc'] == 1 and  release == True and control["winner"] == False):    
        cont.activate(d08)    
        d08.action = "Pose"
        d08.frameStart = (control["disc_p2"]*2 + 32) 
        d08.frameEnd = (control["disc_p2"]*2 + 32)
        disc_08['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1                                               
        control["moves"] += 1
    elif (start == 1 and end == 3 and control['discs'] >= 8 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and disc_08['loc'] == 1 and  release == True and control["winner"] == False):    
        cont.activate(d08)    
        d08.action = "Pose"
        d08.frameStart = (control["disc_p3"]*2 + 62) 
        d08.frameEnd = (control["disc_p3"]*2 + 62)
        disc_08['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1      
        control["moves"] += 1
    elif (start == 2 and end == 1 and control['discs'] >= 8 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and disc_08['loc'] == 2 and  release == True and control["winner"] == False):    
        cont.activate(d08)    
        d08.action = "Pose"
        d08.frameStart = (control["disc_p1"]*2 + 2) 
        d08.frameEnd = (control["disc_p1"]*2 + 2)
        disc_08['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1  
        control["moves"] += 1
    elif (start == 2 and end == 3 and control['discs'] >= 8 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and disc_08['loc'] == 2 and  release == True and control["winner"] == False):   
        cont.activate(d08)    
        d08.action = "Pose"
        d08.frameStart = (control["disc_p3"]*2 + 62) 
        d08.frameEnd = (control["disc_p3"]*2 + 62)
        disc_08['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1                     
        control["moves"] += 1
    elif (start == 3 and end == 1 and control['discs'] >= 8 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and disc_08['loc'] == 3 and  release == True and control["winner"] == False):   
        cont.activate(d08)    
        d08.action = "Pose"
        d08.frameStart = (control["disc_p1"]*2 + 2) 
        d08.frameEnd = (control["disc_p1"]*2 + 2)
        disc_08['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1   
        control["moves"] += 1
    elif (start == 3 and end == 2 and control['discs'] >= 8 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and disc_08['loc'] == 3 and  release == True and control["winner"] == False):  
        cont.activate(d08)    
        d08.action = "Pose"
        d08.frameStart = (control["disc_p2"]*2 + 32) 
        d08.frameEnd = (control["disc_p2"]*2 + 32)
        disc_08['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1                  
        control["moves"] += 1
def mover_d07():
    if (start == 1 and end == 2 and control['discs'] >= 7 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and (disc_08['loc'] == 3 or disc_08['loc'] == 0) and disc_07['loc'] == 1 and  release == True and control["winner"] == False):  
        cont.activate(d07)    
        d07.action = "Pose"
        d07.frameStart = (control["disc_p2"]*2 + 32) 
        d07.frameEnd = (control["disc_p2"]*2 + 32)
        disc_07['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1                                               
        control["moves"] += 1
    elif (start == 1 and end == 3 and control['discs'] >= 7 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and (disc_08['loc'] == 2 or disc_08['loc'] == 0) and disc_07['loc'] == 1 and  release == True and control["winner"] == False):    
        cont.activate(d07)    
        d07.action = "Pose"
        d07.frameStart = (control["disc_p3"]*2 + 62) 
        d07.frameEnd = (control["disc_p3"]*2 + 62)
        disc_07['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1      
        control["moves"] += 1
    elif (start == 2 and end == 1 and control['discs'] >= 7 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and (disc_08['loc'] == 3 or disc_08['loc'] == 0) and disc_07['loc'] == 2 and  release == True and control["winner"] == False):   
        cont.activate(d07)    
        d07.action = "Pose"
        d07.frameStart = (control["disc_p1"]*2 + 2) 
        d07.frameEnd = (control["disc_p1"]*2 + 2)
        disc_07['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1  
        control["moves"] += 1
    elif (start == 2 and end == 3 and control['discs'] >= 7 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and (disc_08['loc'] == 1 or disc_08['loc'] == 0) and disc_07['loc'] == 2 and  release == True and control["winner"] == False):  
        cont.activate(d07)    
        d07.action = "Pose"
        d07.frameStart = (control["disc_p3"]*2 + 62) 
        d07.frameEnd = (control["disc_p3"]*2 + 62)
        disc_07['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1                     
        control["moves"] += 1
    elif (start == 3 and end == 1 and control['discs'] >= 7 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and (disc_08['loc'] == 2 or disc_08['loc'] == 0) and disc_07['loc'] == 3 and  release == True and control["winner"] == False):   
        cont.activate(d07)    
        d07.action = "Pose"
        d07.frameStart = (control["disc_p1"]*2 + 2) 
        d07.frameEnd = (control["disc_p1"]*2 + 2)
        disc_07['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1   
        control["moves"] += 1
    elif (start == 3 and end == 2 and control['discs'] >= 7 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and (disc_08['loc'] == 1 or disc_08['loc'] == 0) and disc_07['loc'] == 3 and  release == True and control["winner"] == False):   
        cont.activate(d07)    
        d07.action = "Pose"
        d07.frameStart = (control["disc_p2"]*2 + 32) 
        d07.frameEnd = (control["disc_p2"]*2 + 32)
        disc_07['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1  
        control["moves"] += 1
def mover_d06():          
    if (start == 1 and end == 2 and control['discs'] >= 6 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and (disc_08['loc'] == 3 or disc_08['loc'] == 0) and (disc_07['loc'] == 3 or disc_07['loc'] == 0) and disc_06['loc'] == 1 and  release == True and control["winner"] == False):  
        cont.activate(d06)    
        d06.action = "Pose"
        d06.frameStart = (control["disc_p2"]*2 + 32) 
        d06.frameEnd = (control["disc_p2"]*2 + 32)
        disc_06['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1                                               
        control["moves"] += 1
    elif (start == 1 and end == 3 and control['discs'] >= 6 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and (disc_08['loc'] == 2 or disc_08['loc'] == 0) and (disc_07['loc'] == 2 or disc_07['loc'] == 0) and disc_06['loc'] == 1 and  release == True and control["winner"] == False):  
        cont.activate(d06)    
        d06.action = "Pose"
        d06.frameStart = (control["disc_p3"]*2 + 62) 
        d06.frameEnd = (control["disc_p3"]*2 + 62)
        disc_06['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1      
        control["moves"] += 1
    elif (start == 2 and end == 1 and control['discs'] >= 6 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and (disc_08['loc'] == 3 or disc_08['loc'] == 0) and (disc_07['loc'] == 3 or disc_07['loc'] == 0) and disc_06['loc'] == 2 and  release == True and control["winner"] == False):  
        cont.activate(d06)    
        d06.action = "Pose"
        d06.frameStart = (control["disc_p1"]*2 + 2) 
        d06.frameEnd = (control["disc_p1"]*2 + 2)
        disc_06['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1  
        control["moves"] += 1
    elif (start == 2 and end == 3 and control['discs'] >= 6 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and (disc_08['loc'] == 1 or disc_08['loc'] == 0) and (disc_07['loc'] == 1 or disc_07['loc'] == 0) and disc_06['loc'] == 2 and  release == True and control["winner"] == False):    
        cont.activate(d06)    
        d06.action = "Pose"
        d06.frameStart = (control["disc_p3"]*2 + 62) 
        d06.frameEnd = (control["disc_p3"]*2 + 62)
        disc_06['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1                     
        control["moves"] += 1
    elif (start == 3 and end == 1 and control['discs'] >= 6 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and (disc_08['loc'] == 2 or disc_08['loc'] == 0) and (disc_07['loc'] == 2 or disc_07['loc'] == 0) and disc_06['loc'] == 3 and  release == True and control["winner"] == False):  
        cont.activate(d06)    
        d06.action = "Pose"
        d06.frameStart = (control["disc_p1"]*2 + 2) 
        d06.frameEnd = (control["disc_p1"]*2 + 2)
        disc_06['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1   
        control["moves"] += 1
    elif (start == 3 and end == 2 and control['discs'] >= 6 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and (disc_08['loc'] == 1 or disc_08['loc'] == 0) and (disc_07['loc'] == 1 or disc_07['loc'] == 0) and disc_06['loc'] == 3 and  release == True and control["winner"] == False):    
        cont.activate(d06)    
        d06.action = "Pose"
        d06.frameStart = (control["disc_p2"]*2 + 32) 
        d06.frameEnd = (control["disc_p2"]*2 + 32)
        disc_06['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1   
        control["moves"] += 1
def mover_d05():
    if (start == 1 and end == 2 and control['discs'] >= 5 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and (disc_08['loc'] == 3 or disc_08['loc'] == 0) and (disc_07['loc'] == 3 or disc_07['loc'] == 0) and (disc_06['loc'] == 3 or disc_06['loc'] == 0) and disc_05['loc'] == 1 and  release == True and control["winner"] == False):   
        cont.activate(d05)    
        d05.action = "Pose"
        d05.frameStart = (control["disc_p2"]*2 + 32) 
        d05.frameEnd = (control["disc_p2"]*2 + 32)
        disc_05['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1                                               
        control["moves"] += 1
    elif (start == 1 and end == 3 and control['discs'] >= 5 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and (disc_08['loc'] == 2 or disc_08['loc'] == 0) and (disc_07['loc'] == 2 or disc_07['loc'] == 0) and (disc_06['loc'] == 2 or disc_06['loc'] == 0) and disc_05['loc'] == 1 and  release == True and control["winner"] == False):  
        cont.activate(d05)    
        d05.action = "Pose"
        d05.frameStart = (control["disc_p3"]*2 + 62) 
        d05.frameEnd = (control["disc_p3"]*2 + 62)
        disc_05['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1      
        control["moves"] += 1              
    elif (start == 2 and end == 1 and control['discs'] >= 5 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and (disc_08['loc'] == 3 or disc_08['loc'] == 0) and (disc_07['loc'] == 3 or disc_07['loc'] == 0) and (disc_06['loc'] == 3 or disc_06['loc'] == 0) and disc_05['loc'] == 2 and  release == True and control["winner"] == False):  
        cont.activate(d05)    
        d05.action = "Pose"
        d05.frameStart = (control["disc_p1"]*2 + 2) 
        d05.frameEnd = (control["disc_p1"]*2 + 2)
        disc_05['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1  
        control["moves"] += 1        
    elif (start == 2 and end == 3 and control['discs'] >= 5 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and (disc_08['loc'] == 1 or disc_08['loc'] == 0) and (disc_07['loc'] == 1 or disc_07['loc'] == 0) and (disc_06['loc'] == 1 or disc_06['loc'] == 0) and disc_05['loc'] == 2 and  release == True and control["winner"] == False):  
        cont.activate(d05)    
        d05.action = "Pose"
        d05.frameStart = (control["disc_p3"]*2 + 62) 
        d05.frameEnd = (control["disc_p3"]*2 + 62)
        disc_05['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1                     
        control["moves"] += 1
    elif (start == 3 and end == 1 and control['discs'] >= 5 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and (disc_08['loc'] == 2 or disc_08['loc'] == 0) and (disc_07['loc'] == 2 or disc_07['loc'] == 0) and (disc_06['loc'] == 2 or disc_06['loc'] == 0) and disc_05['loc'] == 3 and  release == True and control["winner"] == False):  
        cont.activate(d05)    
        d05.action = "Pose"
        d05.frameStart = (control["disc_p1"]*2 + 2) 
        d05.frameEnd = (control["disc_p1"]*2 + 2)
        disc_05['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1
        control["moves"] += 1   
    elif (start == 3 and end == 2 and control['discs'] >= 5 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and (disc_08['loc'] == 1 or disc_08['loc'] == 0) and (disc_07['loc'] == 1 or disc_07['loc'] == 0) and (disc_06['loc'] == 1 or disc_06['loc'] == 0) and disc_05['loc'] == 3 and  release == True and control["winner"] == False):  
        cont.activate(d05)    
        d05.action = "Pose"
        d05.frameStart = (control["disc_p2"]*2 + 32) 
        d05.frameEnd = (control["disc_p2"]*2 + 32)
        disc_05['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1    
        control["moves"] += 1
def mover_d04():
    if (start == 1 and end == 2 and control['discs'] >= 4 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and (disc_08['loc'] == 3 or disc_08['loc'] == 0) and (disc_07['loc'] == 3 or disc_07['loc'] == 0) and (disc_06['loc'] == 3 or disc_06['loc'] == 0) and (disc_05['loc'] == 3 or disc_05['loc'] == 0) and disc_04['loc'] == 1 and  release == True and control["winner"] == False):   
        cont.activate(d04)    
        d04.action = "Pose"
        d04.frameStart = (control["disc_p2"]*2 + 32) 
        d04.frameEnd = (control["disc_p2"]*2 + 32)
        disc_04['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1                                               
        control["moves"] += 1            
    elif (start == 1 and end == 3 and control['discs'] >= 4 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and (disc_08['loc'] == 2 or disc_08['loc'] == 0) and (disc_07['loc'] == 2 or disc_07['loc'] == 0) and (disc_06['loc'] == 2 or disc_06['loc'] == 0) and (disc_05['loc'] == 2 or disc_05['loc'] == 0) and disc_04['loc'] == 1 and  release == True and control["winner"] == False):    
        cont.activate(d04)    
        d04.action = "Pose"
        d04.frameStart = (control["disc_p3"]*2 + 62) 
        d04.frameEnd = (control["disc_p3"]*2 + 62)
        disc_04['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1      
        control["moves"] += 1
    elif (start == 2 and end == 1 and control['discs'] >= 4 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and (disc_08['loc'] == 3 or disc_08['loc'] == 0) and (disc_07['loc'] == 3 or disc_07['loc'] == 0) and (disc_06['loc'] == 3 or disc_06['loc'] == 0) and (disc_05['loc'] == 3 or disc_05['loc'] == 0) and disc_04['loc'] == 2 and  release == True and control["winner"] == False):  
        cont.activate(d04)    
        d04.action = "Pose"
        d04.frameStart = (control["disc_p1"]*2 + 2) 
        d04.frameEnd = (control["disc_p1"]*2 + 2)
        disc_04['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1  
        control["moves"] += 1             
    elif (start == 2 and end == 3 and control['discs'] >= 4 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and (disc_08['loc'] == 1 or disc_08['loc'] == 0) and (disc_07['loc'] == 1 or disc_07['loc'] == 0) and (disc_06['loc'] == 1 or disc_06['loc'] == 0) and (disc_05['loc'] == 1 or disc_05['loc'] == 0) and disc_04['loc'] == 2 and  release == True and control["winner"] == False):   
        cont.activate(d04)    
        d04.action = "Pose"
        d04.frameStart = (control["disc_p3"]*2 + 62) 
        d04.frameEnd = (control["disc_p3"]*2 + 62)
        disc_04['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1                     
        control["moves"] += 1
    elif (start == 3 and end == 1 and control['discs'] >= 4 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and (disc_08['loc'] == 2 or disc_08['loc'] == 0) and (disc_07['loc'] == 2 or disc_07['loc'] == 0) and (disc_06['loc'] == 2 or disc_06['loc'] == 0) and (disc_05['loc'] == 2 or disc_05['loc'] == 0) and disc_04['loc'] == 3 and  release == True and control["winner"] == False):  
        cont.activate(d04)    
        d04.action = "Pose"
        d04.frameStart = (control["disc_p1"]*2 + 2) 
        d04.frameEnd = (control["disc_p1"]*2 + 2)
        disc_04['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1   
        control["moves"] += 1      
    elif (start == 3 and end == 2 and control['discs'] >= 4 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and (disc_08['loc'] == 1 or disc_08['loc'] == 0) and (disc_07['loc'] == 1 or disc_07['loc'] == 0) and (disc_06['loc'] == 1 or disc_06['loc'] == 0) and (disc_05['loc'] == 1 or disc_05['loc'] == 0) and disc_04['loc'] == 3 and  release == True and control["winner"] == False):   
        cont.activate(d04)    
        d04.action = "Pose"
        d04.frameStart = (control["disc_p2"]*2 + 32) 
        d04.frameEnd = (control["disc_p2"]*2 + 32)
        disc_04['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1    
        control["moves"] += 1                
def mover_d03():
    if (start == 1 and end == 2 and control['discs'] >= 3 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and (disc_08['loc'] == 3 or disc_08['loc'] == 0) and (disc_07['loc'] == 3 or disc_07['loc'] == 0) and (disc_06['loc'] == 3 or disc_06['loc'] == 0) and (disc_05['loc'] == 3 or disc_05['loc'] == 0) and (disc_04['loc'] == 3 or disc_04['loc'] == 0) and disc_03['loc'] == 1 and  release == True and control["winner"] == False):   
        cont.activate(d03)    
        d03.action = "Pose"
        d03.frameStart = (control["disc_p2"]*2 + 32) 
        d03.frameEnd = (control["disc_p2"]*2 + 32)
        disc_03['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1                                               
        control["moves"] += 1               
    elif (start == 1 and end == 3 and control['discs'] >= 3 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and (disc_08['loc'] == 2 or disc_08['loc'] == 0) and (disc_07['loc'] == 2 or disc_07['loc'] == 0) and (disc_06['loc'] == 2 or disc_06['loc'] == 0) and (disc_05['loc'] == 2 or disc_05['loc'] == 0) and (disc_04['loc'] == 2 or disc_04['loc'] == 0) and disc_03['loc'] == 1 and  release == True and control["winner"] == False):   
        cont.activate(d03)    
        d03.action = "Pose"
        d03.frameStart = (control["disc_p3"]*2 + 62) 
        d03.frameEnd = (control["disc_p3"]*2 + 62)
        disc_03['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1      
        control["moves"] += 1          
    elif (start == 2 and end == 1 and control['discs'] >= 3 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and (disc_08['loc'] == 3 or disc_08['loc'] == 0) and (disc_07['loc'] == 3 or disc_07['loc'] == 0) and (disc_06['loc'] == 3 or disc_06['loc'] == 0) and (disc_05['loc'] == 3 or disc_05['loc'] == 0) and (disc_04['loc'] == 3 or disc_04['loc'] == 0) and disc_03['loc'] == 2 and  release == True and control["winner"] == False):   
        cont.activate(d03)    
        d03.action = "Pose"
        d03.frameStart = (control["disc_p1"]*2 + 2) 
        d03.frameEnd = (control["disc_p1"]*2 + 2)
        disc_03['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1  
        control["moves"] += 1       
    elif (start == 2 and end == 3 and control['discs'] >= 3 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and (disc_08['loc'] == 1 or disc_08['loc'] == 0) and (disc_07['loc'] == 1 or disc_07['loc'] == 0) and (disc_06['loc'] == 1 or disc_06['loc'] == 0) and (disc_05['loc'] == 1 or disc_05['loc'] == 0) and (disc_04['loc'] == 1 or disc_04['loc'] == 0) and disc_03['loc'] == 2 and  release == True and control["winner"] == False):  
        cont.activate(d03)    
        d03.action = "Pose"
        d03.frameStart = (control["disc_p3"]*2 + 62) 
        d03.frameEnd = (control["disc_p3"]*2 + 62)
        disc_03['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1                     
        control["moves"] += 1                  
    elif (start == 3 and end == 1 and control['discs'] >= 3 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and (disc_08['loc'] == 2 or disc_08['loc'] == 0) and (disc_07['loc'] == 2 or disc_07['loc'] == 0) and (disc_06['loc'] == 2 or disc_06['loc'] == 0) and (disc_05['loc'] == 2 or disc_05['loc'] == 0) and (disc_04['loc'] == 2 or disc_04['loc'] == 0) and disc_03['loc'] == 3 and  release == True and control["winner"] == False):   
        cont.activate(d03)    
        d03.action = "Pose"
        d03.frameStart = (control["disc_p1"]*2 + 2) 
        d03.frameEnd = (control["disc_p1"]*2 + 2)
        disc_03['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1   
        control["moves"] += 1            
    elif (start == 3 and end == 2 and control['discs'] >= 3 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and (disc_08['loc'] == 1 or disc_08['loc'] == 0) and (disc_07['loc'] == 1 or disc_07['loc'] == 0) and (disc_06['loc'] == 1 or disc_06['loc'] == 0) and (disc_05['loc'] == 1 or disc_05['loc'] == 0) and (disc_04['loc'] == 1 or disc_04['loc'] == 0) and disc_03['loc'] == 3 and  release == True and control["winner"] == False):   
        cont.activate(d03)    
        d03.action = "Pose"
        d03.frameStart = (control["disc_p2"]*2 + 32) 
        d03.frameEnd = (control["disc_p2"]*2 + 32)
        disc_03['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1  
        control["moves"] += 1                
def mover_d02():                                                       
    if (start == 1 and end == 2 and control['discs'] >= 2 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and (disc_08['loc'] == 3 or disc_08['loc'] == 0) and (disc_07['loc'] == 3 or disc_07['loc'] == 0) and (disc_06['loc'] == 3 or disc_06['loc'] == 0) and (disc_05['loc'] == 3 or disc_05['loc'] == 0) and (disc_04['loc'] == 3 or disc_04['loc'] == 0)  and (disc_03['loc'] == 3 or disc_03['loc'] == 0) and disc_02['loc'] == 1 and  release == True and control["winner"] == False):    
        cont.activate(d02)    
        d02.action = "Pose"
        d02.frameStart = (control["disc_p2"]*2 + 32) 
        d02.frameEnd = (control["disc_p2"]*2 + 32)
        disc_02['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1                                               
        control["moves"] += 1                
    elif (start == 1 and end == 3 and control['discs'] >= 2 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and (disc_08['loc'] == 2 or disc_08['loc'] == 0) and (disc_07['loc'] == 2 or disc_07['loc'] == 0) and (disc_06['loc'] == 2 or disc_06['loc'] == 0) and (disc_05['loc'] == 2 or disc_05['loc'] == 0) and (disc_04['loc'] == 2 or disc_04['loc'] == 0)  and (disc_03['loc'] == 2 or disc_03['loc'] == 0) and disc_02['loc'] == 1 and  release == True and control["winner"] == False):  
        cont.activate(d02)    
        d02.action = "Pose"
        d02.frameStart = (control["disc_p3"]*2 + 62) 
        d02.frameEnd = (control["disc_p3"]*2 + 62)
        disc_02['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1      
        control["moves"] += 1                                      
    elif (start == 2 and end == 1 and control['discs'] >= 1 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and (disc_08['loc'] == 3 or disc_08['loc'] == 0) and (disc_07['loc'] == 3 or disc_07['loc'] == 0) and (disc_06['loc'] == 3 or disc_06['loc'] == 0) and (disc_05['loc'] == 3 or disc_05['loc'] == 0) and (disc_04['loc'] == 3 or disc_04['loc'] == 0)  and (disc_03['loc'] == 3 or disc_03['loc'] == 0) and disc_02['loc'] == 2 and  release == True and control["winner"] == False):    
        cont.activate(d02)    
        d02.action = "Pose"
        d02.frameStart = (control["disc_p1"]*2 + 2) 
        d02.frameEnd = (control["disc_p1"]*2 + 2)
        disc_02['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1  
        control["moves"] += 1                                  
    elif (start == 2 and end == 3 and control['discs'] >= 2 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and (disc_08['loc'] == 1 or disc_08['loc'] == 0) and (disc_07['loc'] == 1 or disc_07['loc'] == 0) and (disc_06['loc'] == 1 or disc_06['loc'] == 0) and (disc_05['loc'] == 1 or disc_05['loc'] == 0) and (disc_04['loc'] == 1 or disc_04['loc'] == 0)  and (disc_03['loc'] == 1 or disc_03['loc'] == 0) and disc_02['loc'] == 2 and  release == True and control["winner"] == False):  
        cont.activate(d02)    
        d02.action = "Pose"
        d02.frameStart = (control["disc_p3"]*2 + 62) 
        d02.frameEnd = (control["disc_p3"]*2 + 62)
        disc_02['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1                     
        control["moves"] += 1                              
    elif (start == 3 and end == 1 and control['discs'] >= 2 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and (disc_08['loc'] == 2 or disc_08['loc'] == 0) and (disc_07['loc'] == 2 or disc_07['loc'] == 0) and (disc_06['loc'] == 2 or disc_06['loc'] == 0) and (disc_05['loc'] == 2 or disc_05['loc'] == 0) and (disc_04['loc'] == 2 or disc_04['loc'] == 0)  and (disc_03['loc'] == 2 or disc_03['loc'] == 0) and disc_02['loc'] == 3 and  release == True and control["winner"] == False):    
        cont.activate(d02)    
        d02.action = "Pose"
        d02.frameStart = (control["disc_p1"]*2 + 2) 
        d02.frameEnd = (control["disc_p1"]*2 + 2)
        disc_02['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1   
        control["moves"] += 1                  
    elif (start == 3 and end == 2 and control['discs'] >= 2 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and (disc_08['loc'] == 1 or disc_08['loc'] == 0) and (disc_07['loc'] == 1 or disc_07['loc'] == 0) and (disc_06['loc'] == 1 or disc_06['loc'] == 0) and (disc_05['loc'] == 1 or disc_05['loc'] == 0) and (disc_04['loc'] == 1 or disc_04['loc'] == 0)  and (disc_03['loc'] == 1 or disc_03['loc'] == 0) and disc_02['loc'] == 3 and  release == True and control["winner"] == False):  
        cont.activate(d02)    
        d02.action = "Pose"
        d02.frameStart = (control["disc_p2"]*2 + 32) 
        d02.frameEnd = (control["disc_p2"]*2 + 32)
        disc_02['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1  
        control["moves"] += 1                                     
def mover_d01():
    if (start == 1 and end == 2 and control['discs'] >= 1 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and (disc_08['loc'] == 3 or disc_08['loc'] == 0) and (disc_07['loc'] == 3 or disc_07['loc'] == 0) and (disc_06['loc'] == 3 or disc_06['loc'] == 0) and (disc_05['loc'] == 3 or disc_05['loc'] == 0) and (disc_04['loc'] == 3 or disc_04['loc'] == 0)  and (disc_03['loc'] == 3 or disc_03['loc'] == 0) and (disc_02['loc'] == 3 or disc_02['loc'] == 0) and disc_01['loc'] == 1 and  release == True and control["winner"] == False):   
        cont.activate(d01)    
        d01.action = "Pose"
        d01.frameStart = (control["disc_p2"]*2 + 32) 
        d01.frameEnd = (control["disc_p2"]*2 + 32)
        disc_01['loc'] = 2
        control["disc_p1"] -= 1
        control["disc_p2"] += 1                                               
        control["moves"] += 1                          
    elif (start == 1 and end == 3 and control['discs'] >= 1 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and (disc_08['loc'] == 2 or disc_08['loc'] == 0) and (disc_07['loc'] == 2 or disc_07['loc'] == 0) and (disc_06['loc'] == 2 or disc_06['loc'] == 0) and (disc_05['loc'] == 2 or disc_05['loc'] == 0) and (disc_04['loc'] == 2 or disc_04['loc'] == 0)  and (disc_03['loc'] == 2 or disc_03['loc'] == 0) and (disc_02['loc'] == 2 or disc_02['loc'] == 0) and disc_01['loc'] == 1 and  release == True and control["winner"] == False):   
        cont.activate(d01)    
        d01.action = "Pose"
        d01.frameStart = (control["disc_p3"]*2 + 62) 
        d01.frameEnd = (control["disc_p3"]*2 + 62)
        disc_01['loc'] = 3
        control["disc_p1"] -= 1
        control["disc_p3"] += 1      
        control["moves"] += 1                
    elif (start == 2 and end == 1 and control['discs'] >= 1 and (disc_15['loc'] == 3 or disc_15['loc'] == 0) and (disc_14['loc'] == 3 or disc_14['loc'] == 0) and (disc_13['loc'] == 3 or disc_13['loc'] == 0)  and (disc_12['loc'] == 3 or disc_12['loc'] == 0) and (disc_11['loc'] == 3 or disc_11['loc'] == 0) and (disc_10['loc'] == 3 or disc_10['loc'] == 0) and (disc_09['loc'] == 3 or disc_09['loc'] == 0) and (disc_08['loc'] == 3 or disc_08['loc'] == 0) and (disc_07['loc'] == 3 or disc_07['loc'] == 0) and (disc_06['loc'] == 3 or disc_06['loc'] == 0) and (disc_05['loc'] == 3 or disc_05['loc'] == 0) and (disc_04['loc'] == 3 or disc_04['loc'] == 0)  and (disc_03['loc'] == 3 or disc_03['loc'] == 0) and (disc_02['loc'] == 3 or disc_02['loc'] == 0) and disc_01['loc'] == 2 and  release == True and control["winner"] == False):  
        cont.activate(d01)    
        d01.action = "Pose"
        d01.frameStart = (control["disc_p1"]*2 + 2) 
        d01.frameEnd = (control["disc_p1"]*2 + 2)
        disc_01['loc'] = 1
        control["disc_p2"] -= 1
        control["disc_p1"] += 1  
        control["moves"] += 1                              
    elif (start == 2 and end == 3 and control['discs'] >= 1 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and (disc_08['loc'] == 1 or disc_08['loc'] == 0) and (disc_07['loc'] == 1 or disc_07['loc'] == 0) and (disc_06['loc'] == 1 or disc_06['loc'] == 0) and (disc_05['loc'] == 1 or disc_05['loc'] == 0) and (disc_04['loc'] == 1 or disc_04['loc'] == 0)  and (disc_03['loc'] == 1 or disc_03['loc'] == 0) and (disc_02['loc'] == 1 or disc_02['loc'] == 0) and disc_01['loc'] == 2 and  release == True and control["winner"] == False):    
        cont.activate(d01)    
        d01.action = "Pose"
        d01.frameStart = (control["disc_p3"]*2 + 62) 
        d01.frameEnd = (control["disc_p3"]*2 + 62)
        disc_01['loc'] = 3
        control["disc_p2"] -= 1
        control["disc_p3"] += 1                     
        control["moves"] += 1                                               
    elif (start == 3 and end == 1 and control['discs'] >= 1 and (disc_15['loc'] == 2 or disc_15['loc'] == 0) and (disc_14['loc'] == 2 or disc_14['loc'] == 0) and (disc_13['loc'] == 2 or disc_13['loc'] == 0)  and (disc_12['loc'] == 2 or disc_12['loc'] == 0) and (disc_11['loc'] == 2 or disc_11['loc'] == 0) and (disc_10['loc'] == 2 or disc_10['loc'] == 0) and (disc_09['loc'] == 2 or disc_09['loc'] == 0) and (disc_08['loc'] == 2 or disc_08['loc'] == 0) and (disc_07['loc'] == 2 or disc_07['loc'] == 0) and (disc_06['loc'] == 2 or disc_06['loc'] == 0) and (disc_05['loc'] == 2 or disc_05['loc'] == 0) and (disc_04['loc'] == 2 or disc_04['loc'] == 0)  and (disc_03['loc'] == 2 or disc_03['loc'] == 0) and (disc_02['loc'] == 2 or disc_02['loc'] == 0) and disc_01['loc'] == 3 and  release == True and control["winner"] == False):  
        cont.activate(d01)    
        d01.action = "Pose"
        d01.frameStart = (control["disc_p1"]*2 + 2) 
        d01.frameEnd = (control["disc_p1"]*2 + 2)
        disc_01['loc'] = 1
        control["disc_p3"] -= 1
        control["disc_p1"] += 1   
        control["moves"] += 1                       
    elif (start == 3 and end == 2 and control['discs'] >= 1 and (disc_15['loc'] == 1 or disc_15['loc'] == 0) and (disc_14['loc'] == 1 or disc_14['loc'] == 0) and (disc_13['loc'] == 1 or disc_13['loc'] == 0)  and (disc_12['loc'] == 1 or disc_12['loc'] == 0) and (disc_11['loc'] == 1 or disc_11['loc'] == 0) and (disc_10['loc'] == 1 or disc_10['loc'] == 0) and (disc_09['loc'] == 1 or disc_09['loc'] == 0) and (disc_08['loc'] == 1 or disc_08['loc'] == 0) and (disc_07['loc'] == 1 or disc_07['loc'] == 0) and (disc_06['loc'] == 1 or disc_06['loc'] == 0) and (disc_05['loc'] == 1 or disc_05['loc'] == 0) and (disc_04['loc'] == 1 or disc_04['loc'] == 0)  and (disc_03['loc'] == 1 or disc_03['loc'] == 0) and (disc_02['loc'] == 1 or disc_02['loc'] == 0) and disc_01['loc'] == 3 and  release == True and control["winner"] == False):  
        cont.activate(d01)    
        d01.action = "Pose"
        d01.frameStart = (control["disc_p2"]*2 + 32) 
        d01.frameEnd = (control["disc_p2"]*2 + 32)
        disc_01['loc'] = 2
        control["disc_p3"] -= 1
        control["disc_p2"] += 1    
        control["moves"] += 1                    
def codicoes():
    if release == True:
        control['start'] = 0
        control['end'] = 0   
    if control["discs"] == control["disc_p3"] and control["disc_p3"] > 0:
        control['winner'] = True
        txt_1['Text'] = "Congratulations, you win!"+"\nmoved "+str(control["moves"])+" times"
    else:
        control['winner'] = False
          
def gui():
    txt_1['Text'] = "Movements: " + str(control["moves"])
gui()
inicio()
codicoes()
if control["discs"] == 1:                      
    mover_d01()
elif control["discs"] == 2:         
    mover_d01()
    mover_d02()
elif control["discs"] == 3:
    mover_d01()
    mover_d02()
    mover_d03()
elif control["discs"] == 4:      
    mover_d01()
    mover_d02()
    mover_d03()
    mover_d04()
elif control["discs"] == 5:      
    mover_d01()
    mover_d02()
    mover_d03()
    mover_d04()
    mover_d05()
elif control["discs"] == 6:      
    mover_d01()
    mover_d02()
    mover_d03()
    mover_d04()
    mover_d05()
    mover_d06()
elif control["discs"] == 7:      
    mover_d01()
    mover_d02()
    mover_d03()
    mover_d04()
    mover_d05()
    mover_d06()
    mover_d07()
elif control["discs"] == 8:      
    mover_d01()
    mover_d02()
    mover_d03()
    mover_d04()
    mover_d05()
    mover_d06()
    mover_d07()
    mover_d08()
elif control["discs"] == 9:      
    mover_d01()
    mover_d02()
    mover_d03()
    mover_d04()
    mover_d05()
    mover_d06()
    mover_d07()
    mover_d08()
    mover_d09()
elif control["discs"] == 10:      
    mover_d01()
    mover_d02()
    mover_d03()
    mover_d04()
    mover_d05()
    mover_d06()
    mover_d07()
    mover_d08()
    mover_d09()
    mover_d10()
elif control["discs"] == 11:      
    mover_d01()
    mover_d02()
    mover_d03()
    mover_d04()
    mover_d05()
    mover_d06()
    mover_d07()
    mover_d08()
    mover_d09()
    mover_d10()
    mover_d11()
elif control["discs"] == 12:      
    mover_d01()
    mover_d02()
    mover_d03()
    mover_d04()
    mover_d05()
    mover_d06()
    mover_d07()
    mover_d08()
    mover_d09()
    mover_d10()
    mover_d11()
    mover_d12()
elif control["discs"] == 13:      
    mover_d01()
    mover_d02()
    mover_d03()
    mover_d04()
    mover_d05()
    mover_d06()
    mover_d07()
    mover_d08()
    mover_d09()
    mover_d10()
    mover_d11()
    mover_d12()
    mover_d13()
elif control["discs"] == 14:      
    mover_d01()
    mover_d02()
    mover_d03()
    mover_d04()
    mover_d05()
    mover_d06()
    mover_d07()
    mover_d08()
    mover_d09()
    mover_d10()
    mover_d11()
    mover_d12()
    mover_d13()
    mover_d14()
elif control["discs"] == 15:      
    mover_d01()
    mover_d02()
    mover_d03()
    mover_d04()
    mover_d05()
    mover_d06()
    mover_d07()
    mover_d08()
    mover_d09()
    mover_d10()
    mover_d11()
    mover_d12()
    mover_d13()
    mover_d14()
    mover_d15()
# para saber a localização de start do click
if cont.sensors["mo_area_1"].positive and release == True:
        cont.activate(properties)                    
        properties.propName = "start"
        properties.value = "1"
elif cont.sensors["mo_area_2"].positive and release == True:
        cont.activate(properties)                    
        properties.propName = "start"
        properties.value = "2"
elif cont.sensors["mo_area_3"].positive and release == True:
        cont.activate(properties)                    
        properties.propName = "start"
        properties.value = "3"      
#Para saber o end ao arrastar e soltar
if cont.sensors["mo_area_1"].positive and release == False:
     cont.activate(properties)   
     properties.propName = "end"
     properties.value = "1"
elif cont.sensors["mo_area_2"].positive and release == False: 
     cont.activate(properties)   
     properties.propName = "end"
     properties.value = "2"
elif cont.sensors["mo_area_3"].positive and release == False: 
     cont.activate(properties)   
     properties.propName = "end"
     properties.value = "3"
if cont.sensors["m_release"].positive:   
     cont.activate(m_release)
elif cont.sensors["m_click"].positive:   
     cont.activate(m_click)  
# Configuração do Menu de Escolha da quantidade de discs:
def New_Game():
    control["disc_p2"] = 0  
    control["disc_p3"] = 0  
    control["moves"] = 0    
def DiscsSelect():
    if cont.sensors["mo_sel"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (0) 
            menu_b.frameEnd = (0)
            control["discs"] = 0
            # Agora a borda inferior de realce do select
    elif cont.sensors["mo_m01"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (2) 
            menu_b.frameEnd = (2)
            control["discs"] = 1  
            control["disc_p1"] = 1  
            disc_01['loc'] = 1  
            disc_02['loc'] = 0      
            disc_03['loc'] = 0  
            disc_04['loc'] = 0            
            disc_05['loc'] = 0              
            disc_06['loc'] = 0                          
            disc_07['loc'] = 0                                      
            disc_08['loc'] = 0  
            disc_09['loc'] = 0      
            disc_10['loc'] = 0  
            disc_11['loc'] = 0             
            disc_12['loc'] = 0              
            disc_13['loc'] = 0                          
            disc_14['loc'] = 0  
            disc_15['loc'] = 0      
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (0) 
            d02.frameEnd = (0) 
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (0) 
            d03.frameEnd = (0)
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (0) 
            d04.frameEnd = (0)   
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (0) 
            d05.frameEnd = (0)   
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (0) 
            d06.frameEnd = (0) 
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (0) 
            d07.frameEnd = (0) 
            cont.activate(d08) 
            d08.action = "Pose"                        
            d08.frameStart = (0) 
            d08.frameEnd = (0) 
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (0) 
            d09.frameEnd = (0)  
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (0) 
            d10.frameEnd = (0)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart = (0) 
            d11.frameEnd = (0) 
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (0) 
            d12.frameEnd = (0)  
            d13.action = "Pose"
            d13.frameStart = (0)
            d13.frameEnd = (0)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (0)
            d14.frameEnd = (0)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (0)
            d15.frameEnd = (0)            
            New_Game()       
    elif cont.sensors["mo_m02"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (3) 
            menu_b.frameEnd = (3)        
            control["discs"] = 2    
            control["disc_p1"] = 2  
            disc_01['loc'] = 1  
            disc_02['loc'] = 1      
            disc_03['loc'] = 0  
            disc_04['loc'] = 0            
            disc_05['loc'] = 0              
            disc_06['loc'] = 0                          
            disc_07['loc'] = 0                                      
            disc_08['loc'] = 0  
            disc_09['loc'] = 0      
            disc_10['loc'] = 0  
            disc_11['loc'] = 0             
            disc_12['loc'] = 0              
            disc_13['loc'] = 0                          
            disc_14['loc'] = 0  
            disc_15['loc'] = 0      
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (4) 
            d02.frameEnd = (4) 
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (0) 
            d03.frameEnd = (0)
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (0) 
            d04.frameEnd = (0)   
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (0) 
            d05.frameEnd = (0)   
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (0) 
            d06.frameEnd = (0) 
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (0) 
            d07.frameEnd = (0) 
            cont.activate(d08) 
            d08.action = "Pose"                        
            d08.frameStart = (0) 
            d08.frameEnd = (0) 
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (0) 
            d09.frameEnd = (0)  
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (0) 
            d10.frameEnd = (0)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart =(0)
            d11.frameEnd = (0) 
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (0) 
            d12.frameEnd = (0)  
            d13.action = "Pose"
            d13.frameStart = (0)
            d13.frameEnd = (0)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (0)
            d14.frameEnd = (0)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (0)
            d15.frameEnd = (0)                                                 
            New_Game()                           
    elif cont.sensors["mo_m03"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (4) 
            menu_b.frameEnd = (4)
            control["discs"] = 3    
            control["disc_p1"] = 3  
            disc_01['loc'] = 1  
            disc_02['loc'] = 1      
            disc_03['loc'] = 1  
            disc_04['loc'] = 0             
            disc_05['loc'] = 0              
            disc_06['loc'] = 0                          
            disc_07['loc'] = 0                                      
            disc_08['loc'] = 0  
            disc_09['loc'] = 0      
            disc_10['loc'] = 0  
            disc_11['loc'] = 0             
            disc_12['loc'] = 0              
            disc_13['loc'] = 0                          
            disc_14['loc'] = 0  
            disc_15['loc'] = 0  
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (4) 
            d02.frameEnd = (4)             
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (6) 
            d03.frameEnd = (6)
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (0) 
            d04.frameEnd = (0)   
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (0) 
            d05.frameEnd = (0)   
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (0) 
            d06.frameEnd = (0) 
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (0) 
            d07.frameEnd = (0) 
            cont.activate(d08) 
            d08.action = "Pose"                        
            d08.frameStart = (0) 
            d08.frameEnd = (0) 
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (0) 
            d09.frameEnd = (0)  
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (0) 
            d10.frameEnd = (0)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart =(0)
            d11.frameEnd = (0) 
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (0) 
            d12.frameEnd = (0)  
            d13.action = "Pose"
            d13.frameStart = (0)
            d13.frameEnd = (0)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (0)
            d14.frameEnd = (0)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (0)
            d15.frameEnd = (0)                         
            New_Game()  
    elif cont.sensors["mo_m04"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (5) 
            menu_b.frameEnd = (5)
            control["discs"] = 4    
            control["disc_p1"] = 4 
            disc_01['loc'] = 1  
            disc_02['loc'] = 1      
            disc_03['loc'] = 1  
            disc_04['loc'] = 1             
            disc_05['loc'] = 0              
            disc_06['loc'] = 0                          
            disc_07['loc'] = 0                                      
            disc_08['loc'] = 0  
            disc_09['loc'] = 0      
            disc_10['loc'] = 0  
            disc_11['loc'] = 0             
            disc_12['loc'] = 0              
            disc_13['loc'] = 0                          
            disc_14['loc'] = 0  
            disc_15['loc'] = 0             
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (4) 
            d02.frameEnd = (4)             
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (6) 
            d03.frameEnd = (6) 
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (8) 
            d04.frameEnd = (8)   
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (0) 
            d05.frameEnd = (0)   
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (0) 
            d06.frameEnd = (0) 
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (0) 
            d07.frameEnd = (0) 
            cont.activate(d08) 
            d08.action = "Pose"                        
            d08.frameStart = (0) 
            d08.frameEnd = (0) 
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (0) 
            d09.frameEnd = (0)  
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (0) 
            d10.frameEnd = (0)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart =(0)
            d11.frameEnd = (0) 
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (0) 
            d12.frameEnd = (0)  
            d13.action = "Pose"
            d13.frameStart = (0)
            d13.frameEnd = (0)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (0)
            d14.frameEnd = (0)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (0)
            d15.frameEnd = (0)                                  
            New_Game()                    
    elif cont.sensors["mo_m05"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (6) 
            menu_b.frameEnd = (6)
            control["discs"] = 5           
            control["disc_p1"] = 5 
            disc_01['loc'] = 1  
            disc_02['loc'] = 1      
            disc_03['loc'] = 1  
            disc_04['loc'] = 1             
            disc_05['loc'] = 1              
            disc_06['loc'] = 0                          
            disc_07['loc'] = 0                                      
            disc_08['loc'] = 0  
            disc_09['loc'] = 0      
            disc_10['loc'] = 0  
            disc_11['loc'] = 0             
            disc_12['loc'] = 0              
            disc_13['loc'] = 0                          
            disc_14['loc'] = 0  
            disc_15['loc'] = 0              
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (4) 
            d02.frameEnd = (4)             
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (6) 
            d03.frameEnd = (6) 
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (8) 
            d04.frameEnd = (8) 
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (10) 
            d05.frameEnd = (10)   
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (0) 
            d06.frameEnd = (0) 
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (0) 
            d07.frameEnd = (0) 
            cont.activate(d08) 
            d08.action = "Pose"                        
            d08.frameStart = (0) 
            d08.frameEnd = (0) 
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (0) 
            d09.frameEnd = (0)  
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (0) 
            d10.frameEnd = (0)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart =(0)
            d11.frameEnd = (0) 
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (0) 
            d12.frameEnd = (0)  
            d13.action = "Pose"
            d13.frameStart = (0)
            d13.frameEnd = (0)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (0)
            d14.frameEnd = (0)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (0)
            d15.frameEnd = (0)                                              
            New_Game()                    
    elif cont.sensors["mo_m06"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (7) 
            menu_b.frameEnd = (7)
            control["discs"] = 6   
            control["disc_p1"] = 6 
            disc_01['loc'] = 1  
            disc_02['loc'] = 1      
            disc_03['loc'] = 1  
            disc_04['loc'] = 1             
            disc_05['loc'] = 1              
            disc_06['loc'] = 1                          
            disc_07['loc'] = 0                                      
            disc_08['loc'] = 0  
            disc_09['loc'] = 0      
            disc_10['loc'] = 0  
            disc_11['loc'] = 0             
            disc_12['loc'] = 0              
            disc_13['loc'] = 0                          
            disc_14['loc'] = 0  
            disc_15['loc'] = 0                           
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (4) 
            d02.frameEnd = (4)             
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (6) 
            d03.frameEnd = (6) 
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (8) 
            d04.frameEnd = (8) 
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (10) 
            d05.frameEnd = (10) 
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (12) 
            d06.frameEnd = (12) 
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (0) 
            d07.frameEnd = (0) 
            cont.activate(d08) 
            d08.action = "Pose"                        
            d08.frameStart = (0) 
            d08.frameEnd = (0) 
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (0) 
            d09.frameEnd = (0)  
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (0) 
            d10.frameEnd = (0)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart =(0)
            d11.frameEnd = (0) 
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (0) 
            d12.frameEnd = (0)  
            d13.action = "Pose"
            d13.frameStart = (0)
            d13.frameEnd = (0)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (0)
            d14.frameEnd = (0)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (0)
            d15.frameEnd = (0)                                                            
            New_Game()                    
    elif cont.sensors["mo_m07"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (8) 
            menu_b.frameEnd = (8)
            control["discs"] = 7 
            control["disc_p1"] = 7 
            disc_01['loc'] = 1  
            disc_02['loc'] = 1      
            disc_03['loc'] = 1  
            disc_04['loc'] = 1             
            disc_05['loc'] = 1              
            disc_06['loc'] = 1                          
            disc_07['loc'] = 1                                      
            disc_08['loc'] = 0  
            disc_09['loc'] = 0      
            disc_10['loc'] = 0  
            disc_11['loc'] = 0             
            disc_12['loc'] = 0              
            disc_13['loc'] = 0                          
            disc_14['loc'] = 0  
            disc_15['loc'] = 0                                      
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (4) 
            d02.frameEnd = (4)             
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (6) 
            d03.frameEnd = (6) 
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (8) 
            d04.frameEnd = (8) 
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (10) 
            d05.frameEnd = (10) 
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (12) 
            d06.frameEnd = (12)  
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (14) 
            d07.frameEnd = (14) 
            cont.activate(d08) 
            d08.action = "Pose"                        
            d08.frameStart = (0) 
            d08.frameEnd = (0) 
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (0) 
            d09.frameEnd = (0)  
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (0) 
            d10.frameEnd = (0)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart =(0)
            d11.frameEnd = (0) 
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (0) 
            d12.frameEnd = (0)  
            d13.action = "Pose"
            d13.frameStart = (0)
            d13.frameEnd = (0)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (0)
            d14.frameEnd = (0)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (0)
            d15.frameEnd = (0)                                                                      
            New_Game()                               
    elif cont.sensors["mo_m08"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (9) 
            menu_b.frameEnd = (9)
            control["discs"] = 8  
            control["disc_p1"] = 8 
            disc_01['loc'] = 1  
            disc_02['loc'] = 1      
            disc_03['loc'] = 1  
            disc_04['loc'] = 1             
            disc_05['loc'] = 1              
            disc_06['loc'] = 1                          
            disc_07['loc'] = 1                                      
            disc_08['loc'] = 1  
            disc_09['loc'] = 0      
            disc_10['loc'] = 0  
            disc_11['loc'] = 0             
            disc_12['loc'] = 0              
            disc_13['loc'] = 0                          
            disc_14['loc'] = 0  
            disc_15['loc'] = 0                                                 
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (4) 
            d02.frameEnd = (4)             
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (6) 
            d03.frameEnd = (6) 
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (8) 
            d04.frameEnd = (8) 
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (10) 
            d05.frameEnd = (10) 
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (12) 
            d06.frameEnd = (12)  
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (14) 
            d07.frameEnd = (14) 
            cont.activate(d08)    
            d08.action = "Pose"
            d08.frameStart = (16) 
            d08.frameEnd = (16) 
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (0) 
            d09.frameEnd = (0)  
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (0) 
            d10.frameEnd = (0)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart =(0)
            d11.frameEnd = (0) 
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (0) 
            d12.frameEnd = (0)  
            d13.action = "Pose"
            d13.frameStart = (0)
            d13.frameEnd = (0)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (0)
            d14.frameEnd = (0)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (0)
            d15.frameEnd = (0)                                                                                   
            New_Game()                            
    elif cont.sensors["mo_m09"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (10) 
            menu_b.frameEnd = (10)
            control["discs"] = 9
            control["disc_p1"] = 9
            disc_01['loc'] = 1  
            disc_02['loc'] = 1      
            disc_03['loc'] = 1  
            disc_04['loc'] = 1             
            disc_05['loc'] = 1              
            disc_06['loc'] = 1                          
            disc_07['loc'] = 1                                      
            disc_08['loc'] = 1 
            disc_09['loc'] = 1      
            disc_10['loc'] = 0 
            disc_11['loc'] = 0             
            disc_12['loc'] = 0              
            disc_13['loc'] = 0                          
            disc_14['loc'] = 0  
            disc_15['loc'] = 0
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (4) 
            d02.frameEnd = (4)             
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (6) 
            d03.frameEnd = (6) 
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (8) 
            d04.frameEnd = (8) 
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (10) 
            d05.frameEnd = (10) 
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (12) 
            d06.frameEnd = (12)  
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (14) 
            d07.frameEnd = (14) 
            cont.activate(d08)    
            d08.action = "Pose"
            d08.frameStart = (16) 
            d08.frameEnd = (16)  
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (18) 
            d09.frameEnd = (18)  
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (0) 
            d10.frameEnd = (0)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart =(0)
            d11.frameEnd = (0) 
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (0) 
            d12.frameEnd = (0)  
            d13.action = "Pose"
            d13.frameStart = (0)
            d13.frameEnd = (0)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (0)
            d14.frameEnd = (0)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (0)
            d15.frameEnd = (0)                                                                                      
            New_Game()                    
    elif cont.sensors["mo_m10"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (11) 
            menu_b.frameEnd = (11)
            control["discs"] = 10
            control["disc_p1"] =10
            disc_01['loc'] = 1  
            disc_02['loc'] = 1      
            disc_03['loc'] = 1  
            disc_04['loc'] = 1             
            disc_05['loc'] = 1              
            disc_06['loc'] = 1                          
            disc_07['loc'] = 1                                      
            disc_08['loc'] = 1 
            disc_09['loc'] = 1      
            disc_10['loc'] = 1  
            disc_11['loc'] = 0            
            disc_12['loc'] = 0              
            disc_13['loc'] = 0                          
            disc_14['loc'] = 0  
            disc_15['loc'] = 0       
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (4) 
            d02.frameEnd = (4)             
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (6) 
            d03.frameEnd = (6) 
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (8) 
            d04.frameEnd = (8) 
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (10) 
            d05.frameEnd = (10) 
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (12) 
            d06.frameEnd = (12)  
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (14) 
            d07.frameEnd = (14) 
            cont.activate(d08)    
            d08.action = "Pose"
            d08.frameStart = (16) 
            d08.frameEnd = (16)  
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (18) 
            d09.frameEnd = (18)
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (20) 
            d10.frameEnd = (20)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart =(0)
            d11.frameEnd = (0) 
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (0) 
            d12.frameEnd = (0)  
            d13.action = "Pose"
            d13.frameStart = (0)
            d13.frameEnd = (0)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (0)
            d14.frameEnd = (0)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (0)
            d15.frameEnd = (0)             
            New_Game()
    elif cont.sensors["mo_m11"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (12) 
            menu_b.frameEnd = (12)        
            control["discs"] = 11   
            control["disc_p1"] =11
            disc_01['loc'] = 1  
            disc_02['loc'] = 1      
            disc_03['loc'] = 1  
            disc_04['loc'] = 1             
            disc_05['loc'] = 1              
            disc_06['loc'] = 1                          
            disc_07['loc'] = 1                                      
            disc_08['loc'] = 1 
            disc_09['loc'] = 1      
            disc_10['loc'] = 1  
            disc_11['loc'] = 1             
            disc_12['loc'] = 0             
            disc_13['loc'] = 0                          
            disc_14['loc'] = 0  
            disc_15['loc'] = 0 
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (4) 
            d02.frameEnd = (4)             
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (6) 
            d03.frameEnd = (6) 
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (8) 
            d04.frameEnd = (8) 
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (10) 
            d05.frameEnd = (10) 
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (12) 
            d06.frameEnd = (12)  
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (14) 
            d07.frameEnd = (14) 
            cont.activate(d08)    
            d08.action = "Pose"
            d08.frameStart = (16) 
            d08.frameEnd = (16)  
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (18) 
            d09.frameEnd = (18)
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (20) 
            d10.frameEnd = (20)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart = (22) 
            d11.frameEnd = (22) 
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (0) 
            d12.frameEnd = (0)  
            d13.action = "Pose"
            d13.frameStart = (0)
            d13.frameEnd = (0)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (0)
            d14.frameEnd = (0)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (0)
            d15.frameEnd = (0)                        
            New_Game()            
    elif cont.sensors["mo_m12"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (13) 
            menu_b.frameEnd = (13)
            control["discs"] = 12   
            control["disc_p1"] =12
            disc_01['loc'] = 1  
            disc_02['loc'] = 1      
            disc_03['loc'] = 1  
            disc_04['loc'] = 1             
            disc_05['loc'] = 1              
            disc_06['loc'] = 1                          
            disc_07['loc'] = 1                                      
            disc_08['loc'] = 1 
            disc_09['loc'] = 1      
            disc_10['loc'] = 1  
            disc_11['loc'] = 1             
            disc_12['loc'] = 1              
            disc_13['loc'] = 0                          
            disc_14['loc'] = 0  
            disc_15['loc'] = 0             
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (4) 
            d02.frameEnd = (4)             
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (6) 
            d03.frameEnd = (6) 
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (8) 
            d04.frameEnd = (8) 
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (10) 
            d05.frameEnd = (10) 
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (12) 
            d06.frameEnd = (12)  
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (14) 
            d07.frameEnd = (14) 
            cont.activate(d08)    
            d08.action = "Pose"
            d08.frameStart = (16) 
            d08.frameEnd = (16)  
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (18) 
            d09.frameEnd = (18)
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (20) 
            d10.frameEnd = (20)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart = (22) 
            d11.frameEnd = (22)    
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (24) 
            d12.frameEnd = (24)  
            d13.action = "Pose"
            d13.frameStart = (0)
            d13.frameEnd = (0)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (0)
            d14.frameEnd = (0)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (0)
            d15.frameEnd = (0)                                           
            New_Game()            
    elif cont.sensors["mo_m13"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (14) 
            menu_b.frameEnd = (14)
            control["discs"] = 13   
            control["disc_p1"] =13
            disc_01['loc'] = 1  
            disc_02['loc'] = 1      
            disc_03['loc'] = 1  
            disc_04['loc'] = 1             
            disc_05['loc'] = 1              
            disc_06['loc'] = 1                          
            disc_07['loc'] = 1                                      
            disc_08['loc'] = 1 
            disc_09['loc'] = 1      
            disc_10['loc'] = 1  
            disc_11['loc'] = 1             
            disc_12['loc'] = 1              
            disc_13['loc'] = 1                          
            disc_14['loc'] = 0  
            disc_15['loc'] = 0            
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (4) 
            d02.frameEnd = (4)             
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (6) 
            d03.frameEnd = (6) 
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (8) 
            d04.frameEnd = (8) 
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (10) 
            d05.frameEnd = (10) 
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (12) 
            d06.frameEnd = (12)  
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (14) 
            d07.frameEnd = (14) 
            cont.activate(d08)    
            d08.action = "Pose"
            d08.frameStart = (16) 
            d08.frameEnd = (16)  
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (18) 
            d09.frameEnd = (18)
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (20) 
            d10.frameEnd = (20)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart = (22) 
            d11.frameEnd = (22)    
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (24) 
            d12.frameEnd = (24)
            cont.activate(d13)    
            d13.action = "Pose"
            d13.frameStart = (26)
            d13.frameEnd = (26)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (0)
            d14.frameEnd = (0)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (0)
            d15.frameEnd = (0)             
            New_Game()                    
    elif cont.sensors["mo_m14"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (15) 
            menu_b.frameEnd = (15)
            control["discs"] = 14   
            control["disc_p1"] =14
            disc_01['loc'] = 1
            disc_02['loc'] = 1
            disc_03['loc'] = 1
            disc_04['loc'] = 1
            disc_05['loc'] = 1
            disc_06['loc'] = 1
            disc_07['loc'] = 1
            disc_08['loc'] = 1
            disc_09['loc'] = 1
            disc_10['loc'] = 1
            disc_11['loc'] = 1
            disc_12['loc'] = 1            
            disc_13['loc'] = 1
            disc_14['loc'] = 1            
            disc_15['loc'] = 0
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (4) 
            d02.frameEnd = (4)             
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (6) 
            d03.frameEnd = (6) 
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (8) 
            d04.frameEnd = (8) 
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (10) 
            d05.frameEnd = (10) 
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (12) 
            d06.frameEnd = (12)  
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (14) 
            d07.frameEnd = (14) 
            cont.activate(d08)    
            d08.action = "Pose"
            d08.frameStart = (16) 
            d08.frameEnd = (16)  
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (18) 
            d09.frameEnd = (18)
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (20) 
            d10.frameEnd = (20)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart = (22) 
            d11.frameEnd = (22)    
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (24) 
            d12.frameEnd = (24)
            cont.activate(d13)    
            d13.action = "Pose"
            d13.frameStart = (26)
            d13.frameEnd = (26)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (28)
            d14.frameEnd = (28)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (0)
            d15.frameEnd = (0)                          
            New_Game()                    
    elif cont.sensors["mo_m15"].positive:
        if cont.sensors["m_click"].positive:
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (16) 
            menu_b.frameEnd = (16)
            control["discs"] = 15 
            control["disc_p1"] =15
            disc_01['loc'] = 1
            disc_02['loc'] = 1
            disc_03['loc'] = 1
            disc_04['loc'] = 1
            disc_05['loc'] = 1
            disc_06['loc'] = 1
            disc_07['loc'] = 1
            disc_08['loc'] = 1
            disc_09['loc'] = 1
            disc_10['loc'] = 1
            disc_11['loc'] = 1
            disc_12['loc'] = 1            
            disc_13['loc'] = 1
            disc_14['loc'] = 1            
            disc_15['loc'] = 1                        
            cont.activate(d01)    
            d01.action = "Pose"
            d01.frameStart = (2) 
            d01.frameEnd = (2) 
            cont.activate(d02)    
            d02.action = "Pose"
            d02.frameStart = (4) 
            d02.frameEnd = (4)             
            cont.activate(d03)    
            d03.action = "Pose"
            d03.frameStart = (6) 
            d03.frameEnd = (6) 
            cont.activate(d04)    
            d04.action = "Pose"
            d04.frameStart = (8) 
            d04.frameEnd = (8) 
            cont.activate(d05)    
            d05.action = "Pose"
            d05.frameStart = (10) 
            d05.frameEnd = (10) 
            cont.activate(d06)    
            d06.action = "Pose"
            d06.frameStart = (12) 
            d06.frameEnd = (12)  
            cont.activate(d07)    
            d07.action = "Pose"
            d07.frameStart = (14) 
            d07.frameEnd = (14) 
            cont.activate(d08)    
            d08.action = "Pose"
            d08.frameStart = (16) 
            d08.frameEnd = (16)  
            cont.activate(d09)    
            d09.action = "Pose"
            d09.frameStart = (18) 
            d09.frameEnd = (18)
            cont.activate(d10)    
            d10.action = "Pose"
            d10.frameStart = (20) 
            d10.frameEnd = (20)
            cont.activate(d11)    
            d11.action = "Pose"
            d11.frameStart = (22) 
            d11.frameEnd = (22)    
            cont.activate(d12)    
            d12.action = "Pose"
            d12.frameStart = (24) 
            d12.frameEnd = (24)
            cont.activate(d13)    
            d13.action = "Pose"
            d13.frameStart = (26)
            d13.frameEnd = (26)
            cont.activate(d14)    
            d14.action = "Pose"
            d14.frameStart = (28)
            d14.frameEnd = (28)
            cont.activate(d15)    
            d15.action = "Pose"
            d15.frameStart = (30)
            d15.frameEnd = (30)                        
            New_Game()                    
def ShowMenu():    
    if (cont.sensors["mo_sel"].positive or cont.sensors["mo_m01"].positive or cont.sensors["mo_m02"].positive or cont.sensors["mo_m03"].positive or cont.sensors["mo_m04"].positive or cont.sensors["mo_m05"].positive or cont.sensors["mo_m06"].positive or cont.sensors["mo_m07"].positive or cont.sensors["mo_m09"].positive or cont.sensors["mo_m10"].positive or cont.sensors["mo_m11"].positive or cont.sensors["mo_m12"].positive or cont.sensors["mo_m13"].positive or cont.sensors["mo_m14"].positive or cont.sensors["mo_m15"].positive) and (cont.sensors["m_click"].positive):
            cont.activate(menu_b)    
            menu_b.action = "pose_Menu"
            menu_b.frameStart = (0) 
            menu_b.frameEnd = (0) 
def starter_game():
    while (control['initial'] == False):
        cont.activate(menu_b)    
        menu_b.action = "pose_Menu"
        menu_b.frameStart = (8) 
        menu_b.frameEnd = (8)
        control["discs"] = 7 
        control["disc_p1"] = 7 
        disc_01['loc'] = 1  
        disc_02['loc'] = 1      
        disc_03['loc'] = 1  
        disc_04['loc'] = 1             
        disc_05['loc'] = 1              
        disc_06['loc'] = 1                          
        disc_07['loc'] = 1                                      
        disc_08['loc'] = 0  
        disc_09['loc'] = 0      
        disc_10['loc'] = 0  
        disc_11['loc'] = 0             
        disc_12['loc'] = 0              
        disc_13['loc'] = 0                          
        disc_14['loc'] = 0  
        disc_15['loc'] = 0  
        cont.activate(d01)    
        d01.action = "Pose"
        d01.frameStart = (2) 
        d01.frameEnd = (2) 
        cont.activate(d02)    
        d02.action = "Pose"
        d02.frameStart = (4) 
        d02.frameEnd = (4)             
        cont.activate(d03)    
        d03.action = "Pose"
        d03.frameStart = (6) 
        d03.frameEnd = (6) 
        cont.activate(d04)    
        d04.action = "Pose"
        d04.frameStart = (8) 
        d04.frameEnd = (8) 
        cont.activate(d05)    
        d05.action = "Pose"
        d05.frameStart = (10) 
        d05.frameEnd = (10) 
        cont.activate(d06)    
        d06.action = "Pose"
        d06.frameStart = (12) 
        d06.frameEnd = (12)  
        cont.activate(d07)    
        d07.action = "Pose"
        d07.frameStart = (14) 
        d07.frameEnd = (14) 
        cont.activate(d08) 
        d08.action = "Pose"                        
        d08.frameStart = (0) 
        d08.frameEnd = (0) 
        cont.activate(d09)    
        d09.action = "Pose"
        d09.frameStart = (0) 
        d09.frameEnd = (0)  
        cont.activate(d10)    
        d10.action = "Pose"
        d10.frameStart = (0) 
        d10.frameEnd = (0)
        cont.activate(d11)    
        d11.action = "Pose"
        d11.frameStart =(0)
        d11.frameEnd = (0) 
        cont.activate(d12)    
        d12.action = "Pose"
        d12.frameStart = (0) 
        d12.frameEnd = (0)  
        d13.action = "Pose"
        d13.frameStart = (0)
        d13.frameEnd = (0)
        cont.activate(d14)    
        d14.action = "Pose"
        d14.frameStart = (0)
        d14.frameEnd = (0)
        cont.activate(d15)    
        d15.action = "Pose"
        d15.frameStart = (0)
        d15.frameEnd = (0)                                                                      
        New_Game() 
        control['initial'] = True 
        
  
ShowMenu()    
DiscsSelect()
starter_game()  