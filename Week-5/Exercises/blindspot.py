from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

""" Experiment """
def run_trial(side="left"):
    instruction_text = (
        f"Cover your {side} eye.\n\n"
        "Fixate on the black cross.\n\n"
        "Use the ARROW keys to move the circle.\n"
        "Press 1 to make it smaller, 2 to make it larger.\n\n"
        "When the circle disappears (blind spot reached), press SPACE."
    )
    instructions = stimuli.TextScreen("Instructions", instruction_text)
    instructions.present()
    exp.keyboard.wait_char(' ')
    
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0])
    fixation.preload()

    radius = 75
    circle = make_circle(radius)

    fixation.present(True, False)
    circle.present(False, True)

    exp.keyboard.wait()

control.start(subject_id=1)

run_trial()
    
control.end()
