def factorial(num) {
    if (num == 0) {
        return 1
    } else {
        return num * factorial(num - 1)
    }
}

def number = 5
def result = factorial(number)
#test
println("Factorial of $number is: $result")
#test
#test

