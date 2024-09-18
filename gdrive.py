out_file_name = "STAR GOLD HD [00:00-04:00].[15-09-2024] 1080p TPLAY WEB-DL x264 join @tataplay_ripping.mkv"
from bot import app
msg = app.send_message(7126874550, "UploadIng")
import time
from bot.helpers.upload.gdrive import GoogleDriveUploader
srt = time.time()
upload_path = "BotUploads/files/"
uploader = GoogleDriveUploader(app, msg, srt)
uploader.upload_file(out_file_name, upload_path)
print("File Uploaded")            
