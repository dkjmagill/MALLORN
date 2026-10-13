
import numpy as np

def inverse_variance_weighting(values, sigma):

    values = np.array(values)
    variances = np.array(sigma**2)
    weights = 1 / variances
    weighted_average = np.sum(weights * values) / np.sum(weights)
    weighted_variance = 1 / np.sum(weights)

    return weighted_average, np.sqrt(weighted_variance)
 


def baseline_correction_4filter(flux, flux_unc, time,  goback = 100, threshold_obs = 30, unit = 'uJy', peak_time = 0, prop_errors = True, chi_square_correction = True):

    '''
    Function to correct the baseline of a light curve by subtracting the average flux
    of the observations before a specified time (peak_time - goback).


    Parameters:
    flux : array-like
        The flux values of the light curve.
    flux_unc : array-like       
        The uncertainties in the flux values.
    time : array-like
        The time values corresponding to the flux observations.
    goback : float, optional
        The time in days to go back from the peak_time to calculate the baseline (default is 100 days).
    threshold_obs : int, optional
        The minimum number of observations required to perform the baseline correction (default is 30).
    unit : str, optional
        The unit of the flux values (default is 'uJy').
    peak_time : float, optional
        The time at which the peak flux is observed (default is 0).
    prop_errors : bool, optional
        Whether to propagate the baseline correction uncertainty in the flux values (default is True).
    chi_square_correction : bool, optional
        Whether to apply chi-square correction to the uncertainties (default is True).

        

    Returns:
    baseline_crctd_flux : array-like
        The baseline corrected flux values.
    baseline_crctd_flux_unc : array-like
        The uncertainties in the baseline corrected flux values.
    crctn_data : dict
        A dictionary containing additional information about the correction, such as the offset used and the number of
        observations used for the correction.
    flag : bool
    '''
    flag = False
    crctn_data = {}
    #print(peak_time - goback)
    len_gobackd = sum(time<(peak_time - goback))
    #print(time<(peak_time - goback))
    #print('lengoback ', len_gobackd)
    
    #print('test')

    if len_gobackd>threshold_obs:
        flux_base = flux[time<(peak_time - goback)]
        flux_unc_base = flux_unc[time<(peak_time - goback)]
        avg, avg_unc = inverse_variance_weighting(flux_base, flux_unc_base)
        #print(avg)
        
        baseline_crctd_flux = flux - avg

        if prop_errors:
            baseline_crctd_flux_unc = np.sqrt(flux_unc**2 + avg_unc**2)
        else:
            baseline_crctd_flux_unc = flux_unc

        if chi_square_correction:  # setting pre_peak chi_square to 1
            chi_square_pre_peak = np.sum((baseline_crctd_flux[time<(peak_time - goback)] - avg)**2 / baseline_crctd_flux_unc[time<(peak_time - goback)]**2) * 1/(len(flux_base)-1)
            baseline_crctd_flux_unc = baseline_crctd_flux_unc * np.sqrt(chi_square_pre_peak)


        crctn_data['errors_propagated'] = prop_errors
        crctn_data['offset'] = avg
        crctn_data['used_points'] = len_gobackd
        flag = True
        return baseline_crctd_flux, baseline_crctd_flux_unc, crctn_data, flag
    else:
        crctn_data['used_points'] = len_gobackd
        return flux, flux_unc, crctn_data, flag