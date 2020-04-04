import torch

def word_list(seq, word_to_idx):
    idx = [word_to_idx[w] for w in seq]
    idx_tensor = torch.LongTensor(idx)
    return idx_tensor

def toList(s):
    lst = []
    for x in s:
        lst.append(x)
    return lst

def in_and_out(s, word_to_idx):
    tempIn = []
    tempOut = []
    for i in range(1, len(s)):
        w_o = s[i]
        w_i = s[i-1]
        tempIn.append(word_to_idx[w_i])
        tempOut.append(word_to_idx[w_o])
    return torch.tensor(tempIn), torch.tensor(tempOut)




