import os

if os.environ['USER'] in ['phussain']:
    results_directory                   = "/afs/hephy.at/data/cms07/StopsCompressed/"
    postProcessing_output_directory     = "/afs/hephy.at/data/cms07/StopsCompressed/nanoTuples/"
    plot_directory                      = "/afs/hephy.at/user/p/phussain/www/StopsCompressed/"
    private_results_directory           = "/afs/hephy.at/data/cms07/"
if os.environ['USER'] in ['rschoefbeck']:
    results_directory                   = "/afs/hephy.at/data/cms07/StopsCompressed/"
    postProcessing_output_directory     = "/afs/hephy.at/data/cms07/StopsCompressed/nanoTuples/"
    plot_directory                      = "/afs/hephy.at/user/r/rschoefbeck/www/StopsCompressed/"
    private_results_directory           = "/afs/hephy.at/data/cms07/"
