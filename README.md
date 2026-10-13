# MALLORN: Many Artificial LSST Light curves based on Observations of Real Nuclear transients

This GitHub contains the full MALLORN data set. If used, please cite [Magill et al. 2026](https://ui.adsabs.harvard.edu/abs/2026RASTI...5ag019M/abstract).

MALLORN comprises 10 178 simulated LSST light curves, constructed from real Zwicky Transient Facility (ZTF) observations of 64 tidal disruption events (TDEs), 727 nuclear supernovae and 1407 active galactic nuclei (AGN) with spectroscopic labels using Gaussian process fitting, empirically motivated spectral energy distributions from SNCosmo and the baseline from the Rubin Survey Simulator. Our novel approach can be easily adapted to simulate transients for any photometric survey using observations from another, requiring only the limiting magnitudes and an estimate of the cadence of observations.

The [MALLORN Astronomical Classification Challenge](https://www.kaggle.com/competitions/mallorn-astronomical-classification-challenge/overview), focusing on photometrically identifying TDEs within the MALLORN data, ran from 15/10/25 to 31/01/26, attracting ~13000 submissions from ~1000 participants.

Google Colab notebooks are available describing [how to use the data](https://colab.research.google.com/drive/1N7Q1bxc2gxBuOv2eD3fTYsrxoLC2dQAP#scrollTo=06314127) and the [methods used to create the data](https://colab.research.google.com/drive/1oy96r29Zs4U5Hl-THsZPCnOQbuz21hl5#scrollTo=667c20d2).

## File Description:

*MALLORN_lightcurves (1-10).zip* : A compressed folder containing the light curves for objects within splits 1-10. Each split folder contains a 'test_full_lightcurves.csv' file and a 'train_full_lightcurves.csv' file.

*[train/test]_full_lightcurves.csv* : Time series observations of objects in each respective filter. Multiple objects are saved to the one csv file, and can be extracted using the object_id. Contains the full light curves for the objects.

*[train/test]_log.csv* : Additional information about the objects such as the extinction and redshift of the objects. This also includes the SpecType (true classification of the object) and target (binary variable for TDE and non-TDE). The split column in the log files can be used to identify the respective split folder for a given object_id.

*public_test_log.csv* : A version of the 'test_log.csv' with all of the spectroscopic labels made publicly available.

## Log File Column Descriptions:

*object_id* : A combination of 3 Sindarin (Elvish) words which provides a unique identifier for each object.

*Z* : The redshift of the object. For the training data these are spectroscopic redshift values, which have negligible error. For the testing set these are simulated photometric redshift values which do have a corresponding error.

*Z_err* : The error in the redshift. This value is left blank for the training data for the reasons described above.

*EBV* : The extinction coefficient (E(B-V)) value. This provides a measure for the amount the light of the source has been obscured by dust on its path to reach us. This value can be used to de-extinct the flux measurements through a method shown in the ‘Using_the_Data’ notebook.

*SpecType* : The spectroscopically defined type of the object. This value is given in the training data to allow for effective training of classifiers. However, it is left blank for the testing data.

*English Translation* : An English translation of the Object_ID. Unimportant for the classifier challenge but a fun inclusion.

*split* : The name of the split folder that contains the the full lightcurve file for a given object.

*target* (only for training set): The target variable for TDE classification (derived from SpecType). The value is 1 if the source is a TDE and 0 if anything else.

## Data File Column Descriptions: 

*object_id* : Same as described above.

*Time (MJD)* : The date of the observation. In units of MJD (Modified Julian Date) which are commonly used in astronomy. The number indicates the number of days since 17/11/1858.

*Flux* : The measured amount of light from the observation. Given in units of microjansky (μJy). These values are unextincted and need to be corrected for that using the ‘EBV’ value for the corresponding object from the relevant log file.

*Flux_err* : The uncertainty in the flux measurement described above.

*Filter* : The observation filter used for that respective observation. LSST will use six different filters: u, g, r, i, z & y. The filter corresponds to a particular wavelength range. The time series data for each filter should be regarded separately as they can behave differently for a given type of object.
