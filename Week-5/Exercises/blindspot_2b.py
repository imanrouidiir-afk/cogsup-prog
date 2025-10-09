
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_LEFT, K_RIGHT, K_UP, K_DOWN


exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode(on=True)
control.initialize(exp)

exp.add_data_variable_names(["Eye", "Radius", "X_position", "Y_position"])


def make_circle(radius, position=(0, 0)):
    circle = stimuli.Circle(radius, position=position, colour=C_BLACK)
    circle.preload()
    return circle


def run_trial(side):
    
    text = (
        f"Blind Spot Test – {side} Eye\n\n"
        f"1. Cover your { 'left' if side == 'R' else 'right' } eye.\n"
        f"2. Keep looking at the fixation cross (+).\n"
        f"3. Use ARROW KEYS to move the circle.\n"
        f"4. Press 1 to make it smaller, 2 to make it larger.\n"
        f"5. When the circle disappears (blind spot found), press SPACE to continue."
    )
    instructions = stimuli.TextScreen("Instructions", text)
    instructions.present()
    exp.keyboard.wait()  

    
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[-300, 0]if side == "R" else [300, 0]) 
    fixation.preload()

    radius = 75
    circle_pos = [0, 0]  
    circle = make_circle(radius, circle_pos)

    
    running = True
    while running:
        
        fixation.present(clear=True)
        circle.present(clear=False)
        exp.screen.update()
        exp.clock.wait(10)

        key = exp.keyboard.check()

        if key:

            exp.data.add([side, key, radius, circle_pos[0], circle_pos[1]])
            
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

        exp.data.add([side, radius, circle_pos[0], circle_pos[1]])


control.start(subject_id=1)

run_trial("L")  
run_trial("R")  


stimuli.TextScreen("Done!", "You finished the Test.\n\nThank u:)").present()
exp.keyboard.wait()

control.end()

