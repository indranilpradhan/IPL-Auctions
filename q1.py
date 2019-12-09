#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open('ipl_auctions_dataset.txt') as f:
    z = f.readlines()
z.sort(reverse = True,key = lambda x:x.split(':')[3])


# In[2]:


teams =  ["mi", "csk", "dc", "srh", "kkr", "kxip", "rr", "rcb"]
from random import choice
mi = []
csk = []
dc = []
srh = []
kkr = []
kxip = []
rr = []
rcb = []
tot_count = 0


# In[3]:


team_mi = {'ar':0,'bat':0,'bow':0,'wk':0,'ov':0, 'tot':0}
team_csk = {'ar':0,'bat':0,'bow':0,'wk':0,'ov':0,'tot':0}
team_dc = {'ar':0,'bat':0,'bow':0,'wk':0,'ov':0,'tot':0}
team_srh = {'ar':0,'bat':0,'bow':0,'wk':0,'ov':0,'tot':0}
team_kkr = {'ar':0,'bat':0,'bow':0,'wk':0,'ov':0,'tot':0}
team_kxip = {'ar':0,'bat':0,'bow':0,'wk':0,'ov':0,'tot':0}
team_rr = {'ar':0,'bat':0,'bow':0,'wk':0,'ov':0,'tot':0}
team_rcb = {'ar':0,'bat':0,'bow':0,'wk':0,'ov':0,'tot':0}


# In[4]:


a = []
l = []
for i in z:
    t = i.split(':')[0]
    if t not in l:
        a.append(i)
        l.append(t)
with open('sorted_ipl_auctions_dataset.txt','w') as f:
    for i in a:
        f.write(i)


# In[5]:


