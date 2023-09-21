def fin_volume(length=1, width=1, depth=1):
    return length * width * depth, length * width


volumen, area = fin_volume(12,13,2)

# result = fin_volume(12,231,3)

print(f"El volumen es: {volumen} y el area es {area}")
# print(result)