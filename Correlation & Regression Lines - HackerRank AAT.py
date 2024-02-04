# Physics scores
physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]

# History scores
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

# Calculate the means
mean_physics = sum(physics_scores) / len(physics_scores)
mean_history = sum(history_scores) / len(history_scores)

# Calculate the covariance and variances
covariance = sum((x - mean_physics) * (y - mean_history) for x, y in zip(physics_scores, history_scores))
variance_physics = sum((x - mean_physics)**2 for x in physics_scores)
variance_history = sum((y - mean_history)**2 for y in history_scores)

# Calculate the correlation coefficient
correlation_coefficient = covariance / (variance_physics**0.5 * variance_history**0.5)

# Print the result with three decimal places
print(f"{correlation_coefficient:.3f}")
