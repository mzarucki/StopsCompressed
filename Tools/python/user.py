import os

if os.environ['USER'] in ['mzarucki']:
    cache_directory                     = "/eos/user/m/mzarucki/StopsCompressed/"
    analysis_results                    = "/eos/user/m/mzarucki/StopsCompressed/sensitivity/"
    postProcessing_output_directory     = "/eos/user/m/mzarucki/StopsCompressed/nanoTuples/" 
    plot_directory                      = "/eos/user/m/mzarucki/www/2022/StopsCompressed/"
    private_results_directory           = "/eos/user/m/mzarucki/StopsCompressed/private/"

if os.environ['USER'] in ['phussain']:
    cache_directory                     = "/afs/hephy.at/data/cms10/StopsCompressed/"
    analysis_results                    = "/afs/hephy.at/data/cms10/StopsCompressed/"
    postProcessing_output_directory     = "/afs/hephy.at/data/cms10/StopsCompressed/nanoTuples/"
    plot_directory                      = "/afs/hephy.at/user/p/phussain/www/stopsCompressed/"
    private_results_directory           = "/afs/hephy.at/data/cms02/"
    
if os.environ['USER'] in ['priya.hussain']:
    results_directory                   = "/groups/hephy/cms/priya.hussain/StopsCompressed/"
    analysis_results                    = "/scratch-cbe/users/priya.hussain/StopsCompressed/results/"
    #cache_directory                     = "/mnt/hephy/cms/priya.hussain/StopsCompressed/"
    cache_directory                     = "/scratch-cbe/users/priya.hussain/StopsCompressed/cache/analysis/"
    #postProcessing_output_directory     = "/groups/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/"
    postProcessing_output_directory     = "/scratch-cbe/users/priya.hussain/StopsCompressed/nanoTuples/"
    plot_directory                      = "/groups/hephy/cms/priya.hussain/www/StopsCompressed/"
    private_results_directory           = "/groups/hephy/cms/priya.hussain/"

if os.environ['USER'] in ['dietrich.liko']:
    results_directory                   = "/groups/hephy/cms/dietrich.liko/StopsCompressed/"
    analysis_results                    = "/scratch-cbe/users/dietrich.liko/StopsCompressed/results/"
    #cache_directory                     = "/mnt/hephy/cms/priya.hussain/StopsCompressed/"
    cache_directory                     = "/scratch-cbe/users/dietrich.liko/StopsCompressed/cache/analysis/"
    postProcessing_output_directory     = "/groups/hephy/cms/dietrich.liko/StopsCompressed/nanoTuples/"
    plot_directory                      = "/groups/hephy/cms/dietrich.liko/www/StopsCompressed/"
    private_results_directory           = "/groups/hephy/cms/dietrich.liko/"

if os.environ['USER'] in ['janik.andrejkovic']:
    results_directory                   = "/groups/hephy/cms/janik.andrejkovic/StopsCompressed/"
    analysis_results                    = "/scratch/janik.andrejkovic/StopsCompressed/results/"
    # cache_directory                     = "/scratch/priya.hussain/StopsCompressed/cache/analysis/"#"/mnt/hephy/cms/janik.andrejkovic/StopsCompressed/"
    cache_directory                     = "/scratch/janik.andrejkovic/StopsCompressed/cache/analysis/"#"/mnt/hephy/cms/janik.andrejkovic/StopsCompressed/"
    postProcessing_output_directory     = "/groups/hephy/cms/janik.andrejkovic/StopsCompressed/nanoTuples/"
    plot_directory                      = "/groups/hephy/cms/janik.andrejkovic/www/StopsCompressed/"
    private_results_directory           = "/groups/hephy/cms/janik.andrejkovic/"
if os.environ['USER'] in ['prhussai']:
    results_directory                   = "/afs/cern.ch/work/p/prhussai/private/StopsCompressed"
    postProcessing_output_directory     = "/afs/cern.ch/work/p/prhussai/private/StopsCompressed/nanoTuples/"
    plot_directory                      = "/eos/user/p/prhussai/www/"
    private_results_directory           = "/afs/cern.ch/work/p/prhussai/private/StopsCompressed/results"

if os.environ['USER'] in ['rschoefbeck']:
    results_directory                   = "/afs/hephy.at/data/cms02/StopsCompressed/"
    postProcessing_output_directory     = "/afs/hephy.at/data/cms02/StopsCompressed/nanoTuples/"
    plot_directory                      = "/afs/hephy.at/user/r/rschoefbeck/www/StopsCompressed/"
    private_results_directory           = "/afs/hephy.at/data/cms02/"
