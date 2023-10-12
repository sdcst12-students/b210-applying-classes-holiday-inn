class game:
  choices = {'rock':0,'paper':1,'scissors':2,'lizard':3,'spock':4}
  def computerChoice():
    import random
    return random.randint(0,4)
  def playerChoice():
    x = None
    choices = {'rock':0,'paper':1,'scissors':2,'lizard':3,'spock':4,'0':0,'1':1,'2':2,'3':3,'4':4}
    while x not in choices :x = input("\033[0;37;40mEnter a choice: ").strip()
    if x not in choices:print("enter a valid input\n")
    if x == "0" or x == "rock": y = 0
    elif x == "1" or x == "paper": y=  1
    elif x == "2" or x == "scissors": y= 2
    elif x == "3" or x == "lizard": y= 3
    elif x == "4" or x == "spock": y= 4
    else: y= "invalid input"
    return y
  def playerWins(computer,player): 
    if computer == player: i = 0
    elif computer == 0 and player == 1: i = 1
    elif computer == 0 and player == 2: i = -1
    elif computer == 0 and player == 3: i = -1
    elif computer == 0 and player == 4: i = 1
    elif computer == 1 and player == 2: i = 1
    elif computer == 1 and player == 0: i = -1
    elif computer == 1 and player == 3: i = 1
    elif computer == 1 and player == 4: i = -1
    elif computer == 2 and player == 0: i = 1
    elif computer == 2 and player == 1: i = -1
    elif computer == 2 and player == 3: i = -1
    elif computer == 2 and player == 4: i = 1
    elif computer == 3 and player == 0: i = 1
    elif computer == 3 and player == 1: i = -1
    elif computer == 3 and player == 2: i = 1
    elif computer == 3 and player == 4: i = -1
    elif computer == 4 and player == 0: i = -1
    elif computer == 4 and player == 1: i = 1
    elif computer == 4 and player == 2: i = -1
    elif computer == 4 and player == 3: i = 1
    else: i = print("Invalid")
    return i
  print("Enter a Pick in Rock Paper Scissors Lizard Spock\n0 or rock\n1 or paper\n2 or scissors\n3 or lizard\n4 or spock")
  streak = 0
  while True:
    y = playerChoice()
    t = computerChoice()
    if t == 0:print("opponent chose rock.")
    elif t == 1:print("opponent chose paper")
    elif t == 2:print("opponent chose scissors")
    elif t == 3:print("opponent chose lizard")
    elif t == 4:print("opponent chose spock")
    else:print("oh no, an error")
    if playerWins(t,y) == -1:
      print("\033[1;31;40mYou lost")
      streak = 0
    elif playerWins(t,y) == 1:
      print("\033[1;32;40mYou Won")
      streak += 1
    elif playerWins(t,y) == 0:
      print("\033[1;36;40mDraw")
      streak = 0
    if streak == 1:print(f"you have won {streak} once\n\n")
    elif streak == 0:print('You have a streak of 0\n\n')
    else: print(f"you have won {streak} times in a row\n\n")
    def __init__(self):
      pass
g = game()