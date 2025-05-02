# Original block reward for miners was 50 BTC
start_block_reward = 50
# 210_000 blocks, approximately 4 years at 10 minutes per block
reward_interval = 210_000

def max_money():
    # 1 BTC = 100_000_000 satoshis
    current_reward = start_block_reward * 100_000_000
    total = 0
    while current_reward > 0:
        total += reward_interval * current_reward
        # Halve the mining reward using integer division.
        # This discards any fractional satoshis, matching the Bitcoin protocol's halving calculation.
        current_reward //= 2
    return total

print("Total BTC to ever be created:", max_money(), "satoshis")
