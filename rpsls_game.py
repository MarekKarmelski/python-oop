#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rpsls.lizard import Lizard
from rpsls.rock import Rock
from rpsls.real_player import RealPlayer
from rpsls.ai_player import AiPlayer

"""RPSLS game."""


class RPSLSGame:

    APPLICATION_NAME = 'Application: FAMILY'
    LINE_LENGTH = 50

    def run(self):
        run_app = True
        """Run application."""
        self.display_app_name()
        self.display_app_menu()
        while run_app:
            option = self.get_menu_option_from_strem()
            if option == 1:
                self.get_all_family_persons()
                self.display_app_menu()
            elif option == 2:
                self.get_family_person()
                self.display_app_menu()
            elif option == 3:
                self.add_new_person_to_family()
                self.display_app_menu()
            elif option == 4:
                self.remove_family_person()
                self.display_app_menu()
            elif option == 5:
                self.close_app()
                run_app = False

    def display_app_name(self):
        """Display application name."""
        self.print_line()
        print(self.APPLICATION_NAME)
        self.print_line()

    def display_app_menu(self):
        """Display application menu."""
        print('MENU:')
        print('1. Show all family persons')
        print('2. Show family person')
        print('3. Add person')
        print('4. Remove person')
        print('5. Close application')
        self.print_line()

    def close_app(self):
        """Close application."""
        print('CLOSE APPLICATION')
        self.print_line()

    def print_line(self):
        """Print line."""
        print('-' * self.LINE_LENGTH)

rpsls_game = RPSLSGame()
#rpsls_game.run()

ala = 'ala'
ma_kota = 'ma kota'

print('ala'.join('kota'))

#rock = Rock
#rock2 = Rock

#print(rock == rock2)
