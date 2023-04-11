
def validate(fanc):
    def wrapper(*args, **kwargs):
        result = fanc(*args, **kwargs)
        for i in args:
            if i > 256:
                result_string = "Function call is not valid!"
                return result_string
        result_string = result
        return result_string
    return wrapper

@validate
def set_pixel(x: int, y: int, z: int) -> str:
    return "Pixel created!"


