#Display time and data

from datetime import datetime
from zoneinfo import ZoneInfo

def main():
    print("U.S. Time Zone Finder: ")
    print("Enter a valid U.S. time zone abbreviation (e.g., EST, CST, MST, PST, AKST, HST):")
    abbrev = input("Time Zone Abbreviation: ").strip().upper()

    result = get_time(abbrev)
    print(result)

def get_time(abbrev):
    if abbrev not in time_zones:
        return f"Error: '{abbrev}' is not a vaild U.S. time zone abbreviation."
    time_zone = time_zones[abbrev]
    target_timezone = ZoneInfo(time_zone)

    target_time = datetime.now(target_timezone)
    formatted_time = target_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")

    return f"The current time in {abbrev} ({time_zone}) is: {formatted_time}"

time_zones = {
    "EST": "America/New_York",
    "CST": "America/Chicago",
    "MST": "America/Denver",
    "PST": "America/Los_Angeles",
    "AKST": "America/Anchorage",
    "HST": "Pacific/Honolulu"
}

if __name__ == "__main__":
    main()
