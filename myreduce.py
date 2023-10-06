from functools import reduce


def with_index_and_list(aFunc,aList,initialValue=None):
    indexed_list = [ (item, index, aList ) for index, item in enumerate(list)]
    def



@with_index_and_list
def getArgs(previous, current, index, lst):
    print(f"previous: {previous} current: {
          current} index: {index} list: {lst}")
    return None


myList = ["BMW", "Yamaha", "Honda", "Suzuki", "Kawasaki",
          "Ducati", "Triumph", "KTM", "Aprilia", "Harley Davidson"]

print(f"The result is {reduce(getArgs, myList)}")

print(f"The result is {reduce(getArgs, myList, 'None')}")
