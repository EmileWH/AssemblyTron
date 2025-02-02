'''Dilution Script for up to 24 primers and templates

This script contains a protocol for diluting up to 96 primers and templates to concentrations specified in the AssemblyTron.Golden_Gate.Setup_nodigests_seppcr_gradient_24 module. 

This script runs on the OT-2 via the run app. It calls CSVs which must be transferred to the OT-2 processor prior to running. This script is not designed to run a personal computer on the command line.

'''


import pandas
import numpy as np
import os
from opentrons import protocol_api

#Metadata is a dictionary of data that is read by the server and returned to the opentrons app. 
#give yourself credit. you are required to specify the 'apiLevel' herefrom opentrons import protocol_api
metadata = {
    'protocolName': 'ARF7 Deletions Protocol',
    'author': 'John Bryant <jbryant2@vt.edu>',
    'description': 'Protocol for performing PCR reactions and Plasmid assembly for TIR1 and AFB mutants',
    'apiLevel': '2.10'
}
print(metadata)




def run(protocol: protocol_api.ProtocolContext): #for actually running the script in the robot
#will have to indent everything to be defined by the run function

#from opentrons import simulate
#protocol = simulate.get_protocol_api('2.2')
    paths = pandas.read_csv('/data/user_storage/robotpaths.csv')
    paths

    Input_values = pandas.read_csv(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/Input.csv') 
    Date = str(int(Input_values.loc[0].at['Date']))
    Date
    Time = str(int(Input_values.loc[0].at['Time']))
    Time
    os.chdir(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+Date+Time+'_GoldenGate')
    oligos = pandas.read_csv('oligo.csv')
    assembly = pandas.read_csv('assembly.csv')
    pcr = pandas.read_csv('pcr.csv')
    combinations = pandas.read_csv('combinations.csv')
    df = pandas.read_csv('templates.csv')
    #digests = pandas.read_csv('digests.csv')
#labware:
    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', '9')
    #tiprack2 = protocol.load_labware("opentrons_96_tiprack_10ul",'6')
    tiprack3 = protocol.load_labware("opentrons_96_tiprack_10ul", '5')
#tuberack1 = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap','1') #holds stock primers and templates
    watertuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical','3') #holds molec bio grad H2O
    tuberack2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','2') # holds dilute primers and templates
    
    tc_mod = protocol.load_module('Thermocycler Module')
    pcrplate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt')
    temp_module = protocol.load_module('temperature module', 1)
    cold_tuberack = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', label='Temperature-Controlled Tubes')
    temp_module.set_temperature(4)
    print(temp_module.temperature)
    tc_mod.open_lid()

# #########Some notes:    
# #specify the order of stock primers and template in tuberack1 here:
# #good place to add the pop-up window
# #A1-D3 = stock primers
# #D4-D5 = stock templates
# #stock tubes and dilution tubes need to be set up in the same order
# #as of now Q5 is in 
    
#pipettes
    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1])
    left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3])
    
##################################COMMANDS####################################
    
#add water to template dilution tubes. ***df is the template description dataframe
#Since we are just moving water I will use the same pipette tip to save plastic

    x = 'Dilution'
    if x in Input_values['section'].values:

