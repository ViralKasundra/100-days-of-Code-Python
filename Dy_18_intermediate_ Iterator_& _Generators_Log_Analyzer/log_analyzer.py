from log_parser import LogParser
from statistics_generator import log_level_statistics, time_interval_summary
from user_interface import UserInterface

def main():
    # Initialize the user interface
    ui = UserInterface()

    # Input log file
    log_file_path = "example.log"
    ui.input_log_file(log_file_path)

    # Calculate statistics
    statistics = log_level_statistics(ui.log_entries)
    ui.view_statistics(statistics)

    # Generate summary
    summary = time_interval_summary(ui.log_entries)
    ui.view_summary(summary)

if __name__ == "__main__":
    main()
