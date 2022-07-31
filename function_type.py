# function에 type을 사용해서 개발 하는 방법
# function에 tpye을 넣어서 개발을 하는 방법을 여러가지가 있으나, 내가 개발하면서, 얻은 방법을 하나씩 예제를 만들어 작성하려고 한다.
#
#
# 1. Parameter에 type을 지정해서 개발
def get_user_info(name: str, email: str, hobby: str):
    print("당신의 이름은 무엇입니까?: ", name)
    print("당신의 이메일은 무엇입니까?: ", email)
    print("당신의 취미 무엇입니까?: ", hobby)
get_user_info("유영남", "andy1@naver.com", "football")
#
# 2. function return에 타입을 지정하기
def get_user_info1(name: str, email: str, hobby: str) -> str: #return #타입이 어떤 타입으로 정할 수 있다. str, int, List, Tuple, etc....
    return f"안녕하세요 제 이름은{name} 이고 이메일은 {email} 입니다. 취미는 {hobby} 입니다"
print(get_user_info1("유영남", "andy1@naver.com", "football"))
#
# 3. 함수 parameter에 함수가 들어가야 할 경우
from typing import Callable
def cal_add(first_number: int, second_number: int) -> int:
    return first_number + second_number
#      call_add(type1, typ2, call_add return type 지정)
# 여기에다가 조금 더 심화를 하자면 get_func에 return 타입까지 지정할 수 있다.
def get_func(func: Callable[[int, int], int]) -> int:
    return func(1, 2)
print(get_func(cal_add))


## Uinon Type
## Uion Type은 개발하다보면, str로 받고싶을 때가 있고, int으로 받고 있을 때가 있다.
##이럴 때 사용하는 타입 방법이 union을 사용해주면 된다.
from typing import Union
def get_age(age: Union[str, int]):
    if type(age) == type("str"):
        return "문자열 타입"
    else:
        return "int 타입"
print(get_age("17"))
print(get_age(17))

## Optional Type
## Optional Type은 있을 수 도 있고 없을 수 도 있을 때 사용한다.
## Optional[str] -----> Optional[str, None] 같다.
from typing import Optional
name: Optional[str] = "a"
print(name)



## 상수 지정해서 처리해주기
## 보통 파이썬에서 대문자로 변수를 지정해주면, 개발자들은 상수라고 인식한다. 하지만, 이런식으로 사용하게 되면 외부에서 변경을 요쳥했을 때 변하게 된다.
## 그렇다면, 이건 상수가 아니다. 상수라는 것을 알려줘야한다.
## Final Type
from typing_extensions import Final
RATE: Final = 300
RATE = 2
print(RATE)


# # Type alias
# 타입에 이름을 넣어주는 것
# # 복잡하게 타입을 지정할 때 가 있을 수 도 있다
## 복잡한 typing들을 변수처럼 지정해서 사용할 수 있다.
from typing import Union, List, Tuple, Dict
v = Union[int, bool, str, float, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, int]]]
value: v = 1


## TypeDict --> 이방법은 requests 데이터를 요청하고 응답같을 받아올 때 json형식으로 return되는데 어떤 타입으로 들어올지 설정할 수 있다.
# from typing import TypedDict
# class UserInfo(TypedDict):
#     name: str
#     age: int
#     email: str
#     address: str
#
# user1: UserInfo = {"name": "andy", "age": 15, "email": "aa@naver.com", "address": "anywhere"}
# print(user1)


