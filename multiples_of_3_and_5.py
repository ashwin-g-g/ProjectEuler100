#EulerProject100
# Problem 1
# Multiples of 3 and 5
#Solution by: Ashwin (Twitter @ashwin_g_g)

def multiplesOf3and5(limit):
    sum = 0
    i = 3
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

def main():
    limit = int(input("Input the limit : "))
    sum = multiplesOf3and5(limit)
    print(f"Sum of all the multiples of 3 and 5 below {limit} = {sum}")

if __name__ == "__main__":
    main()