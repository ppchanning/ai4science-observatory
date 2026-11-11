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


## Allen Telescope Array：现场部署报道

[NVIDIA原始报道](https://blogs.nvidia.com/blog/ai-joins-the-search-for-extraterrestrial-signals/)发表于2026-10-30；上游证据核查为2026-11-03，本目录于2026-11-04补入。公司报道描述真实望远镜现场部署：Nexus共享仪器、计算资源与管线状态，Holoscan提供实时数据通路。其自然语言协调与专用集成不等同于截图GUI控制，也不是数字仿真实验。

报道包含校准、数据纠错与实时脉冲星检测，但没有给出新检测触发下一次观测的完整闭环轨迹或条件完整的自主性、迁移及性能对照。因此不采用“数周或数年缩至数小时”的效率主张，不据此宣称通用自主科研闭环或独立复现。读者可先看原文的仪器状态协调与实时处理两节，分别核对控制机制和科学反馈证据。

这是公司现场报道，不是原始对照论文。公开预约、个人资格、自动化权限、费用、排队及实验时长均未知；现场部署不能作为开放接入证明。本说明由AI辅助整理，推荐不代表维护者已读完或完成复现。

## Computational Discovery MCP

[Google 官方更新](https://research.google/blog/empirical-research-assistance-era-from-nature-publication-to-catalyzing-computational-discovery/)：2026-11-03新增获准用户的 MCP 接入，网页仍可用；2026-11-11核查。计算科研工具，不是远程实物控制证据。资格需批准，费用、排队、实验/分析时长与集成人时未知。
