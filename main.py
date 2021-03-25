# def sum_mix(arr):
#     return sum(map(int, arr))
#
#
# print(sum_mix([9, 3, '7', '3']))
# print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))
# print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']))

#==============================================================
# def how_many_dalmatians(n):
#     dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
#
#     if n <= 10:
#         return dogs[0]
#     elif n <= 50:
#         return dogs[1]
#     elif n < 101:
#         return dogs[2]
#     else:
#         return dogs[3]

#================================================================
# def fake_bin(x):
#     result = ""
#     for num in x:
#         if int(num) < 5:
#             result = result + "0"
#         else:
#             result = result + "1"
#     return result
#
# print(fake_bin('17932049'))
#================================================================
# def nth_even(n):
#     return 2 * (n - 1)
#
# print(nth_even(10))
#==============small integer in array====================
# def find_smallest_int(arr):
#    return min(arr)
#
# print(find_smallest_int([78, 56, 232, 12, 11, 43]))
# print(find_smallest_int([78, 56, -2, 12, 8, -33]))
# print(find_smallest_int([0, 1 - 2 ** 64, 2 ** 64]))
#============greeting=====================================

# ===================Sorted alphabetically===============================
# def two_sort(array):
#     return '***'.join(min(array))
#
#
#
# print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))# 'b***i***t***c***o***i***n' )
# print(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]))#, 'a***r***e')
# print(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]))#, 'a***b***o***u***t')
# print(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]))#, 'c***o***d***e')
# print(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]))#, 'L***e***t***s')

# ============================Check if it is a vowel=================================================
# def func(inp):
#     return [chr(v) if v in map(ord, "aeiou") else v for v in inp]
#
# print(func([118, "u", 120, 121, "u", 98, 122, "a", 120, 106, 104, 116, 113, 114, 113, 120, 106]))
# # print[118, 117, 120, 121, 117, 98, 122, 97, 120, 106, 104, 116, 113, 114, 113, 120, 106]),
# print(["e", 121, 110, 113, 113, 103, 121, 121, "e", 107, 103], [101, 121, 110, 113, 113, 103, 121, 121, 101, 107, 103]),
# print([118, 103, 110, 109, 104, 106], [118, 103, 110, 109, 104, 106]),
# print([107, 99, 110, 107, 118, 106, 112, 102], [107, 99, 110, 107, 118, 106, 112, 102]),
# print([100, 100, 116, "i", "u", 121], [100, 100, 116, 105, 117, 121]),


#============Longest word========================
# def find_longest(string):
#     return max(map(len, string.split()))
#
# print(find_longest("The quickkkkkk white fox jumped around the massive dog"))
# (find_longest("Take me to tinseltown with you"), 10)
# (find_longest("Sausage chops"), 7)
# (find_longest("Wind your body and wiggle your belly"), 6)
# (find_longest("Lets all go on holiday"), 7)
#========================================================================

# def sum_mix(arr):
#     return sum([int(i) for i in arr])
        #return sum(map(int, arr))   best choice
#print(sum_mix([9, 3, '7', '3']))#, 22)
# print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))#, 42)
# print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']))#, 41)
# print(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']))#, 45)
# print(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]))#, 61)

# =======================================================
# def correct_tail(body, tail):
#     return(True if body[-1] == tail else False)
#
#
# print(correct_tail("Fox", "x"))#, True)
# print(correct_tail("Rhino", "o"))#, True)
# print(correct_tail("Meerkat", "t"))#, True)
# print(correct_tail("Emu", "t"))#, False)
# print(correct_tail("Badger", "s"))#, False)
# print(correct_tail("Giraffe", "d"))#, False)

# my_str = 'Discworld'
# print(my_str.endswith('jockey'))
#===================================================================
# def fake_bin(x):
#     return ''.join('0' if c < '5' else '1' for c in x)



#==============return an array of all integers between the input parameters, including===============





