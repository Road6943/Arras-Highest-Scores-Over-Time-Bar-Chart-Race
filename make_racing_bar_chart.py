"""
Instructions:

* Make a copy of the Arras World Records Sheet @ "https://docs.google.com/spreadsheets/d/1HDQtELScci0UlVR4ESnvhM6V8bgAtNX8GI3pzq7cG8M/edit#gid=388382790"
* Open the HAS_Calculations tab, which may be hidden in which case it can be accessed from the hamburger menu in the bottom left

* Make copies of these 3 google sheets:
    - Submissions Sheet @ https://docs.google.com/spreadsheets/d/1HDQtELScci0UlVR4ESnvhM6V8bgAtNX8GI3pzq7cG8M/edit#gid=475547985
    - Older Arras Submissions @ https://docs.google.com/spreadsheets/d/1iYS59nu9EOwu2fct0SaOxVV8ZwQBXld94AVvFdUggfo/edit#gid=0
    - Oldest Arras Submissions @ https://docs.google.com/spreadsheets/d/1GRGfit3AlRHVEYL-5nhudHuBpj1nRrZqeECdNb5EBm0/edit#gid=0]

* For all sheets, turn off the fancy number formatting by selecting the entire score columns, and clicking "Format" > "Number" > "Automatic" in the menu bar
    - If you don't do this, the csv files will contain "1.23mil" as a string, and not the actual score number of 1234567

* Download "HAS_Calculations" as a csv ("File" > "Download" > "Comma Separated Values .csv") and put it in the main directory
* Download all 3 submissions sheets as csv's and put them in the SUBMISSIONS_CSV_FOLDER_NAME folder

* Now get the airtable sheet that was the original HAS @ https://airtable.com/app5ZFjOGHhw984jO/tblzOQIPr53qJRgYP/viwJt4irlFoJnKAKF?blocks=hide
* Click "Grid View" > "Download CSV" and place the downloaded csv into the find_missing_airtable_scores directory

* Run findMissingAirtableScores.py, and note its terminal output. This script searches the HAS_Calculations sheet for scores with airtable links,
    and then iterates through the Airtable sheet and removes rows which contain at least 1 of the airtable links. The terminal output from this
    script shows Airtable scores that the make_racing_bar_chart.py script cannot handle, and these scores must this be added to the HARDCODED_DATES dict.

* Change the variables below
* Run this script with `python3 make_racing_bar_chart.py`
* If you want the script to run faster, set GENERATE_FLOURISH_CSV to False, which will run the whole script but not write the output to a csv file
* This makes it significantly faster, so only set GENERATE_FLOURISH_CSV to True after you are done hardcoding the scores from imgur and other sites that the script couldn't date on its own

* Check generated_files/missing-scores.txt for any missing scores that the script couldn't give a date to
* If not already set to True, set RUN_WEB_SCRAPER_FOR_MISSING_DATES to True, and rerun make_racing_bar_chart.py
* Copy the terminal output into HARDCODED_DATES (except Failed Scrapes)
* Repeat the previous 2 steps until no new terminal output is being generated that can be copied into HARDCODED_DATES
    and missing-scores.txt is not getting any smaller
    (this is needed because certain url's may fail the scraper on one run but will succeed later)

* Use further manual methods to hardcode dates for the remaining missing scores (opening the links yourself, search discord, dm players, ...)

* Make sure GENERATE_FLOURISH_CSV is set to True now, and rerun the script
* Get the flourish csv file from the generated_files directory
* Go to https://flourish.studio/ and create a Bar Chart Race with that csv file
* Much of the chart customization occurs in the flourish settings, and I have recorded several of the settings I used for the final version of this visualization below
* To figure out which gamemodes to assign custom colors to in Flourish (aka the gamemodes that will actually appear in the visualization),
    make a list, and type/write new items into that list when you see them. Then set that item's custom color to black/some low visibility color
    so that any items not in a already tracked category will pop out. You can do this in Bar Colors - Color Overrides with something like this:
        FFA: #000000
        Open TDM: #000000


FLOURISH SETTINGS: 
Data:
    Label: B
    Values: E-(rightmost column)
    Categories: D
    Image: (None)

    Captions:
        Image: (None)
        From | To | Caption:

Preview:
    Bars:
        No. bars: 20
    Bar colors:
        Color mode: By Category
        Palette: (choose anything, doesn't matter since all visible gamemodes will be custom colored anyways)
        Bar Opacity: 0.95
        Color Overrides: 
FFA: #cb4b16
2TDM: #268bd2 
4TDM: #859900
Open TDM: #2aa198
Maze: #b58900
Maze 4TDM: #d33682
Portal 4TDM: #93a1a1
Domination: #586e75
Squads-Duos: #6c71c4

Legacy FFA: #cb4b16cc
Legacy 2TDM: #268bd2cc
Legacy 4TDM: #859900cc
Legacy Open TDM: #2aa198cc
Legacy Maze: #b58900cc
Legacy Maze 4TDM: #d33682cc
Legacy Portal 4TDM: #93a1a1cc
Legacy Domination: #586e75cc
Legacy Squads-Duos: #6c71c4cc

    Labels:
        Labels mode: Labels on bars
        Bar Labels - Color: #fdf6e3
        Values - Color: #fdf6e3
        Values - Space: 7
    Time Counter & Totalizer:
        Current time counter - size(% of screen): 6
        Total: turn off
    Captions:
        Background:
        Border:
        Opacity:
        Padding:
        Align: Center
        Position: Center Right
        Font Size:
        Text Color:
        Content Mode: HTML
    Controls:
        Show Sort Control: turn off
    Legend:
        Disabled
    Axis:
        Line Color: #657b83
    Timeline & Animation:
        Graph:
            Visibility: Hide (Yes, Hide; I turned the graph off once legacy was added because it became too laggy)
            Height: 7
            Background: #073642
        Axes Color: #fdf6e3
        Timeline Duration: 90
        Time Jump Duration: 1
        Bar Rank Animation Duration: 1.25
        Playback Button:
            Button Color: #657b83
            Icon Color: #eee8d5
    Number Formatting:
        Suffix: M
        Decimal Places: 2
        Remove Trailing Zeros: turn on
        Multiply/Divide Values: turn on
            Divide By: 1000000 (1 million)
    Layout:
        Main Font: Ubuntu
        Background color: #002b36 (solarized dark colors)
        Text Color: #fdf6e3
"""

