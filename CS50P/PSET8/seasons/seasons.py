from datetime import date
import inflect
import sys
p = inflect.engine()


def main():
    birthday = input("Birthday: ")
    minutes = get_minutes(birthday)
    print(n2w(minutes))

#calculate minutes since birth
def get_minutes(input):
    try:
        year,month,day=input.split('-')
        birthday = date(int(year),int(month),int(day))
    except:
        sys.exit("YYYY-MM-DD")

    today = date.today()
    delta = (today - birthday)
    return (delta.days * 24 * 60)

#convert numbers to words
def n2w(mins):
    try:
        if (mins < 0) or (mins % 1 != 0):
            raise ValueError
    except:
        raise ValueError
    words = p.number_to_words(mins, wantlist=False).replace(" and", "")

    words += " minutes"
    words = words.capitalize()

    return (words)




if __name__ == "__main__":
    main()