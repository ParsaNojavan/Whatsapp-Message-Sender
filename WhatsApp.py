import pywhatkit
import pyautogui

NumList = list(map(str,input("Enter the whatsapp numbers separated by kamma : ").split(",")))
Message = input("Please enter the message you want to send : ")
for i in NumList:
    pywhatkit.sendwhatmsg_instantly(i, Message,tab_close=True)
    pyautogui.press("enter")
    print("Message sent to : " + i)

print("All messages sent successfully.")


