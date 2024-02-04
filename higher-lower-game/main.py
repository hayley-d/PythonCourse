logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

from game_data import data
import random

print(logo)
lives = 1
while lives > 0:
    data1 = data[random.randint(0, len(data) - 1)]
    data2 = data[random.randint(0, len(data) - 1)]
    print(f"Compare A: {data1['name']}, a {data1['description']} from {data1['country']}.")
    print(vs)
    print(f"Compare B: {data2['name']}, a {data2['description']} from {data2['country']}.")
    answer = input("who has more followers? Type 'A' or 'B': ")
    if answer.upper() == "A" and data1['follower_count'] > data2['follower_count'] or answer.upper() == "B" and data1['follower_count'] < data2['follower_count']:
        print("Round Complete, next round")
    elif answer.upper() == "A" and data1['follower_count'] < data2['follower_count'] or answer.upper() == "B" and data1['follower_count'] > data2['follower_count']:
        print("Round Lost")
        lives = 0
