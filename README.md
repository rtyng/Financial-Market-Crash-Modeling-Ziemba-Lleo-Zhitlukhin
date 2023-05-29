# Financial-Market-Crash-Modeling-Ziemba-Lleo-Zhitlukhin

# BSEYD Model comes from "Stock Market Crashes Predictable and Unpredictable and What to do about them" by William T. Ziemba, Sebastian Lleo, and Mikhail Zhitlukin

Built and maintained by Randolph Tyng

# The purpose of this data science based project is to gain a better understanding of the process of building a data pipeline

Pipeline:

# grab data, verify reliability, etc. ->
    inspect, analyze, clean, potentially morph into different shape, etc. ->
        descriptive statistics, graphing, etc. ->
            build models, verify them, tune, make sure you understand theoretical and application contexts ->
                test models on various datasets to help with previous step ->
                    let data flow through the models ->
                        analyze results, prepare findings for others

7 step process for data related problems

The area of focus here is modeling financial crashes


# What is the bond-stock earnings yield differential and what is a crash signal?

The model came from the idea that investor dollars are always in competition between being sent into bonds or stocks depending on the interest rate. When rates are low, investor
dollars tend to flow into stocks and the reverse (higher rates, dollars flow towards bonds) is also true. 

So the model is really just based off the distance between r and rho, where r is the yield on a government bond (10 year rate in our case) and rho is the earnings yield (just the 
reverse of the P/E ratio).

What about the crash signal?

The crash signal is defined as S(t) = M(t) - K(t) > 0

# M(t) == Crash prediction measure
# S(t) == Crash signal
# K(t) == Time varying threshold for the signal

These crash prediction models generate a signal over a given time horizon H that indicates a downturn in the equity market.

The purpose of this repository will be to process the Shiller dataset for analysis, build the BSEYD model using the variables from Shiller's data, then visualize and interpret the results. More information on the datasets can be found within the 3 txt files I will try to make them more organized as more work is put in.

In order to be more organized, each part of the pipeline will be in seperate scripts and then merged into one script for a compact analysis script.
