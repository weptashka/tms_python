# декоратор, заставляющий отработать принимаемую функцию 5 раз
# добавить **kwargs для того, чтобы можно было задекорировать любую функцию, даже с параметрами
def retry_five(inner_function):
    def output_function():
        inner_function()
        inner_function()
        inner_function()
        inner_function()
        inner_function()

    return output_function


@retry_five
def simple_function():
    print("Я простая функция")


simple_function()


# декоратор, перехватывающий и модифицирующий аргументы принимаемой функции:
# суть в том, что так обязательно делать, если оборачиваемая функция должна принять какие-либо аргументы

def change_args(input_function):
    def output_function(*args):
        input_function(*args)
    return output_function


@change_args
def print_info(name, age):
    print(f"name: {name}, age: {age}")


print_info("polly", 22)



# игры с возвращаемым значением оборачиваемой функции

def sum_plus_10(input_function):
    def output_function(*args):
        result = input_function(*args)
        return result + 10
    return output_function


@sum_plus_10
def sum(a, b):
    return a + b


print(sum(4, 5))  # 19

