import nltk
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

data_file = open("output-excludedmessages.csv", "r", encoding = "utf-8")

out_file = open("output-excluded-with-sentiment.csv", "w", encoding = "utf-8")
out_file.write("")
out_file.write("neg\tneu\tpos\tcompound\tmessageText\n")

i = 0
for row in data_file:
    if(i != 0 and row.__len__() != 0):
        scores = sia.polarity_scores(row)
        out_file.write(str(scores["neg"]) + "\t")
        out_file.write(str(scores["neu"]) + "\t")
        out_file.write(str(scores["pos"]) + "\t")
        out_file.write(str(scores["compound"]) + "\t")
        out_file.write(str(row) + "\t")

    i += 1

data_file.close()
out_file.close()