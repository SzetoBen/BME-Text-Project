import matplotlib.pyplot as plt

sentiments = {}
with open("output/post_ai_distilbert_output.txt", "r") as f:
    lines = f.readlines()
    for line in lines[1:]:
        if ":" in line:
            key, value = line.strip().split(":")
            sentiments[key] = float(value)

# Extract keys and values
labels = list(sentiments.keys())
values = list(sentiments.values())

# Plot bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(labels, values, color="steelblue", edgecolor="black")

# Annotate bars with values
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f"{height:.2f}", ha="center", va="bottom")

plt.title("Average Sentiment Distribution Pre AI")
plt.ylabel("Average Score")
plt.xlabel("Sentiment")
plt.tight_layout()
plt.savefig("output/plots/postAI-distilbert.png")
plt.show()

sentiments = {}
with open("output/pre_ai_distilbert_output.txt", "r") as f:
    lines = f.readlines()
    for line in lines[1:]:
        if ":" in line:
            key, value = line.strip().split(":")
            sentiments[key] = float(value)

# Extract keys and values
labels = list(sentiments.keys())
values = list(sentiments.values())

# Plot bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(labels, values, color="steelblue", edgecolor="black")

# Annotate bars with values
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f"{height:.2f}", ha="center", va="bottom")

plt.title("Average Sentiment Distribution Pre AI")
plt.ylabel("Average Score")
plt.xlabel("Sentiment")
plt.tight_layout()
plt.savefig("output/plots/preAI-distilbert.png")
plt.show()

