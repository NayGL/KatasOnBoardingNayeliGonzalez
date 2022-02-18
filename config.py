def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()

    $ python config.py
Traceback (most recent call last):
  File "/tmp/config.py", line 9, in <module>
    main()
  File "/tmp/config.py", line 3, in main
    configuration = open('config.txt')
IsADirectoryError: [Errno 21] Is a directory: 'config.txt'

def main():
    try:
        configuration = open('config.txt')
    except Exception:
        print("Couldn't find the config.txt file!")

        $ python config.py
Couldn't find the config.txt file!

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")

        $ python config.py
Found config.txt but couldn't read it

$ rm -f config.txt
$ python config.py
Couldn't find the config.txt file!

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


    try:
    open("mars.jpg")
    except FileNotFoundError as err:
    print("got a problem trying to read the file:", err)
got a problem trying to read the file: [Errno 2] No such file or directory: 'mars.jpg'

    try:
    open("config.txt")
    except OSError as err:
     if err.errno == 2:
        print("Couldn't find the config.txt file!")
    elif err.errno == 13:
    print("Found config.txt but couldn't read it")
Couldn't find the config.txt file!