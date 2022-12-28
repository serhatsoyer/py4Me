variable = 2
print('file2  -  __name__: ', __name__)
def file2_func1(): print(f'file2_func1  -  variable: {variable}')
def file2_func2(): print('file2_func2'); file2_func1()
print("__name__ is '__main__'" if __name__ == '__main__' else "__name__ is NOT '__main__'", 'in file2')