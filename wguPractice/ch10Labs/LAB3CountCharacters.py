def count_character_in_phrase(character, phrase):
    count = phrase.count(character)
    if count == 1:
        return f"{count} {character}"
    else:
        return f"{count} {character}'s"


if __name__ == '__main__':
    input_string = input()
    character, phrase = input_string[0], input_string[1:].strip()
    print(count_character_in_phrase(character, phrase))