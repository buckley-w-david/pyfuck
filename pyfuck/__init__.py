import inspect
from pyfuck.brainfuck_interpreter import BrainfuckInterpreter

from functools import wraps

def brainfuck(f):
    @wraps(f)
    def inner(*args):
        source = f.__doc__
        BrainfuckInterpreter.execute(source)

    return inner
