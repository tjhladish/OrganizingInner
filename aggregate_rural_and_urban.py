#!/usr/bin/python

# This script takes an input file ("all_cases.csv") that contains location-stratified
# disease time series data, and aggregates the disease incidence based on whether the
# location was rural or urban.
#
# You will be making multiple changes to the code below.  Each time you make a
# substantial change, verify that you have not changed the output from the program.
#
# The Exercise:
#
# 1) Read through, understand, and annotate the code.  If you do not understand a line,
# investigate it by experimenting, checking python references, and talking to others.
#
# 2) If there anything simple that can be done to make the code more readable or
# manageable, go ahead and do that--things like renaming variables or reducing the use
# of "magical" numbers.
#
# 3) Break the code up into functional units, and then turn those units into functions.
#
# 4) Write a class that can represent the input data in a useful way.  Create a parser
# function in the class that takes a line of text from the file and returns structured
# data that is useful and easy to understand.

# for these two dicts
urban_ts = dict()
rural_ts = dict()
# for every year
for year in range(1995,2012):
    # create a list with a 0 for each week
    urban_ts[year] = [0]*52 # number of weeks in year?
    rural_ts[year] = [0]*52

header_line = True
# iterate through each line in the file
for line in file("all_cases.csv"):
    # we need to skip the first (header) line
    if header_line == True:
        header_line = False
        continue

    # parse the line into a list of strings
    parts = line.strip().split(',')
    year = int(parts[0])
    muni_num = parts[4]
    case_time_series = map(int, parts[5:])
    if muni_num in ['050','101','041']: # urban municipality codes
        for week in range(0,52):
            urban_ts[year][week] += case_time_series[week]
    else:
        # it's a rural municipality
        for week in range(0,52):
            rural_ts[year][week] += case_time_series[week]

print urban_ts[2011]
print rural_ts[2011]
exit()
header_line = True
print "location total_cases"
for line in file("all_cases.csv"):
    if header_line == True:
        header_line = False
        continue
    parts = line.strip().split(',')
    year = int(parts[0])
    muni_num = parts[4]
    data = map(int, parts[5:])
    print parts[3], parts[4], sum(map(int, parts[5:]))

print
print
print
print "year week urban rural"
for year in range(1995,2012):
    for week in range(0,52):
        print year, week+1, urban_ts[year][week], rural_ts[year][week]
