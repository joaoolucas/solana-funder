from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from solana.keypair import Keypair
from base58 import b58decode
from dotenv import load_dotenv
import os
import json
import time
import random

# Load environment variables
load_dotenv()

# Configuration settings
RPC_URL = "https://api.mainnet-beta.solana.com"
AMOUNT_RANGE = {
    "min": 0.1,
    "max": 0.5
}
DELAY_RANGE = {
    "min": 30,
    "max": 120
}

class SolanaWalletFunder:
    def __init__(self, rpc_url, main_wallet_private_key):
        self.client = Client(rpc_url)
        # Convert private key to Keypair
        self.main_wallet = Keypair.from_secret_key(b58decode(main_wallet_private_key))
        
    def get_balance(self, public_key):
        balance = self.client.get_balance(public_key)
        return balance['result']['value'] / 10**9  # Convert lamports to SOL
    
    def send_sol(self, recipient_address, amount_sol):
        try:
            # Create transfer transaction
            transfer_params = TransferParams(
                from_pubkey=self.main_wallet.public_key,
                to_pubkey=recipient_address,
                lamports=int(amount_sol * 10**9)  # Convert SOL to lamports
            )
            
            transaction = Transaction().add(transfer(transfer_params))
            
            # Send and confirm transaction
            result = self.client.send_transaction(
                transaction,
                self.main_wallet
            )
            
            return result['result']
            
        except Exception as e:
            print(f"Error sending transaction: {str(e)}")
            return None

def fund_multiple_wallets(wallets_path):
    # Get private key from environment variable
    private_key = os.getenv('MAIN_WALLET_PRIVATE_KEY')
    if not private_key:
        raise ValueError("MAIN_WALLET_PRIVATE_KEY not found in .env file")
    
    # Load recipient wallets from txt file
    with open(wallets_path, 'r') as f:
        recipients = [line.strip() for line in f if line.strip()]
    
    # Initialize funder
    funder = SolanaWalletFunder(
        RPC_URL,
        private_key
    )
    
    # Check main wallet balance
    main_balance = funder.get_balance(funder.main_wallet.public_key)
    print(f"Main wallet balance: {main_balance} SOL")
    
    # Process each recipient
    for recipient in recipients:
        # Generate random amount within specified range
        amount = random.uniform(
            AMOUNT_RANGE['min'],
            AMOUNT_RANGE['max']
        )
        
        # Send transaction
        print(f"Sending {amount:.4f} SOL to {recipient}")
        tx_sig = funder.send_sol(recipient, amount)
        
        if tx_sig:
            print(f"Transaction successful: {tx_sig}")
        else:
            print(f"Transaction failed for recipient: {recipient}")
        
        # Random delay between transactions
        delay = random.uniform(
            DELAY_RANGE['min'],
            DELAY_RANGE['max']
        )
        print(f"Waiting {delay:.2f} seconds before next transaction...")
        time.sleep(delay)

if __name__ == "__main__":
    fund_multiple_wallets('wallets.txt') 