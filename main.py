import requests
import os
import csv

def download_photo(ic, folder="photos"):
    os.makedirs(folder, exist_ok=True)

    url = f"https://academic.utm.my/UGStudent/PhotoStudent.ashx?nokp={ic}"
    res = requests.get(url)

    if res.status_code == 200 and len(res.content) > 100:

        filepath = os.path.join(folder, f"{ic}.jpg")
        with open(filepath, "wb") as f:
            f.write(res.content)
        print(f"OK Downloaded {ic}.jpg")
        return filepath
    else:
        print(f"X Not found: {ic}")
        return None

def batch_download(prefix, start, end, output_folder="photos", csv_file="results.csv"):

    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["IC", "Status", "Filepath"])

        for num in range(start, end + 1):
            ic = f"{prefix}{num}" 
            filepath = download_photo(ic, output_folder)

            if filepath:
                writer.writerow([ic, "Downloaded", filepath])
            else:
                writer.writerow([ic, "Not Found", ""])

            ###  stop if too many failing in a raw
            if not filepath and num > start + 200:
                print("Too many missing ICs, stopping batch.")
                break

if __name__ == "__main__":

    prefix = "202403M"   # here so can be adjusted for the batch
    start = 10001        # to the start point
    end = 10500  

    batch_download(prefix, start, end)