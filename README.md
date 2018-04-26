# MultiJoy

This package collates a number of joystick states together and publishes the joystick states in one message. The shipped version of `multijoy` supports 2/3/4 joysticks but it is very easy to support more. 

# Generating new message and launch files

It is easy to modify `multijoy` to support more joysticks. If you want `multijoy` to support 5 joysticks, for example, simply `cd` into `multijoy` and run 

```
$ ./generate.sh 5 && catkin build multijoy
```
and you're done! This creates the files 

```
./msg/MultiJoy5.msg
./launch/joysticks5.launch
```
and also updates the `CMakeLists.txt` for you.
