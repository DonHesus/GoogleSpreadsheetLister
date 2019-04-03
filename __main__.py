"""Main execution script for the List maker"""
import logging

from application import Application


def main():
    try:
        application = Application()
        application.run()
    except Exception as e:
        logging.exception(e)
        exit(1)


if __name__ == '__main__':
    main()
