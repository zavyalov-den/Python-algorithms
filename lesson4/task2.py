import timeit
import cProfile


def sieve(n):
    def gen_sieve(size):
        sieve = [i for i in range(size)]
        sieve[1] = 0
        for i in range(2, size):
            if sieve[i] != 0:
                j = i + i
                while j < size:
                    sieve[j] = 0
                    j += i

        res = [i for i in sieve if i != 0]
        return res
    arr = gen_sieve(n**2)
    # print(len(arr))
    return arr[n - 1]


def prime(n):
    res = []
    num = 2

    while len(res) < n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            res.append(num)

        num += 1

    return res[n - 1]


print(timeit.timeit("sieve(10)", number=100, globals=globals()))  # 0.0037530999999999953
print(timeit.timeit("sieve(50)", number=100, globals=globals()))  # 0.0866797      x23
print(timeit.timeit("sieve(250)", number=100, globals=globals()))  # 2.402756      x648

print(timeit.timeit("prime(10)", number=100, globals=globals()))  # 0.003346000000000071
print(timeit.timeit("prime(50)", number=100, globals=globals()))  # 0.04826639999999971    x27
print(timeit.timeit("prime(250)", number=100, globals=globals()))  # 1.3055485999999998    x393

cProfile.run("sieve(100)")  # 1    0.003    0.003    0.004    0.004 task2.py:6(gen_sieve)
cProfile.run("sieve(500)")  # 1    0.118    0.118    0.145    0.145 task2.py:6(gen_sieve)
cProfile.run("sieve(2500)")  # 1    3.118    3.118    3.772    3.772 task2.py:6(gen_sieve)

cProfile.run("prime(100)")  # 541    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run("prime(500)")  # 3571    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run("prime(2500)")  # 22307    0.002    0.000    0.002    0.000 {built-in method builtins.len}


# Оба варианта показывают квадратичную зависимость от N, однако при больших значениях prime сильно превосходит конкурента,
# во многом благодаря "слабой" реализации моего алгоритма на основе решета. Алгоритм стоило бы оптимизировать, но я не смог сходу
# придумать эффективный алгоритм подсчета зависимости необходимого размера "решета" от искомого N.
