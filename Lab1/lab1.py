import timeit, random, string


def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def quick_sort(arr):
    if not arr:
        return arr
    pivot = arr[len(arr) // 2]
    below = [i for i in arr[len(arr)//2 + 1:] if i < pivot]
    above = [i for i in arr[len(arr)//2 + 1:] if i >= pivot]
    return quick_sort(below) + [pivot] + quick_sort(above)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and k < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(l, r):
    result = []
    while l and r:
        result.append(l.pop(0)) if l[0] <= r[0] else result.append(r.pop(0))
    result = result + l if l else result + r
    return result


def heap_sort(arr):
    for i in range(len(arr) // 2, -1, -1):
        move_down(arr, i, len(arr) - 1)
    for i in range(len(arr)-1, 0, -1):
        if arr[0] > arr[i]:
            arr[0], arr[i] = arr[i], arr[0]
            move_down(arr, 0, i - 1)


def move_down(arr, i, n):
    j = 2 * i + 1
    while j <= n:
        if j < n and arr[j] < arr[j + 1]:
            j += 1
        if arr[j] > arr[i]:
            arr[j], arr[i] = arr[i], arr[j]
            i = j
            j = 2 * i + 1
        else:
            return


def timer(arr, algo, run, default=False):
    sort = timeit.Timer(lambda: globals()[algo](arr.copy())) if not default else timeit.Timer(lambda: sorted(arr.copy()))
    return {algo: format(sort.timeit(run)/run, '.20f')}


def test(arr):
    def _insertion(a):
        insertion_sort(a)
        return str(a == sorted(a))

    def _quick(a):
        return str(sorted(a) == quick_sort(a))

    def _bubble(a):
        bubble_sort(a)
        return str(sorted(a) == a)

    def _merge(a):
        return str(sorted(a) == merge_sort(a))

    def _heap(a):
        heap_sort(a)
        return str(sorted(a) == a)
    return "Insertion: " + _insertion(arr.copy()) + \
           "\nQuick: " + _quick(arr.copy()) + \
           "\nBubble: " + _bubble(arr.copy()) + \
           "\nMerge: " + _merge(arr.copy()) + \
           "\nHeap: " + _heap(arr.copy())

if __name__ == '__main__':
    strings = [''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(5, 10))) for i in range(10000)]
    n = [1000]

    algorithms = ["quick_sort", "merge_sort", "bubble_sort", "insertion_sort", "heap_sort"]
    runs = 1000

    for x in algorithms:
        print(x + "\n")
        results = {}
        for i in n:
            ints = [int(random.random() * 1000) for i in range(i)]
            strings = [''.join(random.choice(string.ascii_lowercase) for k in range(random.randint(5, 10))) for j in range(i)]
            results.update(timer(strings, x, runs))
            for k in results.keys():
                print(str(i) + ": " + str(results[k]) + "\n")


