def is_prime(cc):
    if cc <= 1:
        return False
    elif cc == 2 or cc == 3:
        return True
    elif cc % 2 == 0:
        return False

    for i in range(3, int(cc**0.5) + 1, 2):
        if cc % i == 0:
            return False

    return True

def countPrimeSetBits(left, right):
    count = 0
    for i in range(left, right + 1):
        set_bit_count = bin(i)[2:].count('1')
        if is_prime(set_bit_count):
            count += 1
    return count

result = countPrimeSetBits(842, 888)
print(result)
