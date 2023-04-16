
#####Author= Naufil Bin Imran
######Assignment/ Part: HW6-Q2
########Date Due: 2022-03-31
############I pledge that I have completed this assignment without collaborating with anyone else, in conformance with the NYU School of Engineering Policies and Procedures on Academic Misconduct.



def get_decimal_time(hour, minute, second):
    total_seconds = second + (minute*60) + (hour*3600)
    french_hour = total_seconds // 10000
    french_minute = (total_seconds-(10000*french_hour)) // 100
    french_second = total_seconds % 100
    return "{}:{}:{}".format(french_hour, french_minute, french_second)

decimal_time=get_decimal_time(16, 7, 46)
print(decimal_time)


def  get_decimal_date(month, date, year):
    if month == 1:
        french_month = "Nivôse"
    elif month == 2:
        french_month = "Pluviôse"
    elif month == 3:
        french_month = "Ventôse"
    elif month == 4:
        french_month = "Germinal"
    elif month == 5:
        french_month = "Floréal"
    elif month == 6:
        french_month = "Prairial"
    elif month == 7:
        french_month = "Messidor"
    elif month == 8:
        french_month = "Thermidor"
    elif month == 9:
        french_month = "Fructidor"
    elif month == 10:
        french_month = "Vendémiaire"
    elif month == 11:
        french_month = "Brumaire"
    elif month == 12:
        french_month = "Frimaire"
    french_year = year - 1792
    if date <= 10:
        decade = 1
    elif date > 10 and date <= 20:
        decade = 2
    elif date > 20:
        decade = 3
    return "{} {} Year {}, Décade {}".format(date, french_month, french_year, decade)


revolutionary_date=get_decimal_date(3,22,2022)
print(revolutionary_date)

def get_french_datetime(gregorian_datetime):

    separation_point = gregorian_datetime.find(" ")

    time_string = gregorian_datetime[0:separation_point]

    date_string = gregorian_datetime[separation_point+1:len(gregorian_datetime)-1]

    seperation_colon= time_string.find(":")

    hour_string= time_string[0:seperation_colon]

    seperation_colon2= time_string.find(":",seperation_colon+1)

    minute_string= time_string[seperation_colon+1:seperation_colon2]

    seconds_string= time_string[seperation_colon2+1:]

    decimal_time= get_decimal_time(int(hour_string),int(minute_string),int(seconds_string))


    seperation_slash= date_string.find("/")

    day_string= date_string[0:seperation_slash]

    seperation_slash2= date_string.find("/",seperation_slash+1)

    month_string= date_string[seperation_slash+1:seperation_slash2]

    year_string= date_string[seperation_slash2+1:]    

    decimal_date= get_decimal_date(int(day_string),int(month_string),int(year_string))

    return_string = "{}\n{}".format(decimal_time, decimal_date)
    return return_string


def main():
    gregorian_datetime = "16:07:46 03/22/2022"
    french_datetime = get_french_datetime(gregorian_datetime)
    print(french_datetime)


