#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pathlib import Path

"""JsonDatabase class."""


class JsonDatabase:

    DEFAULT_DB_DIR = 'databases/'
    DB_PREFIX = 'db_'
    DEFAULT_DB_NAME = 'default'
    DB_FILE_EXTENSION = 'json'
    DB_START_INCREMENT_ID = 0

    __db_dir = None
    __db_file_name = None
    __db_file_path = None
    __db_name = None
    __db_data = {}

    def __init__(self, db_name=None, db_dir=None):
        """Init or if database exist open."""
        if db_name is not None and isinstance(db_name, str):
            self.set_db_name(db_name)
        else:
            self.set_default_db_name()
        if db_dir is not None and isinstance(db_dir, str):
            self.set_db_dir(db_dir)
        else:
            self.set_default_db_dir()
        self.set_db_file_name()
        self.set_db_file_path()
        self.connect_db()

    def set_default_db_name(self):
        """Set default databse name."""
        self.__db_name = self.DB_PREFIX + self.DEFAULT_DB_NAME

    def set_db_name(self, db_name):
        """Set database name."""
        self.__db_name = self.DB_PREFIX + db_name

    def set_default_db_dir(self):
        """Set default databse dir."""
        self.__db_dir = self.DEFAULT_DB_DIR

    def set_db_dir(self, db_dir):
        """Set database dir."""
        self.__db_dir = db_dir

    def set_db_file_name(self):
        """Set database file name."""
        self.__db_file_name = self.__db_name + '.' + self.DB_FILE_EXTENSION

    def set_db_file_path(self):
        """Set database file path."""
        self.__db_file_path = self.__db_dir + self.__db_file_name

    def connect_db(self):
        """Connection to database."""
        db_file = Path(self.__db_file_path)
        if db_file.is_file():
            self.open_db(self.__db_file_path)
        else:
            self.init_db(self.__db_file_path)

    def open_db(self, db_path):
        """Open database."""
        with open(db_path, 'r') as db_file:
            self.__db_data = {int(key): value for key, value in json.load(db_file).items()}

    def init_db(self, db_path):
        """Init database."""
        with open(db_path, 'w+') as db_file:
            json.dump({}, db_file)

    def fetch_all(self):
        """Get all data from database."""
        return self.__db_data

    def fetch(self, increment_id=None):
        """Get data from database by increment_id."""
        if increment_id is not None and isinstance(increment_id, int) and increment_id in self.__db_data.keys():
            return self.__db_data[increment_id]
        else:
            print('Can\'t fetch data. Incorrect id')
            return False

    def flush_db(self):
        """Clear databse."""
        self.__db_data = {}
        self.save()

    def add(self, json_string):
        """Add data do database."""
        key = self.get_next_key()
        self.__db_data[key] = json_string
        return self

    def update(self, increment_id=None, json_string=''):
        """Update data in database by increment_id."""
        if increment_id is not None and isinstance(increment_id, int) and increment_id in self.__db_data.keys():
            self.__db_data[increment_id] = json_string
        else:
            print('Can\'t update. Incorrect id')
            return False
        return self

    def delete(self, increment_id=None):
        """Delete data in database by increment_id."""
        if increment_id is not None and isinstance(increment_id, int) and increment_id in self.__db_data.keys():
            del self.__db_data[increment_id]
        else:
            print('Can\'t delete. Incorrect id')
            return False
        return self

    def save(self):
        """Save data to database file."""
        with open(self.__db_file_path, 'w') as db_file:
            json.dump(self.__db_data, db_file)

    def get_last_key(self):
        """Get last increment_id."""
        key_list = list(self.__db_data.keys())
        if len(key_list) > 0:
            last_key = int(max(list(self.__db_data.keys()), key=lambda a: int(a)))
        else:
            last_key = self.DB_START_INCREMENT_ID
        return last_key

    def get_next_key(self):
        """Get next increment_id."""
        return self.get_last_key() + 1

"""persons_json_db = JsonDatabase('persons', '../databases/')
persons_json_db.fetch_all()
persons_json_db.add("{'name': 'a'}").save()
persons_json_db.add("{'name': 'b'}").save()
persons_json_db.delete(12).save()
persons_json_db.update(16, "{'name': 'kotek'}").save()
persons_json_db.flush_db()
pp(persons_json_db.fetch_all())"""