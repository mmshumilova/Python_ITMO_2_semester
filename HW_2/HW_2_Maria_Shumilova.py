#our_str = 'ATAGCCGA' # our string
#x = 0.6   # CG-content
#N = 90000 # amount of random DNA strings


def prob_function(N, x, our_str):
    p_our_str = 1
    p_letter_AT = (1-x)/2
    p_letter_CG = x/2

## 1) prob to get our string
    for letter in our_str:
        if letter == 'G':
            p_our_str *= p_letter_CG
        elif letter == 'C':
            p_our_str *= p_letter_CG
        elif letter == 'A':
            p_our_str *= p_letter_AT
        elif letter == 'T':
            p_our_str *= p_letter_AT

    #print(p_our_str)

# 2) the prob don't get our string in N random DNA strings


    p_not_our_str = (1-p_our_str)**N # N - amount of random DNA strings
    #print(p_not_our_str)

# 3) what's the pbob to get at least 1 our string in N random DNA string
    prob_answ = 1 - p_not_our_str
    return(prob_answ)

prob_function(90000, 0.6, 'ATAGCCGA')
