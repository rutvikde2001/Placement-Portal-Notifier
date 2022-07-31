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
