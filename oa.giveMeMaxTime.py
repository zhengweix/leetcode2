class Solution:
    '''
    You are given a string that represents time in the format hh:mm.
    Some of the digits are blank (represented by ?).
    Fill in ? such that the time represented by this string is the maximum possible. Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.

    Example 1:
    Input: "?4:5?"
    Output: "14:59"

    Example 2
    Input: "23:5?"
    Output: "23:59"

    Example 3:
    Input: "2?:22"
    Output: "23:22"

    Example 4:
    Input: "0?:??"
    Output: "09:59"

    Example 5:
    Input: "??:??"
    Output: "23:59"

    google
    '''
    def giveMeMaxTime(self, input: str) -> str:
        def transform(input: str) -> list:
            output = []
            input = input.split(':')
            for i in input:
                for j in i:
                    output.append(int(j) if j != '?' else j)
            return output
        arr = transform(input)
        s = ''
        h = arr[0] if arr[0] != '?' else 2
        hh = arr[1] if arr[1] != '?' else 3
        if hh < 4:
            s += str(arr[0]) if arr[0] != '?' else str(2)
        else:
            s += str(arr[0]) if arr[0] != '?' else str(1)

        if h < 2:
            s += str(arr[1]) if arr[1] != '?' else str(9)
        else:
            s += str(arr[1]) if arr[1] != '?' else str(3)
        s += ':'
        s += str(arr[2]) if arr[2] != '?' else str(5)
        s += str(arr[3]) if arr[3] != '?' else str(9)
        return s

