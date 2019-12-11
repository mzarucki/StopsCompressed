'''
make flat nTuples for stopsCompressed Gen Samples
'''
import ROOT
import os, sys
ROOT.gROOT.SetBatch(True)
from math                               import sqrt, cos, sin, pi, acos

from RootTools.core.standard            import *

from StopsCompressed.Tools.user         import postProcessing_output_directory

from Analysis.Tools.GenSearch           import *
import imp
#
# Arguments
#
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--small',              action='store_true', help='Run only on a small subset of the data?')#, default = True)
argParser.add_argument('--overwrite',          action='store_true', help='Overwrite?')#, default = True)
argParser.add_argument('--targetDir',          action='store',      default='v01')
argParser.add_argument('--sample',             action='store',      default='fwlite_signals_fastSim_Stops2l_200k', help="Name of the sample loaded from signals. Only if no inputFiles are specified")
argParser.add_argument('--inputFiles',         action='store',      nargs = '*', default=[])
argParser.add_argument('--targetSampleName',   action='store',      default=None, help="Name of the sample in case inputFile are specified. Otherwise ignored")
argParser.add_argument('--nJobs',              action='store',      nargs='?', type=int, default=1,  help="Maximum number of simultaneous jobs.")
argParser.add_argument('--job',                action='store',      nargs='?', type=int, default=0,  help="Run only job i")
args = argParser.parse_args()
#
# Logger
#
import RootTools.core.logger as _logger_rt
logger = _logger_rt.get_logger(args.logLevel, logFile = None)

# Load sample either from 
if len(args.inputFiles)>0:
    logger.info( "Input files found. Ignoring 'sample' argument. Files: %r", args.inputFiles)
    sample = FWLiteSample( args.targetSampleName, args.inputFiles)
else:
    sample_file = "$CMSSW_BASE/src/StopsCompressed/samples/python/signals.py"
    samples = imp.load_source( "samples", os.path.expandvars( sample_file ) )
    sample = getattr( samples, args.sample )
    logger.debug( 'Loaded sample %s with %i files.', sample.name, len(sample.files) )

maxEvents = -1
if args.small: 
    args.targetDir += "_small"
    maxEvents=10 # Number of files
    sample.files=sample.files[:1]

#xsec = sample.xsec
#nEvents = sample.nEvents
#lumiweight1fb = xsec * 1000. / nEvents

# output directory
output_directory = os.path.join(postProcessing_output_directory, 'gen', args.targetDir, 'fwlite_signals_fastSim_Stops2l_200k') 
if not os.path.exists( output_directory ): 
    os.makedirs( output_directory )
    logger.info( "Created output directory %s", output_directory )

# Run only job number "args.job" from total of "args.nJobs"
if args.nJobs>1:
    n_files_before = len(sample.files)
    sample = sample.split(args.nJobs)[args.job]
    n_files_after  = len(sample.files)
    logger.info( "Running job %i/%i over %i files from a total of %i.", args.job, args.nJobs, n_files_after, n_files_before)

products = {
'genParticles':{'type':'vector<reco:GenParticle>', 'label': ( "genParticles" ) },
}

def varnames( vec_vars ):
    return [v.split('/')[0] for v in vec_vars.split(',')]

def vecSumPt(*args):
    return sqrt( sum([o['pt']*cos(o['phi']) for o in args],0.)**2 + sum([o['pt']*sin(o['phi']) for o in args],0.)**2 )

def addIndex( collection ):
    for i  in range(len(collection)):
        collection[i]['index'] = i

# standard variables
variables  = ["run/I", "lumi/I", "evt/l"]

# MET
#variables += ["genMet_pt/F", "genMet_phi/F"]

# jet vector
jet_read_vars       =  "pt/F,eta/F,phi/F,isMuon/I,isElectron/I,isPhoton/I"
jet_read_varnames   =  varnames( jet_read_vars )
jet_write_vars      = jet_read_vars+',matchBParton/I' 
jet_write_varnames  =  varnames( jet_write_vars )
#variables += ["genJet[%s]"%jet_write_vars]
#variables += ["genBj0_%s"%var for var in jet_write_vars.split(',')]
#variables += ["genBj1_%s"%var for var in jet_write_vars.split(',')

