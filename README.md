# Intra-cardiac Blood Flow Pattern Prediction
## 1. Introduction
In standard long-axis cine MR views the intensity fluctuations within the blood pool provide a visual clue about the global blood flow pattern within the cardiac cavities.      In this project, we proposed a deep learning based method for automated intra-cardiac blood flow velocity prediction from standard long-axis Cine MRI.
## 2. Network structure
![image text](https://github.com/xsunn/BloodFlowPrediction/blob/main/model/modelnetwork.png) 
Network architecture
## Visualization samples
Case Num|Cine MRI|4D flow(ground truth)|DL (prediction)
----|----|----|---- 
1| ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/samples/M100_Scan2_4CH.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/samples/M100_Scan2_4CH.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/samples/M100_Scan2_4CH.gif) 
2| ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/samples/M102_Scan2_4CH.gif) | ![image](https://github.com/xsunn/BloodFlowPrediction/blob/main/samples/M102_Scan2_4CH.gif) | ![image text](https://github.com/xsunn/BloodFlowPrediction/blob/main/samples/M102_Scan2_4CH.gif) 
