import os
import time
import requests

# --- 1. CONFIGURATION ---
# All your settings are now in one place for easy changes.
CONFIG = {
    "year": "2022",
    "section": "M",
    "month": 10,
    "start_id": 10001,
    "end_id": 11000,
    "max_failures_in_a_row": 50,
    # This is the URL pattern. The {nokp} part will be replaced.
    "url_pattern": "https://academic.utm.my/UGStudent/PhotoStudent.ashx?nokp={nokp}"
}

def download_image(url, file_path):
    """Attempts to download an image from a URL and saves it."""
    try:
        response = requests.get(url, timeout=10) # Added a timeout for safety
        # Check if the download was successful and the file has content
        if response.status_code == 200 and len(response.content) > 100:
            with open(file_path, "wb") as f:
                f.write(response.content)
            return True
    except requests.exceptions.RequestException as e:
        print(f"  -> Request error: {e}")
    return False

def run_downloader():
    """Main function to run the download process based on CONFIG."""
    # --- 2. SETUP FOLDERS ---
    year_folder = CONFIG["year"]
    month_str = f"{CONFIG['month']:02d}"
    output_folder = os.path.join(year_folder, month_str)
    os.makedirs(output_folder, exist_ok=True)
    
    print(f"Starting downloads for {output_folder}...")
    
    consecutive_failures = 0
    
    # --- 3. MAIN LOOP ---
    for num in range(CONFIG["start_id"], CONFIG["end_id"] + 1):
        # Construct the student ID and the full URL
        nokp = f"{CONFIG['year']}{month_str}{CONFIG['section']}{num}"
        url = CONFIG["url_pattern"].format(nokp=nokp)
        file_path = os.path.join(output_folder, f"{nokp}.jpg")
        
        if download_image(url, file_path):
            print(f"✅ Downloaded {file_path}")
            consecutive_failures = 0 # Reset counter on success
        else:
            consecutive_failures += 1
            print(f"❌ Failed for {nokp} ({consecutive_failures} of {CONFIG['max_failures_in_a_row']})")
        
        # Check if we should stop
        if consecutive_failures >= CONFIG['max_failures_in_a_row']:
            print(f"\nStopping due to {CONFIG['max_failures_in_a_row']} consecutive failures.")
            break
            
        time.sleep(0.1) # A small delay to be polite to the server

# This makes sure the script runs when you execute the file directly
if __name__ == "__main__":
    run_downloader()
