import gdata.photos.service
import gdata.media
import gdata.geo

name = raw_input("Enter the file Name 'or' Path: ")

gd_client = gdata.photos.service.PhotosService()
gd_client.email = '#######' #User ID
gd_client.password = '######' #Password
gd_client.source = 'exampleCo-exampleApp-1'
gd_client.ProgrammaticLogin()

album = gd_client.InsertAlbum(title='New album', summary='This is an album')

album_url = '/data/feed/api/user/%s/albumid/%s' % (gd_client.email, album.gphoto_id.text)
photo = gd_client.InsertPhotoSimple(album_url, 'New Photo', 'Uploaded using the API', name, content_type='image/jpeg')
print "Photo Uploaded Successfully"
