#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Family application class."""

from src.json_database import JsonDatabase
from src.person import Person
from pprint import pprint as pp


class FamilyApplication:

    APPLICATION_NAME = 'Application: FAMILY'
    LINE_LENGTH = 50
    DATABASE_NAME = 'family'
    DATABASE_DIR = 'databases/'

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

    def get_menu_option_from_strem(self):
        """Get option from stream."""
        is_incorrect = True
        while is_incorrect:
            option_number = input('Select option [1-5]: ')
            if option_number.isdigit():
                option_number = int(option_number)
                if option_number in [1, 2, 3, 4, 5]:
                    is_incorrect = False
                else:
                    print('Option number must by from 1 to 5.')
                    self.print_line()
            else:
                print('Option number must by an integer number.')
                self.print_line()
        self.print_line()
        return option_number

    def get_all_family_persons(self):
        """Display all persons in family."""
        print('ALL PERSONS IN FAMILY')
        family_db = JsonDatabase(self.DATABASE_NAME, self.DATABASE_DIR)
        pp(family_db.fetch_all())
        self.print_line()

    def get_family_person(self):
        """Display person in family."""
        print('PERSON IN FAMILY')
        is_incorrect = True
        while is_incorrect:
            person_id = input('Type person id: ')
            if person_id.isdigit():
                is_incorrect = False
            else:
                print('Person id must be an integer number')
        family_db = JsonDatabase(self.DATABASE_NAME, self.DATABASE_DIR)
        pp(family_db.fetch(int(person_id)))
        self.print_line()

    def add_new_person_to_family(self):
        """Add new person to family"""
        print('ADD NEW PERSON TO FAMILY')
        family_db = JsonDatabase(self.DATABASE_NAME, self.DATABASE_DIR)
        new_person = Person()
        new_person.set_firstname(input('Type firstname: '))
        new_person.set_lastname(input('Type lastname: '))
        new_person.set_age(input('Type age: '))
        new_person.set_height(input('Type height: '))
        new_person.set_weight(input('Type weight: '))
        new_person_json = new_person.get_person_like_json()
        family_db.add(new_person_json)
        family_db.save()
        print('Person added')
        self.print_line()

    def remove_family_person(self):
        """Remove person from family."""
        print('REMOVE PERSON')
        is_incorrect = True
        while is_incorrect:
            person_id = input('Type person id: ')
            if person_id.isdigit():
                is_incorrect = False
            else:
                print('Person id must be an integer number')
        family_db = JsonDatabase(self.DATABASE_NAME, self.DATABASE_DIR)
        if family_db.delete(int(person_id)):
            family_db.save()
            print('Person removed')
        self.print_line()

    def close_app(self):
        """Close application."""
        print('CLOSE APPLICATION')
        self.print_line()

    def print_line(self):
        """Print line."""
        print('-' * self.LINE_LENGTH)

application = FamilyApplication()
application.run()
