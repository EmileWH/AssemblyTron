import os
import pandas
import shutil

from tkinter import filedialog
from tkinter import *

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global name
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)
    name = filename

root = Tk()
root.geometry("800x800")
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=0, column=3)



mainloop()




#name = 'JAB-j5__20210603140838kG6Y-Synthetic-GFP-IAA'

os.getcwd()

def walk_up_folder(path, depth=1):
    _cur_depth = 1        
    while _cur_depth < depth:
        path = os.path.dirname(path)
        _cur_depth += 1
    return path   

paths = pandas.read_csv(walk_up_folder(os.getcwd(), 2)+'\paths.csv')
paths

shutil.copy2(name+'/assembly.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
shutil.copy2(name+'/combinations.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
#shutil.copy2(name+'/digests.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
shutil.copy2(name+'/oligo.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
shutil.copy2(name+'/pcr.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')

oligos = pandas.read_csv('oligo.csv')
oligos

#digests = pandas.read_csv('digests.csv')
#digests

pcr = pandas.read_csv('pcr.csv')
pcr

combinations = pandas.read_csv('combinations.csv')
combinations


######################################################################################################3
#make instructions file
e2slot = {}
e2slot['0'] = 'A1'
e2slot['1'] = 'A2'
e2slot['2'] = 'A3'
e2slot['3'] = 'A4'
e2slot['4'] = 'A5'
e2slot['5'] = 'A6'
e2slot['6'] = 'B1'
e2slot['7'] = 'B2'
e2slot['8'] = 'B3'
e2slot['9'] = 'B4'
e2slot['10'] = 'B5'
e2slot['11'] = 'B6'
e2slot['12'] = 'C1'
e2slot['13'] = 'C2'
e2slot['14'] = 'C3'
e2slot['15'] = 'C4'
e2slot['16'] = 'C5'
e2slot['17'] = 'C6'
e2slot['18'] = 'D1'
e2slot['19'] = 'D2'
e2slot['20'] = 'D3'
e2slot['21'] = 'D4'
e2slot['22'] = 'D5'
e2slot['23'] = 'D6'
    

def main():
    f = open('pcr_instructions.txt','w+')
    f.write('Place the coldtuberack in slot 1. \r\n')
    f.write('put 300uL tips in slot 6 & 9, and 10uL tips in slot 5. \r\n')
    f.write('put in a fresh pcr plate into thermocycler. \r\n')

    f.write('Instructions for setting up the coldtuberack: \r\n')
    for i, row in oligos.iterrows():
        f.write('Put '+oligos.loc[i].at['Name']+' in '+e2slot[str(oligos.loc[i].at['ID Number'])]+'\r\n')
    f.close()
    
    Nextslot = len(oligos["ID Number"])
    
    # No digest in this protocol
    # f = open('Golden_Gate_instructions.txt','a+')
    # for i, row in digests.iterrows():
    #     f.write('Put '+digests.loc[i].at['Sequence Source']+' in '+e2slot[str(Nextslot)]+'\r\n')
    #     Nextslot = Nextslot+1
    # f.close()
    
    #Nextslot2 = Nextslot + len(digests["Sequence Source"])-1
    
    f = open('pcr_instructions.txt','a+')
    for i, row in pcr.iterrows():
        
        if i > 0:
            if pcr.loc[i].at['Primary Template'] == pcr.loc[i-1].at['Primary Template']:
                Nextslot = Nextslot
            else:
                Nextslot = Nextslot+1
    
        
        
        f.write('Put '+pcr.loc[i].at['Primary Template']+' in '+e2slot[str(Nextslot)]+'\r\n')
        
   
    #f.write('Place empty tube in C4 for the T4/BSA mix \r\n')
    
    #f.write('Place T4 ligase in C5 \r\n')

    #f.write('Place 100X BSA in C6 \r\n')
    
    #f.write('Place T4 buffer in D2 \r\n')
    #f.write('Place DPNI in D3 \r\n')
    #f.write('Place cutsmart buffer in D4 \r\n')
    #f.write('Place BsaI in D5 \r\n')
    f.write('Place Q5 DNA polymerase in D6 \r\n')
    
    
    totaltubes= Nextslot + len(pcr['Primary Template'])
    
    f.write('Place 24 well tuberack in slot 2. Add '+str(totaltubes)+' empty 1.5 mL tubes to the rack in the same positions. \r\n')
    
    
    
    #numfinaltubes = len(combinations['ID Number'])
    #f.write('Place '+str(numfinaltubes)+' tubes in row C of 24 tuberack in slot 2. Start from D6 and go to D'+str(6-numfinaltubes+1)+' \r\n')

    f.close()

if __name__== "__main__":
    main()

os.system("notepad.exe pcr_instructions.txt")

# def main():
#     f = open('Golden_Gate_instructions.txt','w+')
#     f.write('Place the coldtuberack in slot 1. \r\n')
#     f.write('put 300uL tips in slot 6 & 9, and 10uL tips in slot 5. \r\n')
#     f.write('put in a fresh pcr plate into thermocycler. \r\n')

#     f.write('Instructions for setting up the coldtuberack: \r\n')
#     for i, row in oligos.iterrows():
#         f.write('Put '+oligos.loc[i].at['Name']+' in '+e2slot[str(oligos.loc[i].at['ID Number'])]+'\r\n')
#     f.close()
    
#     Nextslot = len(oligos["ID Number"])
    
#     f = open('Golden_Gate_instructions.txt','a+')
#     for i, row in digests.iterrows():
#         f.write('Put '+digests.loc[i].at['Sequence Source']+' in '+e2slot[str(Nextslot)]+'\r\n')
#         Nextslot = Nextslot+1
#     f.close()
    
#     Nextslot2 = Nextslot + len(digests["Sequence Source"])-1
    
#     f = open('Golden_Gate_instructions.txt','a+')
#     for i, row in pcr.iterrows():
#         f.write('Put '+pcr.loc[i].at['Primary Template']+' in '+e2slot[str(Nextslot2)]+'\r\n')
#         Nextslot2 = Nextslot2+1
    
#     f.write('Place empty tube in C4 for the T4/BSA mix \r\n')
    
#     f.write('Place T4 ligase in C5 \r\n')

#     f.write('Place 100X BSA in C6 \r\n')
    
#     f.write('Place T4 buffer in D2 \r\n')
#     f.write('Place DPNI in D3 \r\n')
#     f.write('Place cutsmart buffer in D4 \r\n')
#     f.write('Place BsaI in D5 \r\n')
#     f.write('Place Q5 DNA polymerase in D6 \r\n')
    
    
#     totaltubes= Nextslot2 + len(pcr['Primary Template'])
    
#     f.write('Place 24 well tuberack in slot 2. Add '+str(totaltubes)+' empty 1.5 mL tubes to the rack in the same positions. \r\n')
    
    
    
#     numfinaltubes = len(combinations['ID Number'])
#     f.write('Place '+str(numfinaltubes)+' tubes in row C of 24 tuberack in slot 2. Start from D6 and go to D'+str(6-numfinaltubes+1)+' \r\n')

#     f.close()


    
    
# if __name__== "__main__":
#     main()

# os.system("notepad.exe Golden_Gate_instructions.txt")


import tkinter as tk
import csv
import pandas as pd
from datetime import date
import os
import shutil

today = date.today()

date = str(today.strftime('%Y%m%d'))
date

#make the run folder of the day
os.chdir(paths.loc[0].at['opentrons_repo']+'/pcr/')
os.mkdir(date+'_pcr')

#copy the temp GoldenGate.py to the new folder
#dst = '/'+date+'GoldenGate'
shutil.copy2(paths.loc[0].at['opentrons_repo']+'/pcr/pcr_nodigests_separatepcrruns.py', paths.loc[0].at['opentrons_repo']+'/pcr/'+date+'_pcr/')

#now rename the script with the date
os.chdir(paths.loc[0].at['opentrons_repo']+'/pcr/'+date+'_pcr')
os.rename('pcr_nodigests_separatepcrruns.py', date+'_pcr.py')
os.chdir(walk_up_folder(os.getcwd(), 2))

#shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/digests.csv',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+'_GoldenGate/')
shutil.move(paths.loc[0].at['opentrons_repo']+'/pcr/combinations.csv',paths.loc[0].at['opentrons_repo']+'/pcr/'+date+'_pcr/')
shutil.move(paths.loc[0].at['opentrons_repo']+'/pcr/pcr.csv',paths.loc[0].at['opentrons_repo']+'/pcr/'+date+'_pcr/')
shutil.move(paths.loc[0].at['opentrons_repo']+'/pcr/assembly.csv',paths.loc[0].at['opentrons_repo']+'/pcr/'+date+'_pcr/')
shutil.move(paths.loc[0].at['opentrons_repo']+'/pcr/oligo.csv',paths.loc[0].at['opentrons_repo']+'/pcr/'+date+'_pcr/')
shutil.move(paths.loc[0].at['opentrons_repo']+'/pcr/pcr_instructions.txt',paths.loc[0].at['opentrons_repo']+'/pcr/'+date+'_pcr/')


###############################################################################################################################################################################################3
#tkinter window

from tkinter import *

input_csv = tk.Tk()
input_csv.geometry('1920x1080')
input_csv.title('Parameters for pcr')
    
def set_variables():
    global stkprm
    global stkvol
    global dilprm
    global primerconc
    global pcrvol
    global templatengs
    global Q5
    global DPNI
    global DPwater
    global cutsmart
    global Date
    global ngdesired
    # global pwldigesttemp
    # global concdigesttemp
    
    global extra1value
    global extra1name
    global extra2value
    global extra2name
    
    global temppwl1
    global temppwl2
    global temppwl3
    global temppwl4
    global temppwl5
    global temppwl6
    global conc1
    global conc2
    global conc3
    global conc4
    global conc5
    global conc6
    stkprm = float(stkprm_entry.get())
    stkvol = float(stkvol_entry.get())
    dilprm = float(dilprm_entry.get())
    primerconc = float(primerconc_entry.get())
    pcrvol = float(pcrvol_entry.get())
    templatengs = float(templatengs_entry.get())
    Q5 = float(Q5_entry.get())
    DPNI = float(DPNI_entry.get())
    DPwater = float(DPwater_entry.get())
    cutsmart = float(cutsmart_entry.get())
    Date = Date_entry.get()
    ngdesired = float(ngdesired_entry.get())
    # pwldigesttemp = float(pwldigesttemp_entry.get())
    # concdigesttemp = float(concdigesttemp_entry.get())
    
    extra1value = float(extra1value_entry.get())
    extra1name = str(extra1name_entry.get())
    extra2value = float(extra2value_entry.get())
    extra2name = str(extra2name_entry.get())


    
    if temppwl1_entry.get() == '':
        temppwl1 = ''
    else:
        temppwl1 = int(temppwl1_entry.get())
    
    if temppwl2_entry.get() == '':
        temppwl2 = ''
    else:
        temppwl2 = int(temppwl2_entry.get())
    
    if temppwl3_entry.get() == '':
        temppwl3 = ''
    else:
        temppwl3 = int(temppwl3_entry.get())
    
    if temppwl4_entry.get() == '':
        temppwl4 = ''
    else:
        temppwl4 = int(temppwl4_entry.get())
    
    if temppwl5_entry.get() == '':
        temppwl5 = ''
    else:
        temppwl5 = int(temppwl5_entry.get())
    
    if temppwl6_entry.get() == '':
        temppwl6 = ''
    else:
        temppwl6 = int(temppwl6_entry.get())
        
        
    
    if conc1_entry.get() == '':
        conc1 = ''
    else:
        conc1 = float(conc1_entry.get())
    
    if conc2_entry.get() == '':
        conc2 = ''
    else:
        conc2 = float(conc2_entry.get())
    
    if conc3_entry.get() == '':
        conc3 = ''
    else:
        conc3 = float(conc3_entry.get())
    
    if conc4_entry.get() == '':
        conc4 = ''
    else:
        conc4 = float(conc4_entry.get())
    
    if conc5_entry.get() == '':
        conc5 = ''
    else:
        conc5 = float(conc5_entry.get())
    
    if conc6_entry.get() == '':
        conc6 = ''
    else:
        conc6 = float(conc6_entry.get())
    
    
    input_csv.destroy()

label_stkprm = tk.Label(text='stkprm',font=('Helvatical bold',14))
label_stkprm.place(relx=0,rely=0.04)

label_stkvol = tk.Label(text='stkvol',font=('Helvatical bold',14))
label_stkvol.place(relx=0,rely=0.07)

label_dilprm = tk.Label(text='dilprm',font=('Helvatical bold',14))
label_dilprm.place(relx=0,rely=0.095)

label_primerconc = tk.Label(text='primerconc',font=('Helvatical bold',14))
label_primerconc.place(relx=0,rely=0.12)

label_pcrvol = tk.Label(text='pcrvol',font=('Helvatical bold',14))
label_pcrvol.place(relx=0,rely=0.145)

label_templatengs = tk.Label(text='templatengs',font=('Helvatical bold',14))
label_templatengs.place(relx=0,rely=0.17)

label_Q5 = tk.Label(text='Q5',font=('Helvatical bold',14))
label_Q5.place(relx=0,rely=0.2)

label_DNP1 = tk.Label(text='DNP1',font=('Helvatical bold',14))
label_DNP1.place(relx=0,rely=0.225)

label_water = tk.Label(text='water',font=('Helvatical bold',14))
label_water.place(relx=0,rely=0.25)

label_Cutsmart = tk.Label(text='cutsmart',font=('Helvatical bold',14))
label_Cutsmart.place(relx=0,rely=0.275)

label_Date = tk.Label(text='date',font=('Helvatical bold',14))
label_Date.place(relx=0,rely=0.3)

label_ngdesired = tk.Label(text='ngdesired',font=('Helvatical bold',14))
label_ngdesired.place(relx=0,rely=0.325)

# label_pwldigesttemp = tk.Label(text='pwldigesttemp',font=('Helvatical bold',14))
# label_pwldigesttemp.place(relx=0,rely=0.35)

# label_concdigesttemp = tk.Label(text='concdigesttemp',font=('Helvatical bold',14))
# label_concdigesttemp.place(relx=0,rely=0.375)

label_extra1 = tk.Label(text='extra1',font=('Helvatical bold',14))
label_extra1.place(relx=0,rely=0.425)

label_extra2 = tk.Label(text='extra2',font=('Helvatical bold',14))
label_extra2.place(relx=0,rely=0.45)

label2 = tk.Label(text="Template pwl",font=('Helvatical bold',12))
label2.place(relx=0.3,rely=0)

label3 = tk.Label(text="Temp conc",font=('Helvatical bold',12))
label3.place(relx=0.4,rely=0.)

#Text Entries

stkprm_entry = tk.Entry()
stkprm_entry.insert(END, '100')
stkprm_entry.place(relx=0.1,rely=0.05,width=35)

stkvol_entry = tk.Entry()
stkvol_entry.insert(END, '1')
stkvol_entry.place(relx=0.1,rely=0.075,width=35)

dilprm_entry = tk.Entry()
dilprm_entry.insert(END, '2.5')
dilprm_entry.place(relx=0.1,rely=0.1,width=35)

primerconc_entry = tk.Entry()
primerconc_entry.insert(END, '0.1')
primerconc_entry.place(relx=0.1,rely=0.125,width=35)

pcrvol_entry = tk.Entry()
pcrvol_entry.insert(END, '25')
pcrvol_entry.place(relx=0.1,rely=0.15,width=35)

templatengs_entry = tk.Entry()
templatengs_entry.insert(END, '0.5')
templatengs_entry.place(relx=0.1,rely=0.175,width=35)

Q5_entry = tk.Entry()
Q5_entry.insert(END, '0')
Q5_entry.place(relx=0.1,rely=0.2,width=35)

DPNI_entry = tk.Entry()
DPNI_entry.insert(END, '1')
DPNI_entry.place(relx=0.1,rely=0.225,width=35)

DPwater_entry = tk.Entry()
DPwater_entry.insert(END, '19')
DPwater_entry.place(relx=0.1,rely=0.250,width=35)

cutsmart_entry = tk.Entry()
cutsmart_entry.insert(END, '5')
cutsmart_entry.place(relx=0.1,rely=0.275,width=35)

Date_entry = tk.Entry()
Date_entry.insert(END, date)
Date_entry.place(relx=0.1,rely=0.3,width=55)

ngdesired_entry = tk.Entry()
ngdesired_entry.insert(END, '100')
ngdesired_entry.place(relx=0.1,rely=0.325,width=35)

# pwldigesttemp_entry = tk.Entry()
# pwldigesttemp_entry.insert(END, '0')
# pwldigesttemp_entry.place(relx=0.1,rely=0.35,width=35)

# concdigesttemp_entry = tk.Entry()
# concdigesttemp_entry.insert(END, '0')
# concdigesttemp_entry.place(relx=0.1,rely=0.375,width=35)

extra1name_entry = tk.Entry()
extra1name_entry.insert(END, 'variable')
extra1name_entry.place(relx=0.1,rely=0.425,width=50)

extra2name_entry = tk.Entry()
extra2name_entry.insert(END, 'variable')
extra2name_entry.place(relx=0.1,rely=0.45,width=50)

extra1value_entry = tk.Entry()
extra1value_entry.insert(END, '0')
extra1value_entry.place(relx=0.15,rely=0.425,width=35)

extra2value_entry = tk.Entry()
extra2value_entry.insert(END, '0')
extra2value_entry.place(relx=0.15,rely=0.45,width=35)

########################################################################################
#entries for pwl number

temppwl1_entry = tk.Entry()
temppwl1_entry.insert(END, '0')
temppwl1_entry.place(relx=0.3,rely=0.05,width = 35)

temppwl2_entry = tk.Entry()
temppwl2_entry.insert(END, '0')
temppwl2_entry.place(relx=0.3,rely=0.1,width = 35)

temppwl3_entry = tk.Entry()
temppwl3_entry.insert(END, '0')
temppwl3_entry.place(relx=0.3,rely=0.15,width = 35)

temppwl4_entry = tk.Entry()
temppwl4_entry.insert(END, '0')
temppwl4_entry.place(relx=0.3,rely=0.2,width = 35)

temppwl5_entry = tk.Entry()
temppwl5_entry.insert(END, '0')
temppwl5_entry.place(relx=0.3,rely=0.25,width = 35)

temppwl6_entry = tk.Entry()
temppwl6_entry.insert(END, '0')
temppwl6_entry.place(relx=0.3,rely=0.3,width = 35)

#########################################################################################3
#entries for concentration
conc1_entry= tk.Entry()
conc1_entry.insert(END, '0')
conc1_entry.place(relx=0.4,rely=0.05,width = 35)

conc2_entry = tk.Entry()
conc2_entry.insert(END, '0')
conc2_entry.place(relx=0.4,rely=0.1,width = 35)

conc3_entry = tk.Entry()
conc3_entry.insert(END, '0')
conc3_entry.place(relx=0.4,rely=0.15,width = 35)

conc4_entry = tk.Entry()
conc4_entry.insert(END, '0')
conc4_entry.place(relx=0.4,rely=0.2,width = 35)

conc5_entry = tk.Entry()
conc5_entry.insert(END, '0')
conc5_entry.place(relx=0.4,rely=0.25,width = 35)

conc6_entry = tk.Entry()
conc6_entry.insert(END, '0')
conc6_entry.place(relx=0.4,rely=0.3,width = 35)

################################################################
#Legend

legend1 = tk.Label(text = "stkprm - concentration of the stock primer you are adding")
legend1.place(relx=0.1,rely=0.5)

legend2 = tk.Label(text = "stkvol - the volume of stock primer you are adding")
legend2.place(relx=0.1,rely=0.525)

legend3 = tk.Label(text = "dilprm - this is the concentration in uM that you want your working dilution to be")
legend3.place(relx=0.1,rely=0.55)

legend4 = tk.Label(text = "primerconc - this is the concentration you want each primer to be in the pcr reaction")
legend4.place(relx=0.1,rely=0.575)

legend5 = tk.Label(text = "pcrvol - this is the total volume of your pcr reaction")
legend5.place(relx=0.1,rely=0.6)

legend6 = tk.Label(text = "templatengs - this is the concentration of template you want in your pcr rxn in ng/uL")
legend6.place(relx=0.1,rely=0.625)

legend7 = tk.Label(text = "Q5 - How much Q5 to add")
legend7.place(relx=0.1,rely=0.65)

legend8 = tk.Label(text = "DPNI - How much DPNI to add")
legend8.place(relx=0.1,rely=0.675)

legend9 = tk.Label(text = "DPwater - How much water goes in your DPNI digestion")
legend9.place(relx=0.1,rely=0.7)

legend10 = tk.Label(text = "cutsmart - How much cutsmart goes in your DPNI digestion")
legend10.place(relx=0.1,rely=0.725)

legend11 = tk.Label(text = "date - Todays date")
legend11.place(relx=0.1,rely=0.75)

legend12 = tk.Label(text = "ngdesired - nanograms desired for reaction")
legend12.place(relx=0.1,rely=0.775)

legend13 = tk.Label(text = "pwldigesttemp - temperature for plasmid restriction enzyme digestion")
legend13.place(relx=0.1,rely=0.8)

legend14 = tk.Label(text = "concdigesttemp - concentration for plasmid digestion")
legend14.place(relx=0.1,rely=0.825)

legend15 = tk.Label(text = "For the extra variables, input the name of the new variable and then the value. Don't change the value from 0 if you don't need to.")
legend15.place(relx=0.1,rely=0.875)

confirm_button = tk.Button(text="Confirm",command=set_variables)
confirm_button.place(relx=0.8,rely=0.8)


input_csv.mainloop()


temppwls = [temppwl1,temppwl2,temppwl3,temppwl4,temppwl5,temppwl6]
tempconcs = [conc1,conc2,conc3,conc4,conc5,conc6]
test = [[0,0,0,0,0,0,0,0,0,0,0,0]]


row = [[stkprm,stkvol,dilprm,primerconc,pcrvol,templatengs,Q5,DPNI,DPwater,cutsmart,Date,ngdesired]]
variables = pd.DataFrame(test,columns=['stkprm','stkvol','dilprm','primerconc','pcrvol','templatengs','Q5','DPNI','DPwater','cutsmart','Date','ngdesired'],index=range(len(temppwls)))
variables.iloc[0]= [stkprm,stkvol,dilprm,primerconc,pcrvol,templatengs,Q5,DPNI,DPwater,cutsmart,Date,ngdesired]
variables['template pwl number'] = temppwls
variables['template concentrations'] = tempconcs

if extra1value != 0: 
    variables[extra1name] = ''
    variables.loc[0,extra1name] = extra1value

if extra2value != 0:
    variables[extra2name] = ''
    variables.loc[0,extra2name] = extra2value

variables

os.chdir(paths.loc[0].at['opentrons_repo']+'/pcr/'+date+'_pcr')
variables.to_csv('Input.csv')
shutil.copy2('Input.csv', paths.loc[0].at['opentrons_repo']+'/pcr/')

os.system("notepad.exe pcr_instructions.txt")
