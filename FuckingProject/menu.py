import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.HowToPlayx, self.HowToPlayy = self.mid_w, self.mid_h + 60
        self.Exitx, self.Exity = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty+20)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text("Start Game", 30, self.startx, self.starty+20)
            self.game.draw_text("HowToPlay", 30, self.HowToPlayx, self.HowToPlayy+40)
            self.game.draw_text("Exit", 30, self.Exitx, self.Exity+60)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.HowToPlayx + self.offset, self.HowToPlayy+40)
                self.state = 'HowToPlay'
            elif self.state == 'HowToPlay':
                self.cursor_rect.midtop = (self.Exitx + self.offset, self.Exity+60)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty+20)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.Exitx + self.offset, self.Exity+60)
                self.state = 'Exit'
            elif self.state == 'HowToPlay':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty+20)
                self.state = 'Start'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.HowToPlayx + self.offset, self.HowToPlayy+40)
                self.state = 'HowToPlay'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'HowToPlay':
                self.game.curr_menu = self.game.HowToPlay
            elif self.state == 'Exit':
                self.game.curr_menu = self.game.Exit
            self.run_display = False

class HowToPlayMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('HowToPlay', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class ExitMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        pygame.quit()
        #self.run_display = True
        #while self.run_display:
        #    self.game.check_events()
        #   if self.game.START_KEY or self.game.BACK_KEY:
        #       self.game.curr_menu = self.game.main_menu
        #        self.run_display = False
        #    self.game.display.fill(self.game.BLACK)
            #self.game.draw_text('Exit', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            #self.game.draw_text('Made by me', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            
        #   self.blit_screen()