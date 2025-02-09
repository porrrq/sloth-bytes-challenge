import re

def hoursPassed(time1,time2):
    pattern = r"(\d+):00\s(\w+)"
    t1_match = re.findall(pattern,time1)
    t2_match = re.findall(pattern,time2)
    t1 = int(t1_match[0][0]) + 12 * (t1_match[0][1]=="PM")
    t2 = int(t2_match[0][0]) + 12 * (t2_match[0][1]=="PM")
    if t2 - t1 == 0:
        return "no time passed"
    else:
        return f"{t2-t1} hours"
    




assert hoursPassed("3:00 AM", "9:00 AM") == "6 hours", "Error"
assert hoursPassed("2:00 PM", "4:00 PM") == "2 hours", "Error"
assert hoursPassed("1:00 AM", "3:00 PM") == "14 hours", "Error"
assert hoursPassed("4:00 PM", "4:00 PM") == "no time passed", "Error"