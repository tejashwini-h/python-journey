# variable scope = where a variable is visible and accessible
# scope resolution => (LEGB) 
# local -> enclosed -> global -> built-in
def func():
    x=1
    print(x)
def func2():
    x=2
    print(x)

func()
func2()
