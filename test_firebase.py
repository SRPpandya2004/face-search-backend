import uuid
from app.core.firebase_storage import FirebaseStorageClient
import os

load_dotenv()

FIREBASE_BUCKET = os.getenv("FIREBASE_BUCKET_NAME")
FIREBASE_KEY_PATH = os.getenv("FIREBASE_CREDENTIALS")

client = FirebaseStorageClient(
    bucket_name=FIREBASE_BUCKET,  # 🔴 CHANGE THIS
    service_account_path=FIREBASE_KEY_PATH,  # 🔴 CHANGE THIS
)

url = client.upload_file(
    local_path="test.jpg",  # 🔴 put a real image here
    remote_path=f"test_uploads/{uuid.uuid4()}.jpg",
)

print("Uploaded image URL:", url)
