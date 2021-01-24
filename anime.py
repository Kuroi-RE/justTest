import requests as request  # calling request
import time


def progressBar(iterable, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)

    def printProgressBar(iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                         (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    printProgressBar(0)
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    print()


items = list(range(0, 57))

for item in progressBar(items, prefix='Progress:', suffix='Complete', length=50):
    time.sleep(0.1)

print("Welcome to Anime Search!")
username = input("Anime Title: ")
response = request.get(
    "https://mhankbarbar.herokuapp.com/api/dewabatch?q=" + username)
    # calling result
if response.json()['status'] == 200:
    print(response.json()['result'])
    # make Error
if response.json()['status'] == False:
    print(response.json()['error'])
## end line