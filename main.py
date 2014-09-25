'''
widget dragging
================

This is an example of easily creating a simple draggable widget.
Will sometimes unexpectedly drop the widget, but is still very functional.

Author@ Joshua Cox
'''

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
        
class Box(FloatLayout):
    
    def __init__(self, **kwargs):
        super(Box, self).__init__(**kwargs)
        
        # create a button and add it to the layout
        button1 = Button(text='zoom zoom!', size_hint=(None, None), size=(100,50), pos=(100,100))
        button2 = Button(text='zoom zoom!', size_hint=(None, None), size=(100,150), pos=(300, 300))
        self.add_widget(button1)
        self.add_widget(button2)
        
        # make an exclusive list so we can control who can be dragged
        self.draggableWidgets = [] 
        self.draggableWidgets.append(button1)
        self.draggableWidgets.append(button2)
    
    def on_touch_move(self, value):
        x = value.pos[0]
        y = value.pos[1]
        
        for widget in self.draggableWidgets:
            if widget.collide_point(x,y): # true if the touch is inside the widget's bounding box
                widget.center = (x, y)
        
class DragApp(App):

    def build(self):    
        return Box()

if __name__ == '__main__':
    DragApp().run()
