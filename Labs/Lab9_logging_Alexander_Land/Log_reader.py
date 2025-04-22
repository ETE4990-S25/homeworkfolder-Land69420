import re
import json

def readlog(logfilename):
    list_of_logs = []
    dict_of_log = {}
    pattern = r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) \| ([^|]+) \|([A-Z]+) \| (.+)$'

    try:
        with open(logfilename) as file:
            lines = file.readlines()

            for line in lines:
                match = re.search(pattern, line)

                if match:
                    timestamp, log_name, log_level, message = match.groups()
                    list_of_logs.append({"timestamp": timestamp, "log name": log_name, "log level":log_level, "message": message})  

                    if log_level not in dict_of_log:
                        dict_of_log[log_level] = {}
                    
                    if message not in dict_of_log[log_level]:
                        dict_of_log[log_level][message] = 0

                    dict_of_log[log_level][message] += 1
    except Exception as e:
        print(f"error {e}")

    return dict_of_log


def save_to_json(dictionary,filename):
    with open(filename, 'w') as json_file:
        json.dump(dictionary, json_file, indent=4)

def loader(filename):
    with open(filename) as file:
        data = json.load(file)
        neater_data = json.dumps(data, indent=2)
        print(neater_data)
    return data

save_to_json(readlog("frontend.log"), "frontend.json")
loader("frontend.json")

