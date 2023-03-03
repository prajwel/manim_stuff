from manim import *
import numpy as np
import random

def get_xy():
    r = 2.45 * np.sqrt(random.random())
    theta = random.random() * 2 * np.pi            
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return np.array([x, y, 0])

class RandomDotss(Scene):
    def construct(self):
        all_dots = VGroup()
        circle = Circle(radius=2.5, color=WHITE)        
        for i in range(10):
            dots = VGroup(*[Dot(get_xy(), 
                          radius=0.05, color=BLUE) 
                          for _ in range(40)])            
#            dots = VGroup(*[Dot(np.array([random.uniform(-1.8, 1.8), 
#                                          random.uniform(-1.8, 1.8), 0]), 
#                          radius=0.05, color=BLUE) 
#                          for _ in range(20)])
                          
            all_dots.add(dots)
            group = VGroup(circle, dots)
            group.move_to(ORIGIN)
            counter = Tex(f"Frame {i+1}/10")
            counter.next_to(group, UP)
            self.add(group, counter)
#            self.wait(0.1)
#            self.remove(dots)
            self.play(FadeOut(dots, counter))

        self.wait(1)    
        all_dots.move_to(ORIGIN)
        group = VGroup(circle, all_dots)
        counter = Tex(f"Events from all 10 frames")
        counter.next_to(group, UP)        
        self.add(group, counter)
        self.wait(10)
        self.play(FadeOut(group, counter))





