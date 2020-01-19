from statistics import median


def findMedianSortedArrays(nums1, nums2):
    combined = nums1 + nums2
    sorted_combined = sorted(combined)
    return float(median(sorted_combined))


def findMedianSortedArraysSimple(nums1, nums2):
    nums = sorted(nums1 + nums2)
    length = len(nums)
    middle = float(length / 2)
    if length % 2 == 0:
        med = (nums[int(middle)] + nums[int(middle - 1)]) / 2
    else:
        med = nums[int(middle - 0.5)]
    return float(med)


def test_1():
    assert findMedianSortedArrays([1, 3], [2]) == 2.0
    assert findMedianSortedArraysSimple([1, 3], [2]) == 2.0


def test_2():
    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert findMedianSortedArraysSimple([1, 2], [3, 4]) == 2.5


def test_3():
    assert findMedianSortedArrays([3], [-2, -1]) == -1.0
    assert findMedianSortedArraysSimple([3], [-2, -1]) == -1.0


def test_4():
    assert findMedianSortedArrays([], [2, 3]) == 2.5
    assert findMedianSortedArraysSimple([], [2, 3]) == 2.5


def test_5():
    assert findMedianSortedArrays([], [1, 2, 3, 4, 5, 6]) == 3.5
    assert findMedianSortedArraysSimple([], [1, 2, 3, 4, 5, 6]) == 3.5
