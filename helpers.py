import pandas as pd

def definePasserRating(att,comp,yds,td,ints): # computes the passer rating of a player
    try:
        a = ((comp / att) - 0.3) * 5
        b = (yds / att - 3) * 0.25
        c = (td / att) * 20
        d = 2.375 - ((ints / att) * 25 )
        vals = [a,b,c,d]
        for index,x in enumerate(vals):
            if x > 2.375:
                vals[index] = 2.375
            elif x < 0:
                vals[index] = 0

        rating = sum(vals) * 100 / 6
        
        return rating

    except Exception as e:
        return 0
    

def passerRatingByRow(row:pd.Series):
    rating = definePasserRating(row["attempts"],row["completions"],row["passing_yards"],row["passing_tds"],row["interceptions"])
    return round(rating,2)


