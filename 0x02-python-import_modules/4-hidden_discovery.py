import marshal

s = open('hidden_4.pyc')

s.seek(8)

code_obj = marshal.load(s)

