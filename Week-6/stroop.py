from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_RED, C_BLUE, C_GREEN, K_j, K_f
import random

""" Constants """
KEYS = [K_j, K_f]
TRIAL_TYPES = ['match', 'mismatch']
C_ORANGE = (255, 165, 0) 
COLORS = {'red': C_RED, 'blue': C_BLUE, 'green': C_GREEN, 'orange': C_ORANGE}
WORDS = list(COLORS.keys())

N_BLOCKS = 2
N_TRIALS_TOTAL = 32
N_TRIALS_IN_BLOCK = N_TRIALS_TOTAL // N_BLOCKS 

INSTR_START = """
In this task, you have to indicate whether the meaning of a word and the color of its font match.
Press J if they do (match), F if they don't (mismatch).\n
Press SPACE to continue.
"""
INSTR_MID = """You have finished half of the experiment, well done! Your task will be the same.\nTake a break then press SPACE to move on to the second half."""
INSTR_END = """Well done! \nThe experiment is now complete.\nPress SPACE to quit."""

FEEDBACK_CORRECT = "Correct!"
FEEDBACK_INCORRECT = "Incorrect."

""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(*stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
# Added 'color_name' for clarity in data file
exp.add_data_variable_names(['block_cnt', 'trial_cnt', 'trial_type', 'word', 'color_name', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

stims = {w: {c: stimuli.TextLine(w, text_colour=COLORS[c]) for c in WORDS} for w in WORDS}
load([stims[w][c] for w in WORDS for c in WORDS])

# Feedback stimuli with color coding
feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT, text_colour=C_GREEN)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT, text_colour=C_RED)
load([feedback_correct, feedback_incorrect])

""" Experiment """
def run_trial(block_id, trial_id, trial_type, word, color_name):
    """
    Runs one trial of the Stroop task.
    """
    stim = stims[word][color_name]
    correct_key = K_j if word == color_name else K_f

    present_for(fixation, t=500) 
    stim.present() 
    key, rt = exp.keyboard.wait(KEYS) 
    correct = key == correct_key

    exp.data.add([block_id, trial_id, trial_type, word, color_name, rt, correct])
    feedback = feedback_correct if correct else feedback_incorrect
    present_for(feedback, t=1000)

control.start(subject_id=1)

present_instructions(INSTR_START)

for block_id in range(1, N_BLOCKS + 1):
    trial_list = []
    for word in WORDS:
        for color_name in WORDS:
            trial_type = 'match' if word == color_name else 'mismatch'
            trial_list.append((trial_type, word, color_name))

    random.shuffle(trial_list)

    for trial_id in range(1, N_TRIALS_IN_BLOCK + 1):
        trial_type, word, color_name = trial_list[trial_id - 1]
        run_trial(block_id, trial_id, trial_type, word, color_name)
    if block_id != N_BLOCKS:
        present_instructions(INSTR_MID)

present_instructions(INSTR_END)

control.end()
