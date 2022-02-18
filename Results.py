#180222 using python to analyse results 
import statistics
results = [93,92,87,86,74,64,80,91]

average = statistics.mean(results)
print(average)

median = statistics.median(results)
print(median)

spread = statistics.stdev(results)
print(spread)

