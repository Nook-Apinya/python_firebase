#from .asyncn import process_pool
from firebase import firebase

dat=firebase.FirebaseApplication('https://python-firebase-125da.firebaseio.com/',None)
data={
    'Age':30,
    'EmpID':'emp02',
    'Name':'Villa',
    'Position':'Tester'

}


result=dat.post('https://python-firebase-125da.firebaseio.com/Employee',data)
print(result)

#fire=firebase.FirebaseApplication('https://python-firebase-125da.firebaseio.com')
firebase = firebase.FirebaseApplication('https://python-firebase-125da.firebaseio.com/', authentication =None)
test=firebase.get('/Employee',None)
print(test)

#test=firebase.get('https://python-firebase-125da.firebaseio.com/Employee',data)
#test = firebase.get('/Data', None)
#print(test)

#for i in test:
#    print(i)