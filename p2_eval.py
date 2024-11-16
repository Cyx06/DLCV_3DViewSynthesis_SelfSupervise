import sys, csv
args = sys.argv

# read your prediction file
with open(args[1], mode='r') as pred:
    reader = csv.reader(pred)
    next(reader, None)  # skip the headers
    pred_dict = {rows[0]: rows[1:] for rows in reader}

# read ground truth data
with open(args[2], mode='r') as gt:
    reader = csv.reader(gt)
    next(reader, None)
    gt_dict = {rows[0]: rows[1:] for rows in reader}

if len(pred_dict) != len(gt_dict):
    sys.exit("Test case length mismatch.")

episodic_acc = 0
for key, value in pred_dict.items():
    if key not in gt_dict:
        sys.exit("Episodic id mismatch: \"{}\" does not exist in the provided ground truth file.".format(key))

    if gt_dict[key] == value: episodic_acc += 1

print(len(pred_dict))
print('Accuracy:', episodic_acc / len(pred_dict))
