# Original block reward for miners was 50 BTC = 50 0000 0000 Satoshis
# 報酬
start_block_reward = 50 * 10**8
# 210000 is around every 4 years with a 10 minute block interval
# 4年ごとに半減していく予定
reward_interval = 210000

# 総額を計算するための関数
def max_money():
    # 報酬
    current_reward = start_block_reward
    total = 0

    while current_reward > 0:
        total += reward_interval * current_reward
        current_reward /= 2
    return total

/# 関数を呼び出し
print("Total BTC to ever be created:", max_money(), "Satoshis")