''' VARIABLES TO CHANGE BEGIN ================================== '''

HAS_CALCULATIONS_SHEET_CSV_PATH = "Arras.io World Records - HAS_Calculations.csv"

# Date when HAS was transfered from Airtable to the Google Sheet, this will be the start date for the racing bar chart
HAS_START_DATE = "11/15/2018"

SUBMISSIONS_CSV_FOLDER_NAME = "submissions_csv_files"
SUBMISSIONS_CSV_NAME = "Arras.io World Records - Submissions.csv"
OLDER_SUBMISSIONS_CSV_NAME = "Older Arras WR Submissions - OlderSubmissions.csv"
OLDEST_SUBMISSIONS_CSV_NAME = "The Oldest Arras WR Submissions - OldSubmissions.csv"

# The csv that will be outputted to and can be inputted into Flourish Studio to generate the Racing Bar Chart
FLOURISH_OUTPUT_CSV_NAME = "Flourish_Racing_Bar_Chart_Data.csv"
GENERATED_FILES_FOLDER_NAME = "generated_files"
# Set this to true when you want an output csv to be generated
# Most of the script is pretty quick, but writing to an output csv takes a while, so only set this to True
#   once you've finished gathering dates for all the scores via the imgur scraper and manual hardcoding
GENERATE_FLOURISH_CSV = False

# if set to true, the rowsWithoutDates will be scraped and their dates printed to the terminal in a format that can directly be copied into HARDCODED_DATES
RUN_WEB_SCRAPER_FOR_MISSING_DATES = True

