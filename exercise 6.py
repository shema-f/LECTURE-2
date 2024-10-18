def number_to_words(n):
    if n == 0:
        return "zero"

    below_20 = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
        "seventeen", "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    thousands = ["", "thousand", "million", "billion"]

    def words(num):
        if num < 20:
            return below_20[num]
        elif num < 100:
            return tens[num // 10] + ("" if num % 10 == 0 else " " + below_20[num % 10])
        elif num < 1000:
            return below_20[num // 100] + " hundred" + ("" if num % 100 == 0 else " " + words(num % 100))
        else:
            for i, word in enumerate(thousands):
                if num < 1000 ** (i + 1):
                    return words(num // (1000 ** i)) + " " + word + ("" if num % (1000 ** i) == 0 else " " + words(num % (1000 ** i)))

    return words(n).strip()

# Get input from the user
try:
    user_input = int(input("Enter a positive integer: "))
    if user_input < 0:
        print("Please enter a positive integer.")
    else:
        print("In words:", number_to_words(user_input))
except ValueError:
    print("Invalid input. Please enter a positive integer.")
