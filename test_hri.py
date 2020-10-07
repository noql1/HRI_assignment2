from naoqi import ALProxy
import time
tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
motionProxy = ALProxy("ALMotion", "127.0.0.1", 9559)

hand= "RShoulderPitch"  # moves forward 
#wrist = "RWristYaw"  # turns left and right 
useSen = 0

while(1):
	x = motionProxy.getAngles(hand, useSen)
	print(x[0])
	if x[0] > 0:
		motionProxy.move(0.0, 0.0, 0.0)
	elif x[0] < 0:
		if x[0] > (-0.9) and x[0] < (-0.65):
			motionProxy.move(1.0, 0.0, 0)
		elif x[0] < (0) and x[0] > (-0.65):
			motionProxy.move(1, 0.0, 0.0)
		elif x[0] > (-0.9):
			motionProxy.move(0.3, 0.0, 0)

	

        
        time.sleep(0.100)
