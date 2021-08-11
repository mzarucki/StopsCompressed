
class wPtWeight:
	def __init__(self):
		#Parameters for 2016 data
		self.params    = { 
				'norm' : 0.94,
				'a0'   : 1.00,
				'a1'   : 1.052,
				'a2'   : 1.179, #greater than 1
				'a3'   : 1.150, #greater than 1
				'a4'   : 1.057,
				'a5'   : 1.000,
				'a6'   : 0.912,
				'a7'   : 0.783,
				}
		self.sys	= {
				'b0' : 0.0,
				'b1' : 0.052,
				'b2' : 0.00,
				'b3' : 0.003,
				'b4' : 0.004,
				'b5' : 0.008,
				'b6' : 0.012,
				'b7' : 0.023,
				}
	def wPtWeight(self,wpt, sigma=0):
		norm = self.params['norm']
		wPt = wpt
		#wPt = r.leptons[0]['wPt']
		#print "Wpt :", wPt
		if wPt < 50:
			a = 'a0'
			b = 'b0'
		elif wPt >= 50 and wPt < 100:
			a = 'a1'
			b = 'b1'
		elif wPt >= 100 and wPt < 150:
			a = 'a2'
			b = 'b2'
		elif wPt >= 150 and wPt < 200:
			a = 'a3'
			b = 'b3'
		elif wPt >= 200 and wPt < 300:
			a = 'a4'
			b = 'b4'
		elif wPt >= 300 and wPt < 400:
			a = 'a5'
			b = 'b5'
		elif wPt >= 400 and wPt < 600:
			a = 'a6'
			b = 'b6'
		elif wPt >= 600:
			a = 'a7'
			b = 'b7'
		else:
			print "Error: Issue with computing wPt weight"
		corr_fact = self.params[a]
		#print "weights: wPt %s , correction factor: %s"%(wPt,corr_fact)
		w = (norm*corr_fact)+(sys_fact*sigma)

		if sigma==0:
			print (norm*corr_fact)
			return (norm*corr_fact)
		elif sigma <0:
			print ((norm*corr_fact)**2)
			return ((norm*corr_fact)**2)
		elif sigma>0:
			print 1
			return 1
		##up=no weight, nom=weighted, down= (reweight)^2
		#print "weight calculated in function: ", w 
		#return (norm*corr_fact)+(sys_fact*sigma) 
		#return	()	