# Assign dates to scores that either the script cannot figure out on its own
#   or that you want to assign a date to that will differ from what the script would assign
HARDCODED_DATES = {
    # These airtable youtube links will be dated to HAS_START_DATE even though we know their earlier dates
    # because there are many images on the airtable that occurred earlier but we don't know exact dates for
    # and thus the whole graphic will start from HAS_START_DATE to maintain consistency

    'www.youtube.com/watch?v=r1TxtoWL19Y': HAS_START_DATE, # 3.686 mil Double Twin Open 3/4 TDM Denied
    'www.youtube.com/watch?v=L3UnMD8zHQU': HAS_START_DATE, # 2.702 mil Auto-Double Open 3/4 TDM Denied
    'https://www.youtube.com/watch?v=asTAKK6wbpk': HAS_START_DATE, # 2.195 mil Necromancer 4TDM Soog
    'https://www.youtube.com/watch?v=zk5ktciy3ck': HAS_START_DATE, # 2.133 mil Musket Open 3/4 TDM Denied
    'https://www.youtube.com/watch?v=rpV7gKdxCAE': HAS_START_DATE, # 2.059 mil Carrier Open 3/4 TDM Denied
    'https://www.youtube.com/watch?v=4FsfyqoiVLo': HAS_START_DATE, # 2.051 mil Bushwhacker Open 3/4 TDM Denied
    'https://youtu.be/0YVawS--zho': HAS_START_DATE, # 2.008 mil Twin Open 3/4 TDM Denied

    'https://www.youtube.com/playlist?list=PLKX9QkIkL2EWu55dDf2ULmzk0p5vvcXFi': "3/28/2021", # 2.378 mil Healer Siege dustin the pro
    'https://www.youtube.com/watch?v=_B-K4Gz5HIY': "7/21/2021", # 2.090 mil Tri-Angle 4TDM Sprunk
    'https://www.youtube.com/watch?v=T4Mu5-AUZYM&t': "7/19/2021", # 3.061 mil Machine Gun 4TDM WL9

    'https://www.reddit.com/r/Diep2io/comments/ohxe6g/25m_poacher_taking_back_wr_from_Lyre/': "7/10/2021", # 2.504 mil Poacher Maze 4TDM uhhh ._.
    'https://www.reddit.com/r/Diep2io/comments/omnwom/29m_manager_maze_3_mil_maze_denial/': "7/18/2021", # 2.981 Manager Maze 2TDM Kris

    'https://i.imgur.com/wjguUFd.png': "5/11/2021", # 4.647 mil Mortar Squads-Duos baking soda
    'https://www.youtube.com/watch?v=WyUdAFhjnpI': "12/13/2018", # 2.146 mil Auto Double 4TDM ProGamer9164

    # Put dates printed to the terminal from the scraper function under here:

    "https://imgur.com/fl0Tv8m": "3/09/2019", # 2.154 mil Auto-5 FFA u/DaGreenball
    "https://imgur.com/a/2ZtnxnK": "7/16/2021", # 2.530 mil Cyclone FFA 132
    "https://imgur.com/K7BOkTP": "9/23/2020", # 2.029 mil Mega Smasher Maze 4TDM NOT|megaball[VN]
    "https://imgur.com/a/MehUq6Z": "7/16/2021", # 2.239 mil Auto-4 Open Maze TDM 132
    "https://imgur.com/a/hxBTT19": "7/16/2021", # 2.521 mil Cyclone Open TDM 132
    "https://imgur.com/a/OKWN8CT": "7/16/2021", # 3.237 mil Cyclone FFA 132
    "https://imgur.com/a/w1ZOmIj": "7/16/2021", # 2.199 mil Auto-4 Open TDM 132
    "https://imgur.com/a/3i2Raz7": "7/16/2021", # 2.878 mil Cyclone Open TDM 132
    "https://imgur.com/a/JA8Xsrw": "7/16/2021", # 2.167 mil Architect FFA 132
    "https://imgur.com/a/yFrqd2o": "7/16/2021", # 3.431 mil Architect Open TDM 132
    "https://imgur.com/a/luva5uJ": "7/16/2021", # 5.094 mil Architect Open TDM 132
    "https://imgur.com/a/vj59t2C": "7/16/2021", # 3.034 mil Cyclone 2TDM 132
    "https://imgur.com/a/mUnvQUl": "7/16/2021", # 2.360 mil Cyclone 4TDM 132
    "https://imgur.com/a/xoGXv7e": "7/16/2021", # 2.283 mil Auto Smasher 2TDM 132
    "https://imgur.com/a/CwCvp1B": "5/11/2021", # 2.512 mil Builder Squads-Duos Chaos
    "https://imgur.com/a/XVMKIPA": "7/05/2021", # 2.328 mil Spike FFA Rog456
    "https://imgur.com/a/o2mP4Z5": "7/16/2021", # 2.844 mil Banshee 2TDM Mine
    "https://imgur.com/a/NDJ4AON": "7/18/2021", # 2.080 mil Boomer Open Maze TDM Mine
    "https://imgur.com/a/4l7WZ5a": "7/19/2021", # 6.757 mil Necromancer 2TDM Roman
    "https://imgur.com/a/WOE5HNb": "7/20/2021", # 2.128 mil Auto-5 2TDM Giggity
    "https://imgur.com/a/AS0xh4H": "7/19/2021", # 2.205 mil Auto Builder Portal 4TDM Lyre
    "https://imgur.com/a/m6SB0Lb": "7/20/2021", # 2.605 mil Tri-Angle Squads-Duos Thx m8
    "https://imgur.com/a/MkAwMlB": "7/20/2021", # 3.127 mil Gunner Trapper 2TDM Broken
    "https://imgur.com/a/VYKtUcX": "7/20/2021", # 2.116 mil Auto Overseer 2TDM Broken
    "https://imgur.com/a/Ei0rWEd": "7/20/2021", # 2.353 mil Manager 4TDM Broken
    "https://imgur.com/a/aUfGGZJ": "7/20/2021", # 3.001 mil Factory Siege Levitate
    "https://imgur.com/a/G6LJM0k": "7/21/2021", # 2.513 mil Factory 2TDM Lyre
    "https://imgur.com/a/tWRcTF0": "7/21/2021", # 2.172 mil Surfer Squads-Duos lou
    "https://imgur.com/a/NqfAzcB": "7/22/2021", # 2.121 mil Banshee 2TDM TacoCat
    "https://imgur.com/a/9V5Ab3b": "7/23/2021", # 2.906 mil Auto Builder Open Maze TDM Mine
    "https://imgur.com/a/PNAWpNd": "7/24/2021", # 2.545 mil Smasher 4TDM asd
    "https://imgur.com/a/vWpuD1m": "10/31/2021", # 3.240 mil Auto Smasher Maze 4TDM Mine
    "https://imgur.com/a/W4HMddb": "11/05/2021", # 10.110 mil Overseer 4TDM Bastard
    "https://imgur.com/a/6FLNoiX": "5/11/2021", # 2.033 mil Overlord Squads-Duos h
    "https://imgur.com/a/5mlQnkx": "12/16/2021", # 2.972 mil Ordnance Open TDM pool noodle
    "https://imgur.com/a/BGpfLsG": "12/16/2021", # 3.677 mil Factory Siege toast?
    "https://imgur.com/a/pNEx5jU": "10/31/2021", # 2.005 mil Hexa Tank FFA bum
    "https://imgur.com/a/w5l7d7h": "12/16/2021", # 2.090 mil Surfer Open TDM aisa
    "https://imgur.com/gallery/FsPyDpO": "12/22/2020", # 4.529 mil Spreadshot Squads-Duos baking soda
    "https://imgur.com/gallery/ErPYeXb": "5/09/2021", # 2.300 mil Crop Duster Maze baking soda
    "https://imgur.com/gallery/dXM4GF4": "7/17/2021", # 3.314 mil Healer Siege KSK
    "https://imgur.com/gallery/MQZhhwc": "7/18/2021", # 2.757 mil Healer Siege KSK
    "https://imgur.com/gallery/wBp26ey": "7/21/2021", # 2.000 mil Overseer Open Maze TDM Onyx
}

