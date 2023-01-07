import re

def12 = r"(?<=[\skK])(\d{8})(?![a-zA-Z\d])|(?<=id=)(\d{4,8})(?=\D)"


def extract_matr_ids(text: str) -> list[int]:
    result = list()
    for elem in re.finditer(def12, text):
        result.append(int(elem.group(0)))
    return result
