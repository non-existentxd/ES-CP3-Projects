import logging
logging.basicConfig(level=logging.DEBUG)

def buggy_functions(a,b):
    result = a * b
    logging.debug(f"a: {a} b: {b} result: {result}")
    return result

#we could use an assert here
print(buggy_functions("2", 3)) #Expect output is 6
