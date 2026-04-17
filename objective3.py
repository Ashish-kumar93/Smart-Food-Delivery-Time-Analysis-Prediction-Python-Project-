#=========OBJECTIVE 3==========

#Evaluate impact of categorical factors (traffic, weather, city)


# Traffic impact
plt.figure()
sns.boxplot(x='Road_traffic_density', y='Time_taken(min)', data=df)
plt.title("Traffic vs Delivery Time")
plt.show()


# Weather impact
df.groupby('Weatherconditions')['Time_taken(min)'].mean().plot(kind='bar')
plt.title("Weather vs Delivery Time")
plt.show()


# City impact
df.groupby('City')['Time_taken(min)'].mean().plot(kind='bar')
plt.title("City vs Delivery Time")
plt.show()


