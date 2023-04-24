import re


def normalize_t2f(text: str):
    """
    Normalize text to float number from a specific format
    Actual number format 35.122,26 -> Normalize to 35122.26
    :param text: A text number with a specific format
    :return: A float number
    """
    regex = r"(\d+)(\.)(\d+)(\,)(\d+)"
    if re.search(regex, text):
        normalized_nb = float(text.replace('.', '').replace(',', '.'))
        return normalized_nb
    return 0.0
