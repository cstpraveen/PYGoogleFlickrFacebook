import gdata.photos.service
import gdata.media
import gdata.geo

gd_client = gdata.photos.service.PhotosService()
gd_client.email = '#######' #User Id
gd_client.password = '#######' #Password
gd_client.source = 'exampleCo-exampleApp-1'
gd_client.ProgrammaticLogin()


albums = gd_client.GetUserFeed()
for album in albums.entry:
  print 'title: %s, number of photos: %s, id: %s' % (album.title.text,
      album.numphotos.text, album.gphoto_id.text)