while tot_count < 144:
    for i in a:
        x = choice(teams)
        t = i.split(':')[1]
        u = i.split(':')[2]
        if x == "mi":
            if t == "India":
                if u == "Batsman" and team_mi['bat'] < 7 and team_mi['tot'] < 18:
                    team_mi['bat'] += 1
                    team_mi['tot'] += 1
                    tot_count += 1
                    mi.append(i)
                elif u == "Bowler" and team_mi['bow'] < 6 and team_mi['tot'] < 18:
                    team_mi['bow'] += 1
                    team_mi['tot'] += 1
                    tot_count += 1
                    mi.append(i)
                elif u == "All-Rounder" and team_mi['ar'] < 4 and team_mi['tot'] < 18:
                    team_mi['ar'] += 1
                    team_mi['tot'] += 1
                    tot_count += 1
                    mi.append(i)
                elif u == "Wicket Keeper" and team_mi['wk'] < 2 and team_mi['tot'] < 18:
                    team_mi['wk'] += 1
                    team_mi['tot'] += 1
                    tot_count += 1
                    mi.append(i)
            else:
                if u == "Batsman" and team_mi['bat'] < 7 and team_mi['ov'] < 7 and team_mi['tot'] < 18:
                    team_mi['bat'] += 1
                    team_mi['tot'] += 1
                    team_mi['ov']+=1
                    tot_count += 1
                    mi.append(i)
                elif u == "Bowler" and team_mi['bow'] < 6 and team_mi['ov'] < 7 and team_mi['tot'] < 18:
                    team_mi['bow'] += 1
                    team_mi['tot'] += 1
                    team_mi['ov']+=1
                    tot_count += 1
                    mi.append(i)
                elif u == "All-Rounder" and team_mi['ar'] < 4 and team_mi['ov'] < 7 and team_mi['tot'] < 18:
                    team_mi['ar'] += 1
                    team_mi['tot'] += 1
                    team_mi['ov']+=1
                    tot_count += 1
                    mi.append(i)
                elif u == "Wicket Keeper" and team_mi['wk'] < 2 and team_mi['ov'] < 7 and team_mi['tot'] < 18:
                    team_mi['wk'] += 1
                    team_mi['tot'] += 1
                    team_mi['ov']+=1
                    tot_count += 1
                    mi.append(i)
        elif x == "csk":
            if t == "India":
                if u == "Batsman" and team_csk['bat'] < 7 and team_csk['tot'] < 18:
                    team_csk['bat'] += 1
                    team_csk['tot'] += 1
                    tot_count += 1
                    csk.append(i)
                elif u == "Bowler" and team_csk['bow'] < 6 and team_csk['tot'] < 18:
                    team_csk['bow'] += 1
                    team_csk['tot'] += 1
                    tot_count += 1
                    csk.append(i)
                elif u == "All-Rounder" and team_csk['ar'] < 4 and team_csk['tot'] < 18:
                    team_csk['ar'] += 1
                    team_csk['tot'] += 1
                    tot_count += 1
                    csk.append(i)
                elif u == "Wicket Keeper" and team_csk['wk'] < 2 and team_csk['tot'] < 18:
                    team_csk['wk'] += 1
                    team_csk['tot'] += 1
                    tot_count += 1
                    csk.append(i)
            else:
                if u == "Batsman" and team_csk['bat'] < 7 and team_csk['ov'] < 7 and team_csk['tot'] < 18:
                    team_csk['bat'] += 1
                    team_csk['tot'] += 1
                    team_csk['ov']+=1
                    tot_count += 1
                    csk.append(i)
                elif u == "Bowler" and team_csk['bow'] < 6 and team_csk['ov'] < 7 and team_csk['tot'] < 18:
                    team_csk['bow'] += 1
                    team_csk['tot'] += 1
                    team_csk['ov']+=1
                    tot_count += 1
                    csk.append(i)
                elif u == "All-Rounder" and team_csk['ar'] < 4 and team_csk['ov'] < 7 and team_csk['tot'] < 18:
                    team_csk['ar'] += 1
                    team_csk['tot'] += 1
                    team_csk['ov']+=1
                    tot_count += 1
                    csk.append(i)
                elif u == "Wicket Keeper" and team_csk['wk'] < 2 and team_csk['ov'] < 7 and team_csk['tot'] < 18:
                    team_csk['wk'] += 1
                    team_csk['tot'] += 1
                    team_csk['ov']+=1
                    tot_count += 1
                    csk.append(i)
        elif x == "dc":
            if t == "India":
                if u == "Batsman" and team_dc['bat'] < 7 and team_dc['tot'] < 18:
                    team_dc['bat'] += 1
                    team_dc['tot'] += 1
                    tot_count += 1
                    dc.append(i)
                elif u == "Bowler" and team_dc['bow'] < 6 and team_dc['tot'] < 18:
                    team_dc['bow'] += 1
                    team_dc['tot'] += 1
                    tot_count += 1
                    dc.append(i)
                elif u == "All-Rounder" and team_dc['ar'] < 4 and team_dc['tot'] < 18:
                    team_dc['ar'] += 1
                    team_dc['tot'] += 1
                    tot_count += 1
                    dc.append(i)
                elif u == "Wicket Keeper" and team_dc['wk'] < 2 and team_dc['tot'] < 18:
                    team_dc['wk'] += 1
                    team_dc['tot'] += 1
                    tot_count += 1
                    dc.append(i)
            else:
                if u == "Batsman" and team_dc['bat'] < 7 and team_dc['ov'] < 7 and team_dc['tot'] < 18:
                    team_dc['bat'] += 1
                    team_dc['tot'] += 1
                    team_dc['ov']+=1
                    tot_count += 1
                    dc.append(i)
                elif u == "Bowler" and team_dc['bow'] < 6 and team_dc['ov'] < 7 and team_dc['tot'] < 18:
                    team_dc['bow'] += 1
                    team_dc['tot'] += 1
                    team_dc['ov']+=1
                    tot_count += 1
                    dc.append(i)
                elif u == "All-Rounder" and team_dc['ar'] < 4 and team_dc['ov'] < 7 and team_dc['tot'] < 18:
                    team_dc['ar'] += 1
                    team_dc['tot'] += 1
                    team_dc['ov']+=1
                    tot_count += 1
                    dc.append(i)
                elif u == "Wicket Keeper" and team_dc['wk'] < 2 and team_dc['ov'] < 7 and team_dc['tot'] < 18:
                    team_dc['wk'] += 1
                    team_dc['tot'] += 1
                    team_dc['ov']+=1
                    tot_count += 1
                    dc.append(i)
        elif x == "srh":
            if t == "India":
                if u == "Batsman" and team_srh['bat'] < 7 and team_srh['tot'] < 18:
                    team_srh['bat'] += 1
                    team_srh['tot'] += 1
                    tot_count += 1
                    srh.append(i)
                elif u == "Bowler" and team_srh['bow'] < 6 and team_srh['tot'] < 18:
                    team_srh['bow'] += 1
                    team_srh['tot'] += 1
                    tot_count += 1
                    srh.append(i)
                elif u == "All-Rounder" and team_srh['ar'] < 4 and team_srh['tot'] < 18:
                    team_srh['ar'] += 1
                    team_srh['tot'] += 1
                    tot_count += 1
                    srh.append(i)
                elif u == "Wicket Keeper" and team_srh['wk'] < 2 and team_srh['tot'] < 18:
                    team_srh['wk'] += 1
                    team_srh['tot'] += 1
                    tot_count += 1
                    srh.append(i)
            else:
                if u == "Batsman" and team_srh['bat'] < 7 and team_srh['ov'] < 7 and team_srh['tot'] < 18:
                    team_srh['bat'] += 1
                    team_srh['tot'] += 1
                    team_srh['ov']+=1
                    tot_count += 1
                    srh.append(i)
                elif u == "Bowler" and team_srh['bow'] < 6 and team_srh['ov'] < 7 and team_srh['tot'] < 18:
                    team_srh['bow'] += 1
                    team_srh['tot'] += 1
                    team_srh['ov']+=1
                    tot_count += 1
                    srh.append(i)
                elif u == "All-Rounder" and team_srh['ar'] < 4 and team_srh['ov'] < 7 and team_srh['tot'] < 18:
                    team_srh['ar'] += 1
                    team_srh['tot'] += 1
                    team_srh['ov']+=1
                    tot_count += 1
                    srh.append(i)
                elif u == "Wicket Keeper" and team_srh['wk'] < 2 and team_srh['ov'] < 7 and team_srh['tot'] < 18:
                    team_srh['wk'] += 1
                    team_srh['tot'] += 1
                    team_srh['ov']+=1
                    tot_count += 1
                    srh.append(i)
        elif x == "kkr":
            if t == "India":
                if u == "Batsman" and team_kkr['bat'] < 7 and team_kkr['tot'] < 18:
                    team_kkr['bat'] += 1
                    team_kkr['tot'] += 1
                    tot_count += 1
                    kkr.append(i)
                elif u == "Bowler" and team_kkr['bow'] < 6 and team_kkr['tot'] < 18:
                    team_kkr['bow'] += 1
                    team_kkr['tot'] += 1
                    tot_count += 1
                    kkr.append(i)
                elif u == "All-Rounder" and team_kkr['ar'] < 4 and team_kkr['tot'] < 18:
                    team_kkr['ar'] += 1
                    team_kkr['tot'] += 1
                    tot_count += 1
                    kkr.append(i)
                elif u == "Wicket Keeper" and team_kkr['wk'] < 2 and team_kkr['tot'] < 18:
                    team_kkr['wk'] += 1
                    team_kkr['tot'] += 1
                    tot_count += 1
                    kkr.append(i)
            else:
                if u == "Batsman" and team_kkr['bat'] < 7 and team_kkr['ov'] < 7 and team_kkr['tot'] < 18:
                    team_kkr['bat'] += 1
                    team_kkr['tot'] += 1
                    team_kkr['ov']+=1
                    tot_count += 1
                    kkr.append(i)
                elif u == "Bowler" and team_kkr['bow'] < 6 and team_kkr['ov'] < 7 and team_kkr['tot'] < 18:
                    team_kkr['bow'] += 1
                    team_kkr['tot'] += 1
                    team_kkr['ov']+=1
                    tot_count += 1
                    kkr.append(i)
                elif u == "All-Rounder" and team_kkr['ar'] < 4 and team_kkr['ov'] < 7 and team_kkr['tot'] < 18:
                    team_kkr['ar'] += 1
                    team_kkr['tot'] += 1
                    team_kkr['ov']+=1
                    tot_count += 1
                    kkr.append(i)
                elif u == "Wicket Keeper" and team_kkr['wk'] < 2 and team_kkr['ov'] < 7 and team_kkr['tot'] < 18:
                    team_kkr['wk'] += 1
                    team_kkr['tot'] += 1
                    team_kkr['ov']+=1
                    tot_count += 1
                    kkr.append(i)
        elif x == "kxip":
            if t == "India":
                if u == "Batsman" and team_kxip['bat'] < 7 and team_kxip['tot'] < 18:
                    team_kxip['bat'] += 1
                    team_kxip['tot'] += 1
                    tot_count += 1
                    kxip.append(i)
                elif u == "Bowler" and team_kxip['bow'] < 6 and team_kxip['tot'] < 18:
                    team_kxip['bow'] += 1
                    team_kxip['tot'] += 1
                    tot_count += 1
                    kxip.append(i)
                elif u == "All-Rounder" and team_kxip['ar'] < 4 and team_kxip['tot'] < 18:
                    team_kxip['ar'] += 1
                    team_kxip['tot'] += 1
                    tot_count += 1
                    kxip.append(i)
                elif u == "Wicket Keeper" and team_kxip['wk'] < 2 and team_kxip['tot'] < 18:
                    team_kxip['wk'] += 1
                    team_kxip['tot'] += 1
                    tot_count += 1
                    kxip.append(i)
            else:
                if u == "Batsman" and team_kxip['bat'] < 7 and team_kxip['ov'] < 7 and team_kxip['tot'] < 18:
                    team_kxip['bat'] += 1
                    team_kxip['tot'] += 1
                    team_kxip['ov']+=1
                    tot_count += 1
                    kxip.append(i)
                elif u == "Bowler" and team_kxip['bow'] < 6 and team_kxip['ov'] < 7 and team_kxip['tot'] < 18:
                    team_kxip['bow'] += 1
                    team_kxip['tot'] += 1
                    team_kxip['ov']+=1
                    tot_count += 1
                    kxip.append(i)
                elif u == "All-Rounder" and team_kxip['ar'] < 4 and team_kxip['ov'] < 7 and team_kxip['tot'] < 18:
                    team_kxip['ar'] += 1
                    team_kxip['tot'] += 1
                    team_kxip['ov']+=1
                    tot_count += 1
                    kxip.append(i)
                elif u == "Wicket Keeper" and team_kxip['wk'] < 2 and team_kxip['ov'] < 7 and team_kxip['tot'] < 18:
                    team_kxip['wk'] += 1
                    team_kxip['tot'] += 1
                    team_kxip['ov']+=1
                    tot_count += 1
                    kxip.append(i)
        if x == "rr":
            if t == "India":
                if u == "Batsman" and team_rr['bat'] < 7 and team_rr['tot'] < 18:
                    team_rr['bat'] += 1
                    team_rr['tot'] += 1
                    tot_count += 1
                    rr.append(i)
                elif u == "Bowler" and team_rr['bow'] < 6 and team_rr['tot'] < 18:
                    team_rr['bow'] += 1
                    team_rr['tot'] += 1
                    tot_count += 1
                    rr.append(i)
                elif u == "All-Rounder" and team_rr['ar'] < 4 and team_rr['tot'] < 18:
                    team_rr['ar'] += 1
                    team_rr['tot'] += 1
                    tot_count += 1
                    rr.append(i)
                elif u == "Wicket Keeper" and team_rr['wk'] < 2 and team_rr['tot'] < 18:
                    team_rr['wk'] += 1
                    team_rr['tot'] += 1
                    tot_count += 1
                    rr.append(i)
            else:
                if u == "Batsman" and team_rr['bat'] < 7 and team_rr['ov'] < 7 and team_rr['tot'] < 18:
                    team_rr['bat'] += 1
                    team_rr['tot'] += 1
                    team_rr['ov']+=1
                    tot_count += 1
                    rr.append(i)
                elif u == "Bowler" and team_rr['bow'] < 6 and team_rr['ov'] < 7 and team_rr['tot'] < 18:
                    team_rr['bow'] += 1
                    team_rr['tot'] += 1
                    team_rr['ov']+=1
                    tot_count += 1
                    rr.append(i)
                elif u == "All-Rounder" and team_rr['ar'] < 4 and team_rr['ov'] < 7 and team_rr['tot'] < 18:
                    team_rr['ar'] += 1
                    team_rr['tot'] += 1
                    team_rr['ov']+=1
                    tot_count += 1
                    rr.append(i)
                elif u == "Wicket Keeper" and team_rr['wk'] < 2 and team_rr['ov'] < 7 and team_rr['tot'] < 18:
                    team_rr['wk'] += 1
                    team_rr['tot'] += 1
                    team_rr['ov']+=1
                    tot_count += 1
                    rr.append(i)
        if x == "rcb":
            if t == "India":
                if u == "Batsman" and team_rcb['bat'] < 7 and team_rcb['tot'] < 18:
                    team_rcb['bat'] += 1
                    team_rcb['tot'] += 1
                    tot_count += 1
                    rcb.append(i)
                elif u == "Bowler" and team_rcb['bow'] < 6 and team_rcb['tot'] < 18:
                    team_rcb['bow'] += 1
                    team_rcb['tot'] += 1
                    tot_count += 1
                    rcb.append(i)
                elif u == "All-Rounder" and team_rcb['ar'] < 4 and team_rcb['tot'] < 18:
                    team_rcb['ar'] += 1
                    team_rcb['tot'] += 1
                    tot_count += 1
                    rcb.append(i)
                elif u == "Wicket Keeper" and team_rcb['wk'] < 2 and team_rcb['tot'] < 18:
                    team_rcb['wk'] += 1
                    team_rcb['tot'] += 1
                    tot_count += 1
                    rcb.append(i)
            else:
                if u == "Batsman" and team_rcb['bat'] < 7 and team_rcb['ov'] < 7 and team_rcb['tot'] < 18:
                    team_rcb['bat'] += 1
                    team_rcb['tot'] += 1
                    team_rcb['ov']+=1
                    tot_count += 1
                    rcb.append(i)
                elif u == "Bowler" and team_rcb['bow'] < 6 and team_rcb['ov'] < 7 and team_rcb['tot'] < 18:
                    team_rcb['bow'] += 1
                    team_rcb['tot'] += 1
                    team_rcb['ov']+=1
                    tot_count += 1
                    rcb.append(i)
                elif u == "All-Rounder" and team_rcb['ar'] < 4 and team_rcb['ov'] < 7 and team_rcb['tot'] < 18:
                    team_rcb['ar'] += 1
                    team_rcb['tot'] += 1
                    team_rcb['ov']+=1
                    tot_count += 1
                    rcb.append(i)
                elif u == "Wicket Keeper" and team_rcb['wk'] < 2 and team_rcb['ov'] < 7 and team_rcb['tot'] < 18:
                    team_rcb['wk'] += 1
                    team_rcb['tot'] += 1
                    team_rcb['ov']+=1
                    tot_count += 1
                    rcb.append(i)


