class LogParser:
    def __init__(self, log_file):
        self.log_file = log_file

    def __iter__(self):
        return self

    def __next__(self):
        line = self.log_file.readline()
        if not line:
            raise StopIteration
        # Implement your log parsing logic here
        return line
