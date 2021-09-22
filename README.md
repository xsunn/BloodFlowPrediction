# Intra-cardiac Blood Flow Pattern Prediction
## 1. Introduction
In standard long-axis cine MR views the intensity fluctuations within the blood pool provide a visual clue about the global blood flow pattern within the cardiac cavities.      In this project, we proposed a deep learning based method for automated intra-cardiac blood flow velocity prediction from standard long-axis Cine MRI.
## 2. Network structure
![image text](https://github.com/xsunn/BloodFlowPrediction/blob/main/model/modelnetwork.png) 
Network architecture
## Visualization samples
Case Num|Cine MRI|4D flow(ground truth)|DL (prediction)|Metrics
----|----|----|---- |---- 
1| ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/CINE/S118.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/GT/S118.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/DL/S118.gif)| EPE: Anlge: Acc: E/A ratio: 
2| ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/CINE/S121.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/GT/S121.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/DL/S121.gif)  
3| ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/CINE/v06.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/GT/v06.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/DL/v06.gif) 
4| ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/CINE/S60.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/GT/S60.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/DL/S60.gif) 
5| ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/CINE/M95.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/GT/M95.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/DL/M95.gif) 
6| ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/CINE/M71.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/GT/M71.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/DL/M71.gif) 
7| ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/CINE/S82.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/GT/S82.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/DL/S82.gif) 
8| ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/CINE/V22.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/GT/v22.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/DL/V22.gif) 
9| ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/CINE/S113.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/GT/S113.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/DL/S113.gif) 
10| ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/CINE/S125.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/GT/S125.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/4CHDEMO/DL/S125.gif) 
