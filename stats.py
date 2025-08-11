from pathlib import Path


def get_book_word_count(relative_book_file_path: str) -> int:
    """
    Read a text file and count the number of words in the document.

    Args:
        relative_book_file_path (str): Path to the text file.

    Returns:
        str: {num_words} words found in the document.
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
