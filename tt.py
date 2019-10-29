

#importing libraries
import pandas as pa
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


#importing dataset
def training():
    dataSet = pa.read_csv('default_of_credit_card_clients.csv')
    X = dataSet.iloc[:,1:-1].values
    Y = dataSet.iloc[:,24].values 
    #missing values
    imputer = Imputer(missing_values='NaN',strategy='mean',axis=0)
    imputer = imputer.fit(X[:,:])
    X[:,:]=imputer.transform(X[:,:])
    #training and testing data
    X_training,X_testing,Y_training,Y_testing = train_test_split(X,Y,test_size=0.3,random_state=0)
    #future scaling
    ss_X = StandardScaler()
    X_training = ss_X.fit_transform(X_training)
    X_testing = ss_X.transform(X_testing)
    classifier = KNeighborsClassifier(n_neighbors=20,metric='minkowski',p=2)
    classifier.fit(X_training,Y_training)
    training_score=classifier.score(X_training,Y_training)
    testing_score=classifier.score(X_testing,Y_testing)
    print("\ntraining score:{}".format(training_score))
    print("\ntesting score:{}".format(testing_score))
    print(X_training[1])
    print(X_training[2])
    xx={"classifier":classifier,"imputer":imputer,"ss":ss_X}
    return xx

