## When are Pre-trained Transformers Robust?

Make sure to set the environment variable `PROJ=robustness` before running these scripts. All commands are run in the base fairseq directory for the corresponding project.

# Pre-training

To preprocess data for the dataset `${DSET}`, run:

`bash preprocessing/pretrain_preprocess.sh pile ${DSET}`

Once done pretraining, the pretraining job can be launched with:

`python3 launch_train.py train=pretrain data=pile train.seed=0 data.fdset=${DSET} data.tdset=null slurm.gres=gpu:8 data.bin.num_classes=null restore=false -m`

# Fine-tuning

Data can be preprocessed as before with genre-specific scripts. For sentiment, use

`bash preprocessing/sent_preprocess.sh sentiment ${DSET} orig`

For nli, use 

`bash preprocessing/mnli_preprocess.sh nli ${DSET} orig`

For STS, use

`TODO: add STS preprocessing script`

Once the data has been fine-tuned,

