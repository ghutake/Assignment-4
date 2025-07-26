file1 = "sample.txt"
try:
    with open(file1, 'r') as file:
        print('reading file content:')
        for index, line in enumerate(file, start=1):
            print(f"line{index}: {line.strip()}")
except fileNotFoundError:
    print(f'error: The file "{file1}" was not found.')