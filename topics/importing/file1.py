variable = 1
print('file1  -  __name__: ', __name__)
def file1_func(): print('file1_func')
print("__name__ is '__main__'" if __name__ == '__main__' else "__name__ is NOT '__main__'", 'in file1')