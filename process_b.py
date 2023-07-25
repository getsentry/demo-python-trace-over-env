import os
import requests

import sentry_sdk
from sentry_sdk.api import continue_trace

sentry_sdk.init(
    dsn="https://d655584d05f14c58b86e9034aab6817f@o447951.ingest.sentry.io/5461230",  # "sentry-python" project on Sentry.io
    debug=True,
    release="0.0.0",
    traces_sample_rate=1.0, 
)


def main():
    # Read sentry environment variables
    environment = {
        "sentry-trace": os.environ.get("SENTRY_TRACE"), 
        "baggage": os.environ.get("SENTRY_BAGGAGE"), 
    }

    # Create and start transaction that is attached 
    # to the trace from the environment variables set in Process A
    transaction = continue_trace(
        environment,
        op="process_b",
        name="process_b",
    )
    with sentry_sdk.Hub.current.start_transaction(transaction):
        # Do some work
        r = requests.get("https://httpbun.org/")
        print(r.status_code)


if __name__ == "__main__":
    main()
