#!/usr/bin/python2.5

import gdata.photos.service
import gdata.media
import gdata.geo

gd_client = gdata.photos.service.PhotosService()
gd_client.email = '#######'     # Set your Picasaweb e-mail address...
gd_client.password = '######'  # ... and password
gd_client.source = 'api-sample-google-com'
gd_client.ProgrammaticLogin()

albums = gd_client.GetUserFeed()
for album in albums.entry:
  print 'Album: %s (%s)' % (album.title.text, album.numphotos.text)

  photos = gd_client.GetFeed('/data/feed/api/user/default/albumid/%s?kind=photo' % (album.gphoto_id.text))
  for photo in photos.entry:
    print '  Photo:', photo.title.text

    tags = gd_client.GetFeed('/data/feed/api/user/default/albumid/%s/photoid/%s?kind=tag' % (album.gphoto_id.text, photo.gphoto_id.text))
    for tag in tags.entry:
      print '    Tag:', tag.title.text

    comments = gd_client.GetFeed('/data/feed/api/user/default/albumid/%s/photoid/%s?kind=comment' % (album.gphoto_id.text, photo.gphoto_id.text))
    for comment in comments.entry:
      print '    Comment:', comment.content.text
