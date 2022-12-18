import pyautogui as auto

import time
loc = 100,870
loc2 = 500, 50
loc3= 550,140
loc4= 400,300
loc5= 500,530
loc6= 500,650

def move_click(loc_x,loc_y,num,time_wait):
    auto.moveTo(loc_x,loc_y)
    auto.click(clicks=num)
    time.sleep(time_wait)

def search(site,key,time_wait):
    auto.typewrite(site)
    auto.press(key)
    time.sleep(time_wait)
def press(key,time_wait):
    auto.press(key)
    time.sleep(time_wait)

move_click(loc[0],loc[1],1,2)
move_click(loc2[0],loc2[1],2,1)
search("youtube.com","enter",5)
move_click(loc3[0],loc3[1],2,0)
search('pycharm tutorial','enter',5)
move_click(loc4[0],loc4[1],1,5)
press('F',3)
press('K',1)
press('esc',3)
move_click(loc5[0],loc5[1],2,2)
press('F',3)
press('K',2)
press('esc',5)
move_click(loc6[0],loc6[1],1,0)












