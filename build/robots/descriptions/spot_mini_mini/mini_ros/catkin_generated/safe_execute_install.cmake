execute_process(COMMAND "/home/nwhu/catkin_ws/build/robots/descriptions/spot_mini_mini/mini_ros/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/nwhu/catkin_ws/build/robots/descriptions/spot_mini_mini/mini_ros/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
