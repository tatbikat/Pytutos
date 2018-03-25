import csv
import json


data = json.load(open('words.json'))


def village_to_csv(village):
    village_list = []
    village_row = False
    with open('Voters_M6_21_Chouf.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open(village + ".csv", "w",newline='') as outfile:
            csvwriter = csv.writer(outfile)
            for line in csv_reader:
                village_row = False
                for k,v in line.items():
                    if k==data["village"] and v== data[village]:
                        village_row= True
                if village_row:
                    village_list.append(line.values())

            csvwriter.writerows(village_list)
print("start exporting data...")
village_to_csv("barja")
village_to_csv("dalhoun")

print("Done")