# In[6]:


with open('mi.txt','w') as f:
    j = 1
    f.write("Team : Mumbai Indians"+"\n")
    f.write("\n")
    for i in mi:
        q =[x for x in i.split(":")]
        f.write("Player " + str(j) + "\n")
        f.write("Name:" + q[0]+"\n")
        f.write("country:" + q[1]+"\n")
        f.write("Ability:" + q[2]+"\n")
        f.write("Fees:" + q[3]+"\n")
        j += 1
with open('csk.txt','w') as f:
    j = 1
    f.write("Team : Chennai Super Kings"+"\n")
    f.write("\n")
    for i in csk:
        q =[x for x in i.split(":")]
        f.write("Player " + str(j) + "\n")
        f.write("Name:" + q[0]+"\n")
        f.write("country:" + q[1]+"\n")
        f.write("Ability:" + q[2]+"\n")
        f.write("Fees:" + q[3]+"\n")
        j += 1
with open('dc.txt','w') as f:
    j = 1
    f.write("Team : Delhi Capitals"+"\n")
    f.write("\n")
    for i in dc:
        q =[x for x in i.split(":")]
        f.write("Player " + str(j) + "\n")
        f.write("Name:" + q[0]+"\n")
        f.write("country:" + q[1]+"\n")
        f.write("Ability:" + q[2]+"\n")
        f.write("Fees:" + q[3]+"\n")
        j += 1
