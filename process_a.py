import os
from subprocess import Popen, PIPE

import sentry_sdk


sentry_sdk.init(
    dsn="https://d655584d05f14c58b86e9034aab6817f@o447951.ingest.sentry.io/5461230",  # "sentry-python" project on Sentry.io
    debug=True,
    release="0.0.0",
    traces_sample_rate=1.0, 
)


def main():
    hub = sentry_sdk.Hub.current

    # Start main transaction
    with hub.start_transaction(op="process_a", name="process_a"):
        # Set Sentry environment variables
        my_env = os.environ.copy()
        my_env["SENTRY_TRACE"] = sentry_sdk.get_traceparent()
        my_env["SENTRY_BAGGAGE"] = sentry_sdk.get_baggage()
     
        # Start process B with Sentry environment variables set
        process = Popen(
            ['python', 'process_b.py'], 
            stdout=PIPE, 
            stderr=PIPE, 
            env=my_env, 
        )
        stdout, stderr = process.communicate()


if __name__ == "__main__":
    main()