''' VARIABLES TO CHANGE END ================================== '''


import csv
from datetime import datetime, timedelta

import time
import asyncio
from typing import get_args
from bs4 import BeautifulSoup
from pyppeteer import launch

async def scrape_dates_from_imgur_to_hardcode_missing_dates(rowsWithoutDates):
    '''
        Scrape a list of rows' links to extract the timestamps and print them to the terminal
        Currently, it only supports imgur.com/a/ and imgur.com/gallery links
    '''
    failedScrapes = []

    # Launch the browser
    browser = await launch()

    # Open a new browser page
    page = await browser.newPage()

    for row in rowsWithoutDates:
        try:
            [score, player, url, tank, gamemode, _] = row
            score = float(score)

            # no i.imgur.com direct image links
            if '//imgur' in url:
                await page.goto(url)
                page_content = await page.content()
                
                # Process extracted content with BeautifulSoup
                soup = BeautifulSoup(page_content, 'html.parser')
                # see imgur's html structure - using.Meta allows it to work on both /a/ and /gallery links
                timestamp = soup.select_one('.Info-Wrapper .Meta [title]')['title']

                # convert timestamp to correct format
                [monthName, dayNum, yearNum] = timestamp.split(' ')[1:4]
                monthNum = time.strptime(monthName,'%b').tm_mon
                formattedDate = f"{monthNum}/{dayNum}/{yearNum}"
                
                # print a string that can be copied directly into HARDCODED_DATES
                formattedScore = "{:.3f} mil".format(score / 1_000_000) if score >= 1_000_000 else "{:.3f} k".format(score / 1000)
                print(f'"{url}": "{formattedDate}", # {formattedScore} {tank} {gamemode} {player}')
                
                # format_score = lambda score: "{:.2f}mil".format(score / 1_000_000) if score >= 1_000_000 else "{:.2f}k".format(score / 1000)
        except:
            failedScrapes.append(row)

    # Close browser
    await browser.close()

    if failedScrapes:
        print("\n\n\nFAILED SCRAPES BELOW:")
    for failedRow in failedScrapes:
        print(failedRow)


