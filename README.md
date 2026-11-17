# Jupyter Notebooks (and other scripts) used with MicroSim simulations

- absEffectSize: finds the absolute effect size of treatment for each dementia and cardiovascular quantile-quantile
                 using a large usual care population and a large sprint treatment population
- absEffectSizeRegression: does the regression for the absEffectSize notebook
- cognitiveImpairmentOutcomes: demonstrates the implementation of a cognitive impairment outcome in trials
- convergenceOfTrialsetResults: checks for convergence of trialset effect size as a function of number of trials (so that we know when to stop)
- cvDementiaQuantiles: calculates quantiles of cardiovascular and dementia risks in a large usual care population
- initialization-models-XX: develop and validate person object models (eg waist for Kaiser person objects)
- parallelTrialset: demonstrates the use of TrialsetSerial and TrialsetParallel classes
- pyproject.toml (and poetry.lock): used to setup poetry with MicroSim Jupyter notebooks, this poetry installation
				    includes additional python modules (compared to MicroSim) that help
				    with visualization, statistical calculations etc
- preliminaryTrials100CvAllDementiaAll: primarily looks at convergence of effect size as a function of number of trials
- standardDeviationGCP: finds the standard deviation of GCP in a large population
- testGcpStrokeModel: using model development results from the original publication, this notebook validates the implementation
                                    of the GCP stroke model on microsim
- validation: aims to reproduce results shown in primary MicroSim publication  
- DataframeVsObjects and DataframeVsObjectsDefinitions: includes relative performance tests for the use of the alive dataframe or 
                               the collection of person objects (population). Some definitions need to be stored to a separate python file
                               (the use of the multiprocessing module in the jupyter notebook requires this).
- population-distributions-XX-NHANES: a series of notebooks to model NHANES data as Gaussians and validate a population obtained from the Gaussians

# Making a Jupyter Notebook Microsim Kernel

The pyproject.toml file in this repository includes packages that are useful for analyzing Microsim simulations in an interactive way using 
Jupyter Notebooks.
Some of the notebooks included in this repository require data in order to run.

- Clone this github repository in the hard drive
- poetry install
- poetry run python -m ipykernel install --user --name microsimKernel
- Change the kernel on the Jupyter Notebook to microsimKernel

