def num_words(text):
    words = text.split()

    return len(words)

def num_chars(text):
    chars = {}
    for char in text:
        char = str.lower(char)
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(items):
    return items["num"]


def sort_chars(things):
    list_of_things = []
    for thing in things:
        new_thing = {"name": thing, "num":things[thing]}
        list_of_things.append(new_thing)
    list_of_things.sort(reverse=True, key=sort_on)
    return(list_of_things)


#def sort_chars(chars):
