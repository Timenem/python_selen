# Your mission is to convert the name of a function (a string) from CamelCase ("MyFunctionName") into the Python format ("my_function_name") where all chars are in lowercase and all words are concatenated with an intervening underscore symbol "_".
# Input: A function name as a CamelCase string.
# Output: The same string, but in under_score.
# Example:
#  from_camel_case('MyFunctionName") =='my_function_name'
#  from_camel_case('IPhone') == 'i_phone'
#  from_camel_case('ThisFunctionIsEmpty') == 'this_function_is_empty'
#  from_camel_case('Name') == 'name'
#  How it is used: To apply function names in the style in which they are adopted in a specific language (Python, JavaScript, etc.).
import re 

def from_camel_case(name: str) -> str:
    if name.istitle():
        return name.lower()
    else:
        name.lower()
        x = re.sub(r'([A-Z])', r' \1', name).split()
        x = [i.lower() for i in x]
        answer = "_".join(x)
        return answer        
    


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))
    
    # assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
