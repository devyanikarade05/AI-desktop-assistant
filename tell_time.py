import datetime as dt

def tell_time(query):
    query = query.lower()
    if "time" in query:
        hour = dt.datetime.now().strftime("%H")
        minute = dt.datetime.now().strftime("%M")

        if int(hour)>12:
          return f"The time is {int(hour)-12} bajke {minute} minutes."
        else:
            return f"The time is {hour} baajke {minute} minutes."
    return ""