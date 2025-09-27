from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY, C_BLACK, C_WHITE

exp = design.Experiment("Kanizsa Square", background_colour=C_GREY)
control.set_develop_mode(True)
control.initialize(exp)

control.start()

screen_w, screen_h = exp.screen.size
side = int(0.25 * screen_w)
radius = int(0.05 * screen_w)

top_left = stimuli.Circle(radius, colour=C_BLACK)
top_right = stimuli.Circle(radius, colour=C_BLACK)
bottom_left = stimuli.Circle(radius, colour=C_WHITE)
bottom_right = stimuli.Circle(radius, colour=C_WHITE)


mask = stimuli.Rectangle((radius, radius), colour=C_GREY)


pac_top_left = top_left.copy()
pac_top_right = top_right.copy()
pac_bottom_left = bottom_left.copy()
pac_bottom_right = bottom_right.copy()

mask_top_left = mask.copy(); mask_top_left.position = (radius//2, radius//2); mask_top_left.plot(pac_top_left)
mask_top_right = mask.copy(); mask_top_right.position = (-radius//2, radius//2); mask_top_right.plot(pac_top_right)
mask_bottom_left = mask.copy(); mask_bottom_left.position = (radius//2, -radius//2); mask_bottom_left.plot(pac_bottom_left)
mask_bottom_right = mask.copy(); mask_bottom_right.position = (-radius//2, -radius//2); mask_bottom_right.plot(pac_bottom_right)

offset = side // 2
pac_top_left.position = (-offset, offset)
pac_top_right.position = (offset, offset)
pac_bottom_left.position = (-offset, -offset)
pac_bottom_right.position = (offset, -offset)

pac_top_left.present(clear=True, update=False)
pac_top_right.present(clear=False, update=False)
pac_bottom_left.present(clear=False, update=False)
pac_bottom_right.present(clear=False, update=True)

exp.keyboard.wait()
control.end()
