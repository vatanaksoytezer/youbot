YOUBOT ROS
===============
ROS drivers and navigation stack for Kuka Youbot

In Youbot Terminal (192.168.1.13 for our lab)
-----------
 ```
 $ pc-set-ip # 192.168.1.146 to connect rosmaster in remote PC
 $ run-driver # roscore should be running in remote PC before this command
 ```
In Remote PC Terminal, without youbot-set-ip, with source-youbot
----------------------------------------------------------------
```
$ roscore
$ roslaunch youbot_mapping multi-gmapping.launch
$ roslaunch youbot_omni_navigation move_base_omni.launch
$ roslaunch youbot_teleop youbot_teleop.launch # For Teleop
```
