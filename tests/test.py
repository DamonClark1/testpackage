from testpackage import myFunction

def test_recursion()

    assert myFunction.sum_array([8, 3, 2, 0, 4]) == 17, 'incorrect'
    assert myFunction.sum_array([10, 100, 12, 9, 2]) == 133, 'incorrect'
    assert myFunction.sum_array([1, 2, 3, 4, 50]) == 60, 'incorrect'

    assert myFunction.fibonacci(1) == 1, 'incorrect'
    assert myFunction.fibonacci(7) == 13, 'incorrect'
    assert myFunction.fibonacci(29) == 514229, 'incorrect'

    assert myFunction.factorial(4) == 24, 'incorrect'
    assert myFunction.factorial(12) == 479001600, 'incorrect'
    assert myFunction.factorial(0) == 1, 'incorrect'

    assert myFunction.reverse('hello') == 'olleh', 'incorrect'
    assert myFunction.reverse('How are you') == 'uoy era woH', 'incorrect'
    assert myFunction.reverse('this is a longer sentence that you will need to reverse') == 'esrever ot deen lliw uoy taht ecnetnes regnol a si siht', 'incorrect'

def test_sorting()

    assert myFunction.bubble_sort([8, 3, 2, 0, 4]) == [0, 2, 3, 4, 8], 'incorrect'
    assert myFunction.bubble_sort([10, 100, 12, 9, 2]) == [2, 9, 10, 12, 100], 'incorrect'
    assert myFunction.bubble_sort([1, 20, 3, 4, 50]) == [1, 3, 4, 20, 50], 'incorrect'

    assert myFunction.merge_sort([8, 3, 2, 0, 4]) == [0, 2, 3, 4, 8], 'incorrect'
    assert myFunction.merge_sort([10, 100, 12, 9, 2]) == [2, 9, 10, 12, 100], 'incorrect'
    assert myFunction.merge_sort([1, 20, 3, 4, 50]) == [1, 3, 4, 20, 50], 'incorrect'

    assert myFunction.quick_sort([8, 3, 2, 0, 4]) == [0, 2, 3, 4, 8], 'incorrect'
    assert myFunction.quick_sort([10, 100, 12, 9, 2]) == [2, 9, 10, 12, 100], 'incorrect'
    assert myFunction.quick_sort([1, 20, 3, 4, 50]) == [1, 3, 4, 20, 50], 'incorrect'
