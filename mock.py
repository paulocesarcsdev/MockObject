Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
s = 'Paulo'
>>> s.add()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s.add()
AttributeError: 'str' object has no attribute 'add'
>>> from unittest.mock import Mock
>>> m = Mock()
>>> m.add()
<Mock name='mock.add()' id='54795696'>
>>> class SubscriptionModelAdmin:
	def message_user(self):
		return 'ASDF'
	def mark_as_paid(self):
		print(self.message_user())

		
>>> model_admin = SubscriptionModelAdmin()
>>> model_admin.mark_as_paid()
ASDF
>>> old_message_user = SubscriptionModelAdmin.message_user
>>> SubscriptionModelAdmin.message_user = Mock(return_value='XYZ')
>>> model_admin.mark_as_paid()
XYZ
>>> #Restarua a classe model admin
>>> SubscriptionModelAdmin.message_user = old_message_user
>>> model_admin.mark_as_paid()
ASDF
>>> 
