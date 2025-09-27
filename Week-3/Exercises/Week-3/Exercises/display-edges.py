from expyriment import design, control, stimuli

exp = design.Experiment(name="screen edges")
control.set_develop_mode()
control.initialize(exp)

width, height = exp.screen.size
print("Screen size:", width, height)

size_square = int(0.05 * width)
half_w, half_h = width // 2, height // 2
half_len = size_square // 2
red = (255, 0, 0)

positions = [
    (-half_w + half_len,  half_h - half_len),   
    ( half_w - half_len,  half_h - half_len),   
    (-half_w + half_len, -half_h + half_len),   
    ( half_w - half_len, -half_h + half_len)]

squares = [
    stimuli.Rectangle(size=(size_square, size_square),
                      position=pos,
                      colour=red,
                      line_width=1)
    for pos in positions]

control.start()
exp.screen.clear()
for square in squares:
    square.present(clear=False, update=False)
exp.screen.update()

exp.keyboard.wait()
control.end()
