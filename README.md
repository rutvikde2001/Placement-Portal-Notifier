# Placement-Portal-Notifier
A simple Python Web-Scraping script that notifies user if there is any new update on SAKEC's Placement Portal for Windows 10 & 11

To use this tool Simply:
1. Download Directory dist>Placement.exe
2. Create a file named password.txt
3. In this file, on first line add your Registration Number.
4. On Second Line add your account password.
5. Now you can run the exe and get notified on all updates on time.


To run it on Startup
1. Create a new task in Task Schedular and name it.
2. Check the box for Run with Highest Privilege.
3. Set Trigger as At log on of any User.
4. Set Action as Start a Program and Select Placement.exe
5. Now add the password.txt file at location C:\Windows\System32\
6. Run the newly created task.

![InkedScreenshot 2022-08-01 000822](https://user-images.githubusercontent.com/68609114/182040668-b9b96e4f-8344-4071-9c67-9e884e54ea07.jpg)


# Whatsapp Notifier Bot
A simple Python Web-Scraping script that notifies user using whatsapp web, if there is any new update on SAKEC's Placement Portal. Only one person needs to run this program at all times using their whatsapp web account.

To use this tool Simply:
1. Download Directory Whatsapp bot
2. Create a file named password.txt
3. In this file, on first line add your Registration Number.
4. On Second Line add your account password.
5. Check your google chrome version and download and place the file in this directory from this link: https://chromedriver.chromium.org/downloads (My chrome driver is Version 108.0.5359.125) 
6. After Downloading the excutable name it as chromedriver.exe and place it in Whatsapp bot folder
7. Using python on a terminal run pip install -r requirement.txt
8. Update the nameList in bot.pyw with exact names you want to send placement updates to.
9. After sucessfully installing all packages, Run bot.pyw file preferable on VSCode or terminal
10. A Chrome window will open asking you to login Whatsapp web using QRCode (There is only 50sec wait to scan your QRCode).
11. Once Logged in the code checks for updates every 15 mins on the portal and sends message on whatsapp.

![image](https://user-images.githubusercontent.com/68609114/211365609-44a372eb-e7d1-47da-bfad-8aa0bc6bcf17.png)

10.
