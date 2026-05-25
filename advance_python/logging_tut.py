# This is where you stop writing "print("Hello world")" and start writing "logging.error("DB Error")"
# Why logging matters:
# Imagine: your AI backend crashes at 3 AM. You are not there.
# How will you know:
# - where it crashed
# - why it crashed
# - which user caused it
# - which API failed
# - which model failed
# That is why logging exists. Not for users. For ENGINEERS.\

#------------------------------------------------------------|
#          Python logging has levels:                        |
#------------------------------------------------------------|
#   Levels             |                  Meaning            |
#------------------------------------------------------------|
# 1) DEBUG             |           Deep developer debugging  |
# 2) INFO              |           Normal system events      |
# 3) WARNING           |           Something suspicious      |
# 4) ERROR             |           Something failed          |
# 5) CRITICAL          |           System may die            |
#------------------------------------------------------------|

# Example:
# import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("AI System started")
# logging.warning("Credits running low")
# logging.error("Model API failed")

# THIS: print("User logged in") Only prints on screen
# BUT THIS: logging.info("User logged in") can:
# save to files, save to cloud, save to monitoring systems, track timestamps, track failures, scale to millions of events.

# CODING TASK: Write a simple AI system logger:
# Requirements: import logging, configure logging
# create: info log, warning log, error log
# Scenario: simulate- AI started, credits low, API failed
# import logging as log
# log.basicConfig(level=log.INFO)
# log.info("AI started")
# log.warning("Credits low")
# log.error("API failed")

# A good real customised log
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(asctime)s | %(message)s" 
)
logging.info("AI server started")

# CODING TASK
# Create: class AIServer:
# Requirements: use logging, custom logging format 
# create methods: start_server(), low_credit_warning(), model_crash()
# Each method should use correct logging level.
# Example:
# server start → INFO
# low credits → WARNING
# model crash → ERROR or CRITICAL\
import logging as log
class AIServer:
    log.basicConfig(
        level=log.INFO,
        format="%(levelname)s | %(asctime)s | %(message)s"
    )
    def start_server(self):
        log.info("Server started")
    def low_credit_warning(self):
        log.warning("Low credit")
    def model_crash(self):
        log.error("Model crashed")
a = AIServer()
a.start_server()
a.low_credit_warning()
a.model_crash()

# MINI CHALLENGE 
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
    force=True
)
class AIModel:
    def load_model(self):
        logging.info("model loaded")
    def generate_response(self):
        logging.info("response generated")
    def crash_model(self):
        try:
            print(10/0)
        except ZeroDivisionError as e:
            logging.error(f"model crashed: {e}")
a = AIModel()
a.load_model()
a.generate_response()
a.crash_model()