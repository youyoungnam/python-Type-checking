

## class 내부에서 사용되는 패턴
#  자기자신을 클래스에 넣을 때(호출할 떄 )
from typing import Optional
class Node:
    # #     # 자기자신이 존재하기 전에 자기자신을 먼저 선언해줘야하지 않나?
    # #     # 여기서 사용하는 방법은 콤마를 사용하는것 이럴경우에 optional사용
    def __init__(self, data: int, node: Optional["Node"]):
        self.data =data
        self.node = node
node2 = Node(12, None)
node1 = Node(27, node2)
node0 = Node(30, node1)



## Generic Types
"""
Generic Types
데이터 형식에 의존하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있는 기술
"""
from typing import Union, Optional, TypeVar, Generic
#
# # # 한개만 타입이 들어올 거면 그냥 Int쓰면된다. 근데 들어올게 다양하다. 그러면 옵션을 줄 수 있다
# ARM = TypeVar("ARM", int, float, str)
# HEAD = TypeVar("HEAD", int, float, str)
#
# # 가독성을 위해 T, K, L 이런식으로 타입핑해주는 경우가 있다.
T = TypeVar("T", int, float, str)
K = TypeVar("K", int, float, str)
#
# class Robot(Generic[ARM,HEAD]):
#     def __init__(self, arm : ARM, head : HEAD):
#         self.arm = arm
#         self.head = head
#
#     def decode(self):
#         # 암호를 해독하는 코드  복잡한 코드
#         bbb: Optional[ARM] = None
# robot1 = Robot[int, int](123, 2323)
# robot2 = Robot[str, int](2313232323,23123214214551)
# robot3 = Robot[float, str](213241490123, 2325738592)

class Robot1(Generic[T, K]):
    def __init__(self, arm : T, head : K):
        self.arm = arm
        self.head = head

    def decode(self):
        # 암호를 해독하는 코드  복잡한 코드
        bbb: Optional[T] = None

robot1 = Robot1[int, int](123, 2323)
robot2 = Robot1[str, int](2313232323,23123214214551)
robot3 = Robot1[float, str](213241490123, 2325738592)

T1 = TypeVar("T1", int, float, str)
K1 = TypeVar("K1", int, float, str)

def test(x: T1) -> T1:
    print(x, type(x))
    return x
# test({"a":1}) 딕타입은 안되는 걸 볼 수 있다
test(14)




## __slot _을 통해 클래스 내 객체 내 변수를 관리하자
## 객체 내에 있는 변수들은 __dict__로 관리된다.
# #     파이썬 인터프리터에게 통보 해당 클래스가 가지는 속성을 제한한다
# #     __dict__를 통해 관리되는 객체의 성능을 최적화 한다 -> 다수의 객체 생성시 메모리 사용 공간 대폭 감소
## __slot__을 사용했을 때 메모리 효율은 좋다. 하지만 무작정 쓰는건 안좋을 수 도 있다.
## 클래스를 다 작성 하고 메모리를 제한적으로 사용해도 괜찮을 때 그때 고치면 된다.
class WithoutslotClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
wsc = WithoutslotClass("a", 1)
print(wsc.__dict__)
wsc["b"] = 1
print(wsc.__dict__)

class WithSlotClass:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age

ws = WithSlotClass("andy", 12)
# print(ws.__dict__) ##리스트 내부에 객체가 사용할 변수를 썼으니 제한을 하게 되고 성능을 향상
print(ws.__slots__)
# 내장 함수 메모리 사용량 비교할 수 있다
import timeit



# isinstance(obj, class) 이것은 이 오브젝트가 클래스에한 인스턴스인지 아닌지 체킹해주는 것
# print(isinstance(88, int))
# print(isinstance(88, float))
# print(isinstance(88, bool))
## type를 체크해주는 함수를 하나 만들자
### 해당 instane를 가지고 함수를 하나 만들자

def type_checker(obj, type) -> None:
    if isinstance(obj, type):
        pass
    else:
        raise TypeError("Type Error")

# # # 이렇게 하나하나 타입 체크함수를 만들어주면 생산성이 떨어진다
# # # 중요한 함수같은 경우 사용한다.

# # mypy 권장 사항 하나의 함수를 만든다고 가정했을 때 따로 스크립트 파일을 만들어 unit적으로 만들고 테스트하면 된다 mypy로
# # 중요한 함수면 기능별로 쪼개서 검사하고 붙이고 반복하면 생산성도 있고 경고성도 가지고 간다.