import nltk, csv
from nltk import FreqDist
from operator import itemgetter

f = open("yaccData.csv")
print("Student Name: Adison Nordstrom")
print("")
with open('yaccData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    timeServed = {}
    count = 0
    states=[]
    statesAll=['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts','Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            #print general president info 
            if int(row[0]) == 45:
                numstr = "3"
                print(row[1] +' '+ row[2] + " is the current President. He has served since " + row[4] + ".")
            else:
                yr1 = int(row[4])
                yr2 = int(row[5])
                num = yr2-yr1
                numstr = str(num)
                states.append(row[3])
                print(row[1] +' '+ row[2] + " was President #" + row[0] + ". He served for " + numstr + " years, from " + row[4] +  " to " + row[5] + ".")
            timeServed[row[1] +' '+ row[2]] = numstr
        
    print("")
    line_count += 1
    fdist = FreqDist(states)
    fdist['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts','Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
    for f, ct in fdist.most_common(50):
        print(str(ct) + " presidents were born in " + f + ".")
    print("")
    statesNP = list(set(statesAll)-set(states))
    print(str(len(statesNP)) + " states have not been the birthplace of a president.")
    print("")
    sortedT = sorted(timeServed.iteritems(), key=lambda x: int(x[1]))
    for p, t in sortedT:
        print(p + " served for at most " + t + " years.")
