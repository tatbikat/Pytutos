import csv
print("Start processing....")
barja_list = []
with open('Voters_M6_21_Chouf.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open("barja.csv", "w",newline='') as outfile:
        csvwriter = csv.writer(outfile)
        for line in csv_reader:
            barja_row = False
            for k,v in line.items():
                if k=="القرية" and v=="برجا":
                    barja_row= True
            if barja_row:
                barja_list.append(line.values())
                #csvwriter.writerow(line.values())
        csvwriter.writerow()
        csvwriter.writerows(barja_list)