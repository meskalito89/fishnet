import doctest


def get_url(url):
    """get_url("some text")
'some text'
geturl('another text')
'anothr text'"""
    print(url)


if __name__ == "__main__":
    doctest.testmod()
