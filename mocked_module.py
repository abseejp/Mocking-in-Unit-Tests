
# Please note that both convert_to_upper() in utility.py and mocked_function() below are kept simple in this example to illustrate the concept of mocking. However, in real-world scenarios, these functions could be much more complex, and mocked_function() will have its own complexities that we're not interested in when testing convert_to_upper().


def mocked_function():
    # Function implementation goes here
    return "External function result"