def bridge_suffle(l1, l2):
    # Create an empty array to store the result
    result = []

    # In case that L1 is longer -> use len(l1) to loop
    # Otherwise, use len(l2) to loop
    looper =  len(l1) if len(l1) >= len(l2) else len(l2)
    
    # append value to `result`
    for i in range(0,looper):
        # Try to apped l1[i]
        try:
            result.append(l1[i])
        except:
            pass # if cannot, just pass.
        try:
        # Try to apped l2[i]
            result.append(l2[i])
        except:
            pass # if cannot, just pass.
    return result

# Test case
assert bridge_suffle(["A", "A", "A"], ["B", "B", "B"]) == ["A", "B", "A", "B", "A", "B"], "Error"
assert bridge_suffle(["C", "C", "C", "C"], ["D"]) == ["C", "D", "C", "C", "C"], "Error"