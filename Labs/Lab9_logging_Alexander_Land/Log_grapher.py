import matplotlib.pyplot as plt
import json

#loader from log reader
def loader(filename):
    """opens json file, prints it readibly, then returns it as a dict"""
    with open(filename) as file:
        data = json.load(file)
        neater_data = json.dumps(data, indent=2)
        print(neater_data)
    return data

def log_json_to_graph(filename):
    """opens json log file and graphs the number of errors at each error level"""
    categories = []
    values = []
    data = loader(filename)

    # makes a dictionary that is indexed at error level and keeps track of the number of errors at that level
    count_of_errors = {}
    for log_level in data: 
        count_of_errors[log_level] = 0  # for each log level make a key with a value of 0
        for error in data[log_level]:  
            count_of_errors[log_level] += data[log_level][error]    
            #for each error message it'll check how many times it occurs and increment that number to whichever log level its currently iterating through

    for error_level in count_of_errors: # puts the keys from counter_of_errors dictionary as catagores and values as values
        categories.append(error_level)
        values.append(count_of_errors[error_level])

    # plots a bar graph for the data
    plt.bar(categories, values)
    plt.title(f'Number of errors in: {filename}')
    plt.xlabel('Error Levels')
    plt.ylabel('# of errors')

    plt.show()

log_json_to_graph("frontend.json")


