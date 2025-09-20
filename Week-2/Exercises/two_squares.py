from expyriment import design, control, stimuli
control.set_develop_mode()
exp = design.Experiment(name="Two Squares")
control.initialize(exp)
left_square = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0), 
position=(-100, 0))
right_square = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0), 
position=(100, 0))
control.start(subject_id=1)
left_square.present(clear=True, update=False)
right_square.present(clear=False, update=True)
exp.keyboard.wait()
control.end()
