

class Color:
    @staticmethod
    def red(string):
        return '\033[31m' + string + '\033[0m'

    @staticmethod
    def green(string):
        return '\033[32m' + string + '\033[0m'

    @staticmethod
    def orange(string):
        return '\033[33m' + string + '\033[0m'

    @staticmethod
    def blue(string):
        return '\033[34m' + string + '\033[0m'

    @staticmethod
    def purple(string):
        return '\033[35m' + string + '\033[0m'
