import pickle

test_data = ['Save me!', 123.456, True]

f = open('test.data', 'wb')
pickle.dump(test_data, f)
f.close()
f = open('test.data', 'rb')
data = pickle.load(f)
f.close()

print(data)