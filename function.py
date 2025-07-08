def even_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")



def area_of_triangle(base, height):
    area = 0.5 * base * height
    print(f"Area of triangle is {area}")



def volume_of_cuboid(length, width, height):
    volume = length * width * height
    print(f"Volume of cuboid is {volume}")


def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(5))

def febbo(n):
    a = 0
    b = 1
    for i in range(n):
        next = a+b
        a = b
        b = next
        print(b , end = " ")   

febbo(10) 

