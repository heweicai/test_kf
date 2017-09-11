# _*_coding:utf-8_*_
def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
print('{0:.4f}'.format(1.0/3))
a = "This is the first sentence. \
This is the second sentence."
b = 'This is the first line\nThis is the second line'
print(a)
print(b)
