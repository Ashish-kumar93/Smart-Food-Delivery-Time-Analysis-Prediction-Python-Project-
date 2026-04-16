#========OBJECTIVE 2===========

#Examine relationship between distance and delivery time

plt.figure()
plt.scatter(df['Distance'], df['Time_taken(min)'])
plt.xlabel("Distance")
plt.ylabel("Delivery Time")
plt.title("Distance vs Delivery Time")
plt.show()
