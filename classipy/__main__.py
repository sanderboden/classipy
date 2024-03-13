import argparse
import subprocess
import logging

from wrappers import Wrappers


if __name__ == "__main__":
    logger = logging.getLogger("classipy")
    logger.debug("Entrypoint...")
    parser = argparse.ArgumentParser("classipy")
    parser.add_argument("fastq")
    parser.add_argument("db")
    parser.add_argument("outdir")
    parser.add_argument("--threads", default=2)

    args = parser.parse_args()
    run = Wrappers(args)