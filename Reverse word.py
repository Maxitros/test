inp = input('Word>> ')
inp_word = inp.split(' ')
inp_word = inp_word[-1::-1]
out = ' '.join(inp_word)
print(out)
