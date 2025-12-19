
import torch
import torch.nn.functional as F
import cv2
import matplotlib.pyplot as plt
import os

# Haar 小波滤波器
def haar_wavelet_filters(device='cpu'):
    ll = torch.tensor([[0.5, 0.5],
                       [0.5, 0.5]], dtype=torch.float32, device=device)
    lh = torch.tensor([[0.5, 0.5],
                       [-0.5, -0.5]], dtype=torch.float32, device=device)
    hl = torch.tensor([[0.5, -0.5],
                       [0.5, -0.5]], dtype=torch.float32, device=device)
    hh = torch.tensor([[0.5, -0.5],
                       [-0.5, 0.5]], dtype=torch.float32, device=device)

    filters = torch.stack([ll, lh, hl, hh], dim=0).unsqueeze(1)  # [4,1,2,2]
    return filters

def dwt_decompose(img_tensor):
    """对输入图像做 Haar 小波分解，返回四个子带"""
    B, C, H, W = img_tensor.shape
    device = img_tensor.device
    filters = haar_wavelet_filters(device).repeat(C, 1, 1, 1)  # [4C,1,2,2]

    subbands = F.conv2d(img_tensor, filters, stride=2, groups=C)  # [B,4C,H/2,W/2]
    LL, LH, HL, HH = torch.chunk(subbands, 4, dim=1)
    return LL, LH, HL, HH

if __name__ == "__main__":
    # 图像路径
    img_path = r"C:\Users\Administrator\Desktop\people.jpg"
    save_path = "./wavelet_with_original.png"

    # 读取图像
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (128,128))  # 缩小方便展示

    # 转 tensor
    img_tensor = torch.from_numpy(img).permute(2,0,1).unsqueeze(0).float() / 255.0  # [1,3,H,W]

    # 小波分解
    LL, LH, HL, HH = dwt_decompose(img_tensor)

    # 转 numpy（只看第一通道）
    LL_img = LL[0,0].detach().numpy()
    LH_img = LH[0,0].detach().numpy()
    HL_img = HL[0,0].detach().numpy()
    HH_img = HH[0,0].detach().numpy()

    # 显示 + 保存
    plt.figure(figsize=(12,6))
    plt.subplot(2,3,1); plt.imshow(img); plt.title("Original"); plt.axis("off")
    plt.subplot(2,3,2); plt.imshow(LL_img, cmap="gray"); plt.title("LL"); plt.axis("off")
    plt.subplot(2,3,3); plt.imshow(LH_img, cmap="gray"); plt.title("LH"); plt.axis("off")
    plt.subplot(2,3,4); plt.imshow(HL_img, cmap="gray"); plt.title("HL"); plt.axis("off")
    plt.subplot(2,3,5); plt.imshow(HH_img, cmap="gray"); plt.title("HH"); plt.axis("off")

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()

    print(f"结果图已保存到: {save_path}")
