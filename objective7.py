#===========OBJECTIVE 7==============
#Visualize relationships between variables

# Scatter
plt.figure()
plt.scatter(df['Distance'], df['Time_taken(min)'])
plt.show()

# Boxplot
plt.figure()
sns.boxplot(x='Road_traffic_density', y='Time_taken(min)', data=df)
plt.show()
