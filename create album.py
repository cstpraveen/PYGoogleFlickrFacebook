import gdata.photos.service
import gdata.media
import gdata.geo

gd_client = gdata.photos.service.PhotosService()
gd_client.email = '#########' #USER ID
gd_client.password = '#########' #Password
gd_client.source = 'exampleCo-exampleApp-1'
gd_client.ProgrammaticLogin()

album = gd_client.InsertAlbum(title='New album', summary='This is an album')
