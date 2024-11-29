import os  # Mengimpor modul os (tidak digunakan dalam kode ini, dapat dihapus jika tidak diperlukan)

# Simulasi cloud storage sebagai dictionary
cloud_storage = {}  # Menggunakan dictionary Python untuk menyimpan file secara virtual

# Fungsi untuk mengunggah file ke "cloud"
def upload_file(file_name, content):
    # Memeriksa apakah file dengan nama yang sama sudah ada di cloud_storage
    if file_name in cloud_storage:
        return f"File '{file_name}' already exists in cloud."  # Mengembalikan pesan jika file sudah ada
    cloud_storage[file_name] = content  # Menyimpan file ke cloud_storage dengan nama file sebagai key
    return f"File '{file_name}' uploaded successfully."  # Mengembalikan pesan keberhasilan

# Fungsi untuk memeriksa keberadaan file di "cloud"
def check_file_exists(file_name):
    return file_name in cloud_storage  # Mengembalikan True jika file ada, False jika tidak

# Fungsi untuk mengunduh file dari "cloud"
def download_file(file_name):
    # Memeriksa apakah file ada di cloud_storage
    if file_name not in cloud_storage:
        return None, f"File '{file_name}' not found in cloud."  # Jika tidak ada, kembalikan None dan pesan kesalahan
    return cloud_storage[file_name], f"File '{file_name}' downloaded successfully."  # Jika ada, kembalikan konten file dan pesan keberhasilan

# --- UAT Test Cases ---
def run_uat_tests():
    print("Starting UAT for Cloud-Based File Storage...\n")  # Menampilkan pesan awal pengujian

    # Test Case 1: Upload a file
    file_name = "test_file.txt"  # Nama file yang akan diunggah
    content = "This is a test file for UAT."  # Konten file yang akan diunggah
    result = upload_file(file_name, content)  # Mengunggah file menggunakan fungsi upload_file
    print(f"Test Case 1: {result}")  # Menampilkan hasil pengujian

    # Test Case 2: Check if the file exists
    file_exists = check_file_exists(file_name)  # Memeriksa apakah file ada di cloud_storage
    print(f"Test Case 2: File exists - {file_exists}")  # Menampilkan hasil pemeriksaan keberadaan file

    # Test Case 3: Download the file and validate content
    downloaded_content, download_result = download_file(file_name)  # Mengunduh file menggunakan fungsi download_file
    print(f"Test Case 3: {download_result}")  # Menampilkan hasil pengunduhan
    assert downloaded_content == content, "File content mismatch!"  # Validasi apakah konten file sesuai dengan yang diunggah
    print("Test Case 3: File content matches the original content.")  # Menampilkan pesan keberhasilan validasi konten

    # Test Case 4: Attempt to upload a duplicate file
    duplicate_result = upload_file(file_name, "New content")  # Mencoba mengunggah file dengan nama yang sama
    print(f"Test Case 4: {duplicate_result}")  # Menampilkan hasil pengujian duplikasi file

    print("\nUAT completed successfully!")  # Menampilkan pesan akhir pengujian

# Menjalankan UAT jika file ini dijalankan langsung
if __name__ == "__main__":
    run_uat_tests()  # Memanggil fungsi untuk menjalankan semua test case
