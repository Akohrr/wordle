### WORDLE ###
num_trials = 6
trial = 0
plays = [" " * 5 for _ in range(num_trials)]
choice = random.choice(lines).upper()
print(choice)
while trial < num_trials:
    word = input("Enter a 5 letter word (type exit to quit): ").upper()
    if word == 'EXIT':
        print("Exit successful")
        break
    if len(word) != 5:
        print("\n" + Back.RED + " Error: Please enter a 5 letter word " + Style.RESET_ALL+"\n")
        continue
    
    plays[trial] = word
    print("|-----"*5 + "|")
    for play in plays:
        for idx in range(len(play)):
            if play[idx] == " ":
                print(f"|  {play[idx]}  ", end="")
            elif play[idx] in choice and play[idx] == choice[idx]:
                print("|" + Back.GREEN + f"  {play[idx]}  ", end="" + Style.RESET_ALL)
            elif play[idx] in choice and play[idx] not in play[:idx]:
                print("|" + Back.YELLOW + f"  {play[idx]}  ", end="" + Style.RESET_ALL)
            else:
                print("|" + Back.LIGHTWHITE_EX + f"  {play[idx]}  ", end="" + Style.RESET_ALL)
        print("|",end="")
        print()
        for _ in play:
            print("|-----", end="")
        print("|",end="")
        print()
    
    trial += 1
