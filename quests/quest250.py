"""
Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps

Notes:

    the returned string should only contain lowercase letters


"""
import re
def kebabize(string:str)->str:
    res_list = [re.sub(pattern='\d+',string=word.lower()+'-',repl='') for word in re.split("([A-Z][^A-Z]*)", string) if word ]
    ans = "".join(res_list)
    if ans.endswith('-'):
        return ( ans[0:-1])
    else:
        return ans
