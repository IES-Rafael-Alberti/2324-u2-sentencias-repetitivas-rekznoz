def anos_cumplidos(edad):
    return [str(num) for num in range(1, edad + 1)]

if __name__ == "__main":
    edad = int(input("Ingresa tu edad "))
    num = anos_cumplidos(edad)
    print("Años -")
    for nums in num:
        print(nums)
