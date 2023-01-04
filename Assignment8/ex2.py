import os


class Reader:

    def __init__(self, path: str):
        self.path = path
        if not os.path.isfile(path):
            print("Error: path must be a file")
            raise ValueError

        self.file = open(path, "rb")

    def close(self):
        self.file.close()

    def __len__(self):
        return os.path.getsize(self.path)

    def __getitem__(self, key):
        if isinstance(key, int):
            if key >= 0:
                if key > self.__len__():
                    raise IndexError("Reader index out of range")
                self.file.seek(key, 0)
            else:
                if -key > self.__len__():
                    raise IndexError("Reader index out of range")
                self.file.seek(key, 2)

            return self.file.read(1)
        else:
            raise TypeError(f"indexing expects 'int', not '{key.__class__.__name__}'")


r = Reader("ex2_data.txt")
print(r.__len__())
print(r[0])
print(r[1])
print(r[-1])
try:
    r["hi"]
except TypeError as e:
    print(f"{type(e).__name__}: {e}")
try:
    r[100]
except IndexError as e:
    print(f"{type(e).__name__}: {e}")
