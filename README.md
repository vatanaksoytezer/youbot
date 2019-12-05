# In Youbot Terminal
pc-set-ip
run-driver
# In Remote PC Terminal, without youbot-set-ip, with source-youbot
roscore
# For Teleop
roslaunch youbot_teleop youbot_teleop.launch
# For Autonomous
# roslaunch youbot_mapping gmapping.launch
roslaunch youbot_omni_navigation move_base_omni.launch
# Multi Robot
roscore
roslaunch youbot_mapping multi-gmapping.launch
roslaunch youbot_omni_navigation move_base_omni.launch

