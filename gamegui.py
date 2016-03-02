#!/usr/bin/env python


import random
import Tkinter as Tk
import tkFont
from mysterious import GuessNumber


__version__ = '1.0.0'


class GameGUI(Tk.Tk, object):

    def __init__(self, game):
        super(GameGUI, self).__init__()
        self.gameplay = game
        self.title('Guess the Number')
        self.canvas = Tk.Canvas(self, width=640, height=360)
        self.canvas.grid(row=0)

        self.answer = []
        self.status = 'splash'
        self.result = None
        self.history = []
        self.half_life = game.lives // 2

        self.big_font = tkFont.Font(family="SketchRockwell", size=96)
        self.med_font = tkFont.Font(family="SketchRockwell", size=72)
        self.reg_font = tkFont.Font(family="SketchRockwell", size=48)
        self.small_font = tkFont.Font(family="SketchRockwell", size=24)
        self.pico_font = tkFont.Font(family="SketchRockwell", size=18)

        self.bind(sequence="<Any-KeyPress>", func=self.input)
        self.splash_screen()



    def splash_screen(self):
        self.canvas.delete()
        self.canvas.create_rectangle(0, 130, 100, 230, fill='#33B5E5', outline='#33B5E5', 
                                activefill='#0099CC', activeoutline='#0099CC', tags='splash')
        self.canvas.create_rectangle(100, 93, 200, 193, fill='#AA66CC', outline='#AA66CC', 
                                activefill='#9933CC', activeoutline='#9933CC', tags='splash')
        self.canvas.create_rectangle(200, 146, 300, 246, fill='#99CC00', outline='#99CC00', 
                                activefill='#669900', activeoutline='#669900', tags='splash')
        self.canvas.create_rectangle(300, 115, 400, 215, fill='#FFBB33', outline='#FFBB33', 
                                activefill='#FF8800', activeoutline='#FF8800', tags='splash')
        self.canvas.create_rectangle(400, 128, 500, 228, fill='#FF4444', outline='#FF4444', 
                                activefill='#CC0000', activeoutline='#CC0000', tags='splash')

        self.canvas.create_text(50, 172, text='g', font=self.big_font, fill='white', tags='splash')
        self.canvas.create_text(150, 140, text='u', font=self.big_font, fill='white', tags='splash')
        self.canvas.create_text(250, 193, text='e', font=self.big_font, fill='white', tags='splash')
        self.canvas.create_text(350, 162, text='s', font=self.big_font, fill='white', tags='splash')
        self.canvas.create_text(450, 175, text='s', font=self.big_font, fill='white', tags='splash')
        self.canvas.create_text(530, 250, text='numbers', font=self.reg_font, fill='black', tags='splash')
        self.canvas.create_text(320, 52, text='Will Skywalker\'s', font=self.small_font, 
                           fill=random.choice(('#0099CC','#9933CC','#669900','#FF8800','#CC0000')), 
                           tags='splash')
        self.canvas.create_text(320, 330, text='Press Space to start', font=self.small_font, 
                           fill='#555555', tags='splash')
        self.bind(sequence="<space>", func=self.start_game)


    def start_game(self, keys=None):
        self.status = 'ingame'
        self.draw_guess()


    def draw_guess(self):
        self.canvas.delete('splash', 'game')
        self.bind(sequence="<Return>", func=self.check)
        for i, num in enumerate(self.answer):
            self.canvas.create_text(100*i+100, 120, text=str(num), font=self.big_font, fill='#333333', tags='game')
        self.canvas.create_text(560, 30, text='Lives: '+str(self.gameplay.lives), font=self.small_font, fill='#336688', tags='game')
        for i, h in enumerate(self.history[:-11:-1]):
            self.canvas.create_text(560, 20*i+120, text=h[0]+'  '+h[1], font=self.pico_font, 
                fill='#000000', tags='game')
        if self.result:
            self.canvas.create_text(220, 290, text=str(self.result[0])+'A', font=self.reg_font, 
                fill=random.choice(('#0099CC','#9933CC','#669900','#FF8800','#CC0000')), tags='game')
            self.canvas.create_text(300, 290, text=str(self.result[1])+'B', font=self.reg_font, 
                fill=random.choice(('#0099CC','#9933CC','#669900','#FF8800','#CC0000')), tags='game')


    def check(self, keys=None):
        if len(self.answer) != 4:
            return
        result = self.gameplay.guess(self.answer)
        # print result, self.answer, self.gameplay.answer
        if result in ('win', 'lose'):
            self.result = None
            if result == 'win':
                self.gameplay.lives += self.half_life
            self.endgame_screen(result)
        else:
            self.result = result
            self.history.append((''.join(self.answer), str(result[0])+'A'+str(result[1])+'B'))
            self.answer = []
            self.draw_guess()


    def endgame_screen(self, result):
        self.answer = []
        self.history = []
        self.status = 'splash'
        self.canvas.delete('splash', 'game')
        self.canvas.create_text(320, 100, text='You '+str(result), font=self.big_font, fill='#336688', tags='splash')
        self.canvas.create_text(320, 330, text='Press Space to start', font=self.small_font, 
                           fill='#555555', tags='splash')
        self.bind(sequence="<space>", func=self.start_game)



    def input(self, key):
        # print key.keysym
        if self.status == 'ingame':
            if key.keysym in '123456789' and len(self.answer) < 4:
                self.answer.append(key.keysym)
            elif key.keysym == 'BackSpace' and len(self.answer) >=  1:
                self.answer.pop(-1)
            elif key.keysym == 'Return':
                self.check()
            self.draw_guess()





if __name__ == '__main__':
    example = GameGUI(GuessNumber())
    example.mainloop()

