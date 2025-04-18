def happyYear(year: int):
    while True:
        year += 1
        y_list = [char for char in str(year)]
        y_set_list = list(set(y_list))
        if sorted(y_list) == sorted(y_set_list):
            found = True
            return year
        else:
            continue
        
if __name__ == "__main__":
    print(happyYear(2017))
    print(happyYear(1990))
    print(happyYear(2021))