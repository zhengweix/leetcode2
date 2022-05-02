class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        a = a[::-1]
        b = b[::-1]
        la = len(a)
        lb = len(b)
        l = max(la, lb)
        c = ''
        for i in range(l):
            if i < la and i < lb:
                aa, bb = int(a[i]), int(b[i])
                c += str(aa ^ bb ^ carry)
                if aa + bb + carry >= 2:
                    carry = 1
                else:
                    carry = 0
            elif lb > la:
                bb = int(b[i])
                c += str(bb ^ carry)
                if bb == 1 and carry == 1:
                    carry = 1
                else:
                    carry = 0
            elif la > lb:
                aa = int(a[i])
                c += str(aa ^ carry)
                if aa == 1 and carry == 1:
                    carry = 1
                else:
                    carry = 0
        if carry == 1:
            c += str(carry)
        return c[::-1]
