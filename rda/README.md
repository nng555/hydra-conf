# Reverse Domain Adaptation

This folder contains configuration files for replicating the experiments in the Reverse Domain Adaptation paper. In addition to this repo, you will need to install [fairseq](https://github.com/nng555/fairseq-ssmba) as well as the 1.0_branch version of [hydra](https://github.com/nng555/hydra/tree/origin/1.0_branch). Note that the linked repos are custom forks with modified code. All repos should be cloned into the home directory. By default slurm will output into the path
`~/slurm/${date}/${job)name}`. 

Before running any commands, make sure to set the environment variable `export PROJ=rda`. All commands are run in the base fairseq directory for the corresponding project.

## Test-time RDA

During test-time RDA,  

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

