class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return "0"
        result=[]
        if (numerator<0) ^ (denominator<0):
            result.append("-")
        nums=abs(numerator)
        den=abs(denominator)

        result.append(str(nums//den))
        remainder=nums%den
        if remainder==0:
            return "".join(result)
        result.append(".")
        rem_pos={}
        while remainder!=0:
            if remainder in rem_pos:
                idx=rem_pos[remainder]
                result.insert(idx,"(")
                result.append(")")
                break
            rem_pos[remainder]=len(result)
            remainder*=10
            result.append(str(remainder//den))
            remainder%=den
        return "".join(result)