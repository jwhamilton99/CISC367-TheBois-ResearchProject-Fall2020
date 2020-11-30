import nltk
import csv
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

data_file = open("output.csv", "r")
csv_data = csv.reader(data_file, delimiter = "\t")

i = 0

out_file = open("output-with-sentiment.csv", "w")
out_file.write("")
out_file.write("messageText\tmessageTextPostProcessing\tnumEmojis\tnumAcronyms\temojis\tacronyms\tneg\tneu\tpos\tcompound\n")

for row in csv_data:
    if(i != 0 and row[1].__len__() != 0):
        for item in row:
            out_file.write(str(item) + "\t")
        
        scores = sia.polarity_scores(row[1])
        out_file.write(str(scores["neg"]) + "\t")
        out_file.write(str(scores["neu"]) + "\t")
        out_file.write(str(scores["pos"]) + "\t")
        out_file.write(str(scores["compound"]) + "\n")

    i += 1

data_file.close()
out_file.close()