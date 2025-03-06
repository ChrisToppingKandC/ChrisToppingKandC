from loguru import logger

@logger.catch
def main(x, y, z):
    return x + y / z

main(1, 2, 0)