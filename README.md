# victor
This is work for my thesis project.

# required packages
ros-melodic-desktop-full #need to trim this down...\
ros-melodic-teleop-twist-keyboard\
ros-melodic-robot-localization\
ros-melodic-hector-sensors-description\
ros-melodic-hector-slam\
ros-melodic-ecl-threads\
ros-melodic-ecl-threads\
ros-melodic-ros-control\
ros-melodic-joint-trajectory-controller\
ros-melodic-rplidar-ros\
ros-melodic-gmapping\
ros-melodic-move-base\
ros-melodic-global-planner\
ros-melodic-dwa-local-planner\
ros-melodic-amcl\
ros-melodic-map-server

# to do
change \<arg name="laser" default="sim"/\> to \<arg name="laser" default="rplidar"/\> in bringup.launch, currently facing VM /dev/ttyUSB0 issue\
dynamic obstacle avoidance implementation\
tune pid values\
figure, configure, and assembly bot in real life\
