# 3D Novel View Synthesis

This project from DLCV(Deep Learing of Computer Vision) hwr.

After excuted step shows below, the script will generate images of hotdog shows below.
![Template](https://raw.githubusercontent.com/Cyx06/DLCV_GAN-DDPM-DANN/main/template.png)

## How to Use This Code

### Prerequisites

1. **Install Required Packages**: 
   ```bash
   pip install requirements.txt
    ```
2. **Run script as shown below**:
    bash hw4_1.sh $1 \$2

    ■ $1: path to the transform_test.json (e.g., */*/transform_test.json)

    Which contains camera poses with the same format as in transfor_train.json, you should predict novel views
base on this file.(you can check the file in the ./ForP1Prepare/transforms_val.json)

    ■ $2: path to the output json file (e.g. hw3/output_p2/pred.json)

    The filename should be same as stated in transform_test.json file. The image size should be the same as training
set, 800x800 pixel.