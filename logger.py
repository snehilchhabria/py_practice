import logging

def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:-%M:%S"
        )
    
    logging.debug("debug message")
    logging.info("info message")
    logging.warning("warning message")
    logging.error("error msg")
    logging.critical("critical msg")
    
if __name__ == "__main__":
    main()