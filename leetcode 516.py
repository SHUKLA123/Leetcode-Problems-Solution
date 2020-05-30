def manachers( S ):
    T = [0] * (2 * (len(s)) + 3)
    sen_char = "@"
    start_sen = "!"
    end_sen = "#"
    for i in range(len(T)):
        if i == 0:
            T[i] = start_sen
        elif i % 2 == 0 and i < len(T) - 1:
            s_index = (i - 1) // 2
            T[i] = S[s_index]
        elif i % 2 == 1 and i < len(T) - 1:
            T[i] = sen_char
        else:
            T[i] = end_sen
    P = [0] * len(T)

    center = right = 0
    max_len = index = 0
    for i in range(1, len(T) - 1):
        mirror = 2 * center - i
        if i < right:
            P[i] = min(right - i, P[mirror])
        while T[i + P[i] + 1] == T[i - (P[i] + 1)]:
            P[i] += 1
        if i + P[i] > right:
            right = i + P[i]
            center = i

        if P[i] > max_len:
            max_len = P[i]
            index = i

    t_arr = T[ index - max_len: index + max_len + 1 ]
    word_arr = [ c for c in t_arr if c != sen_char and c != start_sen and c != end_sen ]
    word = "".join(word_arr)

    return word
# Driver program 
text1 = "bbbab"
print(manachers(text1)) 

# text2 = "abaaba"
# findLongestPalindromicString(text2) 

# text3 = "abababa"
# findLongestPalindromicString(text3) 

# text4 = "abcbabcbabcba"
# findLongestPalindromicString(text4) 

# text5 = "forgeeksskeegfor"
# findLongestPalindromicString(text5) 

# text6 = "caba"
# findLongestPalindromicString(text6) 

# text7 = "abacdfgdcaba"
# findLongestPalindromicString(text7) 

# text8 = "abacdfgdcabba"
# findLongestPalindromicString(text8) 

# text9 = "abacdedcaba"
# findLongestPalindromicString(text9) 

# # This code is contributed by BHAVYA JAIN 