def getField(row, field, sheet="submissions"):
    """
        Each row is an array, and this function lets you get a specific value from that row
        This function is used because row size varies across time and certain rows may not have
            values at certain positions
        Also this function lets you use human readable keynames like timestamp instead of row[0]
        Also, score's are pre-converted from strings into integers
    """
    if sheet == "submissions":
        fields = ["timestamp", "status", "score", "name", "proof", "tank", "gamemode", "specialSubmission", "extraDetails"]
    elif sheet == "has_calculations":
        fields = ["score", "name", "proof", "tank", "gamemode", "isLegacy"]
    elif sheet == "airtable":
        fields = ["score", "name", "tankImage", "tank", "proof", "gamemode", "build"]
    else:
        fields = []

    fieldIndices = { field: i for i,field in enumerate(fields) }
    
    assert field in fieldIndices
    index = fieldIndices[field]

    assert len(row) > index

    # return an integer for the score
    if field == "score":
        score = row[index].strip()

        assert score != ""

        # some scores on Oldest don't have numerical forms, they're just strings like 5.45mil, so account for those here
        if score.endswith("mil"):
            score = float( score.replace("mil", "").strip() ) * 1_000_000
        elif score.endswith("k"):
            score = float( score.replace("k", "").strip() ) * 1000

        # some scores are decimals for whatever reason, so parse them as floats first and then ints
        return int(float(score))


    # return a boolean for isLegacy
    elif field == "isLegacy":
        return row[index].strip().lower() == "k"

    # airtable proof's are in a weird format like this: "imageName (imageLink)"
    elif field == "proof" and sheet == "airtable":
        pass


    # just return a string for all other fields with surrounding whitespace removed
    return row[index].strip()


def parseDate(dateStr):
    return time.strptime(dateStr, "%m/%d/%Y")


