from SortFunctions import quickSort
from SortFunctions import recurSelectionSort
from SortFunctions import selection_sort
import random
import timeit

NUM_OF_ITEMS = 12  # number of items in array
NUM_OF_TESTS = 1025  # number of tests

def doSort(type):
    #get a clean array each time
    rands = random.sample(range(0, 100), NUM_OF_ITEMS)

    #Select the type of sort
    if type == 'q':
        quickSort(rands, 0, len(rands) - 1)
    elif type == 'r':
        recurSelectionSort(rands, len(rands))
    elif type == 's':
        selection_sort(rands)



def main():
    #NUM_OF_ITEMS = 12  # number of items in array
    #NUM_OF_TESTS = 1025  # number of tests

    rands1 = random.sample(range(0, 100), NUM_OF_ITEMS)
    #print("Quick Uns: ", rands1)
    #quickSort(rands1, 0, len(rands1) - 1)
    qtime = timeit.timeit(lambda: doSort('q'),
                          setup="from __main__ import quickSort", number=NUM_OF_TESTS)
    print("Quick Sort took:", qtime)
    #print("Quick Srt: ", rands1)

    rands2 = random.sample(range(0, 100), NUM_OF_ITEMS)
    #print("RecurSelect Uns: ", rands2)
    #recurSelectionSort(rands2, len(rands2))
    # Calling recusrsive selection sort function
    rtime = timeit.timeit(lambda: doSort('r'),
                          setup="from __main__ import recurSelectionSort", number=NUM_OF_TESTS)
    print("Recursive Selection Sort took:", rtime)
    #print("RecurSelect Srt: ", rands2)

    rands3 = random.sample(range(0, 100), NUM_OF_ITEMS)
    #print("IterSelect Uns: ", rands3)
    # Calling recusrsive selection sort function
    #selection_sort(rands3)
    stime = timeit.timeit(lambda: doSort('s'),
                          setup="from __main__ import selection_sort", number=NUM_OF_TESTS)
    print("Iterative Selection Sort took:", stime)
    #print("IterSelect Srt: ", rands3)


if __name__ == "__main__":
    main()
