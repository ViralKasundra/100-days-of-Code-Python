import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor

# Shared message queue
message_queue = queue.Queue()

# Event to signal that the user's name has been obtained
name_obtained_event = threading.Event()

# Lock for synchronization
lock = threading.Lock()

# Variable to store the user's name
user_name = None

# Set to store connected users
connected_users = set()

# Function to get user's name
def get_user_name():
    global user_name
    name = input("Enter your name: ")
    with lock:
        user_name = name
        connected_users.add(user_name)
        name_obtained_event.set()  # Signal that the name has been obtained

# Producer function to send messages
def send_message(producer_id):
    name_obtained_event.wait()  # Wait for the user's name to be obtained
    with lock:
        name = user_name
    while True:
        time.sleep(2)
        message = input("Enter your message (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            message_queue.put(None)  # Signal consumer to exit
            connected_users.remove(name)
            break
        elif message.lower() == 'list':
            print("Connected Users:", ', '.join(connected_users))
            continue
        formatted_message = f"{name} ({time.strftime('%H:%M:%S')}): {message}"
        message_queue.put((producer_id, formatted_message))

# Consumer function to receive messages
def receive_messages(consumer_id):
    while True:
        message = message_queue.get()
        if message is None:
            break  # Exit on signal from producer
        producer_id, received_message = message
        print(f"\nReceived by Consumer-{consumer_id} from Producer-{producer_id}: {received_message}")

# Main function
def main():
    # Create and start a thread to get the user's name
    name_thread = threading.Thread(target=get_user_name)
    name_thread.start()

    # Create and start threads for sending and receiving messages using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(send_message, 1)
        executor.submit(receive_messages, 1)

    # Wait for the name thread to finish
    name_thread.join()

if __name__ == "__main__":
    print("Welcome to the Chat Application using ThreadPoolExecutor, Producer-Consumer Pattern, and Thread-local Data!")
    main()