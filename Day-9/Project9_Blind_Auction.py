from replit import clear

from Project9_art import logo,congratulation
print(logo)

bids={}
bidding_finished=False

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(congratulation)
    print(f"\nThe winner is {winner} with a bid of ₹{highest_bid}")

while not bidding_finished:
    bidder_name=input("Enter you name: ")
    bidding_price=int(input("Enter the bidding price ₹"))
    bids[bidder_name]=bidding_price
    should_continue=input("Are there are any other bidders? yes or no: ")
    if should_continue=="no":
        bidding_finished=True
        find_highest_bidder(bids)
    elif should_continue=="yes":
        '''FAQ: My console doesn't clear()
        This will happen if you’re using an IDE other than replit.'''
        clear()
    else:
        bidding_finished = True


