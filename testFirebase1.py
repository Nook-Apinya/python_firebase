#from .asyncn import process_pool
from firebase import firebase

firebase=firebase.FirebaseApplication('https://python-firebase-125da.firebaseio.com/',None)
data={
    'Age':30,
    'EmpID':'emp02',
    'Name':'Testing',
    'Position':'Tester'

}
result=firebase.post('https://python-firebase-125da.firebaseio.com/',data)
print(result)
