import sys
import zipfile


def addition(a, b):
    to_pad = max(len(a), len(b))
    a = a.rjust(to_pad, '0')[::-1]
    b = b.rjust(to_pad, '0')[::-1]
    a_list = [*map(int, a)]
    b_list = [*map(int, b)]

    result = []
    carryover = 0

    for i in range(len(a)):
        carryover, digit = divmod(a_list[i] + b_list[i] + carryover, 10)
        result.append(str(digit))
    if carryover:
        result.append(str(carryover))

    return ''.join(result[::-1])


def subtraction(a, b):
    to_pad = max(len(a), len(b))
    a = a.rjust(to_pad, '0')
    b = b.rjust(to_pad, '0')
    addendum = ''
    if a < b:
        a, b = b, a
        addendum = '-'
    a_list = [*map(int, a[::-1])]
    b_list = [*map(int, b[::-1])]

    result = []
    carryover = 0
    for i in range(len(a)):
        carryover, digit = divmod(a_list[i] - b_list[i] + carryover, 10)
        result.append(str(digit))
    result = ''.join(result[::-1])
    while result[0] == '0' and len(result) > 1:
        result = result[1:]
    return addendum + result


def main(argv=None):
    path_to_archive = sys.argv[1]
    #  split_path = argv.split('/')
    #  path_to_archive, filename = '/'.join(split_path[:-1]), split_path[-1]

    contents = []
    archive = zipfile.ZipFile(path_to_archive)
    filename = archive.namelist()[0]

    with archive.open(filename) as operations:
        for line in operations:
            contents.append(line.decode("utf-8").strip())
    archive.close()

    a, b, operation = contents
    if operation == '+':
        contents.append(addition(a, b))
    else:
        contents.append(subtraction(a, b))

    contents = '\n'.join(contents)
    with zipfile.ZipFile(path_to_archive, 'w') as archive:
        archive.writestr(filename, contents)
    archive.close()
    # works perfectly fine in my Pycharm with Python3 (python script.py test.zip),
    # modifying txt file directly in .zip,
    # but for whatever reason doesn't work here, and it's impossible to debug.
    # https://drive.google.com/file/d/1NIR67a43JIARL4ayGK-2WXby4scRaycL/view?usp=sharing for proof (video)

if __name__ == '__main__':
    main()