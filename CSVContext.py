import csv, os
from contextlib import contextmanager


class CSVReader:

    def __init__(self, path):
        self._file_path = path

    def __enter__(self):
        self._file = open(self._file_path, "r")
        reader = csv.reader(self._file)
        for line in reader:
            print(",".join(line))
        return f"\nFile readed from {self._file_path}"

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
        if exc_val:
            raise


@contextmanager
def csv_writer(path, csv_data):
    file = open(path, "a")
    writer = csv.writer(file, delimiter=",")

    if os.access(path, os.F_OK):    # if file don't exist - write columns names
        writer.writerow(csv_data[0])

    for line in csv_data[1:]:
        writer.writerow(line)
    yield
    file.close()


if __name__ == "__main__":
    with CSVReader("books.csv") as csv_r:
        print(csv_r)

    data = ["book_name,author,genre".split(","),
            "The Blazing World,Margaret Cavendish,Science Fiction".split(","),
            "A Game of Thrones,George Martin,Fiction".split(","),
            ]

    with csv_writer("books2.csv", data):
        print("\nFile modified at books2.csv")
