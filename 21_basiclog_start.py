# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging
import sys

def main():
    # TODO: Use basicConfig to configure logging
    # to show all logs include debug and info
    # to specify a local text file to save the logs
    # to 
    logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode='w')

    # Try out each of the log levels
    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")

    # TODO: Output formatted strings to the log
    logging.info("Python in verson: %s", sys.version.split()[0])


if __name__ == "__main__":
    main()