def testing(xx):
    p=[]
    p.append([])
    limit_balance=input("\n\nenter limit balance(value>0)\n")
    while 1:
        if limit_balance.isdigit():
            limit_balance=int(limit_balance)
            break
        limit_balance=input("\n\nenter appropriate limit balance(value>0)\n")
    while limit_balance<0 :
        limit_balance=int(input("\n\nenter limit balance which is greater than 0\n"))
    p[0].append(limit_balance)
    sex=input("\n\nselect gender 1.male 2.female\n")
    while 1:
        if sex.isdigit():
            sex=int(sex)
            break
        sex=input("\n\nselect gender 1.male 2.female\n")
    while 1:
        if sex==1 or sex==2:
            break
        sex=int(input("\n\nselect appropriate gender 1.male 2.female\n"))
    p[0].append(sex)
    education=input("\n\nselect education level 1.graduate school 2.university 3.high school 4.others\n")
    while 1:
        if education.isdigit():
            education=int(education)
            break
        education=input("\n\nselect education level 1.graduate school 2.university 3.high school 4.others\n")
    while 1:
        if education==1 or education==2 or education==3 or education==4:
            break
        education=int(input("\n\nselect appropriate education level 1.graduate school 2.university 3.high school 4.others\n"))
    p[0].append(education)
    martial_status=input("\n\nselect marriage status 1.married 2.single 3.others\n")
    while 1:
        if martial_status.isdigit():
            martial_status=int(martial_status)
            break
        martial_status=input("\n\nselect marriage status 1.married 2.single 3.others\n")
    while 1:
        if martial_status==1 or martial_status==2 or martial_status==3:
            break
        martial_status=int(input("\n\nselect appropriate marriage status 1.married 2.single 3.others\n"))
    p[0].append(martial_status)
    age=input("\n\nenter age(>=20)\n")
    while 1:
        if age.isdigit():
            age=int(age)
            break
        age=input("\n\nenter age(>=20)\n")    
    while 1:
        if age>19:
            break
        age=int(input("\n\nenter appropriate age(>=20)\n"))
    p[0].append(age)
    repay_status_sept=input("\n\nselect september repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n")
    while 1:
        if repay_status_sept.isdigit():
            repay_status_sept=int(repay_status_sept)
            break
        repay_status_sept=input("\n\nselect september repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n")
    while 1:
        if repay_status_sept>-2 and repay_status_sept<10:
            break
        repay_status_sept=int(input("\n\nselect appropriate september repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n"))
    p[0].append(repay_status_sept)
    repay_status_aug=input("\n\nselect august repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n")
    while 1:
        if repay_status_aug.isdigit():
            repay_status_aug=int(repay_status_aug)
            break
        repay_status_aug=input("\n\nselect august repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n")
    while 1:
        if repay_status_aug>-2 and repay_status_aug<10:
            break
        repay_status_aug=int(input("\n\nselect appropriate august repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n"))
    p[0].append(repay_status_aug)
    repay_status_july=input("\n\nselect july repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n")
    while 1:
        if repay_status_july.isdigit():
            repay_status_july=int(repay_status_july)
            break
        repay_status_july=input("\n\nselect july repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n")
    while 1:
        if repay_status_july>-2 and repay_status_july<10:
            break
        repay_status_july=int(input("\n\nselect appropriate july repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n"))
    p[0].append(repay_status_july)
    repay_status_june=input("\n\nselect june repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n")
    while 1:
        if repay_status_june.isdigit():
            repay_status_june=int(repay_status_june)
            break
        repay_status_june=input("\n\nselect june repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n")
    while 1:
        if repay_status_june>-2 and repay_status_june<10:
            break
        repay_status_june=int(input("\n\nselect appropriate june repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n"))
    p[0].append(repay_status_june)
    repay_status_may=input("\n\nselect may repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n")
    while 1:
        if repay_status_may.isdigit():
            repay_status_may=int(repay_status_may)
            break
        repay_status_may=input("\n\nselect may repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n")
    while 1:
        if repay_status_may>-2 and repay_status_may<10:
            break
        repay_status_may=int(input("\n\nselect appropriate may repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n"))
    p[0].append(repay_status_may)
    repay_status_april=input("\n\nselect april repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n")
    while 1:
        if repay_status_april.isdigit():
            repay_status_april=int(repay_status_april)
            break
        repay_status_april=input("\n\nselect april repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n")
    while 1:
        if repay_status_april>-2 and repay_status_april<10:
            break
        repay_status_april=int(input("\n\nselect appropriate april repay status -1.pay duly 1.payment delay for one month  2.payment delay for two months 3.payment delay for three months 4.payment delay for four months 5.payment delay for five months 6.payment delay for six months 7.payment delay for seven months 8.payment delay for eight months 9.payment delay for nine months and above\n"))
    p[0].append(repay_status_april)
    amt_bill_stmt_sept=input("\n\nenter amount of bill statement in sept\n")
    while 1:
        if amt_bill_stmt_sept.isdigit():
            amt_bill_stmt_sept=int(amt_bill_stmt_sept)
            break
        amt_bill_stmt_sept=input("\n\nenter amount of bill statement in sept\n")
    p[0].append(amt_bill_stmt_sept)
    amt_bill_stmt_aug=input("\n\nenter amount of bill statement in august\n")
    while 1:
        if amt_bill_stmt_aug.isdigit():
            amt_bill_stmt_aug=int(amt_bill_stmt_aug)
            break
        amt_bill_stmt_aug=input("\n\nenter amount of bill statement in aug\n")
    p[0].append(amt_bill_stmt_aug)
    amt_bill_stmt_july=input("\n\nenter amount of bill statement in july\n")
    while 1:
        if amt_bill_stmt_july.isdigit():
            amt_bill_stmt_july=int(amt_bill_stmt_july)
            break
        amt_bill_stmt_july=input("\n\nenter amount of bill statement in july\n")
    p[0].append(amt_bill_stmt_july)
    amt_bill_stmt_june=input("\n\nenter amount of bill statement in june\n")
    while 1:
        if amt_bill_stmt_june.isdigit():
            amt_bill_stmt_june=int(amt_bill_stmt_june)
            break
        amt_bill_stmt_june=input("\n\nenter amount of bill statement in june\n")
    p[0].append(amt_bill_stmt_june)
    amt_bill_stmt_may=input("\n\nenter amount of bill statement in may\n")
    while 1:
        if amt_bill_stmt_may.isdigit():
            amt_bill_stmt_may=int(amt_bill_stmt_may)
            break
        amt_bill_stmt_may=input("\n\nenter amount of bill statement in may\n")
    p[0].append(amt_bill_stmt_may)
    amt_bill_stmt_april=input("\n\nenter amount of bill statement in april\n")
    while 1:
        if amt_bill_stmt_april.isdigit():
            amt_bill_stmt_april=int(amt_bill_stmt_april)
            break
        amt_bill_stmt_april=input("\n\nenter amount of bill statement in april\n")
    p[0].append(amt_bill_stmt_april)
    amt_paid_sept=input("\n\nenter amount paid in sept\n")
    while 1:
        if amt_paid_sept.isdigit():
            amt_paid_sept=int(amt_paid_sept)
            break
        amt_paid_sept=input("\n\nenter amount paid in sept\n")
    while 1:
        if amt_paid_sept>=0:
            break
        amt_paid_sept=int(input("\n\nenter appropriate amount paid in sept\n"))
    p[0].append(amt_paid_sept)
    amt_paid_aug=input("\n\nenter amount paid in aug\n")
    while 1:
        if amt_paid_aug.isdigit():
            amt_paid_aug=int(amt_paid_aug)
            break
        amt_paid_aug=input("\n\nenter amount paid in aug\n")
    while 1:
        if amt_paid_aug>=0:
            break
        amt_paid_aug=int(input("\n\nenter appropriate amount paid in aug\n"))
    p[0].append(amt_paid_aug)
    amt_paid_july=input("\n\nenter amount paid in july\n")
    while 1:
        if amt_paid_july.isdigit():
            amt_paid_july=int(amt_paid_july)
            break
        amt_paid_july=input("\n\nenter amount paid in july\n")
    while 1:
        if amt_paid_july>=0:
            break
        amt_paid_july=int(input("\n\nenter appropriate amount paid in july\n"))
    p[0].append(amt_paid_july)
    amt_paid_june=input("\n\nenter amount paid in june\n")
    while 1:
        if amt_paid_june.isdigit():
            amt_paid_june=int(amt_paid_june)
            break
        amt_paid_june=input("\n\nenter amount paid in june\n")
    while 1:
        if amt_paid_june>=0:
            break
        amt_paid_june=int(input("\n\nenter appropriate amount paid in june\n"))
    p[0].append(amt_paid_june)
    amt_paid_may=input("\n\nenter amount paid in may\n")
    while 1:
        if amt_paid_may.isdigit():
            amt_paid_may=int(amt_paid_may)
            break
        amt_paid_may=input("\n\nenter amount paid in may\n")
    while 1:
        if amt_paid_may>=0:
            break
        amt_paid_may=int(input("\n\nenter appropriate amount paid in may\n"))
    p[0].append(amt_paid_may)
    amt_paid_april=input("\n\nenter amount paid in april\n")
    while 1:
        if amt_paid_april.isdigit():
            amt_paid_april=int(amt_paid_april)
            break
        amt_paid_april=input("\n\nenter amount paid in april\n")
    while 1:
        if amt_paid_april>=0:
            break
        amt_paid_april=int(input("\n\nenter appropriate amount paid in april\n"))
    p[0].append(amt_paid_april)
    p=xx['ss'].transform(p)
    return xx['classifier'].predict(p)[0]


while 1:
    x=int(input("select option\n 1.training \n 2.testing \n 3.exit\n"))
    if x==1:
        xx=training()
    elif x==2:
        t=testing(xx)
        print("the output is {}".format(t))
    else:
        break






