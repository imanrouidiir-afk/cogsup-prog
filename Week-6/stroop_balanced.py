from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_RED, C_BLUE, C_GREEN, K_r, K_b, K_g, K_o
import random

C_ORANGE = (255, 165, 0) 
COLORS = {'red': C_RED, 'blue': C_BLUE, 'green': C_GREEN, 'orange': C_ORANGE}
WORDS = list(COLORS.keys())
KEYS_TO_COLORS = {K_r: 'red', K_b: 'blue', K_g: 'green', K_o: 'orange'}
RESPONSE_KEYS = list(KEYS_TO_COLORS.keys())

N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 128 // N_BLOCKS # 16 trials per block

INSTR_START = """ Welcome to the Color-Naming Task.

Your task is to identify the COLOR of the font, regardless of the word's meaning.

Use the following keys to respond:
    R: RED
    B: BLUE
    G: GREEN
    O: ORANGE
Press the SPACE bar to begin the experiment.
""" 

INSTR_MID = """Break. Press SPACE to continue."""
INSTR_END = """Done! Press SPACE to quit."""
FEEDBACK_CORRECT = "Correct!"
FEEDBACK_INCORRECT = "Incorrect."

""" Helper Functions """
def present_for(*stims, t=1000):
    # Simplified helper for drawing and waiting
    dt = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    exp.clock.wait(t - (exp.clock.time - dt))

def present_instructions(text):
  instructions = stimuli.TextScreen(text=text, heading="") 
  instructions.present()
  exp.keyboard.wait()
  
""" Global settings """
exp = design.Experiment(name="Stroop_Balanced")
exp.add_data_variable_names(['block_cnt', 'word', 'color_name', 'RT', 'correct'])
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross(); fixation.preload()
stims = {w: {c: stimuli.TextLine(w, text_colour=COLORS[c]) for c in WORDS} for w in WORDS}
for w in WORDS: [stims[w][c].preload() for c in WORDS]
feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT, text_colour=C_GREEN); feedback_correct.preload()
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT, text_colour=C_RED); feedback_incorrect.preload()

def create_balanced_trial_list():
    trial_list = []
    for word in WORDS:
        for color_name in WORDS:
            # The correct key is for the FONT COLOR (color_name)
            correct_key = [k for k, v in KEYS_TO_COLORS.items() if v == color_name][0]
            trial_list.append({
                'word': word,
                'color_name': word,
                'trial_type': 'match' 
                'correct_key': correct_key
            })
        ders = derangements(WORDS)
    mismatch = ders[(subject_id - 1) % len(ders)]

    for word, color_name in zip(WORDS, mismatch):
        correct_key = [k for k, v in KEYS_TO_COLORS.items() if v == color_name][0]
        trial_list.append({
            'word': word,
            'color_name': color_name,
            'trial_type': 'mismatch',
            'correct_key': correct_key
        })
    return trial_list
""" Experiment """
def run_trial(block_id, trial_id, trial_data):
    stim = stims[trial_data['word']][trial_data['color_name']]
    
    present_for(fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait(RESPONSE_KEYS) 

    correct = key == trial_data['correct_key']
    exp.data.add([block_id, trial_id, trial_data['word'], trial_data['color_name'], rt, correct])

    feedback = feedback_correct if correct else feedback_incorrect
    present_for(feedback, t=1000)
N_TRIALS_IN_BLOCK = 8
control.start(subject_id=1)

present_instructions(INSTR_START)

master_template = create_balanced_trial_list()
block_repetitions = 2

for block_id in range(1, N_BLOCKS + 1):
    # Each block is a full, shuffled presentation of the 16 unique trials
    current_block_trials = list(master_template) 
    random.shuffle(current_block_trials)

    for trial_id in range(1, N_TRIALS_IN_BLOCK + 1):
        run_trial(block_id, trial_id, current_block_trials[trial_id - 1])

    if block_id != N_BLOCKS:
        present_instructions(INSTR_MID)

present_instructions(INSTR_END)
control.end()
