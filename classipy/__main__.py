import argparse
import subprocess
import logging.config
import os

import yaml

from wrappers import Wrappers


if __name__ == "__main__":
    loc = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(loc, "../config/logging_config.yml")) as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

    logger = logging.getLogger("classipy")
    logger.debug("Entrypoint...")
    parser = argparse.ArgumentParser("classipy")
    parser.add_argument("fastq")
    parser.add_argument("db")
    parser.add_argument("outdir")
    parser.add_argument("--threads", default=2)

    args = parser.parse_args()
    run = Wrappers(args)

    logger.info("Running Kraken")
    if run.kraken2():
        logger.info("Kraken ran succesfully")
        logger.info("Running Krona")

        if run.krona():
            logger.info("Krona ran succesfully")
