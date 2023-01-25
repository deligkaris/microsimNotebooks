# Jupyter Notebooks (and other scripts) used with MicroSim simulations

- absEffectSize: finds the absolute effect size of treatment for each dementia and cardiovascular quantile-quantile
                 using a large usual care population and a large sprint treatment population
- absEffectSizeRegression: does the regression for the absEffectSize notebook
- cognitiveImpairmentOutcomes: demonstrates the implementation of a cognitive impairment outcome in trials
- cvDementiaQuantiles: calculates quantiles of cardiovascular and dementia risks in a large usual care population
- parallelTrialset: demonstrates the use of TrialsetSerial and TrialsetParallel classes
- pyproject.toml (and poetry.lock): used to setup poetry with MicroSim Jupyter notebooks, this poetry installation
				    includes additional python modules (compared to MicroSim) that help
				    with visualization, statistical calculations etc
- preliminaryTrials100CvAllDementiaAll: primarily looks at convergence of effect size as a function of number of trials
- standardDeviationGCP: finds the standard deviation of GCP in a large population
- validation: aims to reproduce results shown in primary MicroSim publication  
