class messanger:
    def sendmsg(self,message):
        self.message=message
        print(f"sending message to {self.message}")
class camera:
    def capture(self):
        print("taking image")
#multiple inheritance
class smartphone(messanger,camera):
    def makecall(self,number):
        self.number=number
        print(f"making call to {self.number}")

s=smartphone()
s.sendmsg("hello everybody")
s.capture()
s.makecall(12345)