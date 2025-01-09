from Train_eval import train, eval, select_best


def main(model_config=None):
    modelConfig = {
        "state": "eval",  # train, eval, or select_best
        "epoch": 20,
        "band": 205,  # 189, 189, 162, 205      -->图像通道数
        "multiplier": 2,
        "seed": 1,
        "batch_size": 64,
        "group_length": 20,
        "depth": 4,
        "heads": 4,
        "dim_head": 64,
        "mlp_dim": 64,
        "adjust": False,
        "channel": 128,
        "lr": 1e-4,
        "epision": 5,
        "grad_clip": 1.,
        "device": "cuda:3",
        "training_load_weight": None,
        "save_dir": "./Checkpoint/",
        "test_load_weight": "ckpt_10_.pt", # abu-beach-4.mat 17  abu-urban-4 0
        "path": "./dataset/abu-urban-4.mat"
    }
    if model_config is not None:
        modelConfig = model_config
    if modelConfig["state"] == "train":
        train(modelConfig)
    elif modelConfig["state"] == "eval":
        eval(modelConfig)
    else:
        select_best(modelConfig)


if __name__ == '__main__':
    main()
