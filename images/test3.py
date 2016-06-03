# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

import datetime

class PhoneCall ():

    cost_per_sec_under_5_min = 3
    cost_per_min_over_5_min = 150

    def __init__ (self, call_duration, line):
        self.call_duration = call_duration
        self.line = line
    def calculate_cost (self):
        if self.call_duration < datetime.timedelta(minutes=5):
            return int(self.cost_per_sec_under_5_min * self.call_duration.total_seconds())
        else:
            tmp = self.cost_per_min_over_5_min * int((self.call_duration.total_seconds()/60))
            tmp += self.cost_per_min_over_5_min if self.call_duration.total_seconds()%60 != 0 else 0
            return tmp

class Callee ():
    def __init__ (self, phone_number):
        self.phone_number = phone_number
        self.calls = list()
        self._isMaxCallTime = False

    def add_phone_call(self, line, call_duration):
        self.calls.append(PhoneCall(call_duration, line))

    def calc_total_call_costs(self):
        if self._isMaxCallTime == True:
            return 0

        total_cost = 0
        for call in self.calls:
            total_cost += call.calculate_cost()
        return total_cost

    def calc_total_call_duration (self):
        total_duration = datetime.timedelta()
        for call in self.calls:
            #print(call.call_duration)
            total_duration += call.call_duration

        return total_duration

    def setAsMaxCallTime(self):
        self._isMaxCallTime = True

class MonthlyPhoneBill():
    def __init__(self, phone_bill_str):
        self.dict_of_callees = self.dict_phone_logs(phone_bill_str)

    def parse_phone_call_line(self, line):

        tmp = line.split(',')
        time_str = tmp[0]
        time_obj = datetime.datetime.strptime(time_str, '%H:%M:%S')
        timedelta = datetime.timedelta(hours=time_obj.hour, minutes=time_obj.minute, seconds=time_obj.second)

        phone_num_str = int(self._get_digits(tmp[1]))

        return (phone_num_str, timedelta)

    def _get_digits(self, S):
        digits = ""
        count = 0
        for char in S:
            if char.isdigit():
                count += 1
                digits += char

        return digits

    def dict_phone_logs (self, S):

        dict_of_callees = dict()
        lines = S.split("\n")
        count = 0
        for line in lines:
            (phone_str, call_duration) = self.parse_phone_call_line(line)

            if phone_str not in dict_of_callees:
                dict_of_callees[phone_str] = Callee(phone_str)

            dict_of_callees[phone_str].add_phone_call(count, call_duration)
            count += 1

        return dict_of_callees

    def find_and_set_most_called(self):
        max_duration = datetime.timedelta()

        for phone_number, callee  in self.dict_of_callees.items():
            total_call_duration = callee.calc_total_call_duration()
            if total_call_duration > max_duration:
                list_of_phone_numbers = [phone_number]
                max_duration = total_call_duration
            elif total_call_duration == max_duration:
                list_of_phone_numbers.append(phone_number)

        if len(list_of_phone_numbers) == 0:
            self.dict_of_callees[list_of_phone_numbers[0]].setAsMaxCallTime()
        else:
            self.dict_of_callees[min(list_of_phone_numbers)].setAsMaxCallTime()

    def calculate_cost_of_phone_bill(self):
        total_cost = 0
        for phone_number, callee  in self.dict_of_callees.items():
            total_cost += callee.calc_total_call_costs()

        return total_cost

def solution(S):
    # write your code in Python 2.7


    monthly_bill = MonthlyPhoneBill(S)

    monthly_bill.find_and_set_most_called()


    return monthly_bill.calculate_cost_of_phone_bill()

    # calculate the costs of the rest of the callees

    pass


print(solution('00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090\n00:01:07,400-234-091\n00:05:20,400-234-091'))