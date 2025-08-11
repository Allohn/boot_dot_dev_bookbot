from pathlib import Path
import argparse


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
            return open_book_file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {relative_book_file_path}")
    except OSError as error_code:
        raise RuntimeError(
            f"Error reading file {relative_book_file_path}: {error_code}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Display the contents of a book in a plaintext format."
    )
    parser.add_argument(
        "relative_path_to_book",
        help="Path to the book text file. Try the books/ directory",
    )
    args = parser.parse_args()

    book_contents = get_book_text(args.book_path)
    print(book_contents)


if __name__ == "__main__":
    main()
