import csv
from contextlib import contextmanager


class CSV():

    def __init__(self, path):
        self._file_path = path
        self._file = open(self._file_path, "a")

    def __enter__(self):
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
        if exc_val:
            raise


@contextmanager
def csv_d(path):
    file = open(path, "a")
    yield file
    file.close()


data = ["book_name,author,genre".split(","),
        "The Blazing World,Margaret Cavendish,Science Fiction".split(","),
        "A Game of Thrones,George Martin,Fiction".split(","),
        ]

if __name__ == "__main__":
    with CSV("res/csv/books.csv") as csv_c:
        writer = csv.writer(csv_c, delimiter=",")
        for line in data:
            writer.writerow(line)

    with csv_d("res/csv/books2.csv") as csv_def:
        writer = csv.writer(csv_def, delimiter=",")
        for line in data:
            writer.writerow(line)
