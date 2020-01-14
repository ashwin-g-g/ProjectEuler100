#EulerProject100
#Problem 2
#Even Fibonacci numbers
#Solution by: Ashwin (Twitter @ashwin_g_g)

def evenFiboNumberSum(limit):
    num_1 = 1
    num_2 = 2
    next_num = 0
    final_sum = 0
    while num_1 <= limit:
        if num_1 % 2 == 0:
            final_sum += num_1
        next_num = num_1 + num_2
        num_1 = num_2
        num_2 = next_num
    return final_sum
def main():
    limit = int(input("Enter the limit : "))
    sum = evenFiboNumberSum(limit)
    print(f"Sum of even numbers of the fibonacci series is : {sum}")
    return

if __name__ == main():
    main()
