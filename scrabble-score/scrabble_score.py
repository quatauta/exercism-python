def score(word):
    return sum(letters_scores(word))

def letters_scores(letters):
    return map(lambda letter: letter_score(letter), letters)

def letter_score(letter):
    A = E = I = O = U = L = N = R = S = T = 1
    D = G = 2
    B = C = M = P = 3
    F = H = V = W = Y = 4
    K = 5
    J = X = 8
    Q = Z = 10

    return locals().get(letter.upper(), 0)
