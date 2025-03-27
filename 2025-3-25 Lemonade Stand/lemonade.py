def lemonade(queues):
    # Initialize change value
    change = {
        "5":0,
        "10":0,
        "20":0
    }
    for queue in queues:
        if queue == 5:
            # No change needed
            # Receive $5
            change["5"] += 1
        elif queue == 10:
            if change["5"] > 0:
                # Give back one $5
                change["5"] -= 1
                # Receive $10
                change["10"] += 1
            else:
                # Case cannot give back
                return False
        elif queue == 20:
            if change["10"] > 0 and change["5"] > 0:
                # Give back one $10 and one $5
                change["10"] -= 1
                change["5"] -= 1
                # Receive $20
                change["20"] += 1
            elif change["5"] >= 3:
                # Give bank three $5
                change["5"] -= 3
                # Receive $20
                change["20"] += 1
            else:
                # Case cannot give back
                return False
    # All customer satisfy :)
    return True

# Test Case
assert lemonade([5, 5, 5, 10, 20]) == True, "Error"
assert lemonade([5, 5, 10, 10, 20]) == False, "Error"
assert lemonade([10,10]) == False, "Error"
assert lemonade([5, 5, 10]) == True, "Error"
            

    