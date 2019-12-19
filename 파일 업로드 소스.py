#-*- coding: utf-8 -*-
from picamera import PiCamera
from time import sleep
from datetime import datetime
from subprocess import call
import uuid
import smtplib

camera = PiCamera()

tF = str(datetime.now())[:19]
try:
        while True:
                camera.start_preview()
                camera.start_recording('/home/pi/' +tF + '.h264')
                sleep(10000)
#sleep(10)
#camera.stop_recording()
#camera.stop_preview()


except KeyboardInterrupt:

        camera.stop_recording()
        # call("MP4Box -add "+tF +"_vid.h264 "+ tF+"_vid.mp4", shell=True)
        camera.stop_preview()
        camera.close()


        from googleapiclient.discovery import build
        from httplib2 import Http
        from oauth2client import file, client, tools

        try :
            import argparse
            flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        except ImportError:
            flags = None

        SCOPES = 'https://www.googleapis.com/auth/drive.file'
        store = file.Storage('storage.json')
        creds = store.get()

        if not creds or creds.invalid:
            print("make new storage data file ")
            flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
            creds = tools.run_flow(flow, store, flags) \
                    if flags else tools.run(flow, store)

        DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

        FILES = (
            ('/home/pi/' +tF + '.h264'),
        )

    
        file_metadata = {
            'name': 'sample',
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = DRIVE.files().create(body=file_metadata,
                                            fields='id').execute()
        print ('Folder ID: %s' % file.get('id'))

        for file_title in FILES :
            file_name = file_title
            metadata = {'name': file_name,
                        'parents': [file.get('id')],
                        'mimeType': video/h264
                        }
            # media = MediaFileUpload('files/photo.jpg', mimetype='image/jpeg')
            res = DRIVE.files().create(body=metadata, media_body=file_name ).execute()
            if res:
                print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))