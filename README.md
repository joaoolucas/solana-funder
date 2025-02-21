# Solana Wallet Funder

A Python script for automatically distributing SOL to multiple wallet addresses with randomized amounts and timing between transactions.

## Features

- Send SOL to multiple wallet addresses automatically
- Randomized transaction amounts within a configurable range
- Random delays between transactions to avoid pattern detection
- Secure private key management using environment variables
- Simple wallet address management using a text file
- Balance checking before transactions
- Detailed transaction logging

## Requirements

- Python 3.6+
- `solana` Python package
- `python-dotenv`
- `base58`

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install solana python-dotenv base58
   ```

## Configuration

### Environment Variables
1. Copy `.env.example` to `.env`:
   ```
   cp .env.example .env
   ```

2. Edit `.env` and add your main wallet's private key

### Recipient Wallets
Add recipient wallet addresses to `wallets.txt`, one address per line:

```
RECIPIENT_WALLET_ADDRESS_1
RECIPIENT_WALLET_ADDRESS_2
RECIPIENT_WALLET_ADDRESS_3
```

### Transaction Settings
In `main.py`, you can modify these constants to adjust the behavior:

- `AMOUNT_RANGE`: Amount range for each transaction in SOL
- `DELAY_RANGE`: Delay range between transactions in seconds
- `RPC_URL`: Solana RPC URL (default is mainnet-beta)

## Usage

Run the script:

```
python main.py
```

The script will:
1. Check the main wallet's balance
2. Read recipient addresses from wallets.txt
3. For each recipient:
   - Generate a random SOL amount within the configured range
   - Send the transaction
   - Wait for a random delay before the next transaction
4. Log all transaction results to the console

## Security Notes

- Never commit your `.env` file
- Keep your private key secure
- Test with small amounts first
- Consider using a dedicated wallet for funding operations
- Monitor your transactions to ensure everything works as expected

## Error Handling

The script includes error handling for:
- Missing environment variables
- Invalid wallet addresses
- Failed transactions
- Insufficient balance
- Network issues

## Example Output

```
Main wallet balance: 10.5 SOL
Sending 0.2345 SOL to ADDRESS1
Transaction successful: 5KPVxVELSKrx...
Waiting 45.32 seconds before next transaction...
```

## Contributing

Feel free to submit issues and pull requests.
Pay me a coffee: jnmA7qig7BqzeyqRFy93Ys9rGEHPP5F4fjn1zydSXTt

## Credits

Made by mortiee.
Discord: mortiee
Twitter: @0xliberato
