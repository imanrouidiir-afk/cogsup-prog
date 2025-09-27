from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY, C_BLACK, C_WHITE

def kanizsa_rectangle(aspect_ratio=1.5, rect_scale=0.25, circle_scale=0.05):
    exp = design.Experiment("Kanizsa Rectangle", background_colour=C_GREY)
    control.set_develop_mode(True)
    control.initialize(exp)
    control.start()

    w, h = exp.screen.size
    rect_w, rect_h = int(rect_scale * w), int((rect_scale * w) / aspect_ratio)
    r = int(circle_scale * w)

    circles = [stimuli.Circle(r, colour=c) for c in (C_BLACK, C_BLACK, C_WHITE, C_WHITE)]
    masks   = [( r//2,  r//2), (-r//2,  r//2), ( r//2, -r//2), (-r//2, -r//2)]
    pos     = [(-rect_w//2,  rect_h//2), ( rect_w//2,  rect_h//2),
               (-rect_w//2, -rect_h//2), ( rect_w//2, -rect_h//2)]

    for c, m, p in zip(circles, masks, pos):
        stimuli.Rectangle((r, r), colour=C_GREY, position=m).plot(c)
        c.position = p
        c.present(clear=(c==circles[0]), update=(c==circles[-1]))

    exp.keyboard.wait()
    control.end()

if __name__ == "__main__":
    kanizsa_rectangle(aspect_ratio=2.0, rect_scale=0.3, circle_scale=0.07)


