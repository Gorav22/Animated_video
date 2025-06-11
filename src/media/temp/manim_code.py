from manim import *

class ParabolaVsInverse(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 9, 1],
            axis_config={"color": BLUE}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        parabola = axes.plot(lambda x: x**2, color=YELLOW, x_range=[-3, 3])
        inverse = axes.plot(lambda y: np.sqrt(y), color=RED, x_range=[0, 9])
        inverse_neg = axes.plot(lambda y: -np.sqrt(y), color=RED, x_range=[0, 9])
        parabola_label = axes.get_graph_label(parabola, label="y = x^2", x_val=1.5, direction=UR)
        inverse_label = axes.get_graph_label(inverse, label="x = y^2", x_val=7, direction=RIGHT)

        self.play(Create(axes), Write(labels))
        self.wait(0.5)
        self.play(Create(parabola), Write(parabola_label))
        self.wait(0.5)
        self.play(Create(inverse), Create(inverse_neg), Write(inverse_label))
        self.wait(2)