# lepton vector 
lep_vars       =  "pt/F,eta/F,phi/F,pdgId/I,vtx_x/F,vtx_y/F,rho/F"
lep_extra_vars =  "motherPdgId/I"
lep_varnames   =  varnames( lep_vars ) 
lep_all_varnames = lep_varnames + varnames(lep_extra_vars)
#variables     += ["genLep[%s]"%(','.join([lep_vars, lep_extra_vars]))]
# associated jet indices
#variables += [ "genBjLeadlep_index/I", "genBjLeadhad_index/I" ]
#variables += [ "genBjNonZlep_index/I", "genBjNonZhad_index/I" ]
# stop vector
stop_vars       =  "pt/F,eta/F,phi/F,mass/F"
stop_vert_vars =  "x/F,y/F,rho/F"
stop_varnames   =  varnames( stop_vars ) 
stop_vertnames   =  varnames( stop_vert_vars ) 
variables      +=  ["genStop[%s]"%stop_vars]
variables      +=  ["genStop_ver[%s]"%stop_vert_vars]

# Neutralino vector
neu_vars       =  "pt/F,eta/F,phi/F,mass/F,vtx_x/F,vtx_y/F,rho/F"
neu_varnames   =  varnames( neu_vars ) 
#variables     += ["genNeu[%s]"%neu_vars]


# to be stored for each boson
boson_read_varnames= [ 'pt', 'phi', 'eta', 'mass']
# Z vector from gen collection
#variables     += ["genZ_pt/F", "genZ_phi/F", "genZ_eta/F", "genZ_mass/F", "genZ_cosThetaStar/F", "genZ_daughterPdg/I"]
# W vector from genleps
#variables     += ["genLepW_pt/F", "genLepW_phi/F", "genLepW_eta/F", "genLepW_mass/F", "genLepW_lldPhi/F", "genLepW_lldR/F","genLepW_cosThetaStar/F", "genLepW_daughterPdg/I", "genLepNonW_l1_index/I"]
#variables     += ["genLepW_l1_index/I", "genLepW_l2_index/I", "genLepNonW_l1_index/I", "genLepNonW_l2_index/I"]
## W vector
#variables     += ["genW_pt/F", "genW_phi/F", "genW_eta/F", "genW_mass/F", "genW_daughterPdg/I"]

# Lumi weight 1fb
#variables += ["lumiweight1fb/F"]

def fill_vector_collection( event, collection_name, collection_varnames, objects):
    setattr( event, "n"+collection_name, len(objects) )
    for i_obj, obj in enumerate(objects):
        for var in collection_varnames:
            getattr(event, collection_name+"_"+var)[i_obj] = obj[var]
def fill_vector( event, collection_name, collection_varnames, obj):
    for var in collection_varnames:
        setattr(event, collection_name+"_"+var, obj[var] )
    
reader = sample.fwliteReader( products = products )

def filler( event ):
    event.run, event.lumi, event.evt = reader.evt
    if reader.position % 100==0: logger.info("At event %i/%i", reader.position, reader.nEvents)
    # All gen particles
    gp      = reader.products['genParticles']
    #searching for gen particles
    g = GenSearch(gp)
    v = [p.vertex() for p in gp]    
    genStops = map( lambda t:{var: getattr(t, var)() for var in stop_varnames}, filter( lambda p:abs(p.pdgId())==1000006 and g.isLast(p),  gp) )
    genStops_ver = map( lambda t:{var: getattr(t, var)() for var in stop_vertnames}, [ part.vertex() for part in gp if (abs(part.pdgId())==1000006 and g.isLast(part))] )
    
    genStops.sort( key = lambda p:-p['pt'] )
    fill_vector_collection( event, "genStop", stop_varnames, genStops ) 
    fill_vector_collection( event, "genStop_ver", stop_vertnames, genStops_ver ) 

tmp_dir     = ROOT.gDirectory
#post_fix = '_%i'%args.job if args.nJobs > 1 else ''
output_filename =  os.path.join(output_directory, sample.name + '.root')

print output_filename.replace('.root', '.log'), output_filename.replace('.root', '_rt.log')
#logger.   add_fileHandler( output_filename.replace('.root', '.log'), args.logLevel )
_logger_rt.add_fileHandler( output_filename.replace('.root', '_rt.log'), args.logLevel )

if os.path.exists( output_filename ) and not args.overwrite:
    logger.info( "File %s found. Quit.", output_filename )
    sys.exit(0)

output_file = ROOT.TFile( output_filename, 'recreate')
output_file.cd()
maker = TreeMaker(
    sequence  = [ filler ],
    variables = [ TreeVariable.fromString(x) for x in variables ], # + extra_variables,
    treeName = "Events"
    )

tmp_dir.cd()

counter = 0
reader.start()
maker.start()

while reader.run( ):
    maker.run()
    counter += 1
    if counter == maxEvents:  break

logger.info( "Done with running over %i events.", reader.nEvents )

output_file.cd()
maker.tree.Write()
output_file.Close()

logger.info( "Written output file %s", output_filename )
