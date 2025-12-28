
https://www.science.org/content/blog-post/when-c-clogp-stands-crazy-update-fixed
# When C LogP Stands For "Crazy" (November 2013)

## 1. SUMMARY

This 2013 blog post from Science magazine reported a concerning software bug in ChemDraw's cLogP calculation function, commonly used by chemists to predict lipophilicity (a critical drug property). The article revealed that drawing molecules with explicit hydrogens caused the cLogP calculator to produce "crazy" and unrealistic values, indicating a significant software malfunction. The piece identified BioByte as the source of the cLogP algorithm integrated into ChemDraw and noted that while such glitches occurred in various chemical software, this particular bug should have been resolved given the tool's widespread use in drug discovery. The post included an update indicating that PerkinElmer (ChemDraw's owner) had quickly released a patch to fix the issue, while questioning how many users were still running outdated versions with the bug intact.

## 2. HISTORY

Subsequent to this 2013 report, ChemDraw and its integrated property calculation tools have undergone continuous development. CambridgeSoft, the original developer, was acquired by PerkinElmer in 2011, and the software has seen multiple major version releases (currently ChemDraw version 21+ as of 2023-2024), with each iteration improving computational chemistry algorithms and fixing reported bugs. The specific explicit hydrogen cLogP bug was indeed patched as reported in the update, though the broader challenge of accurate logP prediction remains an active area of computational chemistry research. ChemDraw remains widely used in pharmaceutical industry and academic laboratories for molecular drawing and basic property calculations, though more sophisticated ADMET (absorption, distribution, metabolism, excretion, toxicity) prediction platforms and machine learning models have become increasingly important for drug discovery workflows over the past decade. The incident highlighted ongoing software quality challenges in scientific computing tools, where bugs can impact research decisions without immediate detection.

## 3. PREDICTIONS

- *Implicit prediction that bug fixes wouldn't reach all users*: The concern about researchers continuing to use outdated versions with the bug proved valid. Software update adoption in scientific computing often lags, and such glitches can persist in archived analyses and legacy workflows.
- *Implicit expectation that logP calculation reliability would improve*: While ChemDraw's specific bug was fixed, accurate logP prediction remains challenging even with updated software, as no single algorithm performs well across all chemical space. Modern workflows often use consensus from multiple prediction methods.
- *Suggestion that software glitches "should have been fixed by now"*: This expectation underestimated the persistent complexity of handling diverse chemical representations in automated calculators. Chemical drawing software continues to have edge cases, though systematic quality assurance has improved.

## 4. INTEREST

**Rating: 4/9**

This article addresses a practical, real-world computational chemistry bug that affected many researchers, making it moderately interesting for its technical utility and its exposure of software quality issues. However, it ranks in the mid-range because it concerns a specific software defect rather than fundamental scientific discovery or broader biotechnology industry developments, with limited long-term significance beyond software development improvements.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20131118-when-c-clogp-stands-crazy-update-fixed.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_