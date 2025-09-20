from expyriment import design, control, stimuli
control.set_develop_mode()
exp = design.Experiment(name="Labeled Shapes")
control.initialize(exp)
triangle = stimuli.Shape(position=(-150, 0), colour=(128, 0, 128),
                         vertices=[(-25, -25), (25, -25), (0, 25)])
hexagon = stimuli.Shape(position=(150, 0), colour=(255, 255, 0),
                        vertices=[(25, -25), (50, 0), (25, 25),
                                  (-25, 25), (-50, 0), (-25, -25)])
triangle_line = stimuli.Line((0, 50), (0, 100), colour=(255, 255, 255), line_width=3, position=(-150, 25))
hexagon_line = stimuli.Line((0, 50), (0, 100), colour=(255, 255, 255), line_width=3, position=(150, 25))
triangle_label = stimuli.TextLine("triangle", position=(-150, 120), text_colour=(255, 255, 255))
hexagon_label = stimuli.TextLine("hexagon", position=(150, 120), text_colour=(255, 255, 255))
control.start(subject_id=1)
triangle.present(clear=True, update=False)
hexagon.present(clear=False, update=True)
triangle_line.present(clear=False, update=True)
hexagon_line.present(clear=False, update=True)
triangle_label.present(clear=False, update=True)
hexagon_label.present(clear=False, update=True)
exp.keyboard.wait()
control.end()
