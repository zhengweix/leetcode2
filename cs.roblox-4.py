class Solution:
    '''
    A user is uploading a big file to your server. The upload is done by sending file chunks of consecutive byte ranges, and the byte ranges for all chunks are represented as a two-dimensional array chunks. For each chunk chunks[i], the byte range is stored in an array of two 64-bit integers: chunks[i][0] is the index of the leftmost byte in the ith chunk, and chunks[i][1] is the index of the rightmost byte in the ith chunk (both indices are inclusive, 1-based).

    Your task is to determine the total number of bytes (of the overall file) received after each file chunk is received. Note that chunks may intersect or even fully replicate the previous ones - i.e., sending the same data twice.

    Example
    For chunks = [[1, 1], [2, 2], [3, 3]], the output should be solution(chunks) = [1, 2, 3].
    The first chunk only contains the byte 1, so the total number of bytes received becomes 1 after this chunk.
    The second chunk only contains the byte 2, so the total number of bytes received becomes 2 after this chunk.
    The third chunk only contains the byte 3, so the total number of bytes received becomes 3 after this chunk.
    https://codesignal.s3.amazonaws.com/uploads/1622366667087/1.mp4

    Note: If you are not able to see the video, use this link to access it.
    For chunks = [[1, 1], [2, 2], [3, 5]], the output should be solution(chunks) = [1, 2, 5].
    The first chunk only contains the byte 1, so the total number of bytes received becomes 1 after this chunk.
    The second chunk only contains the byte 2, so the total number of bytes received becomes 2 after think chunk.
    The third chunk contains bytes from 3 to 5, so the total number of bytes received becomes 5 after this chunk (from 1 to 5).
    https://codesignal.s3.amazonaws.com/uploads/1622366692624/2.mp4

    Note: If you are not able to see the video, use this link to access it.
    For chunks = [[1, 9], [1, 3], [8, 15], [6, 9], [2, 5]], the output should be solution(chunks) = [9, 9, 15, 15, 15].
    The first chunk contains bytes from 1 to 9, so the total number of bytes received becomes 9.
    The second chunk does not add new data, so the total number of bytes received does not change after this chunk.
    The third chunk contains bytes from 8 to 15, so the total number of bytes received becomes 15 after this chunk (from 1 to 15).
    The rest of the chunks contain bytes that were already received, so none of them change the total number of bytes received.
    https://codesignal.s3.amazonaws.com/uploads/1622366711262/3.mp4

    Note: If you are not able to see the video, use this link to access it.
    For chunks = [[7, 9], [1, 3], [8, 15], [6, 9], [2, 4]], the output should be solution(chunks) = [3, 6, 12, 13, 14].
    Expand to see the example video.
    Note: If you are not able to see the video, use this link to access it.

    Input/Output
    [execution time limit] 4 seconds (py3)
    [input] array.array.integer64 chunks
    An array of arrays, each of which represents the indices of the leftmost and rightmost bytes contained in each file chunk.

    Guaranteed constraints:
    1 ≤ chunks.length ≤ 1000,
    chunks[i].length = 2,
    1 ≤ chunks[i][0] ≤ chunks[i][1] ≤ 1012.

    [output] array.integer64
    An array of integers, each of which represents the cumulative total number of bytes received after each file chunk.

    Input:
chunks:
[[1,1],
 [2,2],
 [3,3]]
Expected Output:
[1, 2, 3]

Input:
chunks:
[[1,1],
 [2,2],
 [3,5]]
Expected Output:
[1, 2, 5]

Input:
chunks:
[[1,9],
 [1,3],
 [8,15],
 [6,9],
 [2,5]]
Expected Output:
[9, 9, 15, 15, 15]

Input:
chunks:
[[7,9],
 [1,3],
 [8,15],
 [6,9],
 [2,4]]
Expected Output:
[3, 6, 12, 13, 14]

Input:
chunks: [[1,1000000000000]]
Expected Output:
[1000000000000]

Input:
chunks:
[[1000000000000,1000000000000],
 [1000000000000,1000000000000],
 [10000000000,100000000000]]
Expected Output:
[1, 1, 90000000002]

Input:
chunks:
[[1,10],
 [10,100],
 [100,1000],
 [1000,10000]]
Expected Output:
[10, 100, 1000, 10000]

Input:
chunks:
[[1,2],
 [1,16],
 [1,9],
 [1,44],
 [1,38]]
Expected Output:
[2, 16, 16, 44, 44]

Input:
chunks:
[[20,24],
 [20,31],
 [20,49],
 [20,91],
 [20,89]]
Expected Output:
[5, 12, 30, 72, 72]

Input:
chunks:
[[242319992485,888494425039],
 [890253050257,893986666716],
 [888022315788,983197327824],
 [375477269778,544174442651],
 [372646369775,471869607388],
 [104710990462,767613232623],
 [885899371431,984870237450],
 [590383734375,800503393032],
 [605928833001,947931236759],
 [948695791408,988903707680],
 [773919986477,782808658175],
 [251948207514,573096090660],
 [90130840141,347207472243],
 [111095701427,417671009162],
 [697732084372,898883057010]]
Expected Output:
[646174432555, 649908049015, 740877335340, 740877335340, 740877335340, 878486337363, 880159246989, 880159246989, 880159246989, 884192717219, 884192717219, 884192717219, 898772867540, 898772867540, 898772867540]
    '''
    def solution(self, songs, animations):