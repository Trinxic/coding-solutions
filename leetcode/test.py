"""
[i, 2, 3, 4, 5, 6, 7] => odd = 1, c_odd = 1
[1, i, 3, 4, 5, 6, 7] => odd = 1, c_odd = 2
[1, 2, i, 4, 5, 6, 7] => odd = 0, c_odd = 2
[1, 2, 3, i, 5, 6, 7] => odd = 0, c_odd = 2
[1, 2, 3, 4, i, 6, 7] => odd = 1, c_odd = 3
[1, 2, 3, 4, 5, i, 7] => odd = 1, c_odd = 4
[1, 2, 3, 4, 5, 6, i] => odd = 0, c_odd = 4
"""

"""
[i, 2, 3, 4, 5, 6, 7] => c_odd = 4, result =  4, odd -> c_odd = (7 - 0 - 4) = 3
[1, i, 3, 4, 5, 6, 7] => c_odd = 3, result =  7, even !->
[1, 2, i, 4, 5, 6, 7] => c_odd = 3, result = 10, odd -> c_odd = (7 - 2 - 3) = 2
[1, 2, 3, i, 5, 6, 7] => c_odd = 2, result = 12, even !->
[1, 2, 3, 4, i, 6, 7] => c_odd = 2, result = 14, odd -> c_odd = (7 - 4 - 2) = 1
[1, 2, 3, 4, 5, i, 7] => c_odd = 1, result = 15, even !->
[1, 2, 3, 4, 5, 6, i] => c_odd = 1, result = 16, odd -> c_odd = (7 - 6 - 1) = 0
"""
