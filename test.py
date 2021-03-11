import hydra
from hydra import slurm_utils
from omegaconf import DictConfig
import os
from omegaconf import OmegaConf

@hydra.main(config_path="robust/config.yaml", strict=False)
def run(cfg: DictConfig) -> None:
    print(cfg.pretty())

if __name__ == "__main__":
    run()
