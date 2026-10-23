# Remote Labs · Evidence Notes

真实硬件、数字仿真与桌面软件分别标记；未证实的接入费用、等待时长、个人资格和自动化权限均为未知。

## LabsLand Electronics Hive

- **verified_at**: 2026-09-28T11:28:47.803630+08:00
- **source_urls**: ["https://labsland.com/en/labs/electronics-hive/", "https://labsland.com/pub/docs/experiments/hive/user/en/using_instruments.html", "https://labsland.com/pub/docs/experiments/hive/user/en/taking_measurements.html", "https://labsland.com/pub/docs/experiments/hive/hive-node-reference-documentation.pdf"]
- **hardware**: 继电器连接真实元件并测量；不是纯模拟
- **interface**: 浏览器仪器界面；Perform Measurement执行物理测量；示波器CSV导出已核（参考文档§4.1.7）
- **feedback**: 用户可依据测量修改电路再次提交；无已核自主agent闭环成绩
- **timing_evidence**: §4.2区分用户取得结果UPRT与包含清理的节点处理HPRT；繁忙时增加排队。表4.1/4.2为2023年5月测试，不外推当前延迟。

## Model Hardware Standard：有限研究预览

[Anthropic原始公告](https://www.anthropic.com/news/model-hardware-standard-research-preview)发表于2026-08-27，本次2026-10-23补充核验，不是当日新发布。该方向提供设备元数据、标准读写和安全限制接口，可经MCP、CLI或代码接入，但依赖可编程硬件与驱动。它是协议和集成方向，不是公开可预约的远程实验设施。

原页描述有限研究预览、首批伙伴及等候名单；未来开源不等于已经开放。设备控制案例不证明通用自主科研闭环。官方集成缩时说法缺少匹配样本和对照，不能视为性能保证。费用、许可、访问资格及排队时间均保持未知，不能解释为免费或允许自动化访问。
