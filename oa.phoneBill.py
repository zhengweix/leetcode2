from math import *
class Solution:
    '''
    Your monthly phone bill has just arrived, and it's unexpectedly large. You decide to verify the amount by recalculating the bill based on your phone call logs and the phone company's charges.

    The logs are given as a string S consisting of N lines separated by end-of-line characters (ASCII code 10). Each line describes one phone call using the following format: "hh:mm:ss,nnn-nnn-nnn", where "hh:mm:ss" denotes the duration of the call (in "hh" hours, "mm" minutes and "ss" seconds) and "nnn-nnn-nnn" denotes the 9-digit phone number of the recipient (with no leading zeros).

    Each call is billed separately. The billing rules are as follows:
    If the call was shorter than 5 minutes, then you pay 3 cents for every started second of the call (e.g. for duration "00:01:07" you pay 67 * 3 = 201 cents).
    If the call was at least 5 minutes long, then you pay 150 cents for every started minute of the call (e.g. for duration "00:05:00" you pay 5 * 150 = 750 cents and for duration "00:05:01" you pay 6 * 150 = 900 cents).
    All calls to the phone number that has the longest total duration of calls are free. In the case of a tie, if more than one phone number shares the longest total duration, the promotion is applied only to the phone number whose numerical value is the smallest among these phone numbers.

    Write a function: class Solution { public int solution(string S); }
    that, given a string S describing phone call logs, returns the amount of money you have to pay in cents.
    For example, given string S with N = 3 lines:
    "00:01:07,400-234-090
    00:05:01,701-080-080
    00:05:00,400-234-090"

    the function should return 900 (the total duration for number 400-234-090 is 6 minutes 7 seconds, and the total duration for number 701-080-080 is 5 minutes 1 second; therefore, the free promotion applies to the former phone number).

    Assume that:
    N is an integer within the range [1..100];
    every phone number follows the format "nnn-nnn-nnn" strictly;
    there are no leading zeros;
    the duration of every call follows the format "hh:mm:ss" strictly (00 ≤ hh ≤ 99, 00 ≤ mm, ss ≤ 59);
    each line follows the format "hh:mm:ss,nnn-nnn-nnn" strictly; there are no empty lines and spaces.
    '''
    @staticmethod
    def phoneBill(input):
        mp = {}  # Create a hashmap to store the phone number and the total call duration for it
        for record in input.split("\n"):
            time, num = record.split(",")
            duration = int(time[:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:8])
            # If already have an entry for a phone number then add this total duration to the existing one else just add it
            mp[num] = duration + mp.get(num, 0)

        # Find the phone call with the longest duration in event of a tie use the one with the least numerical value
        mxDuration, mxNumVal, mxNum = 0, 0, ''
        for num, duration in mp.items():
            if duration > mxDuration:
                mxNum = num
                mxNumVal = int(num.replace('-', ''))
                mxDuration = duration
            elif duration == mxDuration:
                curNumVal = int(num.replace('-', ''))
                if curNumVal < mxNumVal:
                    mxNum = num
                    mxNumVal = curNumVal

        # Finally, evaluate the total cost of the phone bill.
        ans = 0
        for num, duration in mp.items():
            if num == mxNum:
                continue
            if duration > 300:
                ans += ceil(duration/60) * 150
            else:
                ans += duration * 3
        return ans

phoneLog = "00:01:07,400-234-090" + "\n" +"00:05:01,701-080-080" + "\n" +"00:05:00,400-234-090";
print(Solution.phoneBill(phoneLog))