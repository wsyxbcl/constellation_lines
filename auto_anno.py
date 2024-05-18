from utils import FishEyeImage
from astropy.table import Table

# hips_star = Table.read('data/hip_for_cal.fits')

file = './example/022A7236'

pic = FishEyeImage(file+'.jpg', file+'.CR3',f=20.5,k=1)

pic.solve(solve_size=1000)

pic.constellation(fn=file+'_n.jpg')
