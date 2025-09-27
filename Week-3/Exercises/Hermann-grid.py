from expyriment import design, control, stimuli
from expyriment.misc.constants import C_BLACK, C_WHITE

def hermann_grid(square_size=80, spacing=20, rows=6, cols=6,
                 square_colour=C_BLACK, background_colour=C_WHITE):
    exp = design.Experiment("Hermann Grid", background_colour=background_colour)
    control.set_develop_mode(True)
    control.initialize(exp)
    control.start()

    w, h = exp.screen.size
    grid_width  = cols * square_size + (cols - 1) * spacing
    grid_height = rows * square_size + (rows - 1) * spacing
    start_x, start_y = -grid_width // 2, grid_height // 2

    canvas = stimuli.Canvas(size=exp.screen.size, colour=background_colour)

    for i in range(rows):
        for j in range(cols):
            x = start_x + j * (square_size + spacing) + square_size // 2
            y = start_y - i * (square_size + spacing) - square_size // 2
            square = stimuli.Rectangle((square_size, square_size),
                                       position=(x, y),
                                       colour=square_colour)
            square.plot(canvas)

    canvas.present()
    exp.keyboard.wait()
    control.end()

if __name__ == "__main__":
    hermann_grid(square_size=80, spacing=20, rows=6, cols=6,
                 square_colour=C_BLACK, background_colour=C_WHITE)
    
