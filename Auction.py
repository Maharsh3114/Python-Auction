print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
bids = {}
bidding_finished = False

def highest(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
           highest_bid = bid_amount
           winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not  bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid? $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
  if should_continue == "no":
      bidding_finished = True
      highest(bids)
  elif should_continue == "yes":
      bidding_finished = False
  else:
      print("Invalid input program exited")
      exit()
