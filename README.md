# Arras.io Highest Scores Over Time Bar Chart Race

This repo contains a python script (make_racing_bar_chart.py) that can generate a csv file which can be uploaded to flourish.studio in order to generate an interactive bar chart race for the highest arras scores over time. 

Instructions for using the script are located within it as a giant comment. The process is somewhat complicated and involves downloading multiple google sheets as csv files, changing numerous configuration variables, multiple runs and edits and reruns of the make_racing_bar_chart.py script, and much more, so read the instructions carefully. 

The csv file generated by the script that can be uploaded to flourish.studio will be located in the generated_files directory, and is only generated if a certain config variable is set to True because writing to a csv massively increases the script's runtime