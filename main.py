import moxing as mox
mox.file.copy_parallel('./foods_10c', 'obs://huaweia/data')

!python ./train/run.py --data_url './foods_10c/images' --train_url './train_output' --train_epochs 20

import moxing as mox
mox.file.copy_parallel('./deploy', 'obs://huaweia/output/model')

import moxing as mox
mox.file.copy('./train_output/model/best_model.pth', 'obs://huaweia/output/model/best_model.pth')

