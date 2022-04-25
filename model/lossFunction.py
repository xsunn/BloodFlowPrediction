import torch
import torch.nn.functional as F
import math

def EPE(input_flow, target_flow, sparse=False, mean=True):
    # absTarget_flow=torch.square(target_flow)
    # absTarget_flow=torch.sum(absTarget_flow,dim=1)
    #
    # weightMap=(absTarget_flow-absTarget_flow.min())/(absTarget_flow.max()-absTarget_flow.min())
    #
    # weightMap=weightMap*10+1
    #
    # EPE_map = torch.norm(target_flow-input_flow,2,dim=1)
    # # print(EPE_map.shape)
    # EPE_map = torch.mul(EPE_map,weightMap)
    # batch_size = EPE_map.size(0)
    #
    error=0
    b, _, h, w = target_flow.size()
    # print(b,_,h,w)
    for i in range(b):
        absTarget_flow = torch.square(target_flow[i])
        absTarget_flow = torch.sum(absTarget_flow, dim=0)
        # print(absTarget_flow.shape)
        weightMap = (absTarget_flow - absTarget_flow.min()) / (absTarget_flow.max() - absTarget_flow.min())

        weightMap = weightMap * 10 + 1

        EPE_map = torch.norm(target_flow[i] - input_flow[i], 2, dim=0)
        # print(EPE_map.shape)
        EPE_map = torch.mul(EPE_map, weightMap)
        error=error+EPE_map.mean()
    return error/b


def multiscaleEPE(network_output, target_flow, weights=None, sparse=True):
    def one_scale(output, target, sparse):

        b, _, h, w = output.size()


        target_scaled = F.interpolate(target, (h, w), mode='area')
        return EPE(output, target_scaled, sparse, mean=False)

    if type(network_output) not in [tuple, list]:
        network_output = [network_output]
    if weights is None:
        weights = [1, 0.8, 0.7, 0.6]  # as in original article
    # print("network_output",len(network_output))
    assert(len(weights) == len(network_output))

    loss = 0
    for output, weight in zip(network_output, weights):
        loss += weight * one_scale(output, target_flow, sparse)
    return loss



def realEPE(output, target, sparse=False):
    b, _, h, w = target.size()
    error=0
    # upsampled_output = F.interpolate(output, (h,w), mode='bilinear', align_corners=False)
    for i in range(b):
        EPE_map = torch.norm(target[0]-output[0],2,dim=0)
        error=error+EPE_map.mean()
    # EPE_map = torch.norm(target-upsampled_output,2,dim=1)
    return error/b