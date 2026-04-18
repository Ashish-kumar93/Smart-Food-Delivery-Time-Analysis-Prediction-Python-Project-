#-------Analyze correlation among variables affecting delivery time-----
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Analysis")
plt.show()



#==============OBJECTIVE 4=================
#---------Build and evaluate simple linear regression model

X = df[['Distance']]
y = df['Time_taken(min)']

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("MSE:", mean_squared_error(y, y_pred))
print("R2 Score:", r2_score(y, y_pred))

# Plot regression line
plt.figure()
plt.scatter(X, y)
plt.plot(X, y_pred)
plt.title("Regression Line")
plt.show()
