import time

def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def game_over(message="Game Over."):
    print_slow(message)
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        start_game()
    else:
        print_slow("Thanks for playing!")

def start_game():
    print_slow('''
                              _
                          ,--.\`-. __
                        _,.`. \:/,"  `-._
                    ,-*" _,.-;-*`-.+"*._ )
                   ( ,."* ,-" / `.  \.  `.
                  ,"   ,;"  ,"\../\  \:   \
                 (   ,"/   / \.,' :   ))  /
                  \  |/   / \.,'  /  // ,'
                   \_)\ ,' \.,'  (  / )/
                       `  \._,'   `"
                          \../
                          \../
                ~        ~\../           ~~
         ~~          ~~   \../   ~~   ~      ~~
    ~~    ~   ~~  __...---\../-...__ ~~~     ~~
      ~~~~  ~_,--'        \../      `--.__ ~~    ~~
  ~~~  __,--'              `"             `--.__   ~~~
~~  ,--'                                         `--.
  '------......______             ______......------` ~~
  ~~~   ~    ~~      ~ `````---"""""  ~~   ~     ~~
       ~~~~    ~~  ~~~~       ~~~~~~  ~ ~~   ~~ ~~~  ~
    ~~   ~   ~~~     ~~~ ~         ~~       ~~   
             ~        ~~       ~~~       ~
''')

    print_slow("Welcome to the Choose Your Own Adventure game! In this game, you'll be faced with different scenarios and choices that will determine your fate. You'll have to use your wit and strategy to navigate through the challenges and reach the end goal. Are you ready to embark on this adventure? Let's begin!")

    f_choice = input(
        '\nYou\'re at a crossroad. Where do you want to go? Type "left" or "right": ').strip().lower()
    
    if f_choice == "left":
        s_choice = input(
            "\nYou've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across: ").strip().lower()
        
        if s_choice == "wait":
            t_choice = input(
                '\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?: ').strip().lower()
            
            if t_choice == "red":
                game_over("It's a room full of fire.")
            elif t_choice == "yellow":
                print_slow("Congratulations! You found the treasure. You Win!")
            elif t_choice == "blue":
                game_over("You enter a room of beasts.")
            else:
                print_slow("Please enter a valid choice.")
                start_game()
        
        elif s_choice == "swim":
            game_over("You get attacked by an angry trout.")
        else:
            print_slow("Please enter a valid choice.")
            start_game()
    
    elif f_choice == "right":
        game_over("You chose a path that doesn't exist.")
    
    else:
        print_slow("Please enter a valid choice.")
        start_game()

start_game()
