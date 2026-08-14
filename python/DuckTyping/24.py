class Email:
    def sms(self):
        print("message")
class Whatsapp:
    def sms(self):
        print("message")
def sms1(obj):
    obj.sms()
e=Email()
w=Whatsapp()
sms1(e)
sms1(w)
