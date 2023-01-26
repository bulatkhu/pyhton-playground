def strings(arr: str or list):
    result = set()

    def parseArray(array):
        for value in array:
            if type(value) == list:
                parseArray(value)
            else:
                print("value is string", value)
                result.add(value)

    parseArray(arr)

    return list(sorted(result))
