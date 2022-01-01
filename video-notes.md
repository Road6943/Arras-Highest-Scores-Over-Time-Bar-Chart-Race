music:
https://www.youtube.com/watch?v=2RDX5sVEfs4
Hall of the mountain king
I had to normalize it to make it not so loud

start:
Although Arras started in 2017, this video begins from 11/15/18 - the day when “Highest Arras Scores” was added to the WR Sheet
Scores marked with `[LEGACY]` were done with a tank that later received a significant nerf

end:
Why did 4tdm scores explode in 2021?
Thanks to {{list people who helped me}}!

Record with mac shift+cmd+5; put slides in two tabs, one for the first half, and one for the second half; put flourish in another tab;
    Align everything so the screen recording selection shows the right amount of both (allow slides to be cut off on sides)
    Use cntrl+tab in firefox to quickly switch tabs, make sure you're switching between right tabs before video starts
    Also ensure both slides are on the correct slide before video starts
    Use these links to post process:
        https://www.fileconverto.com/add-music-to-video/
        https://stackoverflow.com/questions/43414641/repeat-last-frame-in-video-using-ffmpeg
        {{lots of ffmpeg use}}

~~~~~
Fun Fact (sticky in comments):
Fun Fact:
Stradpult's 10 million Fighter score initially couldn't be submitted as a World Record because the submission form was unable to handle scores higher than 9,999,999.

~~~~~

Fix wrongly-dated scores in next version of this, whenever I make it. For example, Damocles pointed out a mega smasher score that was resubmitted with a different link and thus received an incorrect date - https://discord.com/channels/366661839620407297/903889378231844875/926755119213731840. (Scroll down the discord channel for more links).

~~~~~

Description:

~~~~~

This video shows the highest arras.io scores over time.

=====

Darker/More-Transparent bars marked with `[LEGACY]` are "Legacy Arras Scores", which were done with a tank that has been significantly nerfed since that score. These scores appear in the Legacy Arras Scores sheet, not the Highest Arras Scores sheet.

The graphic starts from November 15, 2018 because that is the date when "Highest Arras Scores" was added to the Arras World Records Spreadsheet.

This project took about 1 week to finish. I made a python script to track down timestamps for every score on Highest and Legacy Arras Scores and used flourish.studio to generate the visualization. You can check out the interactive Flourish graphic at this link:

https://public.flourish.studio/visualisation/8189030/

Code: 
https://github.com/Road6943/Arras-Highest-Scores-Over-Time-Bar-Chart-Race

=====

Special Thanks to the following people for helping me!

- Zeo'Xé aka ZeZo
- Bastard aka Skrialik
- Sjoshi
- Canvas aka oue
- Onyx aka gonials
- northwest ordinance of 1787
- Awootube
- Mine
- 🥕Crazy Carrot🥕

=====

Arras's Score Data is harder to parse than Diep's, but I tried my best. However, there may be occasional mistakes such as scores I forgot to add or incorrect dates.

The main criteria used for this graphic is not necessarily when a score was gotten, but rather when it was submitted to the World Records Spreadsheet. Thus, scores that were obtained on a Date A, but only submitted on a much later Date B, will be assigned Date B to both make my life easier and also to maintain consistency across all scores.

These are the following methods used to assign dates to scores, in order of prominence:

1) Use the Timestamp column(s) of the Submissions/Older Submissions/Oldest Submissions Spreadsheets
2) dl.airtable.com image links are assigned a date of November 15, 2018 (the date when HAS was first moved from Airtable to the Arras WR Spreadsheet)
3) Any further scores that can be manually located on the original HAS Airtable Sheet and were not already assigned a date by a previous method will be hardcoded with the date November 15, 2018 in the script
4) If an image is stored on Discord's CDN, the date of the image is calculated from the snowflake in the url
5) For all undated scores with their proof images stored in an imgur album, a special script will webscrape the imgur link for the album creation date
6) The proof link will be opened up manually. If a computer date can be seen, then that is used. Else, the upload date recorded on the image/video host will be used
7) If a computer date visible in image, that date is used
8) Searching the Discord server to see if an image can be located and its date identified
9) Messaging players on Discord or Reddit to ask them when one of their scores were gotten

=====

Music Used:
––––––––––––––––––––––––––––––
Hall of the Mountain King by Kevin MacLeod http://incompetech.com 
Creative Commons — Attribution 4.0 International — CC BY 4.0 
Free Download / Stream: https://bit.ly/hall-of-the-mountain-king
Music promoted by Audio Library https://youtu.be/2RDX5sVEfs4
––––––––––––––––––––––––––––––
