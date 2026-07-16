class Solution(object):
    def defangIPaddr(self, address):
        return address.replace('.','[.]')
        

class Solution(object):
    def defangIPaddr(self, address):
        ans=""
        for i in address:
            if i!='.':
                ans+=i
            else:
                ans+='[.]'

        return ans