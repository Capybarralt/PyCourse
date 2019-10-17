from configparser import ConfigParser
import sqlite3
import os
import pkg_resources
import shutil

from lesson_utils.app_utils import get_config_dir, get_data_dir


def make_config(*config_files):
    config = ConfigParser()
    config.read(config_files)
    return config


def make_default_config():
    filename = os.path.join(
        get_config_dir(__package__), # !!!!
        'config.ini'
    )

    if not os.path.exists(filename):
        default = pkg_resources.resource_filename(__name__, 'resources/config.ini')
        shutil.copyfile(default, filename)

    return make_config(filename)


config = make_default_config()


def make_connection(name='db'):
    """Возвращает объект-подключения к БД SQLite"""
    db_name = os.path.join(
        get_data_dir(__package__), #!!!!
        config.get(name, 'db_name')
    )

    conn = sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row

    return conn
