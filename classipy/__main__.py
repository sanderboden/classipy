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
    parser = argparse.ArgumentParser(
        "classipy",
        epilog="Developed by Sander Boden. For issues, please refer to https://github.com/sanderboden/classipy/issues.",
    )
    parser.add_argument("fastq", help="path to directory containing fastq files.")
    parser.add_argument("db", help="Path to krakendb directory.")
    parser.add_argument(
        "outdir", help="output directory. Will be created if it doesn't exist."
    )
    parser.add_argument(
        "--threads",
        default=2,
        help="Maximum number of threads to use. (default: 2)",
        type=int,
        metavar="int",
    )
    parser.add_argument(
        "--confidence",
        default=0.0,
        help="Confidence value for kraken2. (default 0.0)",
        type=float,
        metavar="float",
    )

    args = parser.parse_args()
    run = Wrappers(args)

    logger.info("Running Kraken")
    if run.kraken2():
        logger.info("Kraken ran succesfully")
        logger.info("Running Krona")

        if run.krona():
            logger.info("Krona ran succesfully")
