# decorator.py
def registrar_chamada(func):
    def wrapper(*args, **kwargs):
        print(f"Chamando o método: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
