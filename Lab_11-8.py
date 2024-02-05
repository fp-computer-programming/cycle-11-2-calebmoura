# Author: Caleb Moura

# Defining length multiples, then setting it so that a new list is created and returned.
def length_multiples(lst):
    new_lst = [val * idx for idx, val in enumerate(lst)]
    return new_lst

def test_length_multiples():
# Test case 1: Contains only integers.
    input_list = [1, 2, 3, 4, 5]
    assert length_multiples(input_list) == [0, 2, 6, 12, 20]

# Test case 2: Contains integer & float values.
    input_list = [1, 2.5, 3, 4.5, 5]
    assert length_multiples(input_list) == [0, 2.5, 6, 13.5, 20]

# Test case 3: Contains only strings.
    input_list = ["a", "bb", "ccc", "dddd", "eeeee"]
    assert length_multiples(input_list) == ["", "bb", "cccc", "dddddd", "eeeeeee"]

if __name__ == "__main__":
    test_length_multiples()