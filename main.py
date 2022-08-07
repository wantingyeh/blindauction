from replit import clear
from art import logo

## print a logo as the header
print(logo)

## create an empty dictionary to 
bid_log = {}

## Check who can get the highest bid
def find_higest_bidder(bidding_record):
  # For example: bidding record = {"Tina": 42, "Eric": 20}
  # when looping thru a dictionary, it also loops through the keys
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")  

## Looping the questions
is_continue = True  
while is_continue:
  bid_name = input("What is your name: ")
  bid_money = int(input("What is your bid?: $"))
  bid_log[bid_name] = bid_money

  bid_continue = input("Are there any other bidders? Yes/No.\n").lower()
  if bid_continue == "yes":
    clear()
  else:
    is_continue = False
    clear()
    find_higest_bidder(bid_log)




  
