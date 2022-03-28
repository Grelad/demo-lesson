"""Class decorator"""


class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("ABC", self.func(*args, **kwargs), "XYZ", sep="")


@Decorator
def function(alphabet):
    return alphabet


function("...MNO...")