with open('srh.txt','w') as f:
    j = 1
    f.write("Team : Sun Risers Hyderabad"+"\n")
    f.write("\n")
    for i in srh:
        q =[x for x in i.split(":")]
        f.write("Player " + str(j) + "\n")
        f.write("Name:" + q[0]+"\n")
        f.write("country:" + q[1]+"\n")
        f.write("Ability:" + q[2]+"\n")
        f.write("Fees:" + q[3]+"\n")
        j += 1
with open('kkr.txt','w') as f:
    j = 1
    f.write("Team : Kolkata Knight Riders"+"\n")
    f.write("\n")
    for i in kkr:
        q =[x for x in i.split(":")]
        f.write("Player " + str(j) + "\n")
        f.write("Name:" + q[0]+"\n")
        f.write("country:" + q[1]+"\n")
        f.write("Ability:" + q[2]+"\n")
        f.write("Fees:" + q[3]+"\n")
        j += 1
with open('kxip.txt','w') as f:
    j = 1
    f.write("Team : Kings XI Punjab"+"\n")
    f.write("\n")
    for i in kxip:
        q =[x for x in i.split(":")]
        f.write("Player " + str(j) + "\n")
        f.write("Name:" + q[0]+"\n")
        f.write("country:" + q[1]+"\n")
        f.write("Ability:" + q[2]+"\n")
        f.write("Fees:" + q[3]+"\n")
        j += 1
with open('rr.txt','w') as f:
    j = 1
    f.write("Team : Rajasthan Royals"+"\n")
    f.write("\n")
    for i in rr:
        q =[x for x in i.split(":")]
        f.write("Player " + str(j) + "\n")
        f.write("Name:" + q[0]+"\n")
        f.write("country:" + q[1]+"\n")
        f.write("Ability:" + q[2]+"\n")
        f.write("Fees:" + q[3]+"\n")
        j += 1
with open('rcb.txt','w') as f:
    j = 1
    f.write("Team : Royal Challengers Bangalore"+"\n")
    f.write("\n")
    for i in rcb:
        q =[x for x in i.split(":")]
        f.write("Player " + str(j) + "\n")
        f.write("Name:" + q[0]+"\n")
        f.write("country:" + q[1]+"\n")
        f.write("Ability:" + q[2]+"\n")
        f.write("Fees:" + q[3]+"\n")
        j += 1


# In[7]:


print(team_mi)
print(team_csk)
print(team_dc)
print(team_srh)
print(team_kkr)
print(team_kxip)
print(team_rr)
print(team_rcb)

