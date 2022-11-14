class default_locations:

    #mc_2016_data_directory = "/mnt/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/"
    #mc_2016_data_directory = "/groups/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/"
    mc_2016_data_directory = "/eos/cms/store/group/phys_susy/hephy/StopsCompressed/nanoTuples/" # EOS
    #mc_2016_data_directory = "/scratch-cbe/users/dietrich.liko/StopsCompressed/nanoTuples/" # latest
    mc_2016_postProcessing_directory = "compstops_UL16v9_nano_v6/Met/" # EOS
    #mc_2016_postProcessing_directory = "compstops_UL16v9_nano_v7/Met/" # latest
    mc_legacy16_postProcessing_directory = "compstops_2016_nano_v28/Met/"

    #data_2016_data_directory = "/groups/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/" # latest
    data_2016_data_directory = "/eos/cms/store/group/phys_susy/hephy/StopsCompressed/nanoTuples/" # EOS
    #data_2016_data_directory = "/scratch-cbe/users/dietrich.liko/StopsCompressed/nanoTuples/"
    data_2016_postProcessing_directory = "compstops_UL16v9_nano_v6/Met/" # EOS
    #data_2016_postProcessing_directory = "compstops_UL16v9_nano_v7/Met/" # latest

    #mc_2016APV_data_directory = "/groups/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/"
    mc_2016APV_data_directory = "/scratch-cbe/users/dietrich.liko/StopsCompressed/nanoTuples/"
    mc_2016APV_postProcessing_directory = "compstops_UL16APVv9_nano_v7/Met/"

    #data_2016APV_data_directory = "/groups/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/"
    data_2016APV_data_directory = "/scratch-cbe/users/dietrich.liko/StopsCompressed/nanoTuples/"
    data_2016APV_postProcessing_directory = "compstops_UL16APVv9_nano_v7/Met/"

    #mc_2016_36fb_data_directory = "/groups/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/"
    #mc_2016_36fb_postProcessing_directory = "compstops_UL16v9_36fb_nano_v2/Met/"

    #data_2016_36fb_data_directory = "/groups/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/"
    #data_2016_36fb_postProcessing_directory = "compstops_UL16v9_36fb_nano_v2/Met/"

    #change it to scratch for newest version of 2016:
    #mc_2016_data_directory = "/scratch/priya.hussain/StopsCompressed/nanoTuples/"
    ##mc_2016_data_directory = "/groups/hephy/cms/janik.andrejkovic/StopsCompressed/nanoTuples/" #post-processed samples on Janik's /mnt
    # mc_2016_postProcessing_directory = "compstops_2016_nano_v25/Met/"
    #mc_2016_postProcessing_directory = "compstops_2016_nano_v26/Met/"

    ##v27 has fixed leptonSFs and ISR reweighting w/o normalization
    #mc_2016_postProcessing_directory = "compstops_2016_nano_v27/MetSingleLep/"
    #signal_2016_postProcessing_directory = "compstops_2016_nano_v27/Met/"

    # for jet pt threshold 20 GeV use v28
    #mc_2016_postProcessing_directory = "compstops_2016_nano_v28/MetSingleLep/"

    # mc_2016_postProcessing_directory = "compstops_2016_nano_v22/MetSingleLep/looseHybridIso/"
    # mc_2016_postProcessing_directory = "compstops_2016_nano_v11/MetSingleLep/fake/" # samples without Hybrid-Iso cut
    # signal_2016_postProcessing_directory = "compstops_2016_nano_v25/MetSingleLep/"#looseHybridIso/"
    #signal_2016_postProcessing_directory = "compstops_2016_nano_v30/Met/"#looseHybridIso/"
    #signal_2016_postProcessing_directory = "compstops_2016_nano_v27/Met/"
    signal_2016_postProcessing_directory = "compstops_UL16v9_nano_v7/Met/"
    ##samples w/ all ext samples && old ID: v21
    #mc_2016_postProcessing_directory = "compstops_2016_nano_v21/MetSingleLep/"
    ## samples w/ ID mu_medium, el_loose: v22
    #mc_2016_postProcessing_directory = "compstops_2016_nano_v22/MetSingleLep/"
    ##samples w/ all ext samples && mu_medium, el_loose && isPrompt (but intermediate leptons) v23
    #mc_2016_postProcessing_directory = "compstops_2016_nano_v23/MetSingleLep/"
    ##samples w/ all ext samples && mu_medium, el_loose && isPrompt (all final state lep) v24
    #mc_2016_postProcessing_directory = "compstops_2016_nano_v24/MetSingleLep/"
    ## samples isPrompt w genPartFlav match
    #mc_2016_postProcessing_directory = "compstops_2016_nano_v25/MetSingleLep/"

    #signal w/ ID mu_medium, el_loose: v24
    #signal_2016_postProcessing_directory = "compstops_2016_nano_v23/MetSingleLep/"
    #signal_2016_postProcessing_directory = "compstops_2016_nano_v27/MetSingleLep/"
    #signal_2016_postProcessing_directory = "compstops_2016_nano_v24/MetSingleLep/"

    
    # data_2016_data_directory = "/groups/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/"
    #data_2016_data_directory = "/scratch/priya.hussain/StopsCompressed/nanoTuples/"

    ##v27 has fixed leptonSFs and ISR reweighting w/o normalization
    #data_2016_postProcessing_directory = "compstops_2016_nano_v27/MetSingleLep/"

    ##for jets with pt-threshold 20 GeV we use v28
    #data_2016_postProcessing_directory = "compstops_2016_nano_v28/MetSingleLep/"
    
    
    # data_2016_postProcessing_directory = "compstops_2016_nano_v22/MetSingleLep/looseHybridIso/"
    # data_2016_postProcessing_directory = "compstops_2016_nano_v23/MetSingleLep/"
    #data_2016_postProcessing_directory = "compstops_2016_nano_v26/MetSingleLep/"
    #data_2016_postProcessing_directory = "compstops_2016_nano_v15/MetSingleLep/"
    #data_2016_postProcessing_directory = "compstops_2016_nano_v8/MetSingleLep/"
    ## data w/ all ext samples && old ID: v21
    #data_2016_postProcessing_directory = "compstops_2016_nano_v21/MetSingleLep/"
    ## data sample w/ ID mu_medium, el_loose: v22
    #data_2016_postProcessing_directory = "compstops_2016_nano_v22/MetSingleLep/"
    ## data sample w/ ID mu_medium, el_loose && isPrompt (data has no gen info, same with isPrompt flag): v23
    #data_2016_postProcessing_directory = "compstops_2016_nano_v23/MetSingleLep/"


    #mc_2017_data_directory = "/mnt/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/"
    #mc_2017_postProcessing_directory = "compstops_2017_nano_v8/MetSingleLep/"
    #data_2017_data_directory = "/mnt/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/"
    #data_2017_postProcessing_directory = "compstops_2017_nano_v8/MetSingleLep/"


    #mc_2017_data_directory = "/groups/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/"
    mc_2017_data_directory = "/scratch-cbe/users/dietrich.liko/StopsCompressed/nanoTuples/"
    mc_2017_postProcessing_directory = "compstops_UL17v9_nano_v7/Met"

    #data_2017_data_directory = "/groups/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/"
    data_2017_data_directory = "/scratch-cbe/users/dietrich.liko/StopsCompressed/nanoTuples/"
    data_2017_postProcessing_directory = "compstops_UL17v9_nano_v7/Met"

    mc_2018_data_directory = "/eos/user/m/mzarucki/StopsCompressed/nanoTuples/" # EOS
    signal_2018_postProcessing_directory = "stops_2018_nano_v1/Met/"
    #mc_2018_data_directory = "/eos/cms/store/group/phys_susy/hephy/StopsCompressed/nanoTuples/" # EOS
    #mc_2018_data_directory = "/scratch-cbe/users/dietrich.liko/StopsCompressed/nanoTuples/" # latest
    mc_2018_postProcessing_directory = "stops_2018_nano_v1/Met/" # private
    #mc_2018_postProcessing_directory = "compstops_UL18v9_nano_v7/Met/" # latest

    data_2018_data_directory = "/eos/user/m/mzarucki/StopsCompressed/nanoTuples/" # private
    #data_2018_data_directory = "/eos/cms/store/group/phys_susy/hephy/StopsCompressed/nanoTuples/" # EOS
    #data_2018_data_directory = "/scratch-cbe/users/dietrich.liko/StopsCompressed/nanoTuples/" # latest
    data_2018_postProcessing_directory = "stops_2018_nano_v1/Met/" # private
    #data_2018_postProcessing_directory = "compstops_UL18v9_nano_v7/Met/" # latest
