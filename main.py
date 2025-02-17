def count_words(file_contents) -> int:
    """
    Counts the number of words in the given text.
    """
    return len(file_contents.split())

def count_character(file_contents: str) -> dict:
    """
Counts the occurrences of each character in the given text.

Converts the input text to lowercase and calculates the frequency
of each character, returning a dictionary with characters as keys
and their counts as values.

Args:
    file_contents (str): The text to analyze.

Returns:
    dict: A dictionary where keys are characters and values are their
    respective counts in the text.
"""
    count_char = {}
    standardized_text = file_contents.lower()
    for char in standardized_text:
        count_char[char] = count_char.get(char, 0) + 1
    return count_char

def count_alpha(file_contents: str) -> dict:
    """
Counts the occurrences of each alphabetic character in the given text.

Converts the input text to lowercase and counts each alphabetic character,
ignoring non-alphabetic characters. Returns a dictionary with characters
as keys and their counts as values.

Args:
    file_contents (str): The text to analyze.

Returns:
    dict: A dictionary with alphabetic characters as keys and their
    respective counts as values.
"""
    count_alpha = {}
    standardized_text = file_contents.lower()
    for char in standardized_text:
        if char.isalpha():
            count_alpha[char] = count_alpha.get(char, 0) + 1
    return count_alpha

def main():
    """Reads a text file and prints character counts."""
    file_path = '/Users/siddharth/bootdev/workspace/github.com/Sidd1218/bookbot/books/frankenstein.txt'
    
    with open(file_path, 'r') as f:
        file_contents = f.read()
    
    total_characters = count_character(file_contents)
    alphabetic_characters = count_alpha(file_contents)
    
    print(total_characters)
    print(alphabetic_characters)
    print("Alphabetic Character Counts:")
    print(alphabetic_characters)


if __name__ == "__main__":
    main()