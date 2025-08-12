from pathlib import Path
from stats import get_book_word_count, book_character_count, book_sorted_character_list


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


def main() -> None:
    # Print a list of the main text split into words
    book_word_count = get_book_word_count("books/frankenstein.txt")
    book_character_dictionary = book_character_count("books/frankenstein.txt")
    book_sorted_character_count_list = book_sorted_character_list(
        book_character_dictionary
    )

    print(
        """============ BOOKBOT ============"""
        + """\nAnalyzing book found at books/frankenstein.txt..."""
        + """\n----------- Word Count ----------"""
        + f"""\nFound {book_word_count} total words"""
        + """\n----------- Character Count ----------"""
    )
    for i in range(len(book_sorted_character_count_list)):
        print(
            f"{book_sorted_character_count_list[i]['char']}: {book_sorted_character_count_list[i]['num']}"
        )
    print("============= END ===============")


if __name__ == "__main__":
    main()
