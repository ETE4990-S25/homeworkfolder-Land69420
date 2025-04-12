import logging
import logging.handlers

logging.basicConfig(
    level= logging.DEBUG, 
    format= '%(asctime)s | %(name)s |%(levelname)s | %(message)s' # idk if asctime works
    )

# services = ["sqldb", "frontend", "frontend_js", "frontend_flask", "rontend_flask_layer"]

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

