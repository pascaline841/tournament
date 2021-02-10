#!/usr/bin/env/ python3
# coding:utf-8
from controllers.controller import MainController


def main():
    """Entry method."""
    MainController.start_program()
    app = MainController()
    app.run()


if __name__ == "__main__":
    main()
