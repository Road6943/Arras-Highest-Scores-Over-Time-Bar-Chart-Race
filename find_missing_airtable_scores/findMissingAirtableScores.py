# airtable scores on HAS/LAS with 'airtable' in their proof links are already taken care of. Some of the airtable scores
# were converted to imgur or youtube links however, so this script will list those out so they can be hardcoded into the main script
# Run this script, and look at the output, and use that output to identify the matching scores in HAS_Calculations and hardcode
#   the HAS_Calculations links with the HAS Starting Date (Nov 15 2018)

# Run script from within the find_missing_airtable_scores folder

HAS_CALCULATIONS_SHEET_CSV_PATH = "../Arras.io World Records - HAS_Calculations.csv"
AIRTABLE_CSV_PATH = "↓ Also try Other Views ↓-Grid view(1).csv"


import csv

airtableLinksOnHasCalculations = []

with open(HAS_CALCULATIONS_SHEET_CSV_PATH) as hasCalculationsSheet:
    reader = csv.reader(hasCalculationsSheet)
    for row in reader:
        proof = row[2]
        if 'airtable' in proof:
            airtableLinksOnHasCalculations.append(proof)

with open(AIRTABLE_CSV_PATH) as airtableSheet:
    reader = csv.reader(airtableSheet)
    for row in reader:
        proof = row[4]
        if not any(link in proof for link in airtableLinksOnHasCalculations):
            score = row[0]
            player = row[1]
            tank = row[3]
            gamemode = row[5]
            print(f"{score} {tank} {gamemode} {player}")
    

