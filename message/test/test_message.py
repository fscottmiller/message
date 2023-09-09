from message.message import Message
import pytest

# typical use case for new message
def test_new_message():
    content = "you're reading this"
    author = "an author"
    message = Message(content=content, author=author)
    assert message.author == author
    assert message.content == content

# message without content is not allowed
def test_new_message_contains_empty_content():
    with pytest.raises(ValueError):
        message = Message(content="", author="an author")

# message without author is not allowed
def test_new_message_without_author_should_fail():
    with pytest.raises(ValueError):
        message = Message(content="something", author="")
