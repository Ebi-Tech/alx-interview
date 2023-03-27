def canUnlockAll(boxes):
    n = len(boxes)
    # Initialize a boolean list to keep track of which boxes are unlocked
    unlocked = [False] * n
    unlocked[0] = True  # The first box is unlocked
    keys = boxes[0]
    # Initialize the list of keys with the keys from the first box

    # Use a while loop to iterate through the list of keys
    # and unlock the corresponding boxes
    while keys:
        key = keys.pop(0)  # Remove the first key from the list of keys
        if not unlocked[key]:
            unlocked[key] = True
            keys += boxes[key]

    # Use the all() method to check if all boxes are unlocked
    return all(unlocked)
