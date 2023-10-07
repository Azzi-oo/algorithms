
def greet(name='azat'):
    print(f'Hello, {name} !')
    greet2(name)
    print('getting ready to say bye...')
    bye()
    print(greet())


def greet2(name):
    print(f'how are you, {name} ?')
def bye():
    print('ok bye!')