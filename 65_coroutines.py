def searcher():
    import time
    # some 4 secs time consuming task
    book = "This is a book on elliot and his cyber security life"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("Search started")
next(search)
print("Next method run")
search.send("elliot")
input("press any key")
search.send("cyber")
input("press any key")
search.send("alderson")

search.close()
# search.send("something else")