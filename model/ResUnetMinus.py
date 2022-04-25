
import torchvision
import torch
import torch.nn as nn
from modelUtil import conv, predict_flow, deconv


class Decoder(nn.Module):
    def __init__(self, in_channels, middle_channels, out_channels):
        super(Decoder, self).__init__()
        self.up = nn.ConvTranspose2d(in_channels, out_channels, kernel_size=2, stride=2)
        self.conv_relu = nn.Sequential(
            nn.Conv2d(middle_channels, out_channels, kernel_size=3, padding=1),
            # nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Dropout(0.2),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1),
            # nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Dropout(0.2)
        )
    def forward(self, x1, x2):
        x1 = self.up(x1)
        x1 = torch.cat((x1, x2), dim=1)
        x1 = self.conv_relu(x1)
        return x1

class Unet(nn.Module):
    def __init__(self, n_class):
        super().__init__()

        self.base_model = torchvision.models.resnet18(False)
        self.base_layers = list(self.base_model.children())
        self.layer1 = nn.Sequential(
            # nn.Conv2d(7, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False),
            nn.Conv2d(7, 64, kernel_size=(7, 7), stride=(1, 1), padding=(3, 3), bias=False),

            self.base_layers[1],
            self.base_layers[2])

        self.layer2 = nn.Sequential(*self.base_layers[3:5])

        self.layer3 = self.base_layers[5]

        self.layer4 = self.base_layers[6]

        self.layer5 = self.base_layers[7]

        self.decode4 = Decoder(512, 256+256, 256)

        self.decode3 = Decoder(256, 256+128, 256)

        self.decode2 = Decoder(256, 128+64, 128)


        self.decode1 = Decoder(128, 64+64, 64)


        self.decode0 = nn.Sequential(
            nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True),
            nn.Conv2d(64, 32, kernel_size=3, padding=1, bias=False),
            nn.Conv2d(32, 64, kernel_size=3, padding=1, bias=False)
        )
        self.conv_last = nn.Conv2d(64, n_class, 1)
        # self.conv_last = nn.Conv2d(64, n_class, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))


        self.predict_flow4 = predict_flow(256)
        self.predict_flow3 = predict_flow(256)
        self.predict_flow2 = predict_flow(128)
        self.predict_flow1 = predict_flow(64)


    def forward(self, x):
        #
        e1 = self.layer1(x) # 64,128,128; 64,256,

        e2 = self.layer2(e1) # 64,64,64  64,128,128

        e3 = self.layer3(e2) # 128,32,32

        e4 = self.layer4(e3) # 256,16,16

        f = self.layer5(e4) # 512,8,

        d4 = self.decode4(f, e4) # 256,16,16

        flow4=self.predict_flow4(d4)
        d3 = self.decode3(d4, e3) # 256,32,32

        flow3=self.predict_flow3(d3)
        d2 = self.decode2(d3, e2) # 128,64,64


        flow2=self.predict_flow2(d2)
        d1 = self.decode1(d2, e1) # 64,128,128

        out = self.conv_last(d1) # 2,256,256


        if self.training:
            return out,flow2,flow3,flow4
            # return out

        else:
            return out
        # return e2



# from torchsummary import summary
# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#
# modell=Unet(2).cuda()
# summary(modell,(5,256,256))