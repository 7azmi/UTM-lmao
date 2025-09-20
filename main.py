import requests
import os
import time  # optional, for delay

year = "2023"
section = "M"
start_month = 1
end_month = 12
start_number = 10001
end_number = 11000

# Create main year folder
os.makedirs(year, exist_ok=True)

for month in range(start_month, end_month + 1):
    month_str = f"{month:02d}"
    folder_name = os.path.join(year, f"{month_str}")  # 2023/202301
    os.makedirs(folder_name, exist_ok=True)

    consecutive_failures = 0  # reset at the start of each month
    print(f"\nStarting downloads for {folder_name}...")

    for num in range(start_number, end_number + 1):
        nokp = f"{year}{month_str}{section}{num}"
        url = f"https://academic.utm.my/UGStudent/PhotoStudent.ashx?nokp={nokp}"
        response = requests.get(url)

        if response.status_code == 200 and len(response.content) > 100:
            consecutive_failures = 0  # reset on success
            file_path = os.path.join(folder_name, f"{nokp}.jpg")
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f" Downloaded {file_path}")
        else:
            consecutive_failures += 1
            print(f"Failed {nokp} ({consecutive_failures} fails in a row)")

            if consecutive_failures > 4:
                print(f"More than 4 consecutive failures — skipping rest of {folder_name} and moving to next month.")
                break  # skip remaining numbers for this month

