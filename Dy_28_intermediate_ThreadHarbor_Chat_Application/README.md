****ThreadHarbor - Chat Application****

**Introduction**

ThreadHarbor is a chat application that leverages the power of Python's threading, ThreadPoolExecutor, Producer-Consumer pattern, and thread-local data to create a concurrent and interactive messaging platform.

**Functional Requirements**

**1. User Registration**

Users can register in ThreadHarbor by entering their name.

The application waits for user input and stores the user's name using thread-local data.

**2. Message Sending**
After registration, users can send messages.

Messages are produced by a thread and added to a shared message queue.

The application waits for the user's name to be obtained before allowing message sending.

**3. Message Receiving**

ThreadHarbor has a consumer thread that continuously checks the message queue for new messages.

Upon receiving a message, the consumer prints the message to the console, indicating the producer and consumer IDs.


**4. Exiting the Chat**

Users can exit the chat by typing 'exit' as a message.

Exiting the chat removes the user's name from the connected users set.

The consumer receives a signal to exit upon receiving the 'exit' message.

**5. Listing Connected Users**

Users can type 'list' as a message to see the list of connected users.

The list of connected users is displayed in the console.

**6. Thread Synchronization**

Proper thread synchronization is implemented to avoid race conditions.

Locks and events are used to ensure the correct flow of execution between threads.


**7. ThreadPoolExecutor Usage**

ThreadPoolExecutor is utilized for concurrently running threads for message sending and receiving.

The application creates and manages threads efficiently using ThreadPoolExecutor.

**8. Graceful Application Termination**

ThreadHarbor terminates gracefully, ensuring all threads finish their tasks before exiting.

**9. User Experience**

ThreadHarbor provides a clear and user-friendly console interface for user interaction.

Appropriate prompts and messages guide users in using the chat application.

**10. Time Stamping**

Messages include a timestamp indicating the time when the message was sent.
