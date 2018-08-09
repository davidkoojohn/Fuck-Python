from time import sleep


def countdown(n):
    while n > 0:
        yield n
        n -= 1

def main():
    for num in countdown(5):
        print(f'countdown {num}')
        sleep(1)

    print('over!')


    pass

if __name__ == '__main__':
    main()
