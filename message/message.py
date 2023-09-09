"""message module"""

class Content:
    """Content"""

    def __get__(self, obj, objtype=None):
        return self.value
    
    def __set__(self, obj, value):
        if len(value) == 0:
            raise ValueError("Content cannot be empty")
        self.value = value

class Author:
    """Author"""

    def __get__(self, obj, objtype=None):
        return self.value
    
    def __set__(self, obj, value):
        if len(value) == 0:
            raise ValueError("Author cannot be empty")
        self.value = value

class Message:
    """Message class"""

    content = Content()
    author = Author()

    def __init__(self, content, author):
        self._id = None
        self.content = content
        self.author = author