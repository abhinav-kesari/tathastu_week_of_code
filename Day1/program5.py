player1 = int(input("Enter first player run on 60 balls : "))
player2 = int(input("Enter second player run on 60 balls : "))
player3 = int(input("Enter third player run on 60 balls : "))

# Strike rate
player1_strike_rate = (player1 * 100) / 60
player2_strike_rate = (player2 * 100) / 60
player3_strike_rate = (player3 * 100) / 60

print("Strike rate of each players :\nPlayer1:",player1_strike_rate,"\nPlayer2:",player2_strike_rate,"\nPlayer3:",player3_strike_rate)

print("Run scores if each players play 60 balls more:")
print("Player1 run : ",player1*2)
print("Player2 run : ",player2*2)
print("Player3 run : ",player3*2)

print("Maximum sixes Player1 hits : ",player1//6)
print("Maximum sixes Player2 hits : ",player2//6)
print("Maximum sixes Player3 hits : ",player3//6)
