import numpy as np

def refine(raw_results):

    # For each address
    for address in raw_results:
        address_results = raw_results[address]
        old_times = address_results["abs_times"]

        # convert unix time to relevant time frame, starts 0 with first ping
        smallest_time = np.min(old_times)
        unscaled_times = np.subtract(old_times, smallest_time)

        # scale up to minutes instead of milliseconds
        scaled_times = np.divide(unscaled_times, 60 * 1000)

        address_results.update({ "abs_times": scaled_times })

    return raw_results