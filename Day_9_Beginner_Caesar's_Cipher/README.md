******Overview******
The Caesar Cipher program is a Python-based tool for encrypting and decrypting messages using the Caesar cipher technique. The program allows users to input a message, a shift amount, and choose whether to encrypt or decrypt the message. The Caesar cipher technique involves shifting each letter in the message by a fixed number of positions down the alphabet.

**Features**
**1. Input Text**
Description: Users can input a text message that they want to encrypt or decrypt.
Input: The message can include letters (both uppercase and lowercase), numbers, and special characters.
Output: The entered text is processed for encryption or decryption.

**2. Shift Amount**
Description: Users specify a positive integer that determines the number of positions each letter in the message is shifted.
Input: A positive integer.
Output: The entered shift amount is used in the cipher operation.

**3. Cipher Direction**
Description: Users can choose to either encrypt or decrypt the message.
Input: The user specifies "encrypt" or "decrypt" when prompted.
Output: The program performs the selected cipher operation.

**4. Caesar Cipher Algorithm**
Description: The program utilizes the Caesar cipher algorithm to shift the letters in the message according to the shift amount and direction.
Input: The text message, shift amount, and cipher direction.
Output: The result of the encryption or decryption operation.

**5. ASCII Art Start Message**
Description: The program displays an ASCII art message at the start to enhance user experience.
Input: None.
Output: An ASCII art message is presented at the beginning of the program.

**6. Interactive User Experience**
Description: The program provides an interactive experience, allowing users to repeat the cipher operation multiple times.
Input: User choice to continue or exit after each operation.
Output: The program processes multiple cipher operations based on user input.

**7. Input Validation**
Description: The program validates user input, including the shift amount and cipher direction.
Input: User input for shift amount and direction.
Output: Feedback for invalid input and guidance for re-entering valid values.

**Assumptions and Constraints**
1.Users are expected to provide a text message to encrypt or decrypt.
2.The shift amount must be a positive integer.
3.The cipher direction should be either "encrypt" or "decrypt."
4.The program is designed to work with both uppercase and lowercase letters and preserves the case of the original text.
5.Non-alphabetic characters, such as numbers and special symbols, remain unchanged during the cipher operation
