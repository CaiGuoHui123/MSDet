# MSDet: Receptive Field Enhanced Multiscale Detection for Tiny Pulmonary Nodule

Authors: [Guohui Cai](https://github.com/CaiGuoHui123), Ruicheng Zhang, Hongyang He, [Zeyu Zhang](https://steve-zeyu-zhang.github.io/)†, [Daji Ergu](https://ieeexplore.ieee.org/author/37085795653), [Yuanzhouhan Cao](https://scholar.google.com/citations?user=-RBi2JcAAAAJ&hl=en), Jinman Zhao, Binbin Hu, [Zhinbin Liao](https://researchers.adelaide.edu.au/profile/zhibin.liao#), [Yang Zhao](https://yangyangkiki.github.io/), [Ying Cai](https://ieeexplore.ieee.org/author/37087137422)*

*Corresponding author. †Project lead.

<em><b>ICME 2025</b></em>

[[**Paper Link**](https://arxiv.org/abs/2409.14028)] [[Papers With Code](https://paperswithcode.com/paper/msdet-receptive-field-enhanced-multiscale)]

Pulmonary nodules are critical indicators for the early diagnosis of lung cancer, making their detection essential for timely treatment. However, traditional CT imaging methods suffered from cumbersome procedures, low detection rates, and poor localization accuracy. The subtle differences between pulmonary nodules and surrounding tissues in complex lung CT images, combined with repeated downsampling in feature extraction networks, often lead to missed or false detections of small nodules. Existing methods such as FPN, with its fixed feature fusion and limited receptive field, struggle to effectively overcome these issues. To address these challenges, our paper proposed three key contributions: Firstly, we proposed MSDet, a multiscale attention and receptive field network for detecting tiny pulmonary nodules. Secondly, we proposed the extended receptive domain (ERD) strategy to capture richer contextual information and reduce false positives caused by nodule occlusion. We also proposed the position channel attention mechanism (PCAM) to optimize feature learning and reduce multiscale detection errors, and designed the tiny object detection block (TODB) to enhance the detection of tiny nodules. Lastly, we conducted thorough experiments on the public LUNA16 dataset, achieving state-of-the-art performance, with an mAP improvement of 8.8% over the previous state-of-the-art method YOLOv8. These advancements significantly boosted detection accuracy and reliability, providing a more effective solution for early lung cancer diagnosis.

![Fig1](https://github.com/user-attachments/assets/75f026ea-7e28-4931-b58b-20ba7d9de9b5)



![Fig2](https://github.com/user-attachments/assets/6269e425-5987-4712-b9f9-eddff6238b85)

## How to Run the Code

To run the MSDet code, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/CaiGuoHui123/MSDet.git
   cd MSDet
   ```

2. **Install Dependencies**:
   Install required Python packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Dataset**:
   Download the LUNA16 dataset and place it in the `data/` directory (create this directory if it does not exist).

4. **Train the Model**:
   You can train the model using the following command:
   ```bash
   python go_train.py --config configs/config.yaml
   ```

5. **Run Inference**:
   After training the model, you can run inference on test images:
   ```bash
   python infer.py --model_path ./checkpoints/best_model.pth --input ./test_images --output ./results
   ```

6. **Evaluate**:
   Evaluate the model performance with the following command:
   ```bash
   python eval.py --model_path ./checkpoints/best_model.pth --test_data ./test_data
   ```

## Citation

For academic use, please cite:
```
@article{cai2024msdet,
  title={MSDet: Receptive Field Enhanced Multiscale Detection for Tiny Pulmonary Nodule},
  author={Cai, Guohui and Cai, Ying and Zhang, Zeyu and Ergu, Daji and Cao, Yuanzhouhan and Hu, Binbin and Liao, Zhibin and Zhao, Yang},
  journal={arXiv preprint arXiv:2409.14028},
  year={2024}
}
```

## Contact us

Please do not hesitate to open an issue. You don't want to send us an email since you probably not getting prompt feedback.
