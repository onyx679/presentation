# -*- coding: utf-8 -*-
"""批量更新PPT的HTML内容，将主线从科技对比转向制度对比"""

import re

with open(r'index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# Page 2: Problem Framing - 修改标题、引导语、金句、4张卡片
# ============================================================

# 标题
content = content.replace(
    '机器人之争，不只是技术之争',
    '机器人之争，本质是制度之争'
)

# 引导语
content = content.replace(
    '如果只比谁的机器人跑得更快、谁的机械臂更精准，结论会停留在产品层面。真正值得比较的，是各国如何制定产业政策、如何推动技术落地，以及准备靠什么模式来占领未来制造业高地。',
    '如果只比谁的机器人跑得更快、谁的AI更聪明，结论只停留在产品层面。真正值得思考的是：为什么同样一个行业，在不同制度下会走出完全不同的路径？机器人产业的竞争，本质上是两种制度模式的竞争。'
)

# 金句
content = content.replace(
    '更深一层看，机器人竞争的核心不是\u201c谁的产品更酷\u201d，而是',
    '更深一层看，机器人竞争的核心不是\u201c谁的技术更强\u201d，而是'
)
content = content.replace(
    '谁在用哪一套产业发展逻辑推动技术创新与规模应用',
    '谁的制度更能高效整合政策、资本、技术和市场，推动产业从0到1再到N'
)

# 卡片1 Scale - 已经被之前的脚本改过，更新为制度版
content = content.replace(
    '<div class="card-kicker">Scale</div>\n                            <h3 class="card-title">中国已是全球最大机器人市场</h3>',
    '<div class="card-kicker">Scale</div>\n                            <h3 class="card-title">制度效率的量化证明</h3>'
)
# Update the card body text for Scale card (the one we modified earlier)
content = content.replace(
    '2024年中国新增安装29.5万台工业机器人，占全球总量的54%。从2013年超越日本至今，中国已连续12年蝉联全球最大市场。2025年人形机器人出货量更是占到全球的80-90%。',
    '中国用40年追完西方50年的差距。2024年装机29.5万台占全球54%，2025年人形机器人出货占全球80-90%。这种追赶速度在自由市场体制下几乎不可能实现。'
)

# 卡片2 Gap -> Policy
content = content.replace(
    '<div class="card-kicker">Gap</div>\n                            <h3 class="card-title">起步晚不等于永远落后</h3>',
    '<div class="card-kicker">Policy</div>\n                            <h3 class="card-title">产业政策的决定性作用</h3>'
)
content = content.replace(
    '1982年中国才造出第一台示教再现工业机器人样机，比日本晚了近20年。但到2024年，国产品牌市占率已达57%，十年前仅28%。',
    '\u201c中国制造2025\u201d一出台\u2192方向明确\u2192资源集中\u2192国产品牌市占率从28%翻倍到57%。这种\u201c政策引导\u2192产业集聚\u2192规模突破\u201d的路径，是中国制度优势的典型体现。'
)

# 卡片3 Core Parts -> Market
content = content.replace(
    '<div class="card-kicker">Core Parts</div>\n                            <h3 class="card-title">核心零部件仍是\u201c卡脖子\u201d关键</h3>',
    '<div class="card-kicker">Market</div>\n                            <h3 class="card-title">市场机制的双刃剑</h3>'
)
content = content.replace(
    '减速器、伺服电机、控制器三大核心部件长期依赖日本和欧洲进口，尽管国产化率已有突破（超70%），但高端市场仍受制于人。',
    '波士顿动力技术全球最强，却被谷歌、软银、现代汽车踢来踢去\u2014\u2014技术好但不赚钱，在纯市场逻辑下就是\u201c没有价值\u201d。这说明自由市场不一定能有效推动产业发展。'
)

# 卡片4 New Wave -> System
content = content.replace(
    '<div class="card-kicker">New Wave</div>\n                            <h3 class="card-title">人形机器人正在开辟新赛道</h3>',
    '<div class="card-kicker">System</div>\n                            <h3 class="card-title">制度竞争的新战场</h3>'
)
content = content.replace(
    '2025年智元出货超5100台，宇树超4000台，远超美国企业。2026年3月宇树递交科创板IPO，佛山建成首条全自动人形机器人产线（年产能1万台），规模化量产时代正式到来。',
    '人形机器人是中西同时起跑的赛道。2025年中国出货占全球80-90%，2026年佛山建成首条全自动产线。谁的制度更能整合资源，谁就先跑出商业闭环。'
)

# ============================================================
# Page 3: Framework - 修改引导语，调整第5个维度
# ============================================================

content = content.replace(
    '比较中西，不是比产品，而是比产业逻辑',
    '比较中西，不是比产品，而是比制度逻辑'
)
content = content.replace(
    '把问题拉高一层后，比较就不再停留在\u201c谁的机器人更先进\u201d，而是看两套产业发展模式在五个维度上的根本差异。',
    '把问题拉高一层后，比较就不再停留在\u201c谁的机器人更先进\u201d，而是看两种制度模式在五个维度上的根本差异。'
)

# 修改第5个维度：竞争策略 -> 社会治理
content = content.replace(
    '<div class="framework-label">竞争策略</div>\n                            <div class="framework-desc">是以性价比和规模效应抢占市场，还是以技术壁垒和品牌溢价维持优势。</div>\n                            <div class="framework-clue">Cost advantage vs Tech moat</div>',
    '<div class="framework-label">社会治理</div>\n                            <div class="framework-desc">面对机器人替代就业的冲击，是政策主动引导产业升级与就业转型并行，还是依靠市场自发调节。</div>\n                            <div class="framework-clue">Proactive vs Reactive</div>'
)

# ============================================================
# Page 5: Comparison Matrix - 增加社会治理行
# ============================================================

# 在竞争策略行后面增加社会治理行
old_strategy_row = '''                                <tr>
                                    <td>竞争策略</td>
                                    <td>性价比+规模效应，国产品牌以更低价格抢占中低端市场，逐步向高端渗透。</td>
                                    <td>技术壁垒+品牌溢价，达芬奇手术机器人一台1500-2500万元，长期垄断高端市场。</td>
                                </tr>'''
new_strategy_row = '''                                <tr>
                                    <td>竞争策略</td>
                                    <td>性价比+规模效应，国产品牌以更低价格抢占中低端市场，逐步向高端渗透。</td>
                                    <td>技术壁垒+品牌溢价，达芬奇手术机器人一台1500-2500万元，长期垄断高端市场。</td>
                                </tr>
                                <tr>
                                    <td>社会治理</td>
                                    <td>制造业升级配套技能培训，政策引导就业转型，\u201c机器换人\u201d同时配套再就业保障。</td>
                                    <td>市场自发调节为主，社会保障体系兜底但产业转型阵痛明显，\u201c铁锈地带\u201d问题突出。</td>
                                </tr>'''
content = content.replace(old_strategy_row, new_strategy_row)

# ============================================================
# Page 6: Timeline - 更新标题+增加2026节点
# ============================================================

content = content.replace(
    '四十年：从\u201c一穷二白\u201d到全球第一',
    '四十年：政策驱动下的追赶奇迹'
)
content = content.replace(
    '用四十年走完了别人半个世纪的路。',
    '用四十年走完了别人半个世纪的路，并在人形机器人赛道上实现了领跑。这背后是制度优势的集中体现。'
)

# 在24卡片后增加26卡片
old_24_end = '''                                <p>宇树春晚火出圈，智元、小鹏Iron、小米纷纷入局。资本市场一片欢腾，一级市场融资翻倍达286亿。</p>
                            </article>
                        </div>'''
new_24_end = '''                                <p>宇树春晚火出圈，智元、小鹏Iron、小米纷纷入局。资本市场一片欢腾，一级市场融资翻倍达286亿。</p>
                            </article>
                            <article class="case-card">
                                <div class="num">26</div>
                                <h3>量产：规模化时代到来</h3>
                                <p>智元第1万台机器人下线，宇树递交科创板IPO拟募42亿。特斯拉Optimus Gen3开始量产。佛山建成首条全自动产线。</p>
                            </article>
                        </div>'''
content = content.replace(old_24_end, new_24_end, 1)

# ============================================================
# Page 7: Case Study 1 - 重新框定角度为"产业政策的力量"
# ============================================================

content = content.replace(
    '工业机器人：从\u201c买产品\u201d到\u201c买公司\u201d',
    '产业政策的力量：从\u201c买产品\u201d到\u201c买公司\u201d'
)
content = content.replace(
    '中国在工业机器人领域的追赶路径，可以从两个标志性案例看清楚\u2014\u2014一个是\u201c买下对手\u201d，一个是\u201c打破垄断\u201d。',
    '中国在工业机器人领域的追赶，不是某一家企业的单打独斗，而是产业政策引导下的系统性突破。两个标志性案例可以说明一切。'
)

# 库卡卡片 - 增加制度分析
content = content.replace(
    '2016年中国美的以约4.5亿欧元收购德国库卡控股权（94.55%）。德国社会炸锅\u2014\u2014这可是他们的\u201c国家冠军\u201d企业。默克尔政府介入审查最终放行，但此事引发欧洲对中国技术收购的广泛警惕。',
    '2016年美的收购德国库卡94.55%股权。这不是简单的商业收购，而是中国产业政策支持下的战略性技术获取。德国的\u201c震惊\u201d恰恰说明中国制度的整合能力\u2014\u2014一个发展中国家的企业，能够收购发达国家的\u201c国家冠军\u201d。'
)

# 达芬奇卡片 - 增加制度分析
content = content.replace(
    '美国直觉外科的达芬奇系统，一套售价1500-2500万人民币，长期垄断全球手术机器人市场。中国医院想用一台都得掂量掂量。但现在微创医疗、精锋医疗等国产品牌已获批上市，正在凭价格和本地化优势\u201c围攻\u201d达芬奇。',
    '达芬奇手术机器人一套1500-2500万元，垄断了近20年。但在国家\u201c医疗器械自主可控\u201d政策推动下，微创医疗、精锋医疗获批上市，用价格+本地化优势\u201c围攻\u201d达芬奇。这是制度引导下的国产替代路径。'
)

# 全球格局卡片 - 增加制度结论
content = content.replace(
    '过去十年，全球工业机器人安装量几乎翻倍：2014年22.1万台\u21922024年54.2万台。其中亚洲占74%。日本（4.45万台）、美国（3.42万台）、德国（2.70万台）加起来，还不到中国的一半。',
    '国产品牌市占率十年翻倍（28%\u219257%），日美德加起来不到中国一半。当西方还在争论\u201c政府该不该干预市场\u201d时，中国已经用制度效率证明了答案。核心零部件国产化率超70%，但高端减速器仍需突破。'
)

# ============================================================
# Page 8: Case Study 2 - 重新框定为"市场机制的双刃剑"
# ============================================================

content = content.replace(
    '人形机器人：新赛道上的正面交锋',
    '市场机制的双刃剑：人形机器人的不同命运'
)
content = content.replace(
    '如果说工业机器人是\u201c中国追着跑\u201d，那人形机器人就是一个中西几乎同时起跑的新战场。谁能先跑出商业闭环，谁就赢。',
    '同样优秀的技术，在不同制度下结局可以截然不同。人形机器人赛道完美展示了市场机制与举国体制的差异。'
)

# 核心对比框
content = content.replace(
    '波士顿动力的机器人<strong>好是好，但就是不赚钱</strong>，像个球一样被踢来踢去。宇树科技呢？年营收超10亿，<strong>连续5年盈利</strong>，人形机器人做到了9.9万人民币。',
    '波士顿动力在纯市场机制下<strong>技术最强却活得最惨</strong>，被踢来踢去。宇树在中国产业政策+供应链体系下<strong>连续盈利并即将IPO</strong>。'
)
content = content.replace(
    '这背后是两种完全不同的商业逻辑：技术驱动 vs 成本驱动，实验室思维 vs 供应链思维。',
    '这背后不只是商业逻辑的差异，更是两种制度模式对产业发展的不同影响。'
)

# 波士顿动力卡片标题
content = content.replace(
    '<h3>波士顿动力的命运</h3>',
    '<h3>波士顿动力：自由市场的残酷</h3>'
)
content = content.replace(
    '军方项目起家\u2192谷歌收购\u2192整合失败卖给软银\u2192又被韩国现代汽车买走。物流机器人一台30-50万美元，客户算了算：还不如多雇几个人。',
    '军方起家\u2192谷歌\u2192软银\u2192现代汽车，技术顶尖但不赚钱就没人要。纯市场逻辑下，\u201c长期主义\u201d很难生存\u2014\u2014这是自由市场的结构性缺陷。'
)

# 特斯拉卡片
content = content.replace(
    '马斯克把成本从7万美元压到不到2万，目标1万以下。预计2026年量产5万台。用自家工厂做实训场，供应链和自动驾驶高度复用。',
    'Gen3已于2026年1月量产，甚至停产Model S/X转产机器人。成本压到2万美元，目标售价3万。但这种依赖个人企业家意志的模式能复制吗？'
)

# 宇树卡片
content = content.replace(
    'G1人形机器人9.9万人民币，消费级机器狗不到1万。2024年全球卖了2万多台。春晚一战成名，成为中国机器人商业化的标杆。',
    '连续盈利，2026年递交科创板IPO拟募42亿。9.9万的人形机器人靠的不仅是一家企业的努力，而是整个中国供应链体系和产业政策的支撑。'
)
content = content.replace(
    '<h3>宇树科技</h3>',
    '<h3>宇树科技：中国制度的产物</h3>'
)

# Figure AI卡片
content = content.replace(
    '<h3>Figure AI的估值神话</h3>',
    '<h3>智元机器人：中国速度</h3>'
)
content = content.replace(
    '2022年才成立，连产品都没量产，估值已达395亿美元。微软、英伟达、亚马逊、OpenAI纷纷入局。黄仁勋说：机器人的ChatGPT时刻即将到来。',
    '2025年出货5100+台，2026年3月第1万台下线。开源百万真机数据集\u201cAGIBOT World\u201d，这种\u201c集全行业之力\u201d的协同模式，是中国独有的制度优势。'
)

# ============================================================
# Page 9: 整页重写 - 技术难点 -> 社会影响与制度回应
# ============================================================

old_page9 = '''        <!-- 第9页：技术难点与突破 -->
        <section>
            <div class="slide-shell theme-dark">
                <div class="deco-grid" style="top: 62px; right: 52px;"></div>
                <div class="content-wrap">
                    <div class="eyebrow light">Tech Challenges</div>
                    <h2 class="slide-title light">机器人最难的不是下棋，是拿鸡蛋</h2>
                    <p class="slide-lead light">机器人领域有个著名的\u201c莫拉维克悖论\u201d\u2014\u2014人觉得最简单的事，对机器人最难；人觉得最难的事，机器人反而容易做到。</p>

                    <div class="framework-stack">
                        <div class="framework-row">
                            <div class="framework-label">运动本能</div>
                            <div class="framework-desc">人走路、蹲下、单脚跳不用思考，靠本能完成。机器人需要协调几十个关节电机，耗能巨大。婴儿碰火一次就记住，耗能0.001焦耳；训练机器人认火需要上百万张图片，耗能是婴儿的180万倍。</div>
                            <div class="framework-clue">Moravec\u2019s Paradox</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">感知触觉</div>
                            <div class="framework-desc">视觉靠AI多模态已经很强了，听觉也不错。但触觉是噩梦\u2014\u2014拿鸡蛋不碎，感知软硬、粗糙、带刺还是带毛。马斯克老让Optimus拿鸡蛋，就是因为这个最难。</div>
                            <div class="framework-clue">Tactile Sensing</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">泛化能力</div>
                            <div class="framework-desc">教过的事会做，没教过的就懵了\u2014\u2014这不叫智能。通用人形机器人必须能适应新环境，不用预训练就能解决新问题，离这个目标还很远。</div>
                            <div class="framework-clue">Generalization</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">训练数据</div>
                            <div class="framework-desc">大语言模型的语料在网上海量存在，但机器人需要物理环境训练，不可能让它拿1000亿次鸡蛋。两大流派：英伟达的虚拟仿真训练 vs 特斯拉的真实工厂实训。</div>
                            <div class="framework-clue">Data Scarcity</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">商业化</div>
                            <div class="framework-desc">技术好不等于能赚钱。波士顿动力是反面教材\u2014\u2014东西真好，但也真不赚钱。成本压不下来，产品就只能待在实验室。谁先跑通\u201c技术\u2192量产\u2192盈利\u201d闭环，谁就赢。</div>
                            <div class="framework-clue">Commercialization</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''

new_page9 = '''        <!-- 第9页：社会影响与制度回应 -->
        <section>
            <div class="slide-shell theme-dark">
                <div class="deco-grid" style="top: 62px; right: 52px;"></div>
                <div class="content-wrap">
                    <div class="eyebrow light">Social Impact</div>
                    <h2 class="slide-title light">机器人来了，社会准备好了吗？</h2>
                    <p class="slide-lead light">Figure AI说未来4-5年可能有10万级工厂机器人订单。大量岗位可能被替代。面对这个共同挑战，中西的制度给出了不同的答案。</p>

                    <div class="framework-stack">
                        <div class="framework-row">
                            <div class="framework-label">就业冲击</div>
                            <div class="framework-desc">中国：政策引导产业升级与就业转型并行，\u201c机器换人\u201d同时配套再就业培训和社会保障。西方：市场自发调节为主，\u201c铁锈地带\u201d等产业空心化问题突出，转型阵痛明显。</div>
                            <div class="framework-clue">Employment</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">教育转型</div>
                            <div class="framework-desc">中国：国家推动新工科建设和职业教育改革，定向培养机器人、AI产业人才。西方：高校自主调整方向，市场化培训体系灵活但覆盖面有限。</div>
                            <div class="framework-clue">Education</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">技术伦理</div>
                            <div class="framework-desc">中国：政府主导制定AI和机器人伦理规范，自上而下推进标准化。西方：企业自律+行业组织自下而上形成共识，标准制定周期较长。</div>
                            <div class="framework-clue">Ethics</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">社会保障</div>
                            <div class="framework-desc">中国：社保体系持续完善，灵活就业纳入保障范围，兜底能力不断增强。西方：社保体系成熟但面临老龄化财政压力，改革阻力大。</div>
                            <div class="framework-clue">Social Security</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">产业安全</div>
                            <div class="framework-desc">中国：核心技术自主可控作为国家战略，减速器等\u201c卡脖子\u201d环节重点攻关。西方：全球化分工为主，近年开始\u201c友岸外包\u201d和供应链回流。</div>
                            <div class="framework-clue">Industrial Security</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''

content = content.replace(old_page9, new_page9)

# ============================================================
# Page 10: 制度自信与改进空间 - 扩充制度自信面板
# ============================================================

# 更新制度自信面板的描述
content = content.replace(
    '中国用四十年走完了西方半个世纪的路，这种集中力量办大事的能力，在全球范围内几乎没有第二个国家能复制。',
    '中国用四十年走完了西方半个世纪的路，并在人形机器人赛道上实现领跑（出货占全球80-90%）。这种集中力量办大事的制度效率，全球没有第二个国家能复制。'
)

# 更新制度自信的标签
content = content.replace(
    '<span class="metric-pill">政策精准</span>\n                                    <span class="metric-pill">规模优势</span>\n                                    <span class="metric-pill">速度惊人</span>',
    '<span class="metric-pill">政策精准</span>\n                                    <span class="metric-pill">系统整合</span>\n                                    <span class="metric-pill">前瞻布局</span>'
)

# 更新制度自信的列表项 - 第3条
content = content.replace(
    '供应链优势让中国企业能把成本压到极致\u2014\u2014宇树的机器人价格只有波士顿动力的零头。',
    '不只追求技术领先，同步推动就业转型、教育改革、社保完善\u2014\u2014产业发展与社会治理并重。'
)

# ============================================================
# Page 11: 结论 - 突出制度视角
# ============================================================

content = content.replace(
    '<h3>发展模式不同</h3>\n                            <p>中国靠产业政策+规模市场快速追赶，西方靠基础研究+技术壁垒维持先发。两种路径都有成功案例，也都有各自的局限。</p>',
    '<h3>制度模式决定发展路径</h3>\n                            <p>中国靠举国体制+产业政策实现快速追赶，西方靠基础研究+市场竞争维持先发。机器人产业的竞争，本质上是两种制度模式的竞争。</p>'
)

content = content.replace(
    '<h3>商业化路径不同</h3>\n                            <p>美国从算法泛化突破，走通用路线；中国用供应链优势压低成本，挖掘更多应用场景。谁先跑出商业闭环，谁就能获得持续迭代的燃料。</p>',
    '<h3>制度优势正在转化为产业竞争力</h3>\n                            <p>40年从零到全球第一，人形机器人出货占全球80-90%。这不是偶然，而是制度优势\u2014\u2014政策引导、供应链整合、规模市场\u2014\u2014在产业领域的集中体现。</p>'
)

content = content.replace(
    '<h3>未来竞争的关键</h3>\n                            <p>人形机器人是中西几乎同时起跑的新赛道。中国的优势在于规模和成本，短板在于核心部件和原始创新。补上短板，就是从\u201c追赶者\u201d变成\u201c引领者\u201d的关键一步。</p>',
    '<h3>自信与改进并重</h3>\n                            <p>真正的制度自信不是回避短板。高端核心部件、原始创新能力、社会转型配套\u2014\u2014这些改进空间恰恰说明我们的制度有自我完善的能力和空间。</p>'
)

# 结论金句
content = content.replace(
    '中国机器人产业的崛起，不只是一个技术追赶的故事，更是一个制度优势如何转化为产业竞争力的生动案例。我们有理由自信，也有空间进步。',
    '中国机器人产业的崛起，是一个制度优势如何转化为产业竞争力的生动案例。从产业政策到供应链整合，从规模市场到社会治理，中国走出了一条独特的发展道路。我们有理由自信，也有空间进步。'
)

# ============================================================
# Page 12: 参考文献 - 补充来源
# ============================================================

old_refs = '''                            <li>Boston Dynamics / Tesla / Unitree 官方发布资料</li>'''
new_refs = '''                            <li>Boston Dynamics / Tesla / Unitree / AgiBot 官方发布资料</li>
                            <li>Forbes, &ldquo;China Dominates Global Humanoid Robot Shipments&rdquo;, 2026</li>
                            <li>Teslarati, &ldquo;Tesla Optimus Gen 3 Mass Production&rdquo;, 2026</li>'''
content = content.replace(old_refs, new_refs)

# ============================================================
# Write the updated file
# ============================================================

with open(r'index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("=" * 60)
print("All updates applied successfully!")
print(f"File size: {len(content)} characters")
print("=" * 60)

# Verify key changes
checks = [
    ("Page 2 title", "机器人之争，本质是制度之争"),
    ("Page 3 title", "比较中西，不是比产品，而是比制度逻辑"),
    ("Page 3 社会治理", "社会治理"),
    ("Page 5 new row", "社会治理"),
    ("Page 6 title", "政策驱动下的追赶奇迹"),
    ("Page 6 new card", "量产：规模化时代到来"),
    ("Page 7 title", "产业政策的力量"),
    ("Page 8 title", "市场机制的双刃剑"),
    ("Page 9 new", "机器人来了，社会准备好了吗"),
    ("Page 9 就业", "就业冲击"),
    ("Page 10 update", "出货占全球80-90%"),
    ("Page 11 结论1", "制度模式决定发展路径"),
    ("Page 11 结论2", "制度优势正在转化为产业竞争力"),
    ("Page 12 refs", "Forbes"),
]

all_ok = True
for name, text in checks:
    if text in content:
        print(f"  ✅ {name}")
    else:
        print(f"  ❌ {name} - NOT FOUND!")
        all_ok = False

if all_ok:
    print("\n🎉 All 14 checks passed!")
else:
    print("\n⚠️ Some checks failed, please review.")
