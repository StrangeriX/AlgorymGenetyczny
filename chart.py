from typing import List, Tuple, Optional
import matplotlib.pyplot as plot
import imageio


class Chart:
    def __init__(self, subplots: Tuple[int, int]):
        self.subplot_x, self.subplot_y = subplots
        self.fig, self.ax = plot.subplots(self.subplot_x, self.subplot_y)
        self.max_subplots = self.subplot_x * self.subplot_y
        plot.subplot(self.subplot_x, self.subplot_y, 1)
        self.current_subplot = 1

    def clear_axes(self):
        plot.cla()

    def show(self):
        plot.show()

    def title(self, title: str):
        plot.title(title)

    def next_subplot(self):
        if self.current_subplot >= self.max_subplots:
            self.current_subplot = 1
            plot.subplot(self.subplot_x, self.subplot_y, 1)
        else:
            self.current_subplot += 1
            plot.subplot(self.subplot_x, self.subplot_y, self.current_subplot)

    def draw_point(self, x: float, y: float, name: Optional[str] = None, color: Optional[str] = None):
        if color and name:
            plot.scatter(x, y, c=color, label=name)
            plot.legend()
        else:
            plot.scatter(x, y)
        plot.draw()

    def draw_many_points(self, x: List[float], y: List[float], name: Optional[str] = None, point_name: Optional[List[str]] = None, color: Optional[str] = None, size: int = None):
        if name and color:
            if len(x) == len(y):
                plot.scatter(x, y, label=name, c=color, s=size)
                plot.legend()
                plot.draw()
            else:
                raise Exception("Number of x is not same as number of y")
        elif name:
            if len(x) == len(y):
                plot.scatter(x, y, c=color)
                plot.draw()
            else:
                raise Exception("Number of x is not same as number of y")
        else:
            if len(x) == len(y):
                plot.scatter(x, y, c=color)
                plot.draw()
            else:
                raise Exception("Number of x is not same as number of y")
        if point_name:
            plot.scatter(x, y)
            for i, txt in enumerate(point_name):
                plot.annotate(txt, (x[i], y[i]))

    def save_frame(self, i):
        plot.savefig(f"frames/{i}.png")
        plot.close()

    def create_gif(self, iterations):
        with imageio.get_writer('simulation_gif.gif', mode='I') as writer:
            for iteration in range(iterations):
                image = imageio.imread(f"frames/{iteration}.png")
                writer.append_data(image)