# -*- coding: utf-8 -*-
"""V2重建：统一暖纸色 + 精简文字（大数字+短句风格）"""

with open(r'index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 保留从开头到 </head> 的所有CSS（包括用户的封面修改）
head_end = content.find('</head>')
css_section = content[:head_end]

# 提取封面页（用户自己改过的，完整保留）
cover_start = content.find('<!-- ==================== 第1页：封面 ====================')
cover_end = content.find('<!-- ==================== 第2页：引入 ====================')
cover_section = content[cover_start:cover_end].strip()

# === CSS补丁：统一所有主题为暖纸色 ===
css_patch = """
        /* === V2 PATCH: 统一所有主题为暖纸色 === */
        .theme-dark,
        .theme-ink,
        .theme-cool {
            background:
                radial-gradient(circle at top right, rgba(224, 96, 44, 0.06), transparent 28%),
                linear-gradient(180deg, #f5f1ea 0%, #f0ebe2 100%) !important;
        }

        /* 去掉暗色主题的白色文字覆盖 */
        .theme-dark .slide-title,
        .theme-dark .slide-lead,
        .theme-dark .eyebrow,
        .theme-ink .slide-title,
        .theme-ink .slide-lead,
        .theme-ink .eyebrow,
        .theme-cool .slide-title,
        .theme-cool .slide-lead,
        .theme-cool .eyebrow {
            color: inherit !important;
            text-shadow: none !important;
        }

        .theme-dark .eyebrow,
        .theme-ink .eyebrow {
            color: var(--accent) !important;
        }

        .theme-dark .eyebrow::before,
        .theme-ink .eyebrow::before {
            background: var(--accent) !important;
        }

        /* 暗色主题上的框架行改为暖色卡片 */
        .theme-dark .framework-row,
        .theme-ink .framework-row {
            background: var(--card) !important;
            border: 1px solid var(--line) !important;
        }

        .theme-dark .framework-label,
        .theme-ink .framework-label {
            color: var(--accent) !important;
        }

        .theme-dark .framework-desc,
        .theme-ink .framework-desc {
            color: var(--text-body) !important;
        }

        .theme-dark .framework-clue,
        .theme-ink .framework-clue {
            color: var(--text-muted) !important;
        }

        /* strip-card 也统一 */
        .theme-dark .strip-card,
        .theme-ink .strip-card {
            background: var(--card) !important;
            border: 1px solid var(--line) !important;
        }

        .theme-dark .strip-kicker,
        .theme-ink .strip-kicker {
            color: var(--accent) !important;
        }

        .theme-dark .strip-title,
        .theme-ink .strip-title,
        .theme-dark .strip-body,
        .theme-ink .strip-body {
            color: var(--text-body) !important;
        }

        /* value-card */
        .theme-dark .value-card,
        .theme-ink .value-card {
            background: var(--card) !important;
            border: 1px solid var(--line) !important;
        }

        .theme-dark .value-index,
        .theme-ink .value-index {
            color: var(--accent-soft) !important;
        }

        .theme-dark .value-card h3,
        .theme-ink .value-card h3 {
            color: var(--text) !important;
        }

        .theme-dark .value-card p,
        .theme-ink .value-card p {
            color: var(--text-body) !important;
        }

        /* case-prism */
        .theme-dark .case-prism,
        .theme-ink .case-prism,
        .theme-cool .case-prism {
            background: rgba(224, 96, 44, 0.06) !important;
            border: 1px solid rgba(224, 96, 44, 0.15) !important;
        }

        .theme-dark .case-prism .core,
        .theme-ink .case-prism .core,
        .theme-cool .case-prism .core {
            color: var(--text) !important;
        }

        .theme-dark .case-prism .foot,
        .theme-ink .case-prism .foot,
        .theme-cool .case-prism .foot,
        .theme-dark .case-prism .small,
        .theme-ink .case-prism .small,
        .theme-cool .case-prism .small {
            color: var(--text-muted) !important;
        }

        /* case-card */
        .theme-dark .case-card,
        .theme-ink .case-card,
        .theme-cool .case-card {
            background: var(--card) !important;
            border: 1px solid var(--line) !important;
        }

        .theme-dark .case-card .num,
        .theme-ink .case-card .num,
        .theme-cool .case-card .num {
            color: var(--accent-soft) !important;
        }

        .theme-dark .case-card h3,
        .theme-ink .case-card h3,
        .theme-cool .case-card h3 {
            color: var(--text) !important;
        }

        .theme-dark .case-card p,
        .theme-ink .case-card p,
        .theme-cool .case-card p {
            color: var(--text-body) !important;
        }

        /* summary-statement */
        .theme-dark .summary-statement,
        .theme-ink .summary-statement {
            background: rgba(224, 96, 44, 0.06) !important;
            border-left-color: var(--accent) !important;
        }

        .theme-dark .summary-statement .kicker,
        .theme-ink .summary-statement .kicker {
            color: var(--accent) !important;
        }

        .theme-dark .summary-statement .text,
        .theme-ink .summary-statement .text {
            color: var(--text) !important;
        }

        /* 大数字卡片样式 */
        .big-num-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-top: 28px;
        }

        .big-num-card {
            background: var(--card);
            border: 1px solid var(--line);
            border-radius: 22px;
            padding: 32px 28px;
            text-align: center;
        }

        .big-num {
            font-size: 2.8em;
            font-weight: 900;
            color: var(--accent);
            line-height: 1.1;
            margin: 0;
        }

        .big-num-label {
            font-size: 0.7em;
            color: var(--text-muted);
            margin: 8px 0 0;
            font-weight: 400;
        }

        /* 纯文字大字页 */
        .hero-question {
            font-size: 2.6em;
            font-weight: 900;
            color: var(--text);
            line-height: 1.3;
            margin: 80px 0 24px;
        }

        .hero-answer {
            font-size: 1.1em;
            color: var(--accent);
            font-weight: 500;
            margin: 0;
        }

        /* 精简框架行 */
        .compact-row {
            display: grid;
            grid-template-columns: 120px 1fr 8px 1fr;
            gap: 12px;
            align-items: center;
            padding: 16px 20px;
            background: var(--card);
            border: 1px solid var(--line);
            border-radius: 16px;
            margin-bottom: 10px;
        }

        .compact-label {
            font-weight: 700;
            color: var(--accent);
            font-size: 0.78em;
        }

        .compact-val {
            font-size: 0.72em;
            color: var(--text-body);
            line-height: 1.6;
        }

        .compact-vs {
            color: var(--text-muted);
            font-size: 0.65em;
            text-align: center;
        }

        /* 结尾页统一暖色 */
        .ending-card {
            padding: 28px 32px;
            border-radius: 22px;
            background: var(--card);
            border: 1px solid var(--line);
        }

        .ending-card p.label {
            margin: 0 0 6px;
            font-size: 0.56em;
            letter-spacing: 2.5px;
            text-transform: uppercase;
            color: var(--text-muted);
            font-weight: 700;
        }

        @media (max-width: 1000px) {
            .big-num-grid { grid-template-columns: 1fr 1fr; }
            .compact-row { grid-template-columns: 1fr; }
            .hero-question { font-size: 1.8em; }
        }
"""

# 在 </style> 前插入补丁
css_section = css_section.replace('    </style>', css_patch + '\n    </style>')

# === 新的body内容（精简版，保留用户封面） ===
body = '''</head>

<body>
<div class="reveal">
    <div class="slides">

        ''' + cover_section + '''

        <!-- ==================== 第2页：引入（大数字版） ==================== -->
        <section>
            <div class="slide-shell theme-paper">
                <div class="content-wrap narrow">
                    <div class="eyebrow">Introduction</div>
                    <h2 class="slide-title">机器人，真的要来了</h2>
                    <p class="slide-lead">你可能觉得机器人蠢蠢笨笨的，但在资本市场上，这是万亿级赛道，没有人敢缺席。</p>

                    <div class="big-num-grid">
                        <div class="big-num-card">
                            <p class="big-num">286亿</p>
                            <p class="big-num-label">2024年国内融资额，同比翻倍</p>
                        </div>
                        <div class="big-num-card">
                            <p class="big-num">$395亿</p>
                            <p class="big-num-label">Figure AI估值，成立不到3年</p>
                        </div>
                        <div class="big-num-card">
                            <p class="big-num">80-90%</p>
                            <p class="big-num-label">中国人形机器人出货占全球份额</p>
                        </div>
                        <div class="big-num-card">
                            <p class="big-num">40年</p>
                            <p class="big-num-label">从零到全球第一的追赶速度</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第3页：科普（视频占位页） ==================== -->
        <section>
            <div class="slide-shell theme-paper">
                <div class="content-wrap" style="text-align: center;">
                    <div class="eyebrow" style="justify-content: center;">Overview</div>
                    <h2 class="slide-title" style="text-align: center;">机器人到底发展到什么程度了？</h2>

                    <div style="margin-top: 40px; padding: 60px 40px; border-radius: 28px; background: var(--card); border: 2px dashed var(--line); text-align: center;">
                        <p style="color: var(--text-muted); font-size: 0.9em; margin: 0;">🎬 视频展示区（待嵌入宇树G1机器人动画）</p>
                        <p style="color: var(--text-muted); font-size: 0.7em; margin: 12px 0 0; opacity: 0.6;">images/unitree_g1_running.mp4</p>
                    </div>

                    <div class="case-strip" style="margin-top: 28px;">
                        <article class="strip-card">
                            <div class="strip-kicker">工业机器人</div>
                            <p class="strip-title">工厂里的主力军</p>
                        </article>
                        <article class="strip-card">
                            <div class="strip-kicker">服务机器人</div>
                            <p class="strip-title">已经走进生活</p>
                        </article>
                        <article class="strip-card">
                            <div class="strip-kicker">人形机器人</div>
                            <p class="strip-title">下一个风口</p>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第4页：技术难点 ==================== -->
        <section>
            <div class="slide-shell theme-dark">
                <div class="content-wrap">
                    <div class="eyebrow">Tech Challenges</div>
                    <h2 class="slide-title">最难的不是下棋，是拿鸡蛋</h2>
                    <p class="slide-lead">莫拉维克悖论：人觉得最简单的事，对机器人最难。</p>

                    <div class="framework-stack">
                        <div class="framework-row">
                            <div class="framework-label">运动本能</div>
                            <div class="framework-desc">训练机器人走路的耗能是婴儿的180万倍</div>
                            <div class="framework-clue">Moravec's Paradox</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">感知触觉</div>
                            <div class="framework-desc">拿鸡蛋不碎——马斯克的终极测试</div>
                            <div class="framework-clue">Tactile Sensing</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">泛化能力</div>
                            <div class="framework-desc">教过的会做，没教过的就懵——这不叫智能</div>
                            <div class="framework-clue">Generalization</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">训练数据</div>
                            <div class="framework-desc">不可能让机器人拿1000亿次鸡蛋</div>
                            <div class="framework-clue">Data Scarcity</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第5页：核心提问（纯大字页） ==================== -->
        <section>
            <div class="slide-shell theme-paper">
                <div class="content-wrap narrow" style="display: flex; flex-direction: column; justify-content: center; min-height: 70vh;">
                    <p class="hero-question">这么难的事，<br>为什么中国40年就追上了？</p>
                    <p class="hero-answer">答案不在某一家企业，而在制度。</p>
                </div>
            </div>
        </section>

        <!-- ==================== 第6页：五维框架（精简版） ==================== -->
        <section>
            <div class="slide-shell theme-dark">
                <div class="content-wrap">
                    <div class="eyebrow">Framework</div>
                    <h2 class="slide-title">五个维度看制度差异</h2>

                    <div style="margin-top: 24px;">
                        <div class="compact-row">
                            <div class="compact-label">产业政策</div>
                            <div class="compact-val">国家定方向，资源集中</div>
                            <div class="compact-vs">vs</div>
                            <div class="compact-val">市场自己跑，企业自主探索</div>
                        </div>
                        <div class="compact-row">
                            <div class="compact-label">技术路线</div>
                            <div class="compact-val">引进→消化→再创新</div>
                            <div class="compact-vs">vs</div>
                            <div class="compact-val">从零原创，数十年积累</div>
                        </div>
                        <div class="compact-row">
                            <div class="compact-label">市场策略</div>
                            <div class="compact-val">性价比+铺量抢市场</div>
                            <div class="compact-vs">vs</div>
                            <div class="compact-val">技术壁垒+品牌溢价</div>
                        </div>
                        <div class="compact-row">
                            <div class="compact-label">供应链</div>
                            <div class="compact-val">全产业链自主可控</div>
                            <div class="compact-vs">vs</div>
                            <div class="compact-val">全球化分工，控制核心环节</div>
                        </div>
                        <div class="compact-row">
                            <div class="compact-label">社会治理</div>
                            <div class="compact-val">政策主动引导转型</div>
                            <div class="compact-vs">vs</div>
                            <div class="compact-val">市场自发调节</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第7页：两种路径 ==================== -->
        <section>
            <div class="slide-shell theme-paper">
                <div class="content-wrap">
                    <div class="eyebrow">Core Logics</div>
                    <h2 class="slide-title">两种制度逻辑</h2>

                    <div class="logic-grid">
                        <article class="logic-panel china">
                            <div>
                                <div class="logic-tag">China Path</div>
                                <h3>政策驱动 → 规模应用 → 反哺迭代</h3>
                                <div class="logic-metrics">
                                    <span class="metric-pill">28%→57%</span>
                                    <span class="metric-pill">9.9万元</span>
                                    <span class="metric-pill">80-90%份额</span>
                                </div>
                            </div>
                        </article>
                        <article class="logic-panel west">
                            <div>
                                <div class="logic-tag">Western Path</div>
                                <h3>基础研究 → 技术原创 → 品牌壁垒</h3>
                                <div class="logic-metrics">
                                    <span class="metric-pill">减速器垄断</span>
                                    <span class="metric-pill">达芬奇2500万</span>
                                    <span class="metric-pill">波士顿动力被踢</span>
                                </div>
                            </div>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第8页：时间线 ==================== -->
        <section>
            <div class="slide-shell theme-paper">
                <div class="content-wrap">
                    <div class="eyebrow">Timeline</div>
                    <h2 class="slide-title">四十年追赶奇迹</h2>

                    <div class="case-layout">
                        <article class="case-prism">
                            <div class="small">Core Data</div>
                            <p class="core">2024年新增安装<strong>29.5万台</strong>，占全球<strong>54%</strong>，密度<strong>470台/万人</strong></p>
                        </article>

                        <div class="case-grid">
                            <article class="case-card">
                                <div class="num">82</div>
                                <h3>起步</h3>
                                <p>中国第一台工业机器人样机</p>
                            </article>
                            <article class="case-card">
                                <div class="num">13</div>
                                <h3>超越</h3>
                                <p>全球最大市场，但国产占28%</p>
                            </article>
                            <article class="case-card">
                                <div class="num">15</div>
                                <h3>加速</h3>
                                <p>制造2025出台，制度力量显现</p>
                            </article>
                            <article class="case-card">
                                <div class="num">24</div>
                                <h3>爆发</h3>
                                <p>人形机器人元年，融资286亿</p>
                            </article>
                            <article class="case-card">
                                <div class="num">26</div>
                                <h3>量产</h3>
                                <p>智元万台下线，宇树IPO</p>
                            </article>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第9页：案例一 ==================== -->
        <section>
            <div class="slide-shell theme-dark">
                <div class="content-wrap">
                    <div class="eyebrow">Case Study 1</div>
                    <h2 class="slide-title">产业政策的力量</h2>

                    <div class="value-grid">
                        <article class="value-card">
                            <div class="value-index">01</div>
                            <div>
                                <h3>库卡收购</h3>
                                <p>发展中国家企业收购发达国家"国家冠军"</p>
                            </div>
                        </article>
                        <article class="value-card">
                            <div class="value-index">02</div>
                            <div>
                                <h3>达芬奇围攻</h3>
                                <p>国产替代从不可能到正在发生</p>
                            </div>
                        </article>
                        <article class="value-card">
                            <div class="value-index">03</div>
                            <div>
                                <h3>十年翻倍</h3>
                                <p>28%→57%，制度效率的量化证明</p>
                            </div>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第10页：案例二 ==================== -->
        <section>
            <div class="slide-shell theme-paper">
                <div class="content-wrap">
                    <div class="eyebrow">Case Study 2</div>
                    <h2 class="slide-title">市场机制的双刃剑</h2>
                    <p class="slide-lead">同样的赛道，不同的命运。</p>

                    <div class="case-grid" style="grid-template-columns: repeat(2, 1fr);">
                        <article class="case-card">
                            <div class="num">01</div>
                            <h3>波士顿动力</h3>
                            <p>技术最强，但被踢了三次</p>
                        </article>
                        <article class="case-card">
                            <div class="num">02</div>
                            <h3>特斯拉Optimus</h3>
                            <p>个人英雄主义，能复制吗？</p>
                        </article>
                        <article class="case-card">
                            <div class="num">03</div>
                            <h3>宇树科技</h3>
                            <p>9.9万，连续盈利，递交IPO</p>
                        </article>
                        <article class="case-card">
                            <div class="num">04</div>
                            <h3>智元机器人</h3>
                            <p>万台下线，开源百万数据集</p>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第11页：数据对比 ==================== -->
        <section>
            <div class="slide-shell theme-paper">
                <div class="content-wrap">
                    <div class="eyebrow">Data Comparison</div>
                    <h2 class="slide-title">五个维度的制度差异</h2>

                    <div class="matrix-wrap">
                        <table class="matrix-table">
                            <thead>
                                <tr><th>维度</th><th>中国</th><th>西方</th></tr>
                            </thead>
                            <tbody>
                                <tr><td>产业政策</td><td>国家战略明确写入政策文件</td><td>企业主导，政府提供研究资助</td></tr>
                                <tr><td>技术来源</td><td>专利占全球2/3，高端质量有差距</td><td>核心零部件技术主导数十年</td></tr>
                                <tr><td>市场策略</td><td>性价比+规模效应</td><td>技术壁垒+品牌溢价</td></tr>
                                <tr><td>供应链</td><td>国产化率超70%，高端减速器仍依赖日本</td><td>控制核心环节</td></tr>
                                <tr><td>社会治理</td><td>"机器换人"配套再就业保障</td><td>市场调节，"铁锈地带"问题突出</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第12页：社会影响 ==================== -->
        <section>
            <div class="slide-shell theme-dark">
                <div class="content-wrap">
                    <div class="eyebrow">Social Impact</div>
                    <h2 class="slide-title">机器人来了，社会准备好了吗？</h2>

                    <div class="framework-stack">
                        <div class="framework-row">
                            <div class="framework-label">就业</div>
                            <div class="framework-desc">中国：产业升级与再就业并行　｜　西方：市场调节，"铁锈地带"</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">教育</div>
                            <div class="framework-desc">中国：新工科+职教改革定向培养　｜　西方：高校自主调整</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">伦理</div>
                            <div class="framework-desc">中国：政府主导制定规范　｜　西方：行业自律，周期较长</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">社保</div>
                            <div class="framework-desc">中国：灵活就业纳入保障　｜　西方：成熟但面临老龄化压力</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">安全</div>
                            <div class="framework-desc">中国：核心技术自主可控　｜　西方："友岸外包"回流</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第13页：制度自信 ==================== -->
        <section>
            <div class="slide-shell theme-paper">
                <div class="content-wrap">
                    <div class="eyebrow">Assessment</div>
                    <h2 class="slide-title">制度自信与改进空间</h2>

                    <div class="logic-grid">
                        <article class="logic-panel china">
                            <div>
                                <div class="logic-tag">制度自信</div>
                                <h3>举国体制的追赶效率</h3>
                                <div class="logic-metrics">
                                    <span class="metric-pill">40年从零到第一</span>
                                    <span class="metric-pill">市占率翻倍</span>
                                    <span class="metric-pill">社会治理并重</span>
                                </div>
                            </div>
                        </article>
                        <article class="logic-panel west">
                            <div>
                                <div class="logic-tag">改进空间</div>
                                <h3>核心技术与基础研究</h3>
                                <div class="logic-metrics">
                                    <span class="metric-pill">高端减速器依赖日本</span>
                                    <span class="metric-pill">原创专利质量</span>
                                    <span class="metric-pill">长期研究生态</span>
                                </div>
                            </div>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第14页：未来展望 ==================== -->
        <section>
            <div class="slide-shell theme-dark">
                <div class="content-wrap">
                    <div class="eyebrow">Future Outlook</div>
                    <h2 class="slide-title">机器人的下一个十年</h2>

                    <div class="case-strip">
                        <article class="strip-card">
                            <div class="strip-kicker">2026-2027</div>
                            <p class="strip-title">工厂规模化部署</p>
                        </article>
                        <article class="strip-card">
                            <div class="strip-kicker">2027-2030</div>
                            <p class="strip-title">场景大幅拓展</p>
                        </article>
                        <article class="strip-card">
                            <div class="strip-kicker">2030+</div>
                            <p class="strip-title">走进千家万户？</p>
                        </article>
                    </div>

                    <div class="summary-statement" style="margin-top: 24px;">
                        <div class="kicker">关键竞争</div>
                        <div class="text"><strong>制造规模</strong>（中国优势）vs <strong>认知智能</strong>（美国优势），谁是决定性因素？</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第15页：结论 ==================== -->
        <section>
            <div class="slide-shell theme-paper">
                <div class="content-wrap">
                    <div class="eyebrow">Conclusion</div>
                    <h2 class="slide-title">两种制度，两条路径</h2>

                    <div class="closing-stack">
                        <article class="closing-card">
                            <div class="closing-mark">1</div>
                            <h3>制度模式决定发展路径</h3>
                        </article>
                        <article class="closing-card">
                            <div class="closing-mark">2</div>
                            <h3>制度优势正在转化为产业竞争力</h3>
                        </article>
                        <article class="closing-card">
                            <div class="closing-mark">3</div>
                            <h3>自信与改进并重</h3>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第16页：结尾 ==================== -->
        <section>
            <div class="slide-shell theme-paper">
                <div class="content-wrap" style="text-align: center;">
                    <div class="eyebrow" style="justify-content: center;">References & Discussion</div>
                    <h2 style="margin: 0; font-size: 2.4em; font-weight: 900; color: var(--text);">谢谢</h2>
                    <p style="margin: 8px 0 24px; font-size: 0.66em; letter-spacing: 7px; text-transform: uppercase; color: var(--text-muted);">Thank You</p>

                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; text-align: left; max-width: 1100px; margin: 0 auto;">
                        <div class="ending-card">
                            <p class="label">参考文献</p>
                            <ul style="margin: 0; padding: 0 0 0 18px; font-size: 0.58em; line-height: 1.9; color: var(--text-body);">
                                <li>IFR, <em>World Robotics 2025 Report</em></li>
                                <li>中国机器人产业联盟, 2024年产业发展报告</li>
                                <li>国务院,《中国制造2025》/ 十四五机器人规划</li>
                                <li>WIPO, 全球机器人领域专利数据</li>
                                <li>Boston Dynamics / Tesla / Unitree / AgiBot</li>
                                <li>Forbes & Teslarati, 2026 Reports</li>
                            </ul>
                        </div>
                        <div class="ending-card">
                            <p class="label">思考与讨论</p>
                            <ul style="margin: 0; padding: 0 0 0 18px; font-size: 0.62em; line-height: 2; color: var(--text-body);">
                                <li>机器人大规模替代工人，社保准备好了吗？</li>
                                <li>中国需不需要自己的"波士顿动力"？</li>
                                <li>人形机器人走进家庭还要多久？</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>

    </div>
    <div class="page-number-overlay" id="pageNumberOverlay" aria-hidden="true">
        <span class="page-number-current" id="pageNumberCurrent">1</span>
        <span class="page-number-divider">/</span>
        <span class="page-number-total" id="pageNumberTotal">16</span>
    </div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.js"></script>
<script>
    Reveal.initialize({
        hash: true,
        transition: "slide",
        transitionSpeed: "default",
        slideNumber: false,
        controls: true,
        controlsLayout: "edges",
        progress: true,
        center: false,
        keyboard: true,
        overview: true,
        width: "100%",
        height: "100%",
        margin: 0,
        minScale: 0.2,
        maxScale: 2.0
    });

    const totalSlides = document.querySelectorAll(".reveal .slides > section").length;
    const pageNumberCurrent = document.getElementById("pageNumberCurrent");
    const pageNumberTotal = document.getElementById("pageNumberTotal");

    const syncSlideNumber = () => {
        const currentIndex = Reveal.getIndices().h + 1;
        if (pageNumberCurrent) pageNumberCurrent.textContent = String(currentIndex);
        if (pageNumberTotal) pageNumberTotal.textContent = String(totalSlides);
    };

    Reveal.on("ready", syncSlideNumber);
    Reveal.on("slidechanged", syncSlideNumber);
    syncSlideNumber();

    document.addEventListener("keydown", (event) => {
        if (event.key === "f" || event.key === "F") {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(() => {});
            } else {
                document.exitFullscreen().catch(() => {});
            }
        }
    });
</script>
</body>
</html>
'''

final_html = css_section + body

with open(r'index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"✅ V2 rebuild complete!")
print(f"   Total size: {len(final_html)} chars")
print(f"   Sections: {final_html.count('<section>')}")
