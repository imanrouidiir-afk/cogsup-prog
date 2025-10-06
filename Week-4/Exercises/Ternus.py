from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE

control.set_develop_mode(on=True)
exp = design.Experiment()
control.initialize(exp)

RADIUS = 40
TAG_RADIUS = 10
DISTANCE = 150
DISPLAY_FRAMES = 12     
LOW_ISI = 0             
HIGH_ISI = 18           
COLOR = (255, 255, 255)
TAG_COLORS = [(255, 255, 0), (255, 0, 0), (0, 0, 255)]  
BG_COLOR = (0, 0, 0)

exp.screen.colour = BG_COLOR

def frames_to_ms(frames):
    return int(round(frames * (1000 / 60)))


def make_circles(with_tags=False):
    y = 0
    frame1_pos = [(-DISTANCE, y), (0, y), (DISTANCE, y)]        
    frame2_pos = [(0, y), (DISTANCE, y), (DISTANCE * 2, y)]     

    frames = []
    for positions in [frame1_pos, frame2_pos]:
        frame = []
        for i, (x, y) in enumerate(positions):
            big = stimuli.Circle(RADIUS, COLOR)
            if with_tags:
                
                tag = stimuli.Circle(TAG_RADIUS, TAG_COLORS[i], position=(0, 0))
                tag.plot(big)
            big.position = (x, y)
            big.preload()
            frame.append(big)
        frames.append(frame)
    return frames[0], frames[1]


def present_for(stims, frames):
    exp.screen.clear()
    for s in stims:
        s.present(clear=False)
    exp.clock.wait(frames_to_ms(frames))


def add_tags(text):
    tag = stimuli.TextLine(text, position=(0, -200))
    tag.present(clear=False)


displays = [
    ("Element motion (low ISI, white)", LOW_ISI, False),
    ("Group motion (high ISI, white)", HIGH_ISI, False),
    ("Element motion (high ISI, colored centers)", HIGH_ISI, True)
]

for label_text, isi_frames, with_tags in displays:
    frame1, frame2 = make_circles(with_tags=with_tags)

    present_for(frame1, DISPLAY_FRAMES)

    
    if isi_frames > 0:
        exp.screen.clear()
        exp.clock.wait(frames_to_ms(isi_frames))

   
    present_for(frame2, DISPLAY_FRAMES)

    add_tags(label_text)
    exp.clock.wait(frames_to_ms(30))

    if exp.keyboard.check(K_SPACE):
        break

stimuli.TextLine("Experiment ended. Press any key.").present()
exp.keyboard.wait()
control.end()
