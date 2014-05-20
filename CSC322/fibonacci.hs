h3 :: Int -> Integer
h3 0 = 0
h3 n = 2 * h3 (n-1) +1

h4 :: Int -> Integer
h4 0 = 0
h4 n = 2 * h4(n-1) + h3(n - (n - 1))



fib :: Int -> Integer
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

memoized_fib :: Int -> Integer
memoized_fib = (map fib [0 ..] !!)
               where fib 0 = 0
                     fib 1 = 1
                     fib n = memoized_fib (n-2) + memoized_fib (n-1)
