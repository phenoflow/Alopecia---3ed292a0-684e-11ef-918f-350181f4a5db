# phekb, 2024.

import sys, csv, re

codes = [{"code":"704","system":"ICD9 Diagnosis"},{"code":"704.01","system":"ICD9 Diagnosis"},{"code":"L66.0","system":"ICD9 Diagnosis"},{"code":"L66.2","system":"ICD9 Diagnosis"},{"code":"L66.8","system":"ICD9 Diagnosis"},{"code":"L95.9","system":"ICD9 Diagnosis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('alopecia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["alopecia---undefined-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["alopecia---undefined-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["alopecia---undefined-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
