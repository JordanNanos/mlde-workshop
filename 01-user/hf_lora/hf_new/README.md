# Finetuning with LoRA
You can finetune `vicuna-7b-v1.5` with LoRA using the experiment config `distributed.yaml`.
Before submitting the experiment, modify the `bind_mounts` section and fill in a shared_fs path for the hf_cache so we can reuse downloaded models. This is not required but will speed up model loading significantly in subsequent runs.  
Submit the LoRA finetuning experiment to the cluster by running
`det e create distributed.yaml .`

Feel free to modify resources to use more GPUs or modify arguments to play around with different configurations.

Additional example experiment configuration templates are provided for hp search (`adaptive.yaml`) and inetuning all weights with deepspeed (`deepspeed.yaml`) 

NOTE: additional tuning is needed to optimize for training throughput.
