
Sounds = {3: "Pling", 5: "Plang", 7: "Plong"}

def is_divisible_by(number, divisor):
    return number % divisor == 0


def raindrops(number):
    return [Sounds[factor] for factor in Sounds if is_divisible_by(number, factor)]


def convert(number):
    speak = raindrops(number)
    return "".join(speak) if speak else str(number)
