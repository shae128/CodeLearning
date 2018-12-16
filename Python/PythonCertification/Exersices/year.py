def leapCommon(years):

    for year in years:
        if year % 4 != 0:
            print('Common Year')
        elif year % 100 != 0:
            print('Leap Year')
        elif year % 400 != 0:
            print('Common Year')
        else:
            print('Leap Year')


leapCommon([1900, 2000, 2016, 1987])
