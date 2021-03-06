from pathlib import Path

import pandas as pd
import pandas_profiling

if __name__ == "__main__":
    df = pd.read_csv(
        "https://raw.githubusercontent.com/berkmancenter/url-lists/master/lists/et.csv",
        parse_dates=["date_added"],
    )
    profile = df.profile_report(title="Website Inaccessibility Test Lists")
    profile.to_file(output_file=Path("./website_inaccessibility_report.html"))
