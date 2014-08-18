import time 

# some good info on designing PID controls, http://brettbeauregard.com/blog/2011/04/improving-the-beginners-pid-introduction/ 
class PID(object):
	"""PID Control of heater, we need to rework this for time proportioning control"""
	def __init__(self,target,kp=0,ki=0,kd=0.0,interval=60):
		
		self.lastRun = time.time()

		# tuning values 
		self.kp = kp
		self.ki = ki
		self.kd = kd
		self.time_interval = interval

		# zero vars  
		self.input = 0
		self.target = 0
		self.err = 0
		self.last_err = 0
		self.err_sum = 0

	def compute(self,input_data):

		# get the error
		self.input = input_data

		# get current time and diff
		curr = time.time()
		time_diff = round(curr - self.lastRun)

		# get the error
		self.err = self.target - self.input
		
		# and the sum of error over time
		self.err_sum += (self.err * time_diff)
		
		# and rt of change
		self.d_err = (self.err - self.last_err ) / time_diff

		# update last run time to current
		self.last_err = self.err
		self.lastRun = curr

		# output
		return (self.ki * self.err + self.ki * self.err_sum + self.kd * self.d_err)

