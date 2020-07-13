def format_duration(seconds):

    if seconds == 0:
        return "now"
        
    remseconds = ("second",seconds % 60)
    mins = seconds // 60
        
    remmins = ("minute", mins % 60)
    hours = mins // 60
    
    remhours = ("hour", hours % 24)
    days = hours // 24

    remdays = ("day", days % 365)
    years = ("year", days // 365)
    
    outlst = []

    for i in remseconds, remmins, remhours, remdays, years:
        if i[1]:
            if i[1] > 1:
                outlst.insert(0, str(i[1]) + " " + i[0] + "s")
            else:
                outlst.insert(0, str(i[1]) + " " + i[0])

    print(outlst)
                
    if len(outlst) > 2:
        return ', '.join(outlst[:-1]) + " and " + str(outlst[-1])
    elif len(outlst) == 2:
        return " and ".join(outlst)
    elif len(outlst) == 1 :
        return outlst[0]
