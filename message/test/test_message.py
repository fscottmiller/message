from message.message import Message

def test_message_empty_strings():
    message = Message(contents="",author="")
    assert message.author == ""
    assert message.contents == ""

def test_message_empty_contents():
    message = Message(contents="", author="User")
    assert message.author == "User"
    assert message.contents == ""

def test_message_empty_author():
    message = Message(contents="something", author="")
    assert message.contents == "something"
    assert message.author == ""