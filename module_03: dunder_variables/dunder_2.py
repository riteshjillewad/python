# IF WE RUN THE PYTHON FILE DIRECTLY, Then python will assign the name as __main__

print("This will be always executed!")

if __name__ == "__main__":
    print("This will run only if file is runned direclty from CMD")
else:
    print("This will run only when imported")