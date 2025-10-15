from extract.extractor import extract
from transform.transformer import transform
from load.loader import load
from visualize.grafico import main as viz

if __name__ == '__main__':
    extract()
    df = transform()
    load()
    viz()
