# antlr_parsing
Antlr parsing for a chat grammar I was experimenting with.

## Setting up the repository (Chat.g4 needs to exist)
antlr4 -Dlanguage=Python3 Chat.g4

After this, you still have to write the listener. In this case, I have a version in `HtmlChatListener.py`. Otherwise, you can modify `ChatListener.py`

## Running the code
`python3 test_chat.py test_input.txt`

Output is in output.html.
