mountain_in_japan = {
    "Mount Fuji": 3776,
    "Mount Kita": 3193,
    "Mount Okuhotaka": 3190,
    "Mount Aino": 3189,
    "Mount Yari": 3180
}

sorted_mountains = dict(sorted(mountain_in_japan.items(), key=lambda item: item[1], reverse=True))

print(sorted_mountains)