def makeDateLookup():
    """
        Fetch rows from the Submissions Sheet, Older Arras Submissions, and Oldest Arras Submissions
        And use them to generate a dictionary where a score's proof url is keyed to its timestamp
    """

    # Ensures that a row meets the criteria to be considered for this racing bar chart
    # namely, that it's approved ('v' status) and the score is 2 million or higher
    # The specialSubmission field will be ignored since there may be certain scores that were
    # never marked as HAS, such as scores on Oldest Submissions from before HAS was added
    def isValidRow(row):
        # skip info rows at top of sheets by making sure the first character of the first item in the row exists and is a number
        if not row[0] or not row[0][0].isnumeric():
            return False

        # ignore rows without a 'v' status (approved)
        #if getField(row, 'status') != 'v':
        #    return False
        # I commented this out because some scores on HAS_Calculations were submitted, but rejected
        # However, that still allows us to place a date for them

        # ignore rows without a score over 2 million
        if getField(row, 'score') < 2_000_000:
            return False
        
        return True


    # make a submissions array filled with all rows that match the criteria from all the submissions sheets
    # iterate from newest date to oldest (in reverse) to ensure the very first submission date is used for proof links
    # that were submitted multiple times (as the dict entry will be overwritten)
    submissions = []
    for filename in [SUBMISSIONS_CSV_NAME, OLDER_SUBMISSIONS_CSV_NAME, OLDEST_SUBMISSIONS_CSV_NAME]:
        with open(SUBMISSIONS_CSV_FOLDER_NAME + "/" + filename) as submissionsCsvFile:
            reader = csv.reader(submissionsCsvFile)
            rowsFromNewestDateToOldestDate = reversed(list(reader))
            submissions.extend(row for row in rowsFromNewestDateToOldestDate if isValidRow(row))

    # make the timestamp lookup
    dateLookup = {}
    for row in submissions:
        timestamp = getField(row, "timestamp")
        date = timestamp.split(" ")[0]
        proof = getField(row, "proof")
        dateLookup[proof] = date

    return dateLookup


def makeMissingScoresFile(rowsWithoutDates):
    '''
        Create missing-scores.txt, a file that lists out scores that the script couldn't find dates for
    '''
    with open(GENERATED_FILES_FOLDER_NAME + "/" + "missing-scores.txt", "w") as file:
        file.write(f"NUMBER_OF_SCORES_WITH_MISSING_DATES = {len(rowsWithoutDates)}  \n")
        file.write(f"rowsWithoutDates = [ \n")
        for row in rowsWithoutDates:
            file.write(str(row) + ", \n")
        file.write("]")

    if RUN_WEB_SCRAPER_FOR_MISSING_DATES:
        asyncio.get_event_loop().run_until_complete(scrape_dates_from_imgur_to_hardcode_missing_dates(rowsWithoutDates))


def findTimestampsOfScoresOnHasAndLas(dateLookup, hardcodedLookup):
    """
        Go through all scores in HAS_Calculations and find the corresponding dates
        return a list of score objects for all scores in HAS_Calculations with a date added

        Hardcoded Lookup is a dictionary where dates are hardcoded for certain proof links
    """
    
    scores = []
    rowsWithoutDates = []

    with open(HAS_CALCULATIONS_SHEET_CSV_PATH) as file:
        reader = csv.reader(file)
        for row in reader:
            # skip the first 3 rows of HAS Calculations since they're not score rows
            # do this by making sure the first item in the row is a number string
            if not row[0].isnumeric():
                continue

            proof = getField(row, 'proof', sheet="has_calculations")

            if proof in hardcodedLookup:
                date = hardcodedLookup[proof]

            elif proof in dateLookup:
                date = dateLookup[proof]
            
            # airtable scores will be assigned the date when HAS was transfered to the wr sheet
            elif 'airtable' in proof:
                date = HAS_START_DATE

            # for images stored on discord's cdn, extract the snowflake and convert it to a date
            elif '.discordapp.' in proof:
                def getSnowflakeDate(snowflake):
                    # https://gist.github.com/omnituensaeternum/57753daee3a926e92747b3d481d43823
                    DiscordEpoch = 1420070400000
                    input = snowflake
                    UnixTSinMS = input / 4194304 + DiscordEpoch
                    out = datetime.fromtimestamp(UnixTSinMS/1000.0).strftime("%m/%d/%Y")
                    # remove leading 0 on months to maintain consistency with google form timestamp
                    if out[0] == "0":
                        out = out[1:]
                    return out

                def extractSnowflakeFromLink(link):
                    '''
                        split the link at "/"s, then remove all parts that aren't only composed of numbers
                        the second such numeric link part will be the snowflake (the first is the channel id)
                    '''
                    linkParts = link.split("/")
                    numericLinkParts = [part for part in linkParts if part.isnumeric()]
                    return int( numericLinkParts[1] )

                date = getSnowflakeDate( extractSnowflakeFromLink(proof) )

            else:
                rowsWithoutDates.append(row)

            # if a date is before HAS_START_DATE, then make it HAS_START_DATE to maintain consistency across all airtable scores
            # (since a score A might have occurred before a score B, but A can't be truly dated while B can, so just give both the HAS_START_DATE)
            if parseDate(date) < parseDate(HAS_START_DATE):
                date = HAS_START_DATE

            scores.append({
                "row": row,
                "sheet": "has_calculations",
                "date": date,
            })

    makeMissingScoresFile(rowsWithoutDates)

    # save all scores and dates to new csv file
    with open(GENERATED_FILES_FOLDER_NAME + "/" + "HAS_Calculations_With_Dates.csv", "w") as file:
        writer = csv.writer(file)
        for score in sorted(scores, key=lambda score: parseDate(score['date']) ):
            writer.writerow([ score['date'], *score['row'] ])

    return scores


