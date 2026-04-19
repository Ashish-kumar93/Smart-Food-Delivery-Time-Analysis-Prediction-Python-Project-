#==========OBJECTIVE 6==============
#Visualize distribution of delivery time

plt.figure()
plt.hist(df['Time_taken(min)'])
plt.title("Distribution Analysis")
plt.show()
