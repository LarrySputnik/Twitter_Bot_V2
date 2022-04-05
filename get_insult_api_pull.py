import requests
import time
import json

# Request trump insults from api
r = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes")
r.raise_for_status()
# Turn request into a json package
packages_json = r.json()

# List of just the insults
insults = packages_json["messages"]["personalized"]

# Hold all the insults
results = []
# Start timer for entire download
t1 = time.perf_counter()

# Pull quotes from the api and store in results list
for quote in insults:
    results.append(quote)
    # sleep however long it takes to download each item, don't overload server.
    time.sleep(r.elapsed.total_seconds())
    # print out the progress during the download
    print(f"Got {quote} in {r.elapsed.total_seconds()} seconds")

# End timer for total download
t2 = time.perf_counter()
# Print out the total time it took to download all the files in seconds.
print(f"Finished in {t2 - t1} seconds.")

# Write the results list to a json file and save for later use.
with open("insult_info.json", "w") as f:
    json.dump(results, f, indent=2)

