from expyriment import design, control, stimuli
def launching_event(exp, temporal_gap=0, spatial_gap=0, speed_factor=1):
    left_square = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0), position=(-400, 0))
    right_square = stimuli.Rectangle(size=(50, 50), colour=(0, 225, 0), position=(0, 0))
    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)
    exp.clock.wait(500)
    square_length = 50
    displacement_x = 400
    step_size = 10
    while right_square.position[0] - left_square.position[0] > square_length + spatial_gap:
        left_square.move((step_size, 0))
        left_square.present(clear=True, update=False)
        right_square.present(clear=False, update=True)
        exp.clock.wait(20)
    if temporal_gap > 0:
        exp.clock.wait(temporal_gap)
    start_x = right_square.position[0]
    while right_square.position[0] < start_x + displacement_x:
        right_square.move((step_size * speed_factor, 0))
        left_square.present(clear=True, update=False)
        right_square.present(clear=False, update=True)
        exp.clock.wait(20)
control.set_develop_mode()
exp = design.Experiment(name="Launching Function")
control.initialize(exp)
control.start(subject_id=1)
launching_event(exp, temporal_gap=0, spatial_gap=0, speed_factor=1)
exp.clock.wait(1000)
launching_event(exp, temporal_gap=2000, spatial_gap=0, speed_factor=1)
exp.clock.wait(1000)
launching_event(exp, temporal_gap=0, spatial_gap=50, speed_factor=1)
exp.clock.wait(1000)
launching_event(exp, temporal_gap=0, spatial_gap=0, speed_factor=3)
exp.clock.wait(1000)
exp.keyboard.wait()
control.end()
