import datetime

def powerpuff_song():
  print('Blossom! Commander and the leader')
  print('Bubbles! She is the joy and a laugher')
  print('Buttercup! She is the taughest fighter')
  print('Powerpuff save the day...')
  print('tou tou touuuu')

def posca_song():
  print('POSCA POSCAAAA')
  print('tou toudou tou tou tou touuu')
  print('tou toudou tou tou tou touuu')

current_day = datetime.datetime.now().day
if current_day % 2 == 0:
  powerpuff_song()
else:
  posca_song()
