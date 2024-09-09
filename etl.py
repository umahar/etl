def transform(legacy_data):
    data = {}
    for key, value in legacy_data.items():
        print("Key: ", key)
        print("Value: ", value)
        for char in value:
            data.update({char.lower(): key})
    return data


print(transform({1: ["A", "E", "I", "O", "U"]}))
