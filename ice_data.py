from sklearn import svm

data = [[7.0],[6.5],[9.1],[12.4],[19.0],[23.6],[28.0],[29.6],[25.1],[18.9],[13.5],[9.9]]

data_sei = [1122200,945500,1187300,1438400,2331200,3607100,3754100,
            4498100,2678400,1562400,1088100,1311300]

#学習機作成
clf = svm.SVC(gamma=0.01)
clf.fit(data,data_sei)


temp = float(input("気温:"))
judg = clf.predict([[temp]])

print(judg[0])