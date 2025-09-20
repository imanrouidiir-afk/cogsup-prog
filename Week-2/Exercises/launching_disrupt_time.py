from expyriment import design, control, stimuli
control.set_develop_mode()
exp = design.Experiment(name="Launching with Spatial Gap")
control.initialize(exp)
left_square = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0), position=(-400, 0))
right_square = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0), position=(0, 0))
square_length = 50
gap = 50 
displacement_x = 400
step_size = 10
control.start(subject_id=1)
left_square.present(clear=True, update=False)
right_square.present(clear=False, update=True)
exp.clock.wait(500)
while right_square.position[0] - left_square.position[0] > (square_length + gap):
    left_square.move((step_size, 0))
    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)
    exp.clock.wait(20)
start_x = right_square.position[0]
while right_square.position[0] < start_x + displacement_x:
    right_square.move((step_size, 0))
    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)
    exp.clock.wait(20)
exp.keyboard.wait()
control.end()
