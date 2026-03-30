# -*- coding: utf-8 -*-
"""重建PPT：16页完整版，保留原CSS设计系统，重写所有slide内容"""

with open(r'index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到 </style> 和 </head> 的位置，保留CSS
head_end = content.find('</head>')
css_section = content[:head_end + len('</head>')]

# 新的body部分（16页）
body = '''
<body>
<div class="reveal">
    <div class="slides">

        <!-- ==================== 第1页：封面 ==================== -->
        <section>
            <div class="slide-shell cover-slide">
                <div class="deco-orb" style="width: 420px; height: 420px; top: -120px; right: -120px; background: radial-gradient(circle, rgba(242, 171, 112, 0.2), transparent 70%);"></div>
                <div class="deco-orb" style="width: 320px; height: 320px; bottom: -80px; left: -60px; background: radial-gradient(circle, rgba(224, 96, 44, 0.13), transparent 70%);"></div>
                <div class="deco-grid" style="top: 60px; left: 42px;"></div>
                <div class="deco-grid" style="bottom: 62px; right: 44px; opacity: 0.12;"></div>

                <div class="content-wrap cover-layout">
                    <div class="cover-copy">
                        <div class="cover-badge">习近平新时代中国特色社会主义思想概论</div>
                        <h1 class="cover-title">机器人产业发展的两种路径<br>中国追赶与西方先发</h1>
                        <p class="cover-sub">从1982年中国第一台工业机器人到2025年人形机器人出货量占全球80-90%，中国用四十年走完了西方半个世纪的路。这场追赶背后，是两种截然不同的制度逻辑。</p>
                        <div class="cover-info">
                            <div>演讲人：张文豪</div>
                            <div>小组成员：XXX（占位符）</div>
                        </div>
                    </div>
                    <div class="cover-visual">
                        <div class="cover-visual-card">
                            <iframe
                        src="https://app.spline.design/file/b5699b21-c899-49e4-93ea-c50ffc534501?view=preview"
                                title="Spline robot scene"
                                loading="eager"
                                allow="fullscreen"
                            ></iframe>
                            <div class="cover-visual-fade"></div>
                            <div class="cover-visual-mask"></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第2页：引入 ==================== -->
        <section>
            <div class="slide-shell theme-paper">
                <div class="deco-orb" style="width: 460px; height: 460px; top: -180px; right: -160px; background: radial-gradient(circle, rgba(224, 96, 44, 0.08), transparent 70%);"></div>
                <div class="content-wrap narrow">
                    <div class="eyebrow">Introduction</div>
                    <h2 class="slide-title">机器人，真的要来了</h2>
                    <p class="slide-lead">你可能经常刷到机器人出洋相的视频，感觉蠢蠢笨笨的，正事啥也不会。但在资本市场上，围绕机器人的争夺已经进入白热化——这不只是一场技术竞赛，更是一场制度之争。</p>

                    <div class="analysis-grid">
                        <article class="analysis-card">
                            <div class="card-kicker">资本狂热</div>
                            <h3 class="card-title">万亿市场正在成形</h3>
                            <p class="card-body">马斯克说人形机器人Optimus未来年收入可能达万亿美元。黄仁勋说机器人的ChatGPT时刻即将到来。国内一级市场融资286亿，比去年翻了一倍。</p>
                        </article>
                        <article class="analysis-card">
                            <div class="card-kicker">巨头涌入</div>
                            <h3 class="card-title">所有人都在下注</h3>
                            <p class="card-body">Figure AI成立不到3年估值395亿美元，微软、英伟达、OpenAI纷纷入局。国内腾讯、阿里、京东、雷军也密集布局。这个赛道没人敢缺席。</p>
                        </article>
                        <article class="analysis-card">
                            <div class="card-kicker">中国速度</div>
                            <h3 class="card-title">40年追完半个世纪</h3>
                            <p class="card-body">从1982年第一台样机到2024年全球装机量第一，2025年人形机器人出货占全球80-90%。日美德加起来还不到我们一半。</p>
                        </article>
                        <article class="analysis-card">
                            <div class="card-kicker">核心问题</div>
                            <h3 class="card-title">为什么中国能做到？</h3>
                            <p class="card-body">同样的技术领域，为什么在不同制度下会走出完全不同的路径？今天我们就来聊一聊，机器人竞争背后的制度逻辑。</p>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第3页：科普（视频占位页） ==================== -->
        <section>
            <div class="slide-shell theme-ink">
                <div class="deco-orb" style="width: 520px; height: 520px; top: -200px; right: -200px; background: radial-gradient(circle, rgba(242, 171, 112, 0.12), transparent 70%);"></div>
                <div class="content-wrap" style="text-align: center;">
                    <div class="eyebrow light" style="justify-content: center;">Overview</div>
                    <h2 class="slide-title light" style="text-align: center;">机器人到底发展到什么程度了？</h2>
                    <p class="slide-lead light" style="text-align: center; margin: 18px auto 0; max-width: 700px;">从工业机械臂到人形机器人，从仓库分拣到手术台，机器人早已不是科幻电影里的概念。</p>
                    <div style="margin-top: 40px; padding: 60px 40px; border-radius: 28px; background: rgba(255,255,255,0.04); border: 2px dashed rgba(255,255,255,0.15); text-align: center;">
                        <p style="color: rgba(255,255,255,0.5); font-size: 0.9em; margin: 0;">🎬 视频展示区（待嵌入宇树G1机器人动画）</p>
                        <p style="color: rgba(255,255,255,0.35); font-size: 0.7em; margin: 12px 0 0;">images/unitree_g1_running.mp4</p>
                    </div>

                    <div class="case-strip" style="margin-top: 28px;">
                        <article class="strip-card">
                            <div class="strip-kicker">工业机器人</div>
                            <p class="strip-title">工厂里的主力军</p>
                            <p class="strip-body">仓储物流拣货装箱，汽车焊接喷涂，几块钱包邮的背后就是机器人在降本增效。</p>
                        </article>
                        <article class="strip-card">
                            <div class="strip-kicker">服务机器人</div>
                            <p class="strip-title">已经走进生活</p>
                            <p class="strip-body">扫地机器人、酒店送餐、手术辅助……这些大家已经司空见惯了。</p>
                        </article>
                        <article class="strip-card">
                            <div class="strip-kicker">人形机器人</div>
                            <p class="strip-title">下一个风口</p>
                            <p class="strip-body">具身智能——像人一样感知、决策、行动。这才是被推到风口浪尖的新赛道。</p>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第4页：技术难点（莫拉维克悖论） ==================== -->
        <section>
            <div class="slide-shell theme-dark">
                <div class="deco-grid" style="top: 62px; right: 52px;"></div>
                <div class="content-wrap">
                    <div class="eyebrow light">Tech Challenges</div>
                    <h2 class="slide-title light">最难的不是下棋，是拿鸡蛋</h2>
                    <p class="slide-lead light">要理解机器人竞争为什么如此激烈，得先知道这件事有多难。机器人领域有个著名的"莫拉维克悖论"——人觉得最简单的事，对机器人最难。</p>

                    <div class="framework-stack">
                        <div class="framework-row">
                            <div class="framework-label">运动本能</div>
                            <div class="framework-desc">走路、蹲下、单脚跳——我们靠本能0.001焦耳就能完成的动作，机器人需要协调几十个关节电机，训练耗能是婴儿的180万倍。</div>
                            <div class="framework-clue">Moravec's Paradox</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">感知触觉</div>
                            <div class="framework-desc">视觉靠AI已经很强，但触觉是噩梦——拿鸡蛋不碎、感知软硬粗糙。马斯克老让Optimus拿鸡蛋，就是因为这个最难做到。</div>
                            <div class="framework-clue">Tactile Sensing</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">泛化能力</div>
                            <div class="framework-desc">教过的事会做，没教过的就懵——这不叫智能。通用机器人必须能适应新环境、解决新问题，这离目标还很远。</div>
                            <div class="framework-clue">Generalization</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">训练数据</div>
                            <div class="framework-desc">训练ChatGPT有海量网络文本，但你不可能让机器人拿1000亿次鸡蛋。两大流派：英伟达的虚拟仿真 vs 特斯拉的真实工厂实训。</div>
                            <div class="framework-clue">Data Scarcity</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第5页：核心提问——制度之争 ==================== -->
        <section>
            <div class="slide-shell theme-paper">
                <div class="deco-orb" style="width: 460px; height: 460px; top: -180px; right: -160px; background: radial-gradient(circle, rgba(224, 96, 44, 0.08), transparent 70%);"></div>
                <div class="content-wrap narrow">
                    <div class="eyebrow">Core Question</div>
                    <h2 class="slide-title">这么难的事，为什么中国40年就追上了？</h2>
                    <p class="slide-lead">机器人这么难做，那为什么中国能用四十年走完西方半个世纪的路？答案不在某一家企业、某一项技术，而在制度。</p>

                    <div class="statement">机器人竞争的核心不是"谁的产品更酷"，而是<strong>谁的制度更能高效整合政策、资本、技术和市场，推动产业从0到1再到N</strong>。</div>

                    <div class="analysis-grid" style="margin-top: 24px;">
                        <article class="analysis-card">
                            <div class="card-kicker">制度效率</div>
                            <h3 class="card-title">举国体制的追赶速度</h3>
                            <p class="card-body">"中国制造2025"一出台→方向明确→资源集中→国产品牌市占率从28%翻倍到57%。这种效率全球没有第二个国家能复制。</p>
                        </article>
                        <article class="analysis-card">
                            <div class="card-kicker">市场悖论</div>
                            <h3 class="card-title">自由市场不一定能推动产业</h3>
                            <p class="card-body">波士顿动力技术全球最强，却被谷歌→软银→现代汽车踢来踢去。技术好但不赚钱，在纯市场逻辑下就是"没有价值"。</p>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第6页：五维制度框架 ==================== -->
        <section>
            <div class="slide-shell theme-dark">
                <div class="deco-grid" style="top: 62px; right: 52px;"></div>
                <div class="content-wrap">
                    <div class="eyebrow light">Framework</div>
                    <h2 class="slide-title light">五个维度看制度差异</h2>
                    <p class="slide-lead light">把问题拉高一层，比较就不再停留在"谁的机器人更先进"，而是看两种制度模式在五个维度上的根本差异。</p>

                    <div class="framework-stack">
                        <div class="framework-row">
                            <div class="framework-label">产业政策</div>
                            <div class="framework-desc">是靠国家战略集中力量定方向，还是靠市场竞争与企业自主探索。</div>
                            <div class="framework-clue">Policy-driven vs Market-driven</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">技术路线</div>
                            <div class="framework-desc">是引进消化吸收再创新起步，还是从原始创新和长期基础研究起步。</div>
                            <div class="framework-clue">Catch-up vs First-mover</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">市场策略</div>
                            <div class="framework-desc">是以性价比和规模效应抢占市场，还是以技术壁垒和品牌溢价维持优势。</div>
                            <div class="framework-clue">Cost advantage vs Tech moat</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">供应链体系</div>
                            <div class="framework-desc">是举国之力构建完整产业链实现自主可控，还是全球化分工中控制核心环节。</div>
                            <div class="framework-clue">Full-chain vs Key-link</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">社会治理</div>
                            <div class="framework-desc">面对机器人替代就业的冲击，是政策主动引导产业升级与转型并行，还是依靠市场自发调节。</div>
                            <div class="framework-clue">Proactive vs Reactive</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第7页：两种路径核心画像 ==================== -->
        <section>
            <div class="slide-shell theme-cool">
                <div class="deco-orb" style="width: 380px; height: 380px; top: -110px; left: -110px; background: radial-gradient(circle, rgba(112, 128, 148, 0.12), transparent 70%);"></div>
                <div class="content-wrap">
                    <div class="eyebrow">Core Logics</div>
                    <h2 class="slide-title">两种制度逻辑的核心画像</h2>
                    <p class="slide-lead">中国走的是"政策驱动→规模应用→反哺技术迭代"的追赶路径；西方走的是"基础研究→技术原创→品牌与生态壁垒"的先发路径。</p>

                    <div class="logic-grid">
                        <article class="logic-panel china">
                            <div>
                                <div class="logic-tag">China Path</div>
                                <h3>中国路径：举国体制推动产业追赶</h3>
                                <p>从"中国制造2025"到"十四五机器人产业规划"，国家产业政策持续引导资源集中，再依托全球最大制造业市场实现规模化落地和快速迭代。</p>
                                <div class="logic-metrics">
                                    <span class="metric-pill">政策驱动</span>
                                    <span class="metric-pill">规模应用</span>
                                    <span class="metric-pill">供应链碾压</span>
                                </div>
                            </div>
                            <ul class="logic-list">
                                <li><span class="dot"></span><span>国产品牌市占率从2014年约28%提升到2024年的57%，十年翻倍。</span></li>
                                <li><span class="dot"></span><span>宇树、智元等企业凭借供应链优势，将人形机器人价格做到西方的零头。</span></li>
                                <li><span class="dot"></span><span>2025年中国人形机器人出货占全球80-90%，规模化量产时代到来。</span></li>
                            </ul>
                        </article>
                        <article class="logic-panel west">
                            <div>
                                <div class="logic-tag">Western Path</div>
                                <h3>西方路径：技术原创构建长期壁垒</h3>
                                <p>日本发那科、德国库卡、美国波士顿动力——西方企业依靠数十年基础研究积累，在核心零部件和前沿技术上建立了深厚的护城河。</p>
                                <div class="logic-metrics">
                                    <span class="metric-pill">技术原创</span>
                                    <span class="metric-pill">基础研究</span>
                                    <span class="metric-pill">品牌壁垒</span>
                                </div>
                            </div>
                            <ul class="logic-list">
                                <li><span class="dot"></span><span>日本在减速器和伺服电机领域长期占据全球主导地位，技术积累深厚。</span></li>
                                <li><span class="dot"></span><span>德国"工业4.0"将机器人与智能制造深度整合，追求精密与可靠性。</span></li>
                                <li><span class="dot"></span><span>美国在前沿探索上领先（波士顿动力），但产业化路径曲折，商业化困难。</span></li>
                            </ul>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第8页：时间线 ==================== -->
        <section>
            <div class="slide-shell theme-cool">
                <div class="deco-orb" style="width: 420px; height: 420px; bottom: -180px; right: -120px; background: radial-gradient(circle, rgba(224, 96, 44, 0.08), transparent 70%);"></div>
                <div class="content-wrap">
                    <div class="eyebrow">Timeline</div>
                    <h2 class="slide-title">四十年：政策驱动下的追赶奇迹</h2>
                    <p class="slide-lead">1982年中国造出第一台工业机器人样机时，日本发那科已经卖了十几年。但在制度优势的推动下，中国用四十年实现了从追赶到领跑的跨越。</p>

                    <div class="case-layout">
                        <article class="case-prism">
                            <div class="small">Core Data</div>
                            <p class="core">2024年中国新增安装<strong>29.5万台</strong>工业机器人，占全球<strong>54%</strong>。机器人密度达<strong>470台/万人</strong>，超越德国和日本。</p>
                            <p class="foot">国产品牌市占率十年翻倍（28%→57%）。2025年人形机器人出货占全球80-90%。</p>
                        </article>

                        <div class="case-grid">
                            <article class="case-card">
                                <div class="num">82</div>
                                <h3>起步：国家科研立项</h3>
                                <p>中科院沈阳自动化所研制出第一台样机，90年代开始研发喷涂、点焊等专用机器人。</p>
                            </article>
                            <article class="case-card">
                                <div class="num">13</div>
                                <h3>超越：全球最大市场</h3>
                                <p>中国市场超越日本。但此时国产品牌市占率仅28%，市场虽大，用的大部分还是进口的。</p>
                            </article>
                            <article class="case-card">
                                <div class="num">15</div>
                                <h3>加速：制造2025出台</h3>
                                <p>国家产业政策明确方向→资源集中→埃斯顿、汇川等国产品牌快速崛起。制度的力量开始显现。</p>
                            </article>
                            <article class="case-card">
                                <div class="num">24</div>
                                <h3>爆发：人形机器人元年</h3>
                                <p>宇树春晚火出圈，智元、小鹏、小米纷纷入局。一级市场融资翻倍达286亿。</p>
                            </article>
                            <article class="case-card">
                                <div class="num">26</div>
                                <h3>量产：规模化时代到来</h3>
                                <p>智元第1万台下线，宇树递交科创板IPO拟募42亿。佛山建成首条全自动人形机器人产线。</p>
                            </article>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第9页：案例一——产业政策的力量 ==================== -->
        <section>
            <div class="slide-shell theme-ink">
                <div class="content-wrap">
                    <div class="eyebrow light">Case Study 1</div>
                    <h2 class="slide-title light">产业政策的力量：从"买产品"到"买公司"</h2>
                    <p class="slide-lead light">中国在工业机器人领域的追赶，不是某一家企业的单打独斗，而是产业政策引导下的系统性突破。</p>

                    <div class="value-grid">
                        <article class="value-card">
                            <div class="value-index">01</div>
                            <div>
                                <h3>库卡收购案——战略性技术获取</h3>
                                <p>2016年美的收购德国库卡94.55%股权。这不是简单的商业收购，而是产业政策支持下的战略行动。德国的"震惊"恰恰说明中国制度的整合能力——一个发展中国家的企业，能够收购发达国家的"国家冠军"。</p>
                            </div>
                        </article>
                        <article class="value-card">
                            <div class="value-index">02</div>
                            <div>
                                <h3>达芬奇垄断的瓦解——国产替代路径</h3>
                                <p>达芬奇手术机器人一套1500-2500万元，垄断了近20年。在国家"医疗器械自主可控"政策推动下，微创医疗、精锋医疗获批上市，用价格+本地化优势"围攻"达芬奇。这是制度引导下的国产替代。</p>
                            </div>
                        </article>
                        <article class="value-card">
                            <div class="value-index">03</div>
                            <div>
                                <h3>数据背后的制度效率</h3>
                                <p>国产品牌市占率十年翻倍（28%→57%），核心零部件国产化率超70%。日美德加起来装机量不到中国一半。当西方还在争论"政府该不该干预市场"时，中国已经用制度效率证明了答案。</p>
                            </div>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第10页：案例二——市场机制的双刃剑 ==================== -->
        <section>
            <div class="slide-shell theme-paper">
                <div class="deco-orb" style="width: 460px; height: 460px; top: -180px; right: -160px; background: radial-gradient(circle, rgba(224, 96, 44, 0.08), transparent 70%);"></div>
                <div class="content-wrap">
                    <div class="eyebrow">Case Study 2</div>
                    <h2 class="slide-title">市场机制的双刃剑：人形机器人的不同命运</h2>
                    <p class="slide-lead">同样优秀的技术，在不同制度下结局可以截然不同。人形机器人赛道完美展示了市场机制与举国体制的差异。</p>

                    <div class="case-layout">
                        <article class="case-prism">
                            <div class="small">Key Contrast</div>
                            <p class="core">波士顿动力在纯市场机制下<strong>技术最强却活得最惨</strong>，被踢来踢去。宇树在中国制度下<strong>连续盈利并即将IPO</strong>。</p>
                            <p class="foot">这不只是商业逻辑的差异，更是两种制度模式对产业发展的不同影响。</p>
                        </article>

                        <div class="case-grid">
                            <article class="case-card">
                                <div class="num">01</div>
                                <h3>波士顿动力：自由市场的残酷</h3>
                                <p>军方起家→谷歌→软银→现代汽车，技术顶尖但不赚钱就没人要。纯市场逻辑下，"长期主义"很难生存。</p>
                            </article>
                            <article class="case-card">
                                <div class="num">02</div>
                                <h3>特斯拉Optimus：个人英雄主义</h3>
                                <p>Gen3已于2026年1月量产，甚至停产Model S/X转产机器人。成本压到2万美元。但这种依赖个人意志的模式能复制吗？</p>
                            </article>
                            <article class="case-card">
                                <div class="num">03</div>
                                <h3>宇树科技：中国制度的产物</h3>
                                <p>连续盈利，2026年递交科创板IPO拟募42亿。9.9万的人形机器人靠的是整个中国供应链体系和产业政策的支撑。</p>
                            </article>
                            <article class="case-card">
                                <div class="num">04</div>
                                <h3>智元机器人：中国速度的缩影</h3>
                                <p>2025年出货5100+台，2026年3月第1万台下线。开源百万真机数据集，"集全行业之力"的协同是中国独有的制度优势。</p>
                            </article>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第11页：核心数据对比 ==================== -->
        <section>
            <div class="slide-shell theme-paper">
                <div class="content-wrap">
                    <div class="eyebrow">Data Comparison</div>
                    <h2 class="slide-title">用数据说话：五个维度的制度差异</h2>
                    <p class="slide-lead">真正的差异不只是"谁的机器人更多"，而是产业政策、技术路线、市场策略和社会治理上的系统性差别。</p>

                    <div class="matrix-wrap">
                        <table class="matrix-table">
                            <thead>
                                <tr>
                                    <th>维度</th>
                                    <th>中国</th>
                                    <th>西方（美/日/德）</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>产业政策</td>
                                    <td>"中国制造2025"明确将机器人列为十大重点领域，国家战略强力引导。</td>
                                    <td>企业主导技术方向，政府提供基础研究资助（如德国工业4.0）。</td>
                                </tr>
                                <tr>
                                    <td>技术来源</td>
                                    <td>引进消化吸收→原始创新加速。专利占全球2/3，但高端质量有差距。</td>
                                    <td>长期基础研究积累，核心零部件技术主导数十年。</td>
                                </tr>
                                <tr>
                                    <td>市场策略</td>
                                    <td>性价比+规模效应，国产品牌以更低价格抢占市场，逐步向高端渗透。</td>
                                    <td>技术壁垒+品牌溢价，达芬奇手术机器人一台1500-2500万元。</td>
                                </tr>
                                <tr>
                                    <td>供应链</td>
                                    <td>国产化率超70%，但高端减速器仍依赖日本。完整产业链优势明显。</td>
                                    <td>日本垄断高端减速器，全球化分工中控制核心环节。</td>
                                </tr>
                                <tr>
                                    <td>社会治理</td>
                                    <td>制造业升级配套技能培训，"机器换人"同时配套再就业保障。</td>
                                    <td>市场自发调节为主，"铁锈地带"产业空心化问题突出。</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第12页：社会影响与制度回应 ==================== -->
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
                            <div class="framework-desc">中国：政策引导产业升级与就业转型并行，"机器换人"同时配套再就业培训。西方：市场自发调节为主，"铁锈地带"产业空心化问题突出。</div>
                            <div class="framework-clue">Employment</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">教育转型</div>
                            <div class="framework-desc">中国：国家推动新工科建设和职业教育改革，定向培养机器人、AI人才。西方：高校自主调整方向，市场化培训灵活但覆盖面有限。</div>
                            <div class="framework-clue">Education</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">技术伦理</div>
                            <div class="framework-desc">中国：政府主导制定AI和机器人伦理规范，自上而下推进标准化。西方：企业自律+行业组织自下而上形成共识，标准制定周期较长。</div>
                            <div class="framework-clue">Ethics</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">社会保障</div>
                            <div class="framework-desc">中国：社保体系持续完善，灵活就业纳入保障范围，兜底能力增强。西方：社保体系成熟但面临老龄化财政压力，改革阻力大。</div>
                            <div class="framework-clue">Social Security</div>
                        </div>
                        <div class="framework-row">
                            <div class="framework-label">产业安全</div>
                            <div class="framework-desc">中国：核心技术自主可控作为国家战略，减速器等"卡脖子"环节重点攻关。西方：全球化分工为主，近年开始"友岸外包"和供应链回流。</div>
                            <div class="framework-clue">Industrial Security</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第13页：制度自信与改进空间 ==================== -->
        <section>
            <div class="slide-shell theme-cool">
                <div class="deco-orb" style="width: 380px; height: 380px; top: -110px; left: -110px; background: radial-gradient(circle, rgba(112, 128, 148, 0.12), transparent 70%);"></div>
                <div class="content-wrap">
                    <div class="eyebrow">Assessment</div>
                    <h2 class="slide-title">制度自信与改进空间</h2>
                    <p class="slide-lead">真正的制度自信不是回避短板，而是在承认差距的基础上看清优势、持续优化。</p>

                    <div class="logic-grid">
                        <article class="logic-panel china">
                            <div>
                                <div class="logic-tag">制度自信</div>
                                <h3>举国体制的追赶效率</h3>
                                <p>中国用四十年追完西方半个世纪，并在人形机器人赛道上实现领跑（出货占全球80-90%）。这种制度效率全球没有第二家。</p>
                                <div class="logic-metrics">
                                    <span class="metric-pill">政策精准</span>
                                    <span class="metric-pill">系统整合</span>
                                    <span class="metric-pill">前瞻布局</span>
                                </div>
                            </div>
                            <ul class="logic-list">
                                <li><span class="dot"></span><span>"中国制造2025"明确方向后，国产品牌市占率十年翻倍（28%→57%）。</span></li>
                                <li><span class="dot"></span><span>全球最大制造业市场提供了无可比拟的应用场景和数据来源。</span></li>
                                <li><span class="dot"></span><span>不只追求技术领先，同步推动就业转型、教育改革、社保完善——产业发展与社会治理并重。</span></li>
                            </ul>
                        </article>
                        <article class="logic-panel west">
                            <div>
                                <div class="logic-tag">改进空间</div>
                                <h3>核心技术与基础研究的差距</h3>
                                <p>追赶速度再快，也不能忽视那些依然"卡脖子"的环节。正视短板，才能找到下一步突破的方向。</p>
                                <div class="logic-metrics">
                                    <span class="metric-pill">核心部件</span>
                                    <span class="metric-pill">原始创新</span>
                                    <span class="metric-pill">长期研究</span>
                                </div>
                            </div>
                            <ul class="logic-list">
                                <li><span class="dot"></span><span>高端减速器仍依赖日本（哈默纳科、纳博特斯克），高端市场差距明显。</span></li>
                                <li><span class="dot"></span><span>专利数量全球第一（占2/3），但高质量原创性专利比例仍不够。</span></li>
                                <li><span class="dot"></span><span>需要建立容忍"十年不赚钱"前沿探索的基础研究生态。</span></li>
                            </ul>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第14页：未来展望 ==================== -->
        <section>
            <div class="slide-shell theme-ink">
                <div class="deco-orb" style="width: 520px; height: 520px; top: -180px; left: -180px; background: radial-gradient(circle, rgba(242, 171, 112, 0.12), transparent 70%);"></div>
                <div class="content-wrap">
                    <div class="eyebrow light">Future Outlook</div>
                    <h2 class="slide-title light">机器人的下一个十年</h2>
                    <p class="slide-lead light">从实验室到工厂，从工厂到生活。机器人产业正在经历从"能用"到"好用"的关键跨越。</p>

                    <div class="case-strip">
                        <article class="strip-card">
                            <div class="strip-kicker">2026-2027</div>
                            <p class="strip-title">工厂规模化部署</p>
                            <p class="strip-body">特斯拉目标2026年产5-10万台Optimus。智元、宇树批量进入制造业场景，搬运、分拣、质检三大工位率先落地。</p>
                        </article>
                        <article class="strip-card">
                            <div class="strip-kicker">2027-2030</div>
                            <p class="strip-title">场景大幅拓展</p>
                            <p class="strip-body">机器人从工厂走向物流、餐饮、医疗。预计全球人形机器人累计装机超10万台。中国凭供应链优势占据主导地位。</p>
                        </article>
                        <article class="strip-card">
                            <div class="strip-kicker">2030+</div>
                            <p class="strip-title">走进千家万户？</p>
                            <p class="strip-body">马斯克的愿景：每家一台机器人。离这个目标还需泛化能力的重大突破。但从历史看，5-10年可能比我们想象的更快。</p>
                        </article>
                    </div>

                    <div class="summary-statement" style="margin-top: 24px;">
                        <div class="kicker">关键竞争点</div>
                        <div class="text">未来的关键问题是：<strong>制造规模和快速部署</strong>（中国的优势）与<strong>认知智能和软件成熟度</strong>（美国的优势），哪一个会成为行业成熟后的决定性因素？</div>
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
                    <p class="slide-lead">中国和西方在机器人产业上走了两条截然不同的路，但这场竞争远未结束。</p>

                    <div class="closing-stack">
                        <article class="closing-card">
                            <div class="closing-mark">1</div>
                            <h3>制度模式决定发展路径</h3>
                            <p>中国靠举国体制+产业政策实现快速追赶，西方靠基础研究+市场竞争维持先发。机器人产业的竞争，本质上是两种制度模式的竞争。</p>
                        </article>
                        <article class="closing-card">
                            <div class="closing-mark">2</div>
                            <h3>制度优势正在转化为产业竞争力</h3>
                            <p>40年从零到全球第一，人形机器人出货占全球80-90%。这不是偶然，而是政策引导、供应链整合、规模市场共同作用的结果。</p>
                        </article>
                        <article class="closing-card">
                            <div class="closing-mark">3</div>
                            <h3>自信与改进并重</h3>
                            <p>真正的制度自信不是回避短板。高端核心部件、原始创新、社会转型——这些改进空间说明我们的制度有自我完善的能力和空间。</p>
                        </article>
                    </div>

                    <div class="summary-statement">
                        <div class="kicker">Final Statement</div>
                        <div class="text">中国机器人产业的崛起，是一个制度优势如何转化为产业竞争力的生动案例。从产业政策到供应链整合，从规模市场到社会治理，中国走出了一条独特的发展道路。我们有理由自信，也有空间进步。</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 第16页：参考文献 + 思考讨论 + Q&A ==================== -->
        <section>
            <div class="slide-shell theme-dark">
                <div class="deco-orb" style="width: 520px; height: 520px; top: -180px; left: -180px; background: radial-gradient(circle, rgba(242, 171, 112, 0.12), transparent 70%);"></div>
                <div class="deco-grid" style="bottom: 70px; right: 70px; opacity: 0.14;"></div>
                <div class="content-wrap" style="text-align: center;">
                    <div class="eyebrow light" style="justify-content: center;">References &amp; Discussion</div>
                    <h2 style="margin: 0; font-size: 2.2em; font-weight: 900; color: rgba(255,255,255,0.96);">谢谢</h2>
                    <p style="margin: 8px 0 24px; font-size: 0.66em; letter-spacing: 7px; text-transform: uppercase; color: rgba(255,255,255,0.42);">Thank You</p>

                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; text-align: left; max-width: 1100px; margin: 0 auto;">
                        <div style="padding: 24px 28px; border-radius: 22px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.08);">
                            <p style="margin: 0 0 6px; font-size: 0.56em; letter-spacing: 2.5px; text-transform: uppercase; color: rgba(255,255,255,0.48); font-weight: 700;">参考文献</p>
                            <ul style="margin: 0; padding: 0 0 0 18px; font-size: 0.58em; line-height: 1.9; color: rgba(255,255,255,0.7);">
                                <li>IFR, <em>World Robotics 2025 Report</em></li>
                                <li>中国机器人产业联盟, 2024年产业发展报告</li>
                                <li>国务院,《中国制造2025》/ 十四五机器人规划</li>
                                <li>WIPO, 全球机器人领域专利数据</li>
                                <li>Intuitive Surgical, 达芬奇系统官方资料</li>
                                <li>Boston Dynamics / Tesla / Unitree / AgiBot 官方资料</li>
                                <li>Forbes, "China Dominates Humanoid Shipments", 2026</li>
                                <li>Teslarati, "Optimus Gen3 Mass Production", 2026</li>
                            </ul>
                        </div>
                        <div style="padding: 24px 28px; border-radius: 22px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.08);">
                            <p style="margin: 0 0 6px; font-size: 0.56em; letter-spacing: 2.5px; text-transform: uppercase; color: rgba(255,255,255,0.48); font-weight: 700;">思考与讨论</p>
                            <ul style="margin: 0; padding: 0 0 0 18px; font-size: 0.62em; line-height: 2; color: rgba(255,255,255,0.82);">
                                <li>如果机器人真的大规模替代工人，中国的社保体系准备好了吗？</li>
                                <li>波士顿动力"十年不赚钱"的探索模式，中国需不需要？怎么建立？</li>
                                <li>你觉得人形机器人走进家庭还需要多久？最先解决什么问题？</li>
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

# 组合CSS + 新body
final_html = css_section + '\n' + body

with open(r'index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"✅ File rebuilt successfully!")
print(f"   Total size: {len(final_html)} characters")
print(f"   Total sections: {final_html.count('<section>')}")
