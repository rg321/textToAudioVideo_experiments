import os
import sys
from face_swapping import fit_first_on_second

# base_name = 'raghav.jpg'

# img_name = "abc"
def create_allMouths(base_name):

	if not base_name == 'base': # no need for base

		dir_name = 'Mouths_' + base_name
		if not os.path.isdir(dir_name) or \
		   not os.listdir(dir_name):


			if not os.path.isdir(dir_name):
				os.mkdir(dir_name)

			mb = 'Mouths_base'

			all_lips = os.listdir(mb)

			print(f'swapping face for {len(all_lips)} images')
			for lip in all_lips:
				fit_first_on_second(os.path.join(mb,lip), base_name+'.jpg', os.path.join(dir_name, lip))
			
			# print('done creating mouths')
		else:
			print('already present')


if __name__=='__main__':
	try:	
		 arg1 = sys.argv[1]
		 base_name = arg1.split('.')[0] # Mouths_ + base_name will have all images
	except:
		 base_name = 'base'

	create_allMouths(base_name)