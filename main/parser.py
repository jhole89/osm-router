from argparse import ArgumentParser
import os


class AppParser(ArgumentParser):
    def __init__(self):
        """
        Cmd line arg parser

        """
        super().__init__()

    def register_args(self):
        """
        Registers the required arguments

        :return: self
        """
        self.add_argument("file_path", type=self._valid_path, help="Path of graph file")
        self.add_argument("start_node", type=str, help="Origin node to route from")
        self.add_argument("end_node", type=str, help="Destination node to route to")
        return self

    @staticmethod
    def _valid_path(value):
        """
        Checks if path provided is a valid path on local filesystem

        :param value: location on filesystem
        :return: absolute location on filesystem
        """
        abs_path = os.path.abspath(value)
        if not os.path.exists(abs_path):
            raise OSError
        return abs_path
