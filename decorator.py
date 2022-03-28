"""Simple decorator module"""

# Добавить вызов декоратора без синтаксического сахара


# Example #1
from functools import wraps


def embellish_the_story(func):
    """
    Decorator which expands the story.

    Function which is responsible for embellishing the story.

    :param func: decorated function
    :return: wrapped function
    """
    def wrapper(*args, **kwargs):
        """wrapper function"""
        print(
            "Once upon a time...",
            func(),
            "The End.",
            sep="\n"
        )
    return wrapper


@embellish_the_story
def story_telling():
    return "Very very short story."


story_telling()
print("-------------")


# Example #2
def embellish_the_beginning(func):
    """
    Decorator which expands the beginning.

    Function which is responsible for embellishing the beginning of the story.

    :param func: decorated function
    :return: wrapped function
    """
    def wrapper(*args, **kwargs):
        """wrapper function"""
        print(f"Once upon a time...")
        func()
    return wrapper


def embellish_the_end(func):
    """
    Decorator which expands the end of the story.

    Function which is responsible for embellishing the end of the story.

    :param func: decorated function
    :return: wrapped function
    """
    def wrapper(*args, **kwargs):
        """wrapper function"""
        func()
        print(f"The End.")
    return wrapper


@embellish_the_beginning
@embellish_the_end
def another_story():
    print("Very very short story.")


another_story()


def cached(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        ca = cache.get(args)
        if ca:
            print("Value was cached")
            print(ca)
        else:
            print("Value should be calculated")
            calculated = func(*args)
            print(calculated)
            cache[args] = calculated

    return wrapper


@cached
def calc(a, b):
    return a + b


calc(1, 5)  # calculated 6
calc(1, 5)  # cached 6
calc(1, 5)  # cached 6
