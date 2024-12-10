config = {
    'r' : 8,
    'lora_alpha' : 16,
    'lora_dropout' : 0.1,
    'target_module' : ['attn.c_attn', 'attn.c_proj'],
    'model_name' : 'gpt2',
    'device_map' : 'auto',
    'torch_dtype' : 'auto',
    'offload_folder' : "./offload",
    'offload_state_dict' : True,
    'prompt_key1' : 'generated_text',
    'prompt_key2' : 'system',
    'parsing_data_file_path' : 'C:/Users/Administrator/PycharmProjects/project/parsing_output/1706_tokenized.txt' ,
    'parsing_data_path' : 'C:/Users/Administrator/PycharmProjects/project/parsing_output' ,
    'output_path' : 'C:/Users/Administrator/PycharmProjects/project/output',
    'input_path' : 'C:/Users/Administrator/PycharmProjects/project/input',
    'base_path' : 'C:/Users/Administrator/PycharmProjects/project',
    'num_cpus' : 8,
    'num_gpus' : 0,
    'output_dir':"./results",
    'overwrite_output_dir' : True,
    'per_device_train_batch_size' : 1,
    'num_train_epochs' : 2,
    'logging_dir' : './logs',
    'logging_steps' : 10,
    'fp16' : True,
    'gradient_accumulation_steps' : 32,
    'learning_rate' : 1e-5,
    'run_mode' : 'app_execution'

}

"""
if url is more than one, look at util.funct.py

"""
