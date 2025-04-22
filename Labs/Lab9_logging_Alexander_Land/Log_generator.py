import logging
import logging.handlers
import random

logging.basicConfig(
    level= logging.DEBUG, 
    format= '%(asctime)s | %(name)s |%(levelname)s | %(message)s' # idk if asctime works
    )


# loggers
sqldb_Log = logging.getLogger("sql_logger")
sqldb_Log.setLevel(logging.INFO)

frontend_Log = logging.getLogger("frontend")
frontend_Log.setLevel(logging.INFO)

frontend_js_Log = logging.getLogger("frontend.js")
frontend_js_Log.setLevel(logging.INFO)

frontend_flask_Log = logging.getLogger("frontend.flask")
frontend_flask_Log.setLevel(logging.INFO)

frontend_flask_layer_Log = logging.getLogger("frontend.flask.layer")
frontend_flask_layer_Log.setLevel(logging.INFO)

# handlers

sql_handler = logging.handlers.TimedRotatingFileHandler(
    filename= "sql.log",
    when= "D",
    backupCount= 1
)

frontend_handler = logging.handlers.TimedRotatingFileHandler(
    filename= "frontend.log",
    when= "D",
    backupCount= 1
)

frontend_js_handler = logging.handlers.TimedRotatingFileHandler(
    filename= "frontend_js.log",
    when= "D",
    backupCount= 1
)

frontend_flask_handler = logging.handlers.TimedRotatingFileHandler(
    filename= "frontend_flask.log",
    when= "D",
    backupCount= 1
)

frontend_flask_layer_handler = logging.handlers.TimedRotatingFileHandler(
    filename= "frontend_flask_layer.log",
    when= "D",
    backupCount= 1
)

# add the handlers to the loggers
sqldb_Log.addHandler(sql_handler)
frontend_Log.addHandler(frontend_handler)
frontend_js_Log.addHandler(frontend_js_handler)
frontend_flask_Log.addHandler(frontend_flask_layer_handler)
frontend_flask_layer_Log.addHandler(frontend_flask_layer_handler)

# make the log messages

#I asked chat for comedic error messages
list_of_potential_errors = [
    "Something went wrong. Probably your fault.",
    "Uncaught exception in user behavior.",
    "The system has given up. Please proceed manually.",
    "Confidence.exe unexpectedly closed.",
    "Sanity module missing.",
    "Task completion not found.",
    "You\'ve been idle for 3 hours. We assumed you were crying.",
    "Tried to operate before coffee. Not permitted.",
    "Thought process overflowed into dream state.",
    "Recollection of why you walked into the room not available.",
    "No idea what you\'re doing.",
    "Too many browser tabs. One is now sentient.",
    "Too many recursive thoughts.",
    "You can\'t just do that because you feel like it.",
    "Cannot install new personality. Files corrupted.",
    "This seemed like a good idea 3 hours ago.",
    "You argued with someone on the internet.",
    "Connection lost to reality.",
    "Your ambition has been archived or deleted.",
    "Yes, everyone saw that. No, you can\'t undo it."
]
services = ["sqldb", "frontend", "frontend_js", "frontend_flask", "frontend_flask_layer"]

loglevels = ["critical", "error", "warning", "info", "debug"]

def random_error_level(logger, message):
    """takes in the logger and message and gives it a random error level"""
    match random.randint(0,4):
        case 0: logger.critical(message)
        case 1: logger.error(message)
        case 2: logger.warning(message)
        case 3: logger.info(message)
        case 4: logger.debug(message)


# start of main code
for i in range(10):
    random_error_message = list_of_potential_errors[random.randint(0, len(list_of_potential_errors)-1)]
    
    match random.randint(0,4):
        case 0: random_error_level(sqldb_Log, random_error_message)
        case 1: random_error_level(frontend_Log, random_error_message)
        case 2: random_error_level(frontend_js_Log, random_error_message)
        case 3: random_error_level(frontend_flask_Log, random_error_message)
        case 4: random_error_level(frontend_flask_layer_Log, random_error_message)
            
    