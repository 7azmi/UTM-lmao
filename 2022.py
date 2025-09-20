import requests
import os


def download_photos(year, month):
    start_index = 10000
    end_index = 11000
    error_count = 0
    max_errors = 15

    print(f"--- Starting Download for {year}-{month} ---")

    directory = os.path.join(str(year), f"{month:02d}")
    if not os.path.exists(directory):
        os.makedirs(directory)

    print(f"\n>> Checking month: {month}")

    for i in range(start_index, end_index + 1):
        nokp = f"{year}{month:02d}M{i:05d}"
        url = f"https://academic.utm.my/UGStudent/PhotoStudent.ashx?nokp={nokp}"
        response = requests.get(url)

        if response.status_code == 200 and response.content:
            if len(response.content) > 100:  # Check if the content is likely to be a valid image
                # Save the image
                with open(os.path.join(directory, f"{nokp}.jpg"), "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {nokp}.jpg")
                error_count = 0  # Reset error count after a successful download
            else:
                print(f"Skipping {nokp}.jpg, file appears to be empty or invalid.")
        else:
            error_count += 1
            print(f"Failed to download {nokp}.jpg, error count: {error_count}")
            if error_count >= max_errors:
                print("Maximum error count reached, stopping...")
                break

    print(f"\n--- Download process for {year}-{month} complete. ---")

for i in range(1,13):
    download_photos(2022,i)
