ofn = "STAR GOLD HD [00:00-04:00].[15-09-2024] 1080p TPLAY WEB-DL x264 join @tataplay_ripping.mkv"
msg = app.send_message(7126874550, "UploadIng")
import time
srt = time.time()
upload_path = "/BotUploads/"
uploader = GoogleDriveUploader(app, msg, srt)
uploader.upload_file(out_file_name, upload_path, ott=self.ott)
            
