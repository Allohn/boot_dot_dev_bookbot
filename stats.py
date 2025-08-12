from pathlib import Path


def get_book_word_count(relative_book_file_path: str) -> int:
    """
    Read a text file and count the number of words in the document.

    Args:
        relative_book_file_path (str): Path to the text file.

    Returns:
        int: {num_words} words found in the document.
    """
    try:
        with Path(relative_book_file_path).open(
            "r", encoding="utf-8"
        ) as open_book_file:
            # String containing the full text of the .txt file
            book_contents = open_book_file.read()
            # List of strings containing each work of the full text
            book_contents_word_split = book_contents.split()
            book_word_count = len(book_contents_word_split)

            return book_word_count

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {relative_book_file_path}")

    except OSError as error_code:
        raise RuntimeError(
            f"Error reading file {relative_book_file_path}: {error_code}"
        )


def book_character_count(relative_book_file_path: str) -> dict:
    """
    Read a text file and count the number of occurrences of each character in the document.

    Args:
        relative_book_file_path (str): Path to the text file.

    Returns:
        dict: A dictionary of str -> int which gives the integer number of occurences of each character.
    """
    try:
        with Path(relative_book_file_path).open(
            "r", encoding="utf-8"
        ) as open_book_file:
            # String containing the full text of the .txt file
            book_contents = open_book_file.read()

            # Create a list of unique characters in the book
            book_characters = list(book_contents.lower())
            unique_characters = list(set(book_characters))

            # Loop over the unique characters and count their occurrences. Store in a dictionary with a dictionary comprehension.
            character_dictionary = {
                char: book_characters.count(char)
                for char in unique_characters
                if char.isalpha()
            }

            return character_dictionary

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {relative_book_file_path}")

    except OSError as error_code:
        raise RuntimeError(
            f"Error reading file {relative_book_file_path}: {error_code}"
        )


def book_sorted_character_list(character_count_dictionary: dict) -> list:
    """
    Create a more generic list of dictionaries with {"char": str, "num": int} for each character in the input dictionary.

    Args:
        character_count_dictionary: Dictionary with characters as keys and their counts as values.

    Returns:
        list: A sorted list of dictionaries of the form {"char": str, "num": int}.
    """
    # Create a list of dictionaries with {"char": str, "num": int} for each character in the input dictionary
    character_list = [
        {"char": char, "num": num} for char, num in character_count_dictionary.items()
    ]

    # Sort the list by the "num" key in descending order
    character_list.sort(reverse=True, key=sort_by_num_key)

    return character_list


def sort_by_num_key(items: dict[str, int]) -> int:
    """Key for .sort() method to sort a dictionary by its values.

    Args:
        items (dict): A dictionary with a "num" key.

    Returns:
        int: The value of the "num" key.
    """

    # Add an exception for when the key does not exist
    # Add an exception for when the value is not an integer
    # Add an exception for when the items is not a dictionary
    return items["num"]
