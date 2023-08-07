import pywhatkit

#send message to contact
phone_number = input("enter phone number")
pywhatkit.sendwhatmsg(phone_no=phone_number ,message="test",time_hour=7,time_min=20,wait_time=15,tab_close=True,close_time=2) #给手机号发送test，在7点20分
#whatsapp会在7点20分打开，然后等待15秒后，给phone_number发送“test”，然后2秒关闭页面


#send message ot group
group_id = input("your group id")
pywhatkit.sendwhatmsg_to_group(group_id=group_id, message="test",time_hour=7,time_min=20)
