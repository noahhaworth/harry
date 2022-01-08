# Install script for directory: /home/nwhu/catkin_ws/src/robots/descriptions/mini-cheetah-gazebo-urdf/yobo_model/yobotics_gazebo

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/nwhu/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/nwhu/catkin_ws/build/robots/descriptions/mini-cheetah-gazebo-urdf/yobo_model/yobotics_gazebo/catkin_generated/installspace/yobotics_gazebo.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/yobotics_gazebo/cmake" TYPE FILE FILES
    "/home/nwhu/catkin_ws/build/robots/descriptions/mini-cheetah-gazebo-urdf/yobo_model/yobotics_gazebo/catkin_generated/installspace/yobotics_gazeboConfig.cmake"
    "/home/nwhu/catkin_ws/build/robots/descriptions/mini-cheetah-gazebo-urdf/yobo_model/yobotics_gazebo/catkin_generated/installspace/yobotics_gazeboConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/yobotics_gazebo" TYPE FILE FILES "/home/nwhu/catkin_ws/src/robots/descriptions/mini-cheetah-gazebo-urdf/yobo_model/yobotics_gazebo/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/yobotics_gazebo" TYPE PROGRAM FILES
    "/home/nwhu/catkin_ws/src/robots/descriptions/mini-cheetah-gazebo-urdf/yobo_model/yobotics_gazebo/scripts/imu_sensor.py"
    "/home/nwhu/catkin_ws/src/robots/descriptions/mini-cheetah-gazebo-urdf/yobo_model/yobotics_gazebo/scripts/odometry_tf.py"
    "/home/nwhu/catkin_ws/src/robots/descriptions/mini-cheetah-gazebo-urdf/yobo_model/yobotics_gazebo/scripts/odometry.py"
    )
endif()

