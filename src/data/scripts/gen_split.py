
import os
import random
import numpy as np


annotations_foder_path =r"E:\shenghuo\tmp\399_det\data\VOC2007\Annotations"
names = os.listdir(annotations_foder_path)
real_names = [name.split(".")[0] for name in names]
print(real_names)
random.shuffle(real_names)
print(real_names)
length = len(real_names)
split_point = int(length * 0.2)
val_names = real_names[:split_point]
train_names = real_names[split_point:]
np.savetxt('val.txt', np.array(val_names), fmt="%s", delimiter="\n")
np.savetxt('test.txt', np.array(val_names), fmt="%s", delimiter="\n")
np.savetxt('train.txt', np.array(train_names), fmt="%s", delimiter="\n")
