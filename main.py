from pathlib import Path


def get_book_text(relative_book_file_path: str) -> str:
    """
    Read and return the full contents of a text file.

    Args:
        relative_book_file_path (str): Path to the text file.

    Returns:
        str: file
    """
    try:
        with Path(relative_book_file_path).open(
            "r", encoding="utf-8"
        ) as open_book_file:
            # Return the full text of the book
            return open_book_file.read()

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {relative_book_file_path}")

    except OSError as error_code:
        raise RuntimeError(
            f"Error reading file {relative_book_file_path}: {error_code}"
        )


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


def main() -> None:
    # Print all of the book contents
    # book_contents = get_book_text("books/frankenstein.txt")
    # print(book_contents)

    # Print a list of the main text split into words
    book_word_count = get_book_word_count("books/frankenstein.txt")
    print(f"{book_word_count} words found in the document")


if __name__ == "__main__":
    main()
