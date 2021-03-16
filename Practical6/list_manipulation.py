# import required module
import matplotlib.pyplot as plt
# create 2 lists
gene_lengths = [9410, 394141, 4442, 105338, 19149,
                76779, 126550, 36296, 842, 159]
exon_counts = [51, 1142, 42, 216, 25, 650, 32533, 57, 1, 523]
# generate average length list
average_list = [gene_lengths[i]/exon_counts[i] for i in range(10)]
# print sorted list
print(sorted(average_list))
# draw the boxplot
plt.boxplot(average_list, labels="x")
plt.title("average length")
plt.show()