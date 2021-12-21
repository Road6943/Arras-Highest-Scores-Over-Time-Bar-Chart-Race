music:
In the Hall of the Mountain King, the part from 40-ish to 2:15-ish is perfect, and the first 40 seconds can be a lead-in of sorts
    - https://www.youtube.com/watch?v=tpcee4-g0Nw&list=PLgg6LswqK80ZOtKndAbJmk6Azi3gzJRjR&index=11
    - though I'm not doing the long intro anymore so maybe a different music is needed now

How disclaimers will be shown:
```
1) Show semi-customized submission form. Zoom in so recorded screen matches flourish, and then Type(or just show pre-typed stuff in long answer box if typing is too long/loud):
score: Hello! Thanks for clicking this video! Before we begin, here's some disclaimers:
name: Darker bars marked with [LEGACY] were done with a tank that has since been nerfed significantly.
extraDetails: The video starts from 11/15/18 since that's when Highest Arras Scores was added to the Arras WR Spreadsheet.

STOP STOP STOP
Some of these can be captions inside flourish
- video starts from 11/15/18
- [LEGACY] explanation

{{PASTE the following into Proof}}::{{
    Arras's Score Data is harder to parse than Diep's, but I tried my best. However, there may be occasional mistakes such as scores I forgot to add or incorrect dates.

    The main criteria used for this visualization is not necessarily when a score was obtained, but rather when it was submitted to the World Records Spreadsheet. Read the description for more info.
}}
Surfer
Open TDM (reference to ExC's 9.1mil)
Highest Arras Scores
{{
    CUSTOM CHECKBOX QUESTION: 
    Special Thanks To:
    [x] sjoshi
    [x] skrialik (bastard)
    [x] Crazy Carrot
}}
{{Hit Submit, and redirect to custom submit message ("Without further ado, Let's Begin!), and maybe throw a link to the flourish visualization in there to click and start}}

=====

Description:

TODO: add links to stuff and music credits and all that

Darker/More-Transparent bars marked with `[LEGACY]` are "Legacy Arras Scores", which were done with a tank that has been significantly nerfed since that score. These scores appear in the Legacy Arras Scores sheet, not the Highest Arras Scores sheet.

The graphic starts from November 15, 2018 because that is the date when "Highest Arras Scores" was added to the Arras World Records Spreadsheet.

This project took about 1 week to finish. I made a python script to track down timestamps for every score on Highest and Legacy Arras Scores and used flourish.studio to generate the visualization. Check the video description for more info!

Special Thanks to sjoshi and Skrialik (Bastard) and Crazy Carrot for helping me!

-----

Arras's Score Data is harder to parse than Diep's, but I tried my best. However, there may be occasional mistakes such as scores I forgot to add or incorrect dates.

The main criteria used for this graphic is not necessarily when a score was gotten, but rather when it was submitted to the World Records Spreadsheet. Thus, scores that were obtained on a Date A, but only submitted on a much later Date B, will be assigned Date B to:

1) make my life easier

2) maintain consistency across scores (Score X may have been done & submitted earlier than Score Y, but Score Y may have a date visible in its proof images while Score X's images only show the game screen. If I used the date visible in the images for Score Y and the Google Sheet Timestamp for Score X, then I might mistakenly assume Score Y happened before Score X.)

-----

These are the following methods used to assign dates to scores, in order of prominence:

1) Use the Timestamp column(s) of the Submissions/Older Submissions/Oldest Submissions Spreadsheets
2) dl.airtable.com image links are assigned a date of November 15, 2018 (the date when HAS was first moved from Airtable to the Arras WR Spreadsheet)
3) Any further scores that can be manually located on the original HAS Airtable Sheet and were not already assigned a date by a previous method will be hardcoded with the date November 15, 2018 in the script
4) If an image is stored on Discord's CDN, the date of the image is calculated from the snowflake in the url
5a) If a video is uploaded to YouTube, the YouTube link will be opened manually and the video upload date will be hardcoded into the script
5b) The process from 4a will be repeated for images from other sites such as Imgur.com, Reddit.com, and ibb.co
6) If a computer date visible in image, that date is used
7) Searching the Discord server to see if an image can be located and its date identified
8) Messaging players on Discord or Reddit to ask them when one of their scores were gotten
