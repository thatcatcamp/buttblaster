from bing_image_downloader import downloader as xx
query_string = "bicycle green"
xx.download(query_string, limit=100,  output_dir='images/train/bicycle', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
