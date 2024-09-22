# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# top-level folder for each specific model found within the models/ directory at
# the top-level of this source tree.

from dataclasses import dataclass
from functools import lru_cache
from typing import List, Optional

from .datatypes import (
    CheckpointQuantizationFormat,
    CoreModelId,
    Model,
    SamplingParams,
    SamplingStrategy,
)

LLAMA2_VOCAB_SIZE = 32000
LLAMA3_VOCAB_SIZE = 128256


def resolve_model(descriptor: str) -> Optional[Model]:
    for m in all_registered_models():
        descriptors = [
            m.descriptor(shorten_default_variant=False),
            m.descriptor(shorten_default_variant=True),
        ]
        if descriptor in descriptors:
            return m
    return None


@lru_cache
def all_registered_models() -> List[Model]:
    return llama2_family() + llama3_family() + llama3_1_family() + safety_models()


def recommended_sampling_params() -> SamplingParams:
    return SamplingParams(
        strategy=SamplingStrategy.top_p,
        temperature=1.0,
        top_p=0.9,
    )


def llama2_family() -> List[Model]:
    return [
        *llama2_base_models(),
        *llama2_instruct_models(),
    ]


def llama3_family() -> List[Model]:
    return [
        *llama3_base_models(),
        *llama3_instruct_models(),
    ]


def llama3_1_family() -> List[Model]:
    return [
        *llama3_1_base_models(),
        *llama3_1_instruct_models(),
    ]


def llama2_base_models() -> List[Model]:
    return [
        Model(
            core_model_id=CoreModelId.meta_llama2_7b,
            is_default_variant=True,
            description_markdown="Llama 2 7b model",
            huggingface_repo="meta-llama/Llama-2-7b",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": LLAMA2_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 256,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.meta_llama2_13b,
            is_default_variant=True,
            description_markdown="Llama 2 13b model",
            huggingface_repo="meta-llama/Llama-2-13b",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 5120,
                "n_layers": 40,
                "n_heads": 40,
                "n_kv_heads": 8,
                "vocab_size": LLAMA2_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 256,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.meta_llama2_70b,
            is_default_variant=True,
            description_markdown="Llama 2 70b model",
            huggingface_repo="meta-llama/Llama-2-70b",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": LLAMA2_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=8,
        ),
    ]


def llama3_base_models() -> List[Model]:
    return [
        Model(
            core_model_id=CoreModelId.meta_llama3_8b,
            is_default_variant=True,
            description_markdown="Llama 3 8b model",
            huggingface_repo="meta-llama/Meta-Llama-3-8B",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": LLAMA3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 1024,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.meta_llama3_70b,
            is_default_variant=True,
            description_markdown="Llama 3 70b model",
            huggingface_repo="meta-llama/Meta-Llama-3-70B",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": LLAMA3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=8,
        ),
    ]


def llama3_1_base_models() -> List[Model]:
    return [
        Model(
            core_model_id=CoreModelId.meta_llama3_1_8b,
            is_default_variant=True,
            description_markdown="Llama 3.1 8b model",
            huggingface_repo="meta-llama/Meta-Llama-3.1-8B",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": LLAMA3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 1024,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.meta_llama3_1_70b,
            is_default_variant=True,
            description_markdown="Llama 3.1 70b model",
            huggingface_repo="meta-llama/Meta-Llama-3.1-70B",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": LLAMA3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=8,
        ),
        Model(
            core_model_id=CoreModelId.meta_llama3_1_405b,
            is_default_variant=False,
            description_markdown="Llama 3.1 405b model (BF16 weights)",
            huggingface_repo="meta-llama/Meta-Llama-3.1-405B",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 16384,
                "n_layers": 126,
                "n_heads": 128,
                "n_kv_heads": 8,
                "vocab_size": LLAMA3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.2,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=8,
        ),
        Model(
            core_model_id=CoreModelId.meta_llama3_1_405b,
            is_default_variant=True,
            description_markdown="Llama 3.1 405b model (FP8 quantized)",
            huggingface_repo="meta-llama/Meta-Llama-3.1-405B-FP8",
            quantization_format=CheckpointQuantizationFormat.fp8_mixed,
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 16384,
                "n_layers": 126,
                "n_heads": 128,
                "n_kv_heads": 8,
                "vocab_size": LLAMA3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.2,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=8,
        ),
        Model(
            core_model_id=CoreModelId.meta_llama3_1_405b,
            is_default_variant=False,
            description_markdown="Llama 3.1 405b model (BF16 weights for mp16)",
            huggingface_repo="meta-llama/Meta-Llama-3.1-405B",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 16384,
                "n_layers": 126,
                "n_heads": 128,
                "n_kv_heads": 16,
                "vocab_size": LLAMA3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.2,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=16,
        ),
    ]


