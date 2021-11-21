# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
import os

from bit import PrivateKeyTestnet

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
from constants import *
# YOUR CODE HERE
 
 
# Create a function called `derive_wallets`
def derive_wallets(coin):
    command = f"php ./derive --mnemonic={mnemonic} --coin={coin} --numderive={numderive} --format=json -g" # YOUR CODE HERE
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

print(derive_wallets(ETH))

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = ""# YOUR CODE HERE

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account():
    # YOUR CODE HERE
    a = 1

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx():
    # YOUR CODE HERE
    a = 1

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx():
    # YOUR CODE HERE
    a = 1

