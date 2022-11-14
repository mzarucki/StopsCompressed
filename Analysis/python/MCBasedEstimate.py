# Logging
import logging
logger = logging.getLogger(__name__)

from StopsCompressed.Analysis.Region import Region
from StopsCompressed.Analysis.SystematicEstimator import SystematicEstimator
from StopsCompressed.Analysis.SetupHelpers import lepChannels
from Analysis.Tools.u_float      import u_float


class MCBasedEstimate(SystematicEstimator):
    def __init__(self, name, sample, cacheDir=None):
        super(MCBasedEstimate, self).__init__(name, cacheDir=cacheDir)
        self.sample=sample
        # FastSim and 76X only for the MCBasedEstimate. Dirty. Looks whether one of the samples is fastsim.
        self.isFastSim = getattr(sample, "isFastSim", False) 
        
    def _estimate(self, region, channel, setup):

        ''' Concrete implementation of abstract method 'estimate' as defined in Systematic
        '''

        logger.debug( "MC prediction for %s channel %s" %(self.name, channel) )
        if channel=='all':
            # 'all' is the total of all contributions
            logger.debug("Estimate:", sum([self.cachedEstimate(region, c, setup) for c in lepChannels]))
            return sum([self.cachedEstimate(region, c, setup) for c in lepChannels])

        else:
            preSelection = setup.preselection('MC',channel=channel, isFastSim = self.isFastSim)
            cut = "&&".join([region.cutString(setup.sys['selectionModifier']), preSelection['cut']])
            weight = preSelection['weightStr']

            logger.debug( "Using cut %s and weight %s"%(cut, weight) )
    	    print "MC yield: ", setup.lumi/1000.*u_float(**self.sample.getYieldFromDraw(selectionString = cut, weightString = weight) )
            return setup.lumi/1000.*u_float(**self.sample.getYieldFromDraw(selectionString = cut, weightString = weight) )
