#Hypothesis testing (Distance-Based T-Test)

median_distance = df['Distance'].median()

short_dist = df[df['Distance'] <= median_distance]['Time_taken(min)']
long_dist = df[df['Distance'] > median_distance]['Time_taken(min)']

print("Short Count:", len(short_dist))
print("Long Count:", len(long_dist))

print("Mean Short:", short_dist.mean())
print("Mean Long:", long_dist.mean())

# Perform T-test
t_stat, p_value = ttest_ind(short_dist, long_dist)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Decision
if p_value < 0.05:
    print("Reject Hypothesis → Distance affects delivery time")
else:
    print("Fail to Reject Hypothesis")
