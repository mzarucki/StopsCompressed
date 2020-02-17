import os

if os.environ['USER'] in ['phussain']:
    results_directory                   = "/afs/hephy.at/data/cms02/StopsCompressed/"
    postProcessing_output_directory     = "/afs/hephy.at/data/cms02/StopsCompressed/nanoTuples/"
    plot_directory                      = "/afs/hephy.at/user/p/phussain/www/stopsCompressed/"
    private_results_directory           = "/afs/hephy.at/data/cms02/"
    
if os.environ['USER'] in ['priya.hussain']:
    results_directory                   = "/mnt/hephy/cms/priya.hussain/StopsCompressed/"
    postProcessing_output_directory     = "/mnt/hephy/cms/priya.hussain/StopsCompressed/nanoTuples/"
    plot_directory                      = "/users/priya.hussain/www/StopsCompressed/"
    private_results_directory           = "/mnt/hephy/cms/priya.hussain/"

if os.environ['USER'] in ['rschoefbeck']:
    results_directory                   = "/afs/hephy.at/data/cms02/StopsCompressed/"
    postProcessing_output_directory     = "/afs/hephy.at/data/cms02/StopsCompressed/nanoTuples/"
    plot_directory                      = "/afs/hephy.at/user/r/rschoefbeck/www/StopsCompressed/"
    private_results_directory           = "/afs/hephy.at/data/cms02/"
