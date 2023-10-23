
# Password Generator

1.Introduction

Designe Python program to create secure and random passwords for users. It generates passwords by combining letters, symbols, and numbers according to user-specified parameters.

2. User Input and Parameters

The program begins by welcoming the user and prompting them to provide the following parameters for their password:
Number of letters (nr_letters)
Number of symbols (nr_symbols)
Number of numbers (nr_numbers)
3. Password Generation

The program generates the password based on the user's parameters by combining characters from the following character sets:

Letters: a-z (both lowercase and uppercase)
Symbols: !, #, $, %, &, (, ), *, +
Numbers: 0-9
It uses the random module to select characters randomly from each character set according to the specified counts


4. Password Composition
The program appends the randomly selected characters to a list called 'password.'
The password is constructed in the following order:
Letters
Symbols
Numbers

5. Password Security
To enhance the security of the generated password, the program shuffles the characters in the 'password' list to ensure a random order.

6. Output
The program displays the generated password as the final output. The user receives a secure and random password based on their input.

7. Usage
Users can execute the program to create passwords based on their desired combination of letters, symbols, and numbers.

8. Future Enhancements
Possible enhancements include allowing users to specify password length and customize character sets for more advanced requirements.

9. Conclusion
The Password Generator provides a simple yet effective solution for creating secure passwords with various combinations of characters. It enhances the user's ability to generate strong and random passwords for improved online security.