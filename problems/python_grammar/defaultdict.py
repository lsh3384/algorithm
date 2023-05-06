from collections import defaultdict

int_default_dict = defaultdict(int)
print(int_default_dict['undefined']) # what이라는 키에 해당하는 값이 없음에도 불구하고 0이 출력이 되는 것을 알 수 있다.

str_default_dict = defaultdict(str)
print(str_default_dict['undefined']) # what이라는 키에 해당하는 값이 없음에도 불구하고 빈 문자열이 출력이 되는 것을 알 수 있다.

list_default_dict = defaultdict(list)
print(list_default_dict['undefined']) # what이라는 키에 해당하는 값이 없음에도 불구하고 빈 리스트가 출력이 되는 것을 알 수 있다.

set_default_dict = defaultdict(set)
print(set_default_dict['undefined']) # what이라는 키에 해당하는 값이 없음에도 불구하고 빈 set가 출력이 되는 것을 알 수 있다.


'''
difaultdict를 사용하는 이유는 기본 dictionary에서 key가 없을 때 발생하는 에러를 방지하기 위함이다.
key가 없이 dictionary에 접근해도 difault로 정해놓은 값으로 생성해서 반환해주기 때문에
키에 해당하는 값이 없는 경우에 대한 예외처리를 하지 않아도 되기 때문에 코드가 더 간결해진다. 
코딩 테스트에서 예외 처리하는데 쓰는 시간과, 더욱더 가독성이 좋은 코드를 작성할 수 있기 때문에
핵심이 되는 로직에 더 집중할 수 있다는 장점이 있다.
'''