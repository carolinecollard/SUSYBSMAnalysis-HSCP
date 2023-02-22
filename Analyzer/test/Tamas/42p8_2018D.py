
from CRABClient.UserUtilities import config
config = config()

config.section_('General')
config.General.requestName = 'Analysis_MET_Run2018D_CodeV42p8_v1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'HSCParticleProducerAnalyzer_master_cfg.py'
config.JobType.allowUndistributedCMSSW = True
#config.JobType.maxJobRuntimeMin = 3000
config.JobType.maxMemoryMB = 4000
config.JobType.inputFiles = ['SUSYBSMAnalysis/HSCP/data/CorrFact2018PixL1.txt','SUSYBSMAnalysis/HSCP/data/CorrFact2018PixL2.txt','SUSYBSMAnalysis/HSCP/data/CorrFact2018PixL3.txt','SUSYBSMAnalysis/HSCP/data/CorrFact2018PixL4.txt','SUSYBSMAnalysis/HSCP/data/CorrFact2018PixR1.txt','SUSYBSMAnalysis/HSCP/data/CorrFact2018PixR2.txt','SUSYBSMAnalysis/HSCP/data/template_2018D_v2.root','MuonTimeOffset.txt']
config.JobType.pyCfgParams = ['GTAG=106X_dataRun2_v36', 'SAMPLE=isData', 'YEAR=2018', 'ERA=D']

config.section_('Data')
config.Data.inputDataset = '/MET/Run2018D-15Feb2022_UL2018-v1/AOD'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 50
config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
#MASZK2017config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt'
config.Data.outputDatasetTag = config.General.requestName
config.Data.outLFNDirBase = '/store/user/tvami/HSCP'
config.Data.ignoreLocality = True
config.Data.partialDataset = True
config.Data.publication = False

config.section_('Site')
config.Site.whitelist = ['T2_DE_DESY','T2_CH_CERN','T2_IT_Bari','T1_IT_*','T2_US_*', 'T3_US_FNALLPC','T2_HU_Budapest','T2_FR_*', 'T2_UK_London_IC']
config.Site.storageSite = 'T2_HU_Budapest'
#config.Site.storageSite = 'T3_US_FNALLPC'
  