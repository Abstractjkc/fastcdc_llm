import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

from gear_table import GEAR_TABLE
def analyze_randomness(data):
    data = np.array(data, dtype=np.uint64)
    n = len(data)
    MAX_VAL = 2**64
    
    print(f"样本量: {n}")
    
    # 1. 均值检验
    actual_mean = np.mean(data)
    theoretical_mean = (MAX_VAL - 1) / 2
    print(f"实际均值: {actual_mean:.2e}")
    print(f"理论均值: {theoretical_mean:.2e}")
    print(f"偏差比: {abs(actual_mean - theoretical_mean) / theoretical_mean:.4%}")

    # 2. 卡方检验 (划分为 100 个桶)
    num_bins = 100
    counts, _ = np.histogram(data, bins=np.linspace(0, MAX_VAL - 1, num_bins + 1, dtype = np.float64))
    expected_count = n / num_bins
    chi_stat, p_val = stats.chisquare(counts, f_exp=[expected_count] * num_bins)
    print(f"\n卡方检验 (Bins={num_bins}):")
    print(f"p-value: {p_val:.4f} ({'显著均匀' if p_val > 0.05 else '分布不均'})")

    # 3. 比特分布分析
    bit_counts = np.zeros(64)
    for val in data:
        # 统计每个 bit 位上 1 的个数
        binary = bin(val)[2:].zfill(64)
        for i in range(64):
            if binary[63-i] == '1':
                bit_counts[i] += 1
    
    bit_ratios = bit_counts / n
    print(f"\n比特位分布 (前 5 位): {bit_ratios[:5]}")
    print(f"比特位分布 (后 5 位): {bit_ratios[-5:]}")
    print(f"比特位最大偏差: {np.max(np.abs(bit_ratios - 0.5)):.4%}")

    # 4. 可视化
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.bar(range(num_bins), counts)
    plt.title("Value Distribution (Histogram)")
    
    plt.subplot(1, 2, 2)
    plt.plot(range(64), bit_ratios, 'ro-')
    plt.axhline(0.5, color='k', linestyle='--')
    plt.title("Bit-level Frequency (Ideal 0.5)")
    plt.ylim(0.4, 0.6)
    plt.savefig('pic/randomness_test.png')
    print("\n分布图已保存为 pic/randomness_test.png")

# 使用示例 (替换为你自己的数据)
my_data = GEAR_TABLE
analyze_randomness(my_data)
