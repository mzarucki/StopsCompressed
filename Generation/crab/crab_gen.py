from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.workArea    = "Stops2l"
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../cfg/cmssw_10_2_12_patch1_fastSim.py'
config.JobType.disableAutomaticOutputCollection = False
config.JobType.maxMemoryMB = 4000

config.section_("Data")
config.Data.splitting = 'EventBased'

config.Data.unitsPerJob = 5000
config.Data.totalUnits  = 1000000 
config.Data.publication = True
config.Data.publishDBS = 'phys03'

#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
config.section_("User")

if __name__ == '__main__':

    import os
    from CRABAPI.RawCommand import crabCommand

    for mstop, dm, ctau in [ 
        (250, 20, 0.001), (250, 20, 0.01), (250, 20, 0.1), (250, 20, 0.2), (250, 20, 200),
        (500, 20, 0.001), (500, 20, 0.01), (500, 20, 0.1), (500, 20, 0.2), (500, 20, 200),
         ]:
        config.Data.outputDatasetTag = "Stops2l"
        #config.JobType.inputFiles = [os.path.join(gridpack_dir, gridpack)]
        config.General.requestName = "DisplacedStops-mstop-%i-dm-%i-ctau-%s"%( mstop, dm, str(ctau).replace('.','p') )
        config.Data.outputPrimaryDataset = config.General.requestName # dataset name
        config.JobType.pyCfgParams = ['mstop=%f'%mstop, 'dm=%f'%dm, 'ctau=%f'%ctau]
        #print config.Data.outputPrimaryDataset, config.JobType.pyCfgParams
        crabCommand('submit', '--dryrun', config = config)
        #crabCommand('submit', config = config)
    #crabCommand('submit', config = config)