def llama2_instruct_models() -> List[Model]:
    return [
        Model(
            core_model_id=CoreModelId.meta_llama2_7b_chat,
            is_default_variant=True,
            description_markdown="Llama 2 7b chat model",
            huggingface_repo="meta-llama/Llama-2-7b-chat",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": LLAMA2_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 256,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.meta_llama2_13b_chat,
            is_default_variant=True,
            description_markdown="Llama 2 13b chat model",
            huggingface_repo="meta-llama/Llama-2-13b-chat",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 5120,
                "n_layers": 40,
                "n_heads": 40,
                "n_kv_heads": 8,
                "vocab_size": LLAMA2_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 256,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.meta_llama2_70b_chat,
            is_default_variant=True,
            description_markdown="Llama 2 70b chat model",
            huggingface_repo="meta-llama/Llama-2-70b-chat",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": LLAMA2_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 256,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=8,
        ),
    ]


def llama3_instruct_models() -> List[Model]:
    return [
        Model(
            core_model_id=CoreModelId.meta_llama3_8b_instruct,
            is_default_variant=True,
            description_markdown="Llama 3 8b instruct model",
            huggingface_repo="meta-llama/Meta-Llama-3-8B-Instruct",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": LLAMA3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 1024,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.meta_llama3_70b_instruct,
            is_default_variant=True,
            description_markdown="Llama 3 70b instruct model",
            huggingface_repo="meta-llama/Meta-Llama-3-70B-Instruct",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": LLAMA3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=8,
        ),
    ]


