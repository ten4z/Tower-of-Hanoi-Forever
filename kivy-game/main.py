"""
Desenvolvido por Josiel Soares
visite minha home page: http://www.josielsoares.com
Foi usado o Kivy Framework
Foi usado a linguagem de programação Python
Com ambiente miniconda e sistema operacional Linux Mint 22.04
este projeto está na versão 1.0a
O Ziga "eu aqui" desejo melhorar este App
este arquivo pode ser usado por você se quiser
continuar por si próprio o projeto.
No entanto pretendo finalizar este projeto 
adicionando animações e validando os movimentos.
Agora tem o layout base da torre de hanói
e um drag and drop do primeiro rectangle do Kivy
Você pode encontrar este mesmo projeto na 
seção de Downloads de minha Home Page.
Se você é novo por aqui: Seja Bem Vindo! 
Se você já é chegado: Fique à vontade!
Valeeeu!
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line
from random import random
class DrawingWidget(Widget):
    def __init__(self):
        super(DrawingWidget, self).__init__()
        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.rect_colour = Color(1, 0, 0, 1)  # note that we must reset the colour
            #pino 1
            Color(0.1,0.1,0.1, 1)
            Rectangle(size=(20, 220),
                      pos=(200, 120))        
            Rectangle(size=(260, 20),
                      pos=(80, 100))
            # pino 2
            Color(0.1,0.1,0.1, 1)
            Rectangle(size=(20, 220),
                      pos=(500, 120))
            Rectangle(size=(260, 20),
                      pos=(380, 100))
            # pino 3
            Color(0.1,0.1,0.1, 1)
            Rectangle(size=(20, 220),
                      pos=(800, 120))
            Rectangle(size=(260, 20),
                      pos=(680, 100))
            for k in range(10):
                Color(random(), random(), random(), 0.85)
                self.n_rect = Rectangle(size=(230-20*k, 20),
                      pos=((195+20*k)/2, 20*k+120))
        self.bind(pos=self.update_rectangle, size=self.update_rectangle)
    def mover_default_rect(self, tx, ty):
        self.n_rect.pos = [tx, ty]
    def update_rectangle(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size
    def on_touch_down(self, touch):
        super(DrawingWidget, self).on_touch_down(touch)
        with self.canvas:
            Color(random(), random(), random(), 0.7)
            self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)
    def on_touch_move(self, touch):
        self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]
        #print("touch_x: ", touch.x, "touch_y: ", touch.y)
        self.mover_default_rect(touch.x, touch.y)
class Ziga_Hanoi_Game(App):
    def build(self):
        App.title = "Ziga Torre de Hanói"
        Window.size = (1024,520)
        root_widget = DrawingWidget()
        return root_widget
if __name__ == "__main__":
    Ziga_Hanoi_Game().run()