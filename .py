#=========OBJECTIVE-1======

#-------Analyze distribution and patterns in delivery time
# Histogram
plt.figure()
plt.hist(df['Time_taken(min)'])
plt.title("Delivery Time Distribution")
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.show()

# Traffic distribution
plt.figure()
df['Road_traffic_density'].value_counts().plot(kind='bar')
plt.title("Traffic Density Distribution")
plt.show()

