#silent auction problem
import os

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS or Linux
    else:
        os.system('clear')


print("*********Welcome to Silent Auction*********")
bids={"owner":0}
flag=False
while not flag:
    name=input("enter bidder name")
    bids[name]=int(input("enter bid amount :"))

    next=input("Are there any bidders? type 'yes' or 'no' " )


    if next.lower()=="no":
        flag=True
    else:
        flag=False
        clear_terminal()


def max_bid(bids):
    max=bids["owner"]
    bidder="owner"
    for keys in bids:
        if max<bids[keys]:
            max=bids[keys]
            bidder=keys


    print(f'the winner is {bidder} with a bid of {max}')

max_bid(bids)



