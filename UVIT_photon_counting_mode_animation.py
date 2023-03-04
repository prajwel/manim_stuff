from manim import *
import numpy as np
import random

def get_xy(seed):
    random.seed(seed)
    r = 2.45 * np.sqrt(random.random())
    theta = random.random() * 2 * np.pi            
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return np.array([x, y, 0])

class RandomDots(Scene):
    def construct(self):
        all_dots = VGroup()
        circle = Circle(radius=2.5, color=WHITE)   
        circle.move_to(ORIGIN)
        self.play(FadeIn(circle))     
        for i in range(5):
            dots = VGroup(*[Dot(get_xy(((i + 1) * 1000) + (j + 1)), 
                          radius=0.05, color=BLUE) 
                          for j in range(40)])            
                          
            all_dots.add(dots)
            dots.move_to(ORIGIN)
            counter = Tex(f"Frame {i+1}/5")
            counter.next_to(circle, UP)
            if i == 0: 
                self.play(FadeIn(counter))   
                self.play(FadeIn(dots))    
                self.wait(1)       
            else:                        
                self.play(FadeIn(dots, counter), run_time = 0.5)
            self.play(FadeOut(dots, counter), run_time = 0.5)

#        self.wait(0.5)    
        all_dots.move_to(ORIGIN)
        title = Tex(f"Events from all 5 frames")
        title.next_to(circle, UP)     
        self.play(FadeIn(title))       
        self.play(FadeIn(all_dots))       
        
        big_square = Square(side_length=5, color=WHITE, stroke_width=2)
        big_square.move_to(all_dots)
        self.play(FadeIn(big_square))        
        self.play(FadeOut(circle, title))                              

#        self.wait(1) 
        
#        self.play(FadeOut(title))                              
                
        small_squares = VGroup()
        for i in range(-2, 3):
            for j in range(-2, 3):
                square = Square(side_length=1, color=WHITE, fill_opacity=0.0)
                square.move_to(np.array([i*1, j*1, 0]))
                small_squares.add(square)
        small_squares.move_to(big_square)
        self.play(FadeIn(small_squares))       
        big_square.set_stroke(width = 0)                                                    
                        
        num_dots = [0] * 25
        for dott in all_dots:
            for dot in dott:
                if -2.5 < dot.get_center()[0] < 2.5 and -2.5 < dot.get_center()[1] < 2.5:        
                    index_x = int((dot.get_center()[0] + 2.5) // 1)
                    index_y = int((dot.get_center()[1] + 2.5) // 1)
                    index = index_y + index_x * 5
                    num_dots[int(index)] += 1         
                           
#        self.wait(2) 

        all_text = VGroup()
        for i, square in enumerate(small_squares):
            text = Text(str(num_dots[i]), font_size=30, color=WHITE)
            text.move_to(square.get_center())
            all_text.add(text)
            if i in range(5):
                self.play(FadeIn(text))     
            else: 
                self.play(FadeIn(text, run_time = 0.2))     

        self.wait(1)             
        self.play(FadeOut(all_dots)) 
        
        for i, square in enumerate(small_squares):
            opacity_value = num_dots[i] / np.max(num_dots)
            if i in range(5):            
                fade_in = square.animate.set_fill(color=BLUE, opacity=opacity_value)
                fade_out = FadeOut(all_text[i])
                fade_in_out = AnimationGroup(fade_in, fade_out)
                self.play(fade_in_out)
                square.set_stroke(width = 0)                              
            else: 
                fade_in = square.animate.set_fill(color=BLUE, opacity = opacity_value)
                fade_out = FadeOut(all_text[i])            
                fade_in_out = AnimationGroup(fade_in, fade_out)
                self.play(fade_in_out, run_time = 0.2)  
                square.set_stroke(width = 0)                              
#                            
#                self.play(square.animate.set_fill(color=BLUE, opacity=opacity_value), 
#                          run_time = 0.2)   
#                self.play(FadeOut(all_text[i], run_time = 0.2))     
#            square.set(stroke_width = 0)                                      

        title = Tex(f"Final image")
        title.next_to(big_square, UP)    
        self.play(FadeIn(title))                                                                 
        self.wait(5)





