
import torch    # gọi thư viện torch
import torch.nn as nn

# xây dựng class softmax và kế thừa từ lớp Module của pytoch


class Softmax(nn.Module):  # kế thừa từ lớp nn.Module của pytoch
    def __init__(self):
        super().__init__()  # kế thừa lại các thuộc tính của torch.module

    def forward(self, data):
        exp_datai = torch.exp(data)

        # tính tổng từng phần tử theo từng cột dim = 0
        # keepdim=True để kết quả sum ra giữ nguyên chiều của ma trận
        return exp_datai/torch.sum(exp_datai, dim=0, keepdim=True)


# xây dựng class softmaxtable và kế thừa từ lớp lớp Module của pytoch


class Softmaxtable(nn.Module):  # kế thừa từ lớp nn.Module của pytoch
    def __init__(self):
        super().__init__()  # kế thừa lại các thuộc tính của torch.module

    def forward(self, data):
        c = torch.max(data)
        exp_datai = torch.exp(data-c)
        return exp_datai/torch.sum(exp_datai, dim=0, keepdim=True)


if __name__ == '__main__':
    data = torch . Tensor([1, 2, 3])
    softmax = Softmax()
    softmax_table = Softmaxtable()
    output = softmax(data)
    output2 = softmax_table(data)
    print(output)
    print(output2)
