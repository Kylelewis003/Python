import datetime
time_str = input("enter date in this format yyyy-mm-dd :")
time=datetime.datetime.strptime(time_str, "%Y-%m-%d") 
    
