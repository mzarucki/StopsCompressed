# Get Estimates
```
Example command:

python run_estimate.py --selectEstimator WJets     --year 2016 --all

This will get the estimates for WJets, which cantake up some time. We need to run over DY, Top, single Top, VV, TTX, QCD and Data to be prepared. To get the estimates for all redions, use --all flag. One region can be selected by --selectRegion 1 . For omitting systematic uncertainties use --noSystematics.
Can take a look at runEstimateOnClip.py for submission.
```

# Run Limits
```
python run_limit.py --fitAll --expected --only=T2tt_450_370

To run over control regions use --control2016. If running over only control regions you can remove --expected which will then take observed results from Data. Using --fitAll will run the fit in both signal and control regions. If you don't want to unblind, use --expected in this case.
```

# Plot Limits
```
Run run_limit.py without --only to get limit on all points. It will produce a root file, in results directory, with 2D histogram in it. There are 2 scripts currently, for producing exclusion plot with mStop and dm vs mNeu.
plot_SMS_limit.py produces mStop vs mNeu plot, and plot_SMS_limit_v2.py plots dm vs mNeu.
```
