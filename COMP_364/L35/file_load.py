from memory_profiler import profile

@profile
def data_load_list(path, encoding="utf-8"):
    return open(path, "r", encoding=encoding).readlines()

@profile
def lazy_read(path, lines, encoding="utf-8"):
    file_handle = open(path, "r", encoding=encoding)
    line_count = 0
    while line_count < lines:
        yield file_handle.readline()
        line_count += 1

# questions = data_load_list("Questions.csv", encoding="latin-1")

g = lazy_read("Questions.csv", 10, encoding="latin-1")