def makeFlourishCsvFile(scoresWithDates):
    """
        convert all the scores and their dates into a csv file that can be uploaded to flourish.studio to generate a bar chart race

        scoresWithDates is a list of score structs

        the generated flourish csv file will be in the generated_files folder
    """

    # if given a date like "1/31/2020", returns "2/1/2020"
    def get_next_date(dateStr):
        today = datetime.strptime(dateStr, "%m/%d/%Y")
        tomorrow = today + timedelta(days=1)
        return tomorrow.strftime("%-m/%-d/%Y")
    
    starting_date = HAS_START_DATE
    # find last date in the scoresWithDates list
    all_dates_of_scores = [score['date'] for score in scoresWithDates]
    ending_date = max(all_dates_of_scores, key=lambda dateStr: parseDate(dateStr))
    #ending_date = datetime.today().strftime("%-m/%-d/%Y")

    dates = []
    d = starting_date
    while d != get_next_date(ending_date):
        dates.append(d)
        d = get_next_date(d)

    # convert dates from 1/2/2021 format to 1/2/21 format (short years)
    # so that I can make their font size bigger in Flourish
    formatted_dates = [
        datetime.strptime(dateStr, "%m/%d/%Y").strftime("%-m/%-d/%y")
        for dateStr in dates
    ]


    with open(GENERATED_FILES_FOLDER_NAME + "/" + FLOURISH_OUTPUT_CSV_NAME, "w") as flourishCsvFile:
        writer = csv.writer(flourishCsvFile)

        # header row
        writer.writerow(["Description", "Description & Legacy Status", "Gamemode",  "Gamemode & Legacy Status", *formatted_dates])
        
        for score in scoresWithDates:
            # make helper function to get field with less typing
            gF = lambda fieldName: getField(score['row'], fieldName, sheet=score['sheet'])
            tank = gF('tank')
            gamemode = gF('gamemode')
            player = gF('name')
            scoreNumber = gF('score')
            isLegacy = gF('isLegacy')

            description = f"{tank} · {gamemode} by {player}"
            descriptionAndLegacyStatus = f"[LEGACY] {description}" if isLegacy else description
            gamemodeAndLegacyStatus = f"Legacy {gamemode}" if isLegacy else gamemode

            new_csv_row = [description, descriptionAndLegacyStatus, gamemode, gamemodeAndLegacyStatus]

            for day in dates:
                # if score hasn't happened yet as of current day, then set it to 0
                if parseDate(day) < parseDate(score['date']):
                    new_csv_row.append(0)
                # if current day is on or after when the score was gotten, append the score's numerical score value
                else:
                    new_csv_row.append(scoreNumber)

            writer.writerow(new_csv_row)

    
def main():
    dateLookup = makeDateLookup()
    scoresWithDates = findTimestampsOfScoresOnHasAndLas(dateLookup, HARDCODED_DATES)
    # only generate output if the user sets this variable to True, as writing csv output takes a while and should only be done
    # at the very end once all scores' dates are found and accounted for
    if GENERATE_FLOURISH_CSV:
        makeFlourishCsvFile(scoresWithDates)


if __name__ == "__main__":
    main()
    