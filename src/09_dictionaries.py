"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
dict = {
    "lat": 42,
    "lon": -120,
    "name": "Fourth?"
}
waypoints.append(dict)

print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE

for d in waypoints:
    d.update((k, "not a real place") for k, v in d.items() if v == "a place")
    d.update((k, -130) for k, v in d.items() if v == -121)
print("Update:", waypoints)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
def value_for_key(d,key1,key2):
    for i in d:
        for k, v in i.items():
            if k == key1 or k ==key2:
                print("Location:", k, v)


value_for_key(waypoints, "lat", "lon")