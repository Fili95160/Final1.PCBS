"""A series of trials where a Circle is presented and the participant must press a key as quickly as possible.
"""
import random 
from expyriment import design, control, misc, stimuli

########## *******************  PART 1.Experiment settings ******************* ####################

NTRIALS = 5 
ITI = 1000  # inter trial interval

exp = design.Experiment(name="Side Detection")
control.initialize(exp)

blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("Instructions",
    f"""From time to time, a Circle will appear at the center of screen.

    Your task is to press the space bar key as quickly as possible when you see it (We measure your reaction-time).

    There will be {3*NTRIALS} trials in total.

    Press the space bar to start.""")

###### 1.A --> Definition of the only two possible trials made up of two stimuli "Blue/Red"

#Stimulus red
visual_trial_red = design.Trial()
visual_trial_red.add_stimulus(stimuli.Circle(radius=100, colour=(255,0,0)))

#Stimulus blue
visual_trial_blue = design.Trial()
visual_trial_blue.add_stimulus(stimuli.Circle(radius=100, colour= (0,0,255)))

###### 1.B --> Definition of Associated Blocks "Blue/Red"


visual_block_red = design.Block("red")

# Buidlding red block with 5 stimuli

for i in range(NTRIALS): 

    visual_block_red.add_trial(visual_trial_red)

exp.add_block(visual_block_red) # Adding red block to experiment

# Building blue block with 5 stimuli

visual_block_blue = design.Block("blue")

for i in range(NTRIALS):

    visual_block_blue.add_trial(visual_trial_blue)

exp.add_block(visual_block_blue) # Adding blue block to experiment
    
exp.add_data_variable_names([ 'block' , 'key' , 'time' ]) # Implementing data frame's columns name to study after experiment

visual_block_random = design.Block('random')

L=["red" , "blue"]
for i in range(NTRIALS):

    rand = random.choice(L)
    visual_block_random.name == rand

    if(random == "red"):

        visual_block_random.add_trial(visual_trial_red)

    else:

        visual_block_random.add_trial(visual_trial_blue)

        

exp.add_block(visual_block_random)


########## *******************  PART 2.Experiment ******************* ####################


control.start(skip_ready_screen=True) #begining experiment
instructions.present()
exp.keyboard.wait()

exp.clock.wait( 3000 )

for b in exp.blocks: # moving through each block

    for t in b.trials: # iterating over stimuli inside each code

        blankscreen.present()
        exp.clock.wait( ITI ) # Fixed time between each stimulus.
        exp.clock.wait( random.randint(1000, 2000) ) # Random time between 1 and 3 sec. between each stimulus.
        t.stimuli[0].present() # Printing stimulus.

        key, rt = exp.keyboard.wait(misc.constants.K_SPACE) # monitoring time
        
        exp.data.add( [ b.name, key, rt ] ) #Adding data to our database

control.end() # ending experiment

