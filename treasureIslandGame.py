import sys

print(r"""
                                __...----..
                             .-'           `-.
                            /        .---.._  \
                            |        |   \  \ |
                             `.      |    | | |        _____
                               `     '    | | /    _.-`      `.
                                \    |  .'| //'''.'            \
                                 `---'_(`.||.`.`.'    _.`.'''-. \
                                    _(`'.    `.`.`'.-'  \\     \ \
                                   (' .'   `-._.- /      \\     \ |
                                  ('./   `-._   .-|       \\     ||
                                  ('.\ | | 0') ('0 __.--.  \`----'/
                             _.--('..|   `--    .'  .-.  `. `--..'
               _..--..._ _.-'    ('.:|      .  /   ` 0 `   \
            .'         .-'        `..'  |  / .^.           |
           /         .'                 \ '  .             `._
        .'|                              `.  \`...____.----._.'
      .'.'|         .                      \ |    |_||_||__|
     //   \         |                  _.-'| |_ `.   \
     ||   |         |                     /\ \_| _  _ |
     ||   |         /.     .              ' `.`.| || ||
     ||   /        ' '     |        .     |   `.`---'/
   .' `.  |       .' .'`.   \     .'     /      `...'
 .'     \  \    .'.'     `---\    '.-'   |
)/\ / /)/ .|    \             `.   `.\   \
 )/ \(   /  \   |               \   | `.  `-.
  )/     )   |  |             __ \   \.-`    \
         |  /|  )  .-.      //' `-|   \  _   /
        / _| |  `-'.-.\     ||    `.   )_.--'
        )  \ '-.  /  '|     ''.__.-`\  | 
       /  `-\  '._|--'               \  `.
       \    _\                       /    `---.
  LGB  /.--`  \                      \    .''''\
       `._..._|                       `-.'  .-. |
                                        '_.'-./.'

    """)



print(f'Welcome To Treasure Island.\nYour mission is to find the treasure')

userInput = input('Do You Want To Go Left Or Right [L or R]?\n')

if userInput == "R":
    print(f'Fall Into A Hole.\nGame Over.')
    sys.exit()
else:
    userInput_1 = input('Will you swim or wait [S or W]?\n')
    if userInput_1 == "S":
        print(f'Attacked by Trout.\nGame Over.')
        sys.exit()
    else:
        userInput_2 = input('Which Door You Want To Go Blue Or Red or Yellow [B or R or Y]?\n')
        if userInput_2 == "R":
            print(f'Burned By Fire.\nGame Over')
            sys.exit
        elif userInput_2 == "B":
            print(f'Eaten By Beasts.\nGame Over')
        elif userInput_2 == "Y":
            print(f'You Win')
        else:
            print(f'Game Over.')


