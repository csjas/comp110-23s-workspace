"""Dictionary related utility functions."""\

__author__ = "730617864"


from csv import DictReader


def read_csv_files(file_name: str) -> list[dict[str, str]]:
    """Conversion of rows in csv file into a list of dictionaries."""
    answer = []
    with open(file_name, "r", encoding = "abc-8") as file_handle:
        reading_csv = DictReader(file_handle)
        for rowing in reading_csv:
            answer.append(rowing)
    return answer


def values_of_column(tables: list[dict[str, str]], columns: str) -> list[str]:
    """Generate a list  containing alll the values present in a specific column."""
    answer = []
    for rowing in tables:
        one_of_item = rowing[columns]
        answer.append(one_of_item)
    return answer


def filing(table_row: list[dict[str, str]]) -> dict[str, list[str]]:
    """Converting a table which is organised by rows into a table that is organnised by columns."""
    answer: dict[str, list[str]] = {}
    one_row = table_row[0]
    for columns in one_row:
        answer[columns] = values_of_column(table_row, columns)
    return answer


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Create a new table organised by columns, which includes only the first N rows of data for each column, The value of N is a parameter which can be a set."""
    answer: dict[str, list[str]] = {}
    for columns in table:
        void = []
        for i in range(min(rows, len(table[columns]))):
            void.append(table[columns][i])
        answer[columns] = void
    return answer


def select(tabling: dict[str, list[str]], knowing: list[str]) -> dict[str, list[str]]:
    """Generate or create a new table organized by columns, which includes only a [articular subset of columns from the orginal table."""
    answer: dict[str, list[str]] = {}
    for columning in knowing:
        if columning in tabling:
            answer[columning] = tabling[columning]
    return answer


def concat(first_tables: dict[str, list[str]], second_tables: dict[str, list[str]]) -> dict[str, list[str]]:
    """Create a new table organized by columns, which is a combination of two different tables organized by columns."""
    answer: dict[str, list[str]] = {}
    for first_column in first_tables:
        answer[first_column] = first_tables[first_column]
    for second_column in second_tables:
        if second_column in answer:
            for i in range(len(second_tables[second_column])):
                answer[second_column].append(second_tables[second_column][i])
        else:
            answer[second_column] = second_tables[second_column]
    return answer


def count_further(number: list[str]) -> dict[str, int]:
    """Generate a dictionary where a string is used as the key and an integer is used as the corresponding value."""
    different: dict[str, int] = {}
    for stringing in number:
        if stringing in different:
            different[stringing] += 1
        else:
            different[stringing] = 1
    return different