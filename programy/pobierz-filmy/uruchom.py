# pip install smart_open[http]
from smart_open import open

def stream_uri(uri_in, uri_out, chunk_size=1 << 18):  # 256kB chunks
    """Write from uri_in to uri_out with minimal memory footprint."""
    with open(uri_in, "rb") as fin, open(uri_out, "wb") as fout:
        while chunk := fin.read(chunk_size):
            fout.write(chunk)

# from https to disk
stream_uri("https://www.youtube.com/watch?v=vh3g2D12suQ", "./sample-video.mp4")
