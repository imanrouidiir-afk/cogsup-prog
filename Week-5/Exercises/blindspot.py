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
        f"Cover your {side} eye."
        " "
        "Fixate on the black cross."
        "Use the ARROW keys to move the circle."
        "Press 1 to make it smaller, 2 to make it larger."
        "When the circle disappears (blind spot reached), press SPACE."
    )
    instructions = stimuli.TextScreen("Instructions", instruction_text)
    instructions.present()
    exp.keyboard.wait_char(' ')
    
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0] if side == "left" else [-300, 0])
    fixation.preload()

    radius = 75
    circle_pos = [0, 0]
    circle = make_circle(radius)

    fixation.present(True, False)
    circle.present(False, True)
    
    running = True 
    while running:
        fixation.present(clear=True)
        circle.present(clear=False)
        exp.screen.update()
        exp.clock.wait(10)

     key = exp.keyboard.wait()
            if key:
            
            if key == K_LEFT:
                circle_pos[0] -= 10
            if key == K_RIGHT:
                circle_pos[0] += 10
            if key == K_UP:
                circle_pos[1] += 10
            if key == K_DOWN:
                circle_pos[1] -= 10

            if key == ord('1'):
                radius -= 5
            if key == ord('2'):
                radius += 5
            
            if key == ord(' '):
                running = False

            
            circle = make_circle(radius, circle_pos)

control.start(subject_id=1)

run_trial("L")
run_trial("R") 

stimuli.TextScreen("Done!", "You finished the Test.\n\nThank u:)").present()
exp.keyboard.wait()

control.end()
