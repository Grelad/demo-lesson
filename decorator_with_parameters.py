"""Decorator with parameters module"""


def add_chapter_with_embellishing_the_story(chapter: int):
    """
    Decorator which expands the story.

    Function which is responsible for embellishing the story with chapter number, beginning and the end of the story.

    :param chapter: gets int value of the chapter
    :return: wrapped function
    """
    print(f"Chapter {chapter}\n")

    def embellish_the_story(func):
        """
        inner decorator which expands the story.

        Function which is responsible for embellishing the story.

        :param func: decorated function
        :return: wrapped function
        """

        def wrapper(*args, **kwargs):
            """wrapper function"""
            print(
                f"Once upon a time...",
                func(*args, **kwargs),
                "The End.",
                sep="\n"
            )
        return wrapper
    return embellish_the_story


@add_chapter_with_embellishing_the_story(1)
def story_telling(story: int):
    return story


story_telling("Very very short story.")
