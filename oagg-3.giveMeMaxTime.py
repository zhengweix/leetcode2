class Solution:
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

