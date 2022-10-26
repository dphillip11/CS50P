#these are zero indexed

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

def main():

    type = False
    while type == False:
        date = input("Date:")
        type = checkdate(date)

    print(f"{y}-{m:02}-{d:02}")



def checkdate(input):
    # update variables globally
    global m
    global d
    global y

    #check seperation type, "/" or " "
    if "/" in input:
        #incorrect format will result in failed checkdate
        try:
            # split into varaiables
            m, d, y = input.split(sep = "/")

            #convert them to integers
            m = int(m)
            d = int(d)
            y = int(y)

            #check they are with reasonable range
            if  int(m) > 12 or int(d) > 31:
                return False
            else:
                #satisfy criteria, so pass
                return True
        except:
            return False

    #second seperation type
    elif " " in input and "," in input:
        try:
            m, d, y = input.split(sep = " ")
            #remove comma after date
            d = d.rstrip(",")
            m = months.index(m.title()) + 1
            m = int(m)
            d = int(d)
            y = int(y)
            if  m > 12 or d > 31:
                return False
            else:
                return True
        except:
            return False

    else:
        return False

main()