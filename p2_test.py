import os
import numpy as np
import torch
from p2_utils import my_argparse, get_dataloader
from p2_data import load_data, save_prediction
from p2_model import ResNet50

def test(test_dataloader, model, device):
	model.to(device)
	model.eval()
	prediction = []
	with torch.no_grad():
		for data in test_dataloader:
			data = data.to(device)
			output = model(data)
			_, index = torch.max(output, dim = 1)
			prediction.append(index.cpu().detach().numpy())
	# notice to add axis = 0, it's important!, if we don't set axis = 0 will cause error and die in here D:
	prediction = np.concatenate(prediction, axis = 0)
	return prediction

def main(args):
	device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
	print('load testing data...')
	test_image_name = load_data(args.test_img_dir, args.test_csv_dir, 'test')
	test_dataloader = get_dataloader(args.test_img_dir, test_image_name, None, 'test')
	print('test model...')
	# specified model
	model = ResNet50()
	model.load_state_dict(torch.load(os.path.join(args.test_model_dir), map_location = device))
	prediction = test(test_dataloader, model, device)
	save_prediction(test_image_name, prediction, args.result_csv_dir)

if __name__ == '__main__':
	args = my_argparse()
	main(args)