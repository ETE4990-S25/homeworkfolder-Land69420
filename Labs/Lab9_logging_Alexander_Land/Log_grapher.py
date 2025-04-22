import matplotlib.pyplot as plt

import Log_reader

def log_json_to_graph(filename):
    categories = []
    values = []
    data = Log_reader.loader(filename)

    count_of_errors = {}
    for log_level in data:
        count_of_errors[log_level] = 0
        for error in data[log_level]:
            count_of_errors[log_level] += data[log_level][error]

    for error_level in count_of_errors:
        categories.append(error_level)
        values.append(count_of_errors[error_level])

    plt.bar(categories, values)
    plt.title(f'Number of errors in: {filename}')
    plt.xlabel('Error Levels')
    plt.ylabel('# of errors')


    plt.show()

log_json_to_graph("frontend.json")


