num = 5
float_num = 2.12345
my_str = 'abcd'

# 1. % 를 사용하는 방법
print('num: %d' % num + ', float_num: %.2f' % float_num + ', str: %s' % my_str)
# .2f 는 소수점 두 자리까지 출력을 의미

# 2. format 함수를 사용하는 방법
print('num: {}, float_num: {:.2f}, str: {}'.format(num, float_num, my_str))

# 3. f, F 사용
print(f'num: {num}, float_num: {float_num:.2f}, str: {my_str}')
print(F'num: {num}, float_num: {float_num:.2f}, str: {my_str}')
