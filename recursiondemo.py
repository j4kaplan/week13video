

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)


def reverse(s):
    if len(s) <=1:
        return s
    return reverse(s[1:]) + s[0]


def ispalindrome(text):
    if len(text) <=1:
        return True
    if text[0] != text[-1]:
        return False
    return ispalindrome(text[1:-1])

def fib(n):
    if n<3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    num = int(input("what humber do you want to calculate?"))
    result_fib = factorial(num)
    print(f"the factorial of {num} is {result_fib}")
    fib_result = fib(num)
    print(f"the fibonacci result for {num} is {fib_result}")


    #result = factorial(100)
    #print(result)
    #reversed_string = reverse("qwertyuiop")
    #print(reversed_string)
    #text_to_test = "ASDFGHJKLKJHGFDSA"
    #result_text = ispalindrome(text_to_test)
    #print(f"is {text_to_test} reversible a palindrome? {result_text}")


main()