#add water for templates
        right_pipette.pick_up_tip()
        for i, row in df.iterrows():
            if df.loc[i].at['water to add'] > 8:
                right_pipette.aspirate(volume = df.loc[i].at['water to add'], location = watertuberack['A1'], rate=1.0) #total vol dilute template - vol stock template to add
                right_pipette.dispense(df.loc[i].at['water to add'], tuberack2[df.loc[i].at['template_well']], rate=1.0)
            if df.loc[i].at['water to add'] < 8:
                right_pipette.aspirate(volume = 3*(df.loc[i].at['water to add']), location = watertuberack['A1'], rate=1.0) #total vol dilute template - vol stock template to add
                right_pipette.dispense(3*(df.loc[i].at['water to add']), tuberack2[df.loc[i].at['template_well']], rate=1.0)
        #right_pipette.blow_out()
    #digestions water
        # for i, row in digests.iterrows():
        #     right_pipette.aspirate(volume = digests.loc[i].at['water to add'], location = watertuberack['A1'], rate=1.0) #total vol dilute template - vol stock template to add
        #     right_pipette.dispense(digests.loc[i].at['water to add'], tuberack2[digests.loc[i].at['well']], rate=1.0)
            #right_pipette.blow_out()

    #add water to primer dilution tubes
        for i, row in oligos.iterrows():
            right_pipette.aspirate(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'], watertuberack['A1'], rate=1.0) #need to put 39uL of water into each dilution tube for primers,) #we need to find better way to loop through these commands
            right_pipette.dispense(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'], tuberack2[oligos.loc[i].at['well']], rate=1.0)
            #right_pipette.blow_out()
        right_pipette.drop_tip()    
        
    #add stock templates to dilution tubes
        for i, row in df.iterrows():
            if df.loc[i].at['water to add'] > 8:
                left_pipette.pick_up_tip()
                left_pipette.aspirate(df.loc[i].at['amount of template to add'], cold_tuberack[df.loc[i].at['template_well']], rate=1.0) #dilution well corresponds to stock well
                left_pipette.dispense(df.loc[i].at['amount of template to add'], tuberack2[df.loc[i].at['template_well']], rate=1.0) #makes a 12.5ng/uL template
                left_pipette.mix(3,5,tuberack2[df.loc[i].at['template_well']])
            #left_pipette.blow_out()
                left_pipette.drop_tip()
            if df.loc[i].at['water to add'] < 8:
                left_pipette.pick_up_tip()
                left_pipette.aspirate(3*(df.loc[i].at['amount of template to add']), cold_tuberack[df.loc[i].at['template_well']], rate=1.0) #dilution well corresponds to stock well
                left_pipette.dispense(3*(df.loc[i].at['amount of template to add']), tuberack2[df.loc[i].at['template_well']], rate=1.0) #makes a 12.5ng/uL template
                left_pipette.mix(3,5,tuberack2[df.loc[i].at['template_well']])
                #left_pipette.blow_out()
                left_pipette.drop_tip()

    #add stock templates for digests:
        # for i, row in digests.iterrows():
        #     left_pipette.pick_up_tip()
        #     left_pipette.aspirate(digests.loc[i].at['amount of template to add'], cold_tuberack[digests.loc[i].at['well']], rate=1.0) #dilution well corresponds to stock well
        #     left_pipette.dispense(digests.loc[i].at['amount of template to add'], tuberack2[digests.loc[i].at['well']], rate=1.0) #makes a 12.5ng/uL template
        #     #left_pipette.blow_out()
        #     left_pipette.drop_tip()
        
    #add stock primers to dilution tube
        for i, row in oligos.iterrows():
            left_pipette.pick_up_tip() #add in an iterrows function
            left_pipette.aspirate(oligos.loc[i].at['volume of stock primer to add'], cold_tuberack[oligos.loc[i].at['well']], rate=1.0)
            left_pipette.dispense(oligos.loc[i].at['volume of stock primer to add'], tuberack2[oligos.loc[i].at['well']], rate=1.0)
            left_pipette.mix(3,5,tuberack2[oligos.loc[i].at['well']])
            #left_pipette.blow_out()
            left_pipette.drop_tip()
        
    #mix contents with pipette tip (reps, max volume, location) for templates and primers
        for i, row in df.iterrows():
            if df.loc[i].at['water to add'] > 8:
                right_pipette.pick_up_tip()
                right_pipette.mix(3,df.loc[i].at['water to add'],tuberack2[df.loc[i].at['template_well']])
                #right_pipette.blow_out()
                right_pipette.drop_tip()
            if df.loc[i].at['water to add'] < 8:
                right_pipette.pick_up_tip()
                right_pipette.mix(3,3*(df.loc[i].at['water to add']),tuberack2[df.loc[i].at['template_well']])
                #right_pipette.blow_out()
                right_pipette.drop_tip()

        # for i, row in digests.iterrows():
        #     right_pipette.pick_up_tip()
        #     right_pipette.mix(3,digests.loc[i].at['water to add'],tuberack2[digests.loc[i].at['well']])
        #     #right_pipette.blow_out()
        #     right_pipette.drop_tip()
            
        for i, row in oligos.iterrows():
            right_pipette.pick_up_tip()
            right_pipette.mix(3,oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'],tuberack2[oligos.loc[i].at['well']])
            #right_pipette.blow_out()
            right_pipette.drop_tip()

    #robot pauses so user can take out stock primers and put in DNPNI
        protocol.pause('Take all stock primers and templates out. Add Q5 to D6, BsaI to D5, and cutsmart to D4. Then proceed')
        

