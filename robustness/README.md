# When are Pre-trained Transformers Robust?

Make sure to set the environment variable `export PROJ=robustness` before running these scripts. All commands are run in the base fairseq directory for the corresponding project.

## Pre-training

To preprocess data for the dataset `${DSET}`, run:

`bash preprocessing/pretrain_preprocess.sh pile ${DSET}`

Once done pretraining, the pretraining job can be launched with:

`python3 launch_train.py train=pretrain data=pile train.seed=0 data.fdset=${DSET} data.tdset=null slurm.gres=gpu:8 data.bin.num_classes=null restore=false -m`

## Fine-tuning

Data can be preprocessed as before with genre-specific scripts. For sentiment, use

`bash preprocessing/sent_preprocess.sh sentiment ${DSET} orig`

For nli, use 

`bash preprocessing/mnli_preprocess.sh nli ${DSET} orig`

For STS, use

`TODO: add STS preprocessing script`

Once the data has been fine-tuned, we can launch the corresponding job with the following command. Different tasks and domains can be trained by changing `data` and `data.fdset` accordingly.

`python3 launch_train.py data=robust_nli data/bin=orig train.seed=0 data.fdset=fiction slurm.gres=gpu:4 -m`

Once launched, the job should take approximately 1-2 hours to complete, with the outputs in the corresponding slurm folders. To evaluate the model, run the following command, modifying as before `data` and `data.fdset` to change the model you are evaluating, as well as specifying `eval.model.date` to point to the specific date it was trained on. Change `data.tdset` to modify the domain in which to evaluate the model, if different from the one it is trained on. To evaluate on the test split, add the additional override `eval.split=test`

`python3 eval_roberta_glue.py data=robust_nli data/bin=orig train.seed=0 data.fdset=fiction data.tdset=fiction eval.model.date=2021-03-30 -m`

In order to view the results run the following command. Note that this command is not run on slurm, just locally. The script will average across all seeds provided in `display.seed`, so change this override accordingly. If a seed or file is missing, it will be ignored. As before, adjust `display.dir.date` to match the date that the models were evaluated on.

`python3 display_results.py data=robust_nli data/bin=orig display.dir.date=2021-03-30 +display.seed="[$(seq -s, 0 1 9)]"`

