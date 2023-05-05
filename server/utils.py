def data(state):
    if state == 'open':
        ActIndex = '1'
        AcsRes = '1'
        Time = '1'
    else:
        ActIndex = '1'
        AcsRes = '0'
        Time = '1'
    
    return 'DATA={"ActIndex":"' + ActIndex + '","AcsRes":"' + AcsRes + '","Time":"' + Time + '"}'
