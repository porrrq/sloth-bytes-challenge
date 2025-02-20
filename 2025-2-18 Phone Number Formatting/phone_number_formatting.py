def format_phone_number(nums:list) -> str:
    '''
    Formatting a list of number to phone number.
    
    Args:
        nums (list): The list of 10 numbers (0-9)
    
    Returns:
        str: A phone number e.g (555) 555-5555
    '''
    return f'({nums[0]}{nums[1]}{nums[2]}) {nums[3]}{nums[4]}{nums[5]}-{nums[6]}{nums[7]}{nums[8]}{nums[9]}'

assert format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
assert format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8]) == "(519) 555-4468"
assert format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7]) == "(345) 501-2527"

if __name__ == "__main__":
    print(f"1.) \nFrom: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]\nTo: {format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])}\n")
    
    print(f"2.) \nFrom: [5, 1, 9, 5, 5, 5, 4, 4, 6, 8]\nTo: {format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8])}\n")
    
    print(f"3.) \nFrom: [3, 4, 5, 5, 0, 1, 2, 5, 2, 7]\nTo: {format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7])}\n")
    
    # OUTPUT:
    # 1.) 
    # From: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # To: (123) 456-7890

    # 2.)
    # From: [5, 1, 9, 5, 5, 5, 4, 4, 6, 8]
    # To: (519) 555-4468

    # 3.)
    # From: [3, 4, 5, 5, 0, 1, 2, 5, 2, 7]
    # To: (345) 501-2527
    





