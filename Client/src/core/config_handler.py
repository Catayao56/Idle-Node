# -*- coding: utf-8 -*-

import os
import sys

import time
import base64

# from core import aes

class ConfigHandler:
    """
    class ConfigHandler():
        The class containing methods to use the configuration file.
    """

    def __init__(self, config_path="data/config.dat"):
        """
        def __init__():
            The initialization method for ConfigHandler() class.
        """

        self.config_path = config_path
        # self.cipher = aes.AESCipher()

    def _open_config_file(self):
        """
        def _open_config_path():
            Open the config file.
        """

        try:
            with open(self.config_path, 'r') as fopen:
                data = fopen.read()

        except(FileNotFoundError, IOError, EOFError,
                PermissionError, IsADirectoryError):
            raise IOError("Error reading the configuration file!")

        else:
            # print(data)  # DEV0005
            try:
                data = base64.b64decode(data)

            except(TypeError, ValueError, UnicodeDecodeError):
                raise IOError("The configuration file is corrupt or decrypted!")

            else:
                try:
                    return str(data.decode())

                except(TypeError, ValueError,UnicodeDecodeError):
                    raise IOError("The configuration file is corrupt or decrypted!")

    def _save_config_file(self, config_data):
        """
        def _save_config_file():
            Save the config file.
        """

        try:
            with open(self.config_path, 'w') as fopen:
                data = fopen.write('')

        except(FileNotFoundError, IOError, EOFError,
               PermissionError, IsADirectoryError):
            raise IOError("Error writing to the configuration file!")

        else:
            try:
                with open(self.config_path, 'w') as fopen:
                    data = fopen.write(base64.b64encode(config_data.encode()).decode())

            except(FileNotFoundError, IOError, EOFError,
                   PermissionError, IsADirectoryError):
                raise IOError("Error writing to the configuration file!")

            else:
                return 0

    def get(self, data=None):
        """
        def get():
            Get data from config file.
        """

        contents = self._open_config_file()

        if data is None:
            return contents.split('\n')

        else:
            # print(contents)  # DEV0005
            contents = contents.split('\n')

            for content in contents:
                # print(content)  # DEV0005
                if content.startswith('#'):
                    continue

                elif content.startswith(data + '='):
                    # print("\t\t\tb: ", content)  # DEV0005
                    # This if-else statement below is *specially* for booleans.
                    # DEV0001: Might introduce bugs in the future!
                    if content.replace('\n', '').partition('=')[2].lower() == "true":
                        return True

                    elif content.replace('\n', '').partition('=')[2].lower() == "false":
                        return False

                    elif content.replace('\n', '').partition('=')[2].isdigit():
                        return int(content.replace('\n', '').partition('=')[2])

                    elif content.replace('\n', '').partition('=')[2].replace('.', '').isdigit():
                        return float(content.replace('\n', '').partition('=')[2])

                    elif content.replace('\n', '').partition('=')[2] == "None":
                        return None

                    else:
                        return content.replace('\n', '').partition('=')[2]

                else:
                    continue


    def set(self, variable=None, value=None):
        """
        def set():
            Set a new value for `variable`.
        """

        if variable is None or value is None:
            return 11

        else:
            try:
                variable = str(variable)
                value = str(value)

            except(TypeError, ValueError):
                return 11

            else:
                contents = self._open_config_file().split('\n')
                new_config = []
                for content in contents:
                    # print(content)  # DEV0005
                    if content.startswith('#'):
                        new_config.append(content)

                    elif content.startswith(variable + '='):
                        new_config.append(variable + '=' + value)

                    elif content == "":
                        new_config.append('')

                    else:
                        new_config.append(content)

                result = ""
                for line in new_config:
                    # print('`' + line + '`')  # DEV0005
                    if line == "":
                        result += ''

                    else:
                        result += line + '\n'

                # print(result)  # DEV0005
                try:
                    self._save_config_file(result)

                except Exception as error:
                    print(error)
                    return 1

                else:
                    return 0
