class UserInterface:
    def __init__(self):
        self.log_entries = []

    def input_log_file(self, file_path):
        with open(file_path, 'r') as log_file:
            for line in log_file:
                self.log_entries.append(line)

    def view_statistics(self):
        statistics = log_level_statistics(self.log_entries)
        # Display statistics to the user

    def view_summary(self):
        summary = time_interval_summary(self.log_entries)
        # Display summaries to the user
