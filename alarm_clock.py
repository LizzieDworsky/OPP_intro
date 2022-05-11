
class AlarmClock:
    def __init__(self):
        self.current_time = ""
        self.alarm_is_on = True
        self.alarm_time = ""

    def update_current_time(self):
        print (self.current_time)
        self.current_time = input ("Please update the current time: ")
        print (f"The current time is now {self.current_time}.")
    
    def set_alarm_time(self):
        print (self.alarm_time)
        self.alarm_time = input ("Please update the time you would like the alarm set to: ")
        print (f"The alarm time is now set to {self.alarm_time}.")
    
    def turn_alarm_on_off(self):
        if self.alarm_is_on == True:
            user_selection = input ("The alarm is currently on. Would you like to turn it off, y/n? ")
            if user_selection == "y":
                self.alarm_is_on = False
                print ("The alarm is now off.")
            else:
                print ("We will leave the alarm on.")
        else:
            user_selection = input ("The alarm is currently off. Would you like to turn it on, y/n? ")
            if user_selection == "y":
                self.alarm_is_on = True
                update_alarm = input (f"The alarm is currently set to {self.alarm_time}. Would you like to change it, y/n? ")
                if update_alarm == "y":
                    self.alarm_time = self.set_alarm_time()
                else:
                    print (f"We will leave the alarm set to {self.alarm_time}.")
            else:
                print ("We will leave the alarm off.")