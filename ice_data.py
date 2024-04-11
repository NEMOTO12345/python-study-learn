# プログラムを賢くしていく

# 171cm 60kg 女
# 172cm 59kg 男
# 167cm 51kg 男
# 168cm 57kg 女
# 159cm 54kg 女

# ユーザー入力で身長、体重を入力させる
# ↓
# 男女判断
# ↓
# 性別をユーザーに入力させる

# human.csvに情報を追加
# その際、学習機が正解だったら1、間違っていたら0をD列に追記する



from sklearn import svm

sei = ["","男","女"]
data,data_sei = [],[]

with open("data/human.csv", "r") as f:
    for line in f:
        temp = line.strip().split(",")
        data.append([int(temp[0]),int(temp[1])])
        data_sei.append(int(temp[2]))

#学習機を作る
clf = svm.SVC(gamma=0.01)
clf.fit(data,data_sei)

h = int(input("身長:"))
w = int(input("体重:"))

judg = clf.predict([[h,w]]) #多重配列で渡す,戻り値は配列
print(f"{sei[judg[0]]}です。") #戻り値が配列なので0番目を指定

ans = int(input("正解は？1：男、2：女で入力"))

if judg == ans:
    print("成功")
    score = 1
else:
    print("失敗")
    score = 0

with open("data/human.csv", "a") as f:
    f.write(f"{h},{w},{ans},{score}\n")