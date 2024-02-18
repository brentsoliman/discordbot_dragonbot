

ranking = {
    1:"1st",
    2:'2nd',
    3:"3rd",
    4:"4th",
    5:"5th",
    6:"6th",
    7:"7th",
    8:"8th",
    9:"9th",
    10:"10th",
    11:"11th",
    12:"12th",
    13:"13th",
    14:"14th",
    15:"15th",
    16:"16th",
    17:"17th",
    18:"18th",
    19:"19th",
    20:"20th",
    21:"21th",
    22:"22th",
    23:"23th",
    24:"24th",
    25:"25th",
    26:"26th",
    27:"27th",
    28:"28th",
    29:"29th"
}


def getRankingString(lst,timeString):
    ret = "" + "{:>22}".format("{} Leaderboard\n".format(timeString))
    for x in range(len(lst)):
        ret += "\n{:<5}  {:<10}  {} miles".format(ranking[x + 1],lst[x][0],lst[x][1])
    return ret