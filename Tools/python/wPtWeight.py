
class wPtWeight:
	def __init__(self):
		#Parameters for 2016 data
		self.params    = { 
		    'norm' : 0.94,
		    'a0'   : 1.00,
		    'a1'   : 1.052,
		    'a2'   : 1.179,
		    'a3'   : 1.150,
		    'a4'   : 1.057,
		    'a5'   : 1.000,
		    'a6'   : 0.912,
		    'a7'   : 0.783,
		    }
	def wPtWeight(self,wpt):
		norm = self.params['norm']
		wPt = wpt
		#wPt = r.leptons[0]['wPt']
		#print "Wpt :", wPt
		if wPt < 50:
			a = 'a0'
		elif wPt >= 50 and wPt < 100:
			a = 'a1'
		elif wPt >= 100 and wPt < 150:
			a = 'a2'
		elif wPt >= 150 and wPt < 200:
			a = 'a3'
		elif wPt >= 200 and wPt < 300:
			a = 'a4'
		elif wPt >= 300 and wPt < 400:
			a = 'a5'
		elif wPt >= 400 and wPt < 600:
			a = 'a6'
		elif wPt >= 600:
			a = 'a7'
		else:
			print "Error: Issue with computing wPt weight"
		corr_fact = self.params[a]
		#print "weights: wPt %s , correction factor: %s"%(wPt,corr_fact)
		return norm*corr_fact 
				
