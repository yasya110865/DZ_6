import os
import sys
import victory
def create_dir(name):
        if not os.path.exists(name):
            os.mkdir(name)
        return os.path.exists(name)
def rem_dir(name):
    if os.path.exists(name):
        os.rmdir(name)
        return True
    elif not os.path.exists(name):
        return False

def test_create_dir():
    assert create_dir('test2') == True

def test_rem_dir():
    rem_dir('test2') == True

def test_get_login():
    assert os.getlogin() == 'user-1'

def test_victory():
    assert victory.victory(1, '14.03.1879') == True


