#!/bin/bash
db_ingest --tiledb_metadata encode.dnase.tasks.ENCSR000EID \
	  --array_name ENCSR000EID.chr1 \
	  --chrom_sizes hg38.chrom.sizes \
	  --attribute_config encode_pipeline \
	  --coord_tile_size 10000 \
	  --task_tile_size 1 \
	  --write_chunk 10000000 \
	  --threads 40 \
	  --max_queue_size 50 \
	  --max_mem_g 500


