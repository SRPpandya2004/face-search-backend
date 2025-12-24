import os
from typing import Optional

import firebase_admin
from firebase_admin import credentials, storage
from google.cloud.storage.blob import Blob


class FirebaseStorageClient:
    def __init__(
        self,
        bucket_name: str,
        service_account_path: Optional[str] = None,
    ):
        """
        Initialize Firebase Storage client

        Credential priority:
        1) service_account_path argument
        2) FIREBASE_SERVICE_ACCOUNT environment variable
        """

        if not firebase_admin._apps:
            # Choose credential source
            if service_account_path:
                if not os.path.exists(service_account_path):
                    raise FileNotFoundError(
                        f"Service account file not found: {service_account_path}"
                    )
                cred = credentials.Certificate(service_account_path)
            else:
                env_path = os.getenv("FIREBASE_SERVICE_ACCOUNT")
                if not env_path:
                    raise ValueError(
                        "Firebase service account not found.\n"
                        "Provide service_account_path OR set FIREBASE_SERVICE_ACCOUNT env var."
                    )
                cred = credentials.Certificate(env_path)

            firebase_admin.initialize_app(
                cred,
                {"storageBucket": bucket_name},
            )

        self.bucket = storage.bucket()

    def upload_file(
        self,
        local_path: str,
        remote_path: str,
        make_public: bool = True,
    ) -> str:
        blob: Blob = self.bucket.blob(remote_path)
        blob.upload_from_filename(local_path)

        if make_public:
            blob.make_public()
            return blob.public_url

        return blob.path

    def upload_bytes(
        self,
        data: bytes,
        remote_path: str,
        content_type: str = "image/jpeg",
        make_public: bool = True,
    ) -> str:
        blob: Blob = self.bucket.blob(remote_path)
        blob.upload_from_string(data, content_type=content_type)

        if make_public:
            blob.make_public()
            return blob.public_url

        return blob.path

    def generate_signed_url(
        self,
        remote_path: str,
        expiration_seconds: int = 3600,
    ) -> str:
        blob: Blob = self.bucket.blob(remote_path)
        return blob.generate_signed_url(
            expiration=expiration_seconds,
            method="GET",
        )
