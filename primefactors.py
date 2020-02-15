#EulerProject100
# Problem 3
# Largest Prime Factor
#Solution by: Ashwin (Twitter @ashwin_g_g)

def largest_prime_factor(num):
    prime = 2
    max = 1
    while prime <= num:
        if num % prime == 0:
            max = prime
            num = num / prime
        else:
            prime += 1
    return max

def main():
    number = int(input("Enter the number:"))
    result = largest_prime_factor(number)
    print(f"The largest prime factor is : {result}")

if __name__ == "__main__":
    main()