def llama3_1_instruct_models() -> List[Model]:
    return [
        Model(
            core_model_id=CoreModelId.meta_llama3_1_8b_instruct,
            is_default_variant=True,
            description_markdown="Llama 3.1 8b instruct model",
            huggingface_repo="meta-llama/Meta-Llama-3.1-8B-Instruct",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": LLAMA3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 1024,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.meta_llama3_1_70b_instruct,
            is_default_variant=True,
            description_markdown="Llama 3.1 70b instruct model",
            huggingface_repo="meta-llama/Meta-Llama-3.1-70B-Instruct",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": LLAMA3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=8,
        ),
        Model(
            core_model_id=CoreModelId.meta_llama3_1_405b_instruct,
            is_default_variant=False,
            description_markdown="Llama 3.1 405b instruct model (BF16 weights)",
            huggingface_repo="meta-llama/Meta-Llama-3.1-405B-Instruct",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 16384,
                "n_layers": 126,
                "n_heads": 128,
                "n_kv_heads": 8,
                "vocab_size": LLAMA3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.2,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=8,
        ),
        Model(
            core_model_id=CoreModelId.meta_llama3_1_405b_instruct,
            is_default_variant=True,
            description_markdown="Llama 3.1 405b instruct model (FP8 quantized)",
            huggingface_repo="meta-llama/Meta-Llama-3.1-405B-Instruct-FP8",
            quantization_format=CheckpointQuantizationFormat.fp8_mixed,
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 16384,
                "n_layers": 126,
                "n_heads": 128,
                "n_kv_heads": 8,
                "vocab_size": LLAMA3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.2,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=8,
        ),
        Model(
            core_model_id=CoreModelId.meta_llama3_1_405b_instruct,
            is_default_variant=False,
            description_markdown="Llama 3.1 405b instruct model (BF16 weights for mp16)",
            huggingface_repo="meta-llama/Meta-Llama-3.1-405B-Instruct",
            recommended_sampling_params=recommended_sampling_params(),
            model_args={
                "dim": 16384,
                "n_layers": 126,
                "n_heads": 128,
                "n_kv_heads": 16,
                "vocab_size": LLAMA3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.2,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=16,
        ),
    ]


@lru_cache
def safety_models() -> List[Model]:
    return [
        Model(
            core_model_id=CoreModelId.llama_guard_3_8b,
            is_default_variant=True,
            description_markdown="Llama Guard v3 8b system safety model",
            huggingface_repo="meta-llama/Llama-Guard-3-8B",
            model_args={
                "dim": 4096,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 1024,
                "n_heads": 32,
                "n_kv_heads": 8,
                "n_layers": 32,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
                "vocab_size": LLAMA3_VOCAB_SIZE,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.llama_guard_3_8b,
            is_default_variant=False,
            description_markdown="Llama Guard v3 8b system safety model",
            huggingface_repo="meta-llama/Llama-Guard-3-8B-INT8",
            quantization_format=CheckpointQuantizationFormat.int8,
            model_args={
                "dim": 4096,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 1024,
                "n_heads": 32,
                "n_kv_heads": 8,
                "n_layers": 32,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
                "vocab_size": 128256,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.prompt_guard_86m,
            is_default_variant=True,
            description_markdown="Prompt Guard 86M injection safety model",
            huggingface_repo="meta-llama/Prompt-Guard-86M",
            model_args={},
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.llama_guard_2_8b,
            is_default_variant=True,
            description_markdown="Llama Guard v2 8b system safety model",
            huggingface_repo="meta-llama/Meta-Llama-Guard-2-8B",
            model_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": LLAMA2_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 256,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=1,
        ),
    ]


@dataclass
class LlamaDownloadInfo:
    folder: str
    files: List[str]
    pth_size: int


def llama_meta_net_info(model: Model) -> LlamaDownloadInfo:
    """Information needed to download model from llamameta.net"""

    pth_count = model.pth_file_count
    if model.core_model_id == CoreModelId.meta_llama3_1_405b:
        if pth_count == 16:
            folder = "Meta-Llama-3.1-405B-MP16"
        elif model.quantization_format == CheckpointQuantizationFormat.fp8_mixed:
            folder = "Meta-Llama-3.1-405B"
        else:
            folder = "Meta-Llama-3.1-405B-MP8"
    elif model.core_model_id == CoreModelId.meta_llama3_1_405b_instruct:
        if pth_count == 16:
            folder = "Meta-Llama-3.1-405B-Instruct-MP16"
        elif model.quantization_format == CheckpointQuantizationFormat.fp8_mixed:
            folder = "Meta-Llama-3.1-405B-Instruct"
        else:
            folder = "Meta-Llama-3.1-405B-Instruct-MP8"
    elif model.core_model_id == CoreModelId.llama_guard_3_8b:
        if model.quantization_format == CheckpointQuantizationFormat.int8:
            folder = "Meta-Llama-Guard-3-8B-INT8-HF"
        else:
            folder = "Meta-Llama-Guard-3-8B"
    elif model.core_model_id == CoreModelId.prompt_guard_86m:
        folder = "Prompt-Guard"
    elif model.core_model_id == CoreModelId.llama_guard_2_8b:
        folder = "llama-guard-2"
    else:
        folder = model.huggingface_repo.split("/")[-1]
        if "Llama-2" in folder:
            folder = folder.lower()

    files = ["checklist.chk"]
    if (
        model.core_model_id == CoreModelId.llama_guard_3_8b
        and model.quantization_format == CheckpointQuantizationFormat.int8
    ):
        files.extend(
            [
                "generation_config.json",
                "model-00001-of-00002.safetensors",
                "model-00002-of-00002.safetensors",
                "special_tokens_map.json",
                "tokenizer.json",
                "tokenizer_config.json",
                "model.safetensors.index.json",
            ]
        )
    elif model.core_model_id == CoreModelId.prompt_guard_86m:
        files.extend(
            [
                "model.safetensors",
                "special_tokens_map.json",
                "tokenizer.json",
                "tokenizer_config.json",
            ]
        )
    else:
        files.extend(
            [
                "tokenizer.model",
                "params.json",
            ]
        )
        if model.quantization_format == CheckpointQuantizationFormat.fp8_mixed:
            files.extend([f"fp8_scales_{i}.pt" for i in range(pth_count)])
        files.extend([f"consolidated.{i:02d}.pth" for i in range(pth_count)])

    return LlamaDownloadInfo(
        folder=folder,
        files=files,
        pth_size=llama_meta_pth_size(model),
    )


# Sadness because Cloudfront rejects our HEAD requests to find Content-Length
def llama_meta_pth_size(model: Model) -> int:
    if model.core_model_id not in (
        CoreModelId.meta_llama3_1_405b,
        CoreModelId.meta_llama3_1_405b_instruct,
    ):
        return 0

    if model.pth_file_count == 16:
        return 51268302389
    elif model.quantization_format == CheckpointQuantizationFormat.fp8_mixed:
        return 60903742309
    else:
        return 101470976045
