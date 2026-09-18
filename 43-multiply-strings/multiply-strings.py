class Solution(object):
    def multiply(self, num1, num2):
        #x=int(num1)
        #y=int(num2)
        #product=x*y
        #return str(product)
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        n1, n2 = len(num1), len(num2)
        # result can have at most n1 + n2 digits
        result = [0] * (n1 + n2)
        
        # Reverse iterate so that we go from least significant digit to most
        for i in range(n1 - 1, -1, -1):
            digit1 = ord(num1[i]) - ord('0')
            for j in range(n2 - 1, -1, -1):
                digit2 = ord(num2[j]) - ord('0')
                
                # Position in result array
                p1 = i + j       # higher digit position
                p2 = i + j + 1   # lower digit position
                
                mul = digit1 * digit2
                total = mul + result[p2]
                
                result[p2] = total % 10
                result[p1] += total // 10
        
        # Convert result array to string, skipping leading zeros
        result_str = ''.join(map(str, result))
        result_str = result_str.lstrip('0')
        
        return result_str if result_str else "0"