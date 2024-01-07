import codes
import pandas as pd

train_size = 200
test_size = 10

(Zstab_x_train, Zstab_y_train, Xstab_x_train, Xstab_y_train, Zstab_x_test, Zstab_y_test, Xstab_x_test, Xstab_y_test), _ = codes.generate_training_data(train_size=train_size, test_size=test_size)

print("Zstab_x_train: ", Zstab_x_train)
print("Zstab_y_train: ", Zstab_y_train)
print("Xstab_x_train: ", Xstab_x_train)
print("Xstab_y_train: ", Xstab_y_train)

L = 3
first_raw = []
train_examples = []
for i in range(L):
    for j in range(L):
        first_raw.append("Z/Xstab_x_" + str(i) + str(j))
for i in range(2*L):
    for j in range(L):
        first_raw.append("Z/Xstab_y_" + str(i) + str(j))

print(first_raw)

for i in range(train_size):
    train_example = list(Zstab_x_train[i]) + list(Zstab_y_train[i])
    train_examples.append(train_example)
for i in range(train_size):
    train_example = list(Xstab_x_train[i]) + list(Xstab_y_train[i])
    train_examples.append(train_example)
# print(len(first_raw))
# print(len(train_examples[0]))
data = {'name': first_raw}
for i in range(train_size):
    data['train_example_' + str(i)] = train_examples[i]
for i in range(train_size, 2 * train_size):
    data['train_example_' + str(i)] = train_examples[i]
# 创建 DataFrame
df = pd.DataFrame(data)

# 转置 DataFrame
df_transposed = df.T

# 将转置后的 DataFrame 写入 CSV 文件
df_transposed.to_csv('./data/train_onehot_quantum.csv', header=False)
