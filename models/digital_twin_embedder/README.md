---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:44
- loss:CosineSimilarityLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: How comfortable are you with data structures and algorithms?
  sentences:
  - I have a solid foundation in core CS concepts such as algorithms, data structures,
    operating systems, DBMS, and object-oriented programming. I use these fundamentals
    when designing efficient pipelines, handling large datasets, and structuring application
    logic.
  - The Document Extractor and Classifier app is a document processing and text classification
    project where I designed a pipeline to process university past-year question paper
    PDFs. The system extracts text, uses custom fine-tuned BERT and TF-IDF-based models
    to classify content into relevant chapters or topics, and then auto-generates
    spreadsheets summarizing the extracted information for easier exam preparation
    and analysis.
  - 'I did a product case study on Overleaf, where I identified requirements for the
    next phase of the product. I followed a structured process: understanding the
    company, product, and market; conducting user research; identifying pain points;
    and then using RICE and Kano models to prioritize features that deliver the most
    value to users.'
- source_sentence: What extracurricular activities have you been involved in?
  sentences:
  - I’ve built generative AI applications such as a next-token generation model (a
    mini GPT-like system) and experimented with zero-shot and few-shot prompting for
    large language models using APIs. I’ve also designed prompt engineering strategies,
    evaluated LLM behavior for tasks like time-series classification, and integrated
    LLM-style capabilities into prototype applications.
  - I have participated in event management for hackathons, anchored and presented
    in orientation programs, and led the LDCE Computer Girls’ Kho-Kho team to a runner-up
    position. I also reached the semifinals in a coding competition and attended a
    faculty development program on leveraging AI in healthcare delivery systems.
  - Yes, many of my projects have been team-based, such as the Human Activity Recognition
    project and several course projects. I’ve also led and participated in extracurricular
    teams like sports and hackathons, which helped me develop collaboration, communication,
    and leadership skills.
- source_sentence: What experience do you have with computer vision?
  sentences:
  - I’ve worked extensively with computer vision for tasks like human activity recognition,
    object detection, and satellite-image-based change detection. This includes using
    YOLO, CNN-based models, and custom pipelines for super-resolution and image reconstruction.
    I’ve also designed and evaluated vision pipelines that run efficiently on large
    datasets.
  - 'My core AI/ML skills include building and deploying ML pipelines end-to-end:
    data preprocessing, feature engineering, model training and validation, and performance
    optimization. I have worked on classical ML models, deep learning architectures,
    computer vision, temporal change detection, and NLP pipelines including BERT-based
    models and TF-IDF transformers.'
  - I have experience designing relational schemas and building full CRUD backends
    using MySQL with JDBC, Java Spring, and Java Swing. I’ve also integrated ML pipelines
    into backend services, where the database stores inputs, predictions, and metadata
    for later analysis.
- source_sentence: Can you introduce yourself?
  sentences:
  - I am Ruddhi P Shah, a Computer Engineering student specializing in Artificial
    Intelligence and Machine Learning. I love building systems that combine Generative
    AI, agentic workflows, document processing, NLP, and full-stack engineering into
    practical products that solve real problems and are easy to trust.
  - I usually start by clarifying the problem and constraints, then break it down
    into manageable components. I explore existing methods or baselines, design experiments,
    and iterate based on data and feedback. Throughout, I try to keep the solution
    explainable and maintainable so that others can understand and build on it.
  - I am pursuing the IIT Madras Degree in Data Science and Applications. It deepens
    my foundation in statistics, data analysis, and machine learning, and complements
    my core Computer Engineering degree by giving me a more formal grounding in data-centric
    thinking.
- source_sentence: What was your contribution to change detection in the internship?
  sentences:
  - I built image classifiers on the MNIST and Fashion-MNIST datasets, training and
    comparing multiple CNN architectures. I also used t-SNE for feature visualization,
    evaluated performance across models, and experimented with finetuning and regularization
    techniques to improve generalization.
  - In my generative AI project at IIT Gandhinagar, I developed and trained a next-token
    generation model – essentially a small GPT-style language model. I implemented
    the architecture, trained it on text data, and then built a Streamlit demo where
    users could interactively generate continuations of prompts and observe how the
    model learns language patterns.
  - I proposed and implemented a method for temporal change detection using deep learning
    models like LSTM and ConvLSTM. This improved the existing ML pipeline’s performance
    and helped detect changes in brick kiln sites and technology adoption over time
    more accurately.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision c9745ed1d9f207416be6d2e6f8de32d1f16199bf -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'What was your contribution to change detection in the internship?',
    'I proposed and implemented a method for temporal change detection using deep learning models like LSTM and ConvLSTM. This improved the existing ML pipeline’s performance and helped detect changes in brick kiln sites and technology adoption over time more accurately.',
    'I built image classifiers on the MNIST and Fashion-MNIST datasets, training and comparing multiple CNN architectures. I also used t-SNE for feature visualization, evaluated performance across models, and experimented with finetuning and regularization techniques to improve generalization.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.5176, 0.4285],
#         [0.5176, 1.0000, 0.4065],
#         [0.4285, 0.4065, 1.0000]])
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 44 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 44 samples:
  |         | sentence_0                                                                        | sentence_1                                                                         | label                                                         |
  |:--------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:--------------------------------------------------------------|
  | type    | string                                                                            | string                                                                             | float                                                         |
  | details | <ul><li>min: 7 tokens</li><li>mean: 12.45 tokens</li><li>max: 18 tokens</li></ul> | <ul><li>min: 39 tokens</li><li>mean: 67.23 tokens</li><li>max: 98 tokens</li></ul> | <ul><li>min: 1.0</li><li>mean: 1.0</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                  | sentence_1                                                                                                                                                                                                                                                                                                                                                                   | label            |
  |:----------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
  | <code>What experience do you have with computer vision?</code>              | <code>I’ve worked extensively with computer vision for tasks like human activity recognition, object detection, and satellite-image-based change detection. This includes using YOLO, CNN-based models, and custom pipelines for super-resolution and image reconstruction. I’ve also designed and evaluated vision pipelines that run efficiently on large datasets.</code> | <code>1.0</code> |
  | <code>Can you give an example of a product case study you have done?</code> | <code>I did a product case study on Overleaf, where I identified requirements for the next phase of the product. I followed a structured process: understanding the company, product, and market; conducting user research; identifying pain points; and then using RICE and Kano models to prioritize features that deliver the most value to users.</code>                 | <code>1.0</code> |
  | <code>How comfortable are you with data structures and algorithms?</code>   | <code>I have a solid foundation in core CS concepts such as algorithms, data structures, operating systems, DBMS, and object-oriented programming. I use these fundamentals when designing efficient pipelines, handling large datasets, and structuring application logic.</code>                                                                                           | <code>1.0</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 3
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Framework Versions
- Python: 3.12.12
- Sentence Transformers: 5.1.2
- Transformers: 4.57.2
- PyTorch: 2.9.0+cu126
- Accelerate: 1.12.0
- Datasets: 4.0.0
- Tokenizers: 0.22.1

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->