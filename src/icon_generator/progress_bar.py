
def printProgressBar (iteration, total, decimals = 1, ):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
    """

    length = 100
    fill = '█'
    printEnd = "\r"
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\rProgress |{bar}| {percent}%', end = printEnd)

    if iteration == total: 
        print("\nGenerating icons completed! :)")