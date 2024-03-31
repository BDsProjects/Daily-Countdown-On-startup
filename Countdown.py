import os
import datetime #Pulls current and Future Dates
import tkinter as tk #For Generating the display window

CurrentTime = datetime.datetime.now()
FormatCurrentTime = CurrentTime.strftime("%Y-%m-%d %H:%M:%S") #Erases decimals places from the seconds
print(FormatCurrentTime) #Display truncated Current time

FutureDate = datetime.datetime(2024, 5, 5, 9, 45, 0)
FormatFutureDate = FutureDate.strftime("%Y-%m-%d %H:%M:%S")
print(FutureDate)

TimeTill = FutureDate - CurrentTime
#FormatTimeTill = TimeTill.datetime.strftime() 
print(TimeTill)

def create_window():
    window = tk.Tk()
    window.title("Days till Graduation")
    label = tk.Label(window, text="The countdown until graduation on May 5th, at 9:45 AM is " + str(TimeTill))
    label.pack()
    window.mainloop()

create_window()


#What need to be done: 
#1. Truncate TimeTill and make as a datetime object (might be the right word)
#2. Fill the text in with correct identifiers so that is displays it as "this many hours, days, minutes, seconds, etc"
#3. Customize the window and add effects color, etc
#4. Integrate into system so that it opens once or twice a day regardless of startup mode. 