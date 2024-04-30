det cmd run --config-file mistral.yaml --context . \
    "python -m vllm.entrypoints.openai.api_server \
    --model mistralai/Mistral-7B-Instruct-v0.2 \
    --dtype bfloat16 \
    --port 8001
    --api-key token-abc123" \
    
