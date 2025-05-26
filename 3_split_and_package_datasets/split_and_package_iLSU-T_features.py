import torch
import pickle, gzip
import os
import argparse
import pysrt
import numpy as np

def n1Dtensors_to_2Dtensor(list_of_tensors):
	for i in range(len(list_of_tensors)):
		list_of_tensors[i] = list_of_tensors[i].squeeze()
	tensor = torch.vstack(list_of_tensors)
	return tensor

def get_text_of_samples(ilsut_videoclips_dir):	
	videoclip_and_srt_files = os.listdir(ilsut_videoclips_dir)
	os.chdir(ilsut_videoclips_dir)
	dataset_texts = {}
	contador = 0
	for videoclip_and_srt_file in videoclip_and_srt_files:
		if videoclip_and_srt_file.endswith('.srt'):
			contador += 1
			print(contador)
			sub = pysrt.open(videoclip_and_srt_file)
			dataset_texts[videoclip_and_srt_file[:-4]] = sub.text
	return dataset_texts

root_path = '.../iLSU_T/i3dASL2k_feats/span8_stride2/' # for ASL-2k visual features
# root_path = '.../iLSU_T/i3dBSL5k_feats/span8_stride2/' # for BSL-5k visual features
os.chdir(root_path)

i3d_features_list = os.listdir()

ilsut_videoclips_dir = '.../iLSU_T/video_clips/'

print('loading...')
label_texts = get_text_of_samples(ilsut_videoclips_dir)
print('done!')

N = len(i3d_features_list)

np.random.seed(42)
shuffle_idx = np.random.permutation(N)

prop = {}
prop['test'] = 0.1
prop['dev'] = 0.1
prop['train'] = 0.8


# data splits will be conformed in this order: test, dev, train
beg_idx_test, beg_idx_dev, beg_idx_train = 0, int(np.ceil(N*prop['test'])), int(np.ceil(N*(prop['test']+prop['dev'])))
end_idx_test, end_idx_dev, end_idx_train = beg_idx_dev, beg_idx_train, N

for split in ['test', 'dev', 'train']:

	dataset = []
	if split == 'test':
		a, b = beg_idx_test, end_idx_test
	if split == 'dev':
		a, b = beg_idx_dev, end_idx_dev
	if split == 'train':
		a, b = beg_idx_train, end_idx_train

	for i in range(a, b):
		i3d_features_file = i3d_features_list[shuffle_idx[i]]
		
		print('split ' + split + ' --- ' + i3d_features_file[:-3] + ' --- ' + str(round(i/len(i3d_features_list)*100, 2)) + '%')
		sample = {}
		sample['name'] = split + '/' + i3d_features_file[:-3]
		sample['text'] = label_texts[i3d_features_file[:-3]]
		sample['signer'] = 'S' + i3d_features_file[:-3].split('.avi_')[0].split('_')[-1][1:]
		sample['gloss'] = label_texts[i3d_features_file[:-3]] 
		
		i3dfeats = torch.load(os.path.join(root_path, i3d_features_file))

		if i3dfeats == []:
			print('empty features')
		if i3dfeats != []:
			sample['sign'] = n1Dtensors_to_2Dtensor(i3dfeats)
			dataset.append(sample)

	# for ASL-2k visual features
	with gzip.open('../packaged/ilsut.i3dfeats_2000.span8_stride2.' + split, 'wb') as f:
		pickle.dump(dataset,f)	

	# for BSL-5k visual features
	# with gzip.open('../packaged/ilsut.i3dfeats_5383.span8_stride2.' + split, 'wb') as f:
	# 	pickle.dump(dataset,f)	
