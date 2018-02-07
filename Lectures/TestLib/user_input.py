def user_input():
    global radius
    global start_node
    global end_node
    inp = input("What txt file do you want to read: Germany, Hungary or SampleCoordinates - Possible inputs: g, h and s")
    if inp == "g" or inp == "G":
        radius = 0.0025
        start_node = 1573
        end_node = 10584
        return "GermanyCities.txt"
    elif inp == "h" or inp == "H":
        radius = 0.005
        start_node = 311
        end_node = 702
        return "HungaryCities.txt"
    elif inp == "s" or inp == "S":
        radius = 0.08
        start_node = 0
        end_node = 5
        return "SampleCoordinates.txt"