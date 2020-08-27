from SortFunctions import quickSort
from SortFunctions import recurSelectionSort
from SortFunctions import selection_sort
import random
import timeit


def main():
    numOfItems = 12  # number of items in array
    numOfTests = 200  # number of tests

    rands1 = random.sample(range(0, 100), numOfItems)
    print("Quick Uns: ", rands1)
    #quickSort(rands1, 0, len(rands1) - 1)
    qtime = timeit.timeit(lambda: quickSort(rands1, 0, len(rands1) - 1),
                          setup="from __main__ import quickSort", number=numOfTests)
    print("Quick Sort took:", qtime)
    print("Quick Srt: ", rands1)

    rands2 = random.sample(range(0, 100), numOfItems)
    print("RecurSelect Uns: ", rands2)
    #recurSelectionSort(rands2, len(rands2))
    # Calling recusrsive selection sort function
    rtime = timeit.timeit(lambda: recurSelectionSort(rands2, len(rands2)),
                          setup="from __main__ import recurSelectionSort", number=numOfTests)
    print("Recursive Selection Sort took:", rtime)
    print("RecurSelect Srt: ", rands2)

    rands3 = random.sample(range(0, 100), numOfItems)
    print("IterSelect Uns: ", rands3)
    # Calling recusrsive selection sort function
    #selection_sort(rands3)
    stime = timeit.timeit(lambda: selection_sort(rands3),
                          setup="from __main__ import selection_sort", number=numOfTests)
    print("Iterative Selection Sort took:", stime)
    print("IterSelect Srt: ", rands3)


if __name__ == "__main__":
    main()
