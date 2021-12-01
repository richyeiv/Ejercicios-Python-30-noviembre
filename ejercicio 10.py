def es_anagrama(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

print(es_anagrama("evil", "live"))
