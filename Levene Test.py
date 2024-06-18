from statistics import mean, variance
from scipy.stats import levene

group1 = [1,3,4,5,7]
group2 = [2,5,8,9]

stat, p_value = levene(group1, group2)

# Output the results
print(f"mean group 1: {mean(group1)}")
print(f"variance group 1: {variance(group1)}")
print(f"mean group 2: {mean(group2)}")
print(f"variance group 2: {variance(group2)}")
print(f"Test Statistic: {stat}")
print(f"P-Value: {p_value}")

# Decision rule
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: Variances are not equal.")
else:
    print("Fail to reject the null hypothesis: Variances are equal.")
