import re
import json

def readlog(logfilename):
    """reads the log file, parses it, and returns a dict with the number of occurances of each error message at each error level
    It also can return a list of each log if slightly modified."""
    # list_of_logs = [] #unused list that also holds each log
    dict_of_log = {}
    # regex pattern that puls out, the time, log_name, log_level, and message. Chat made the regex but I made everything else based on NGCP code I made
    pattern = r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) \| ([^|]+) \|([A-Z]+) \| (.+)$' 


    try:
        with open(logfilename) as file:
            lines = file.readlines()

            for line in lines: 
                match = re.search(pattern, line) #checks line by line for the regex pattern

                if match:
                    timestamp, log_name, log_level, message = match.groups() # if a line is match it'll section each section of the data into its respective value
                    # list_of_logs.append({"timestamp": timestamp, "log name": log_name, "log level":log_level, "message": message})  #unused list it could output

                    if log_level not in dict_of_log: #adds log level if its not in the dictionary
                        dict_of_log[log_level] = {}
                    
                    if message not in dict_of_log[log_level]: # adds the message if its not in the dictionary at that log level
                        dict_of_log[log_level][message] = 0

                    dict_of_log[log_level][message] += 1 #since the log level and message are in the dict with the above part, this will increment it every time that message shows up
    except Exception as e: # I learned this neat way of handling erros so it'll print the error if something happens when opening the file
        print(f"error {e}")

    return dict_of_log


def save_to_json(dictionary,filename): 
    """takes dict and dumps it in json file"""
    with open(filename, 'w') as json_file:
        json.dump(dictionary, json_file, indent=4)

def loader(filename): 
    """opens json file, prints it readibly, then returns it as a dict"""
    with open(filename) as file:
        data = json.load(file)
        neater_data = json.dumps(data, indent=2)
        print(neater_data)
    return data


save_to_json(readlog("frontend.log"), "frontend.json")
loader("frontend.json")

