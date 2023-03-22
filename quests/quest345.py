S = '''Alabama,AL
Alaska,AK
Arizona,AZ
Connecticut,CT
Georgia,GA
Hawaii,HI
Iowa,IA
Kansas,KS
Kentucky,KY
Louisiana,LA
Maine,ME
Maryland,MD
Minnesota,MN
Mississippi,MS
Missouri,MO
Montana,MT
Nevada,NV
Pennsylvania,PA
Tennessee,TN
Texas,TX
Vermont,VT
Virginia,VA
Guam,GU
Northern Mariana Islands,MP
U.S. Virgin Islands,VI'''
def abbr(s):
    return {x[0]: x[1] for i in S.split('\n') if (x:=i.split(','))}.get(s,
        (lambda s: ''.join(filter(str.isupper, s)) if ' ' in s else s[:2].upper())(s))
