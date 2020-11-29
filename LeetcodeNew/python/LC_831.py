"""
if email -> format email aka lowercase all and mask the first part
if phone number -> format phonenumber aka take the last 4 number and add prefix
"""


class Solution:
    def maskPII(self, s):
        return self.email(s) if (s.find('@') != -1) else self.phone(s)

    def email(self ,s): # format Email
        s = s.split('@')
        return s[0].lower()[0] + '***** '+ s[0].lower()[-1] + '@' + s[1].lower()

    def phone(self ,s)  :# format phone number
        s = ''.join([l for l in s if l in map(str ,range(0 ,10))])
        return (('+ '+ '* ' *(len(s ) -10) + '-') if (len(s ) -10 >0) else '') + '***-***-' + s[-4:]



