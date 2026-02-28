# if name == __main__: this script can be imported or run standalone
#                       functions and classes in this module can be reused
#                       without the main block of code

# eg : library 
d#ef main():
    # program goes here
  #  pass
#if __name__ == '__main__':
    #main()
# python runs files in 2 ways 
# 1) run directly (as a program)
# 2) import inside another function 
# this way comes under the import way
# we use this bcz to prevent the unwanted code execution when importing .
# unwanted execution i avoided by this eg :
def add(a,b):
    return a+b
def main():
    # program goes here
    print("calculator is ready")
    add(5,4)
if __name__ == '__main__':
    main()
# we can run this in 2 ways , only add part or add and main both parts ...this is the main benefits
# either python add.py{only add part is executed} , or python main.py{only main part}
