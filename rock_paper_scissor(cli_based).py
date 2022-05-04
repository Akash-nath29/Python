#rock scissor paper
import random
from colored import fg , attr

reset=attr('reset')

yellow=fg('yellow')
white=fg('white')
magenta=fg('magenta')
cyan=fg('cyan')
red=fg('red')

print("\t\t Rock Paper Scissor Game\n\t\t  Made with ♡ By Akash")

while True:
    def game():
        user_input=str(input(yellow+"Enter your choice [rock,paper,scissor] :"+reset))
        probable_output=["rock","scissor","paper"]
        system_output=random.choice(probable_output)
        print(magenta+f"System's choice:{system_output.title()}"+reset)
        if user_input.lower()==system_output:
            print(cyan+"Draw"+reset) 
        elif user_input.lower()=="rock" and system_output=="paper":
            print(cyan+"System wins"+reset)
        elif user_input.lower()=="rock" and system_output=="scissor":
            print(cyan+"You win"+reset)
        elif user_input.lower()=="paper" and system_output=="rock":
            print(cyan+"You win"+reset)
        elif user_input.lower()=="paper" and system_output=="scissor":
            print(cyan+"System wins"+reset)
        elif user_input.lower()=="scissor" and system_output=="rock":
            print(cyan+"System wins"+reset)
        elif user_input.lower()=="scissor" and system_output=="paper":
            print(cyan+"You win"+reset)
        else:
            print(red+'Try again'+reset)
            game()
        def end():        
            continuity=str(input(white+"Wanna play again?[Y/N]:"+reset))
            if continuity.lower()=="n":
                print("Thanks for playing")
                exit()
            elif continuity.lower()=='y':
                game()
            else:
                print(red+"Try again"+reset)
                end()
        end()
    game()