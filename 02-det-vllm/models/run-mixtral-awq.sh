det cmd run --config-file mixtral-awq.yaml --context . \
    "python -m vllm.entrypoints.openai.api_server \
    --model TheBloke/Nous-Hermes-2-Mixtral-8x7B-SFT-AWQ \
    --dtype auto \
    --quantization awq \
    --port 8002 \
    --api-key token-abc123" \
    
