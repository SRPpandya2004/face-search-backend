import uuid
from app.core.firebase_storage import FirebaseStorageClient

client = FirebaseStorageClient(
    bucket_name="face-search-project-36f9e.firebasestorage.app",  # 🔴 CHANGE THIS
    service_account_path="secrets/firebase_service_account.json",  # 🔴 CHANGE THIS
)

url = client.upload_file(
    local_path="test.jpg",  # 🔴 put a real image here
    remote_path=f"test_uploads/{uuid.uuid4()}.jpg",
)

print("Uploaded image URL:", url)
