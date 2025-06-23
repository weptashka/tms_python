# ----- Вложенности, замыкания, области видимости, всякие local и nonlocal
def id_generator(start: int, step: int = 1):
    start -= 1

    def generate():
        nonlocal start
        start += step
        return start
    return generate


generator = id_generator(start=1, step=2)


