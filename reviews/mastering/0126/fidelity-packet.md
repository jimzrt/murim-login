# Fidelity Gate — Chapter 126

Audit the complete assembled English chapter against the Korean source.
Report only genuine source-fidelity defects: wrong action, subject, object,
causality, quantity, mechanism, terminology, ambiguity, joke logic, register,
or physical detail. Check repeated UI labels and counters against how they
behave across the whole scene. Interpret idioms by their function, not by
translating their component words. Do not report optional stylistic rewrites.
Do not invent `current` spans that are absent from the assembled English.
Do not report a glossary-correct rendering as a defect merely because the
baseline used an older synonym.

Return exactly one JSON object and no Markdown fence:

{
  "summary": "brief assessment",
  "findings": [
    {
      "id": "F01",
      "severity": "critical|major|minor",
      "source": "source location",
      "current": "exact uniquely occurring English span",
      "defect": "specific fidelity defect",
      "replacement": "finished replacement only when necessary",
      "rationale": "source-grounded reason",
      "confidence": 0.0
    }
  ]
}

Use an empty findings array when the chapter is faithful. A critical or major
finding blocks promotion; minor findings are recorded for human inspection.

## Korean source

```text
  1|＃126화
  2|
  3|
  4|
  5|나흘 전, 모든 임무를 끝마치고 태원진가로 복귀한 위팽은 자신의 빠른 일 처리를 뼛속 깊이 후회했다.
  6|
  7|‘하루만 늦게 올걸.’
  8|
  9|그러나 이미 늦었다. 하오문의 전서응을 받은 진위경이 눈을 까뒤집고 길길이 날뛰고 있었으니까.
 10|
 11|“이 개 같은 마적 놈들이 감히!”
 12|
 13|“또 무슨 일입니까?”
 14|
 15|“풍양, 적풍단, 항산검문, 내 동생들, 위험! 매우 위험! 당장 출발!”
 16|
 17|“……호위대 소집하겠습니다.”
 18|
 19|모든 장애물을 치워 버린 지금, 진위경의 권위는 절대적이었다. 반 시진이 채 지나기도 전에 두 사람은 오십 명의 정예 호위대와 함께 가문을 나섰고, 쉬지 않고 내달렸다.
 20|
 21|그리고 이틀 후, 말을 갈아타기 위해 들른 하오문 지부에서 새로운 소식을 접했다.
 22|
 23|“뭐라? 풍양이 죽고 적풍단이 궤멸했어?”
 24|
 25|“옛! 본 문이 파악한 바에 의하면, 삼백여 명에 달하는 적의 병력 대부분이 몰살당했고 진태경 공자께서 풍양을 쓰러트리셨답니다.”
 26|
 27|“오오, 오오오. 태경이가!”
 28|
 29|세상을 다 가진 듯한 진위경의 웃음은 이어지는 말에 씻은 듯이 사라졌다.
 30|
 31|“다시 한번 말해 보게. 무경이가 어찌 되었다고?”
 32|
 33|“그, 그게, 풍양과의 생사결에서 상당한 부상을 입으셨다고…… 하지만 목숨에도 지장 없고 빠르게 회복 중이니 걱정하실 필요 없을 듯싶습니다.”
 34|
 35|이미 틀렸다. 진위경의 귀에는 ‘상당한 부상’밖에 들리지 않았을 것이다.
 36|
 37|어릴 적 아우들의 손가락에 가시라도 박히는 날이면 마치 손가락이 잘린 것처럼 야단법석을 피워 대던 그다.
 38|
 39|‘그런데 약간의 부상도 아니고 상당한 부상이라니. 난리 났군.’
 40|
 41|위팽은 지금까지의 경험을 토대로 다음 순간 벌어질 상황을 예측했고, 아니나 다를까 정확히 들어맞았다.
 42|
 43|“무경이가 사경을 헤맨다니!”
 44|
 45|진위경의 포효에 하오문도가 눈을 깜빡였다.
 46|
 47|“예, 예?”
 48|
 49|“풍양! 네놈이 감히 내 아우를 죽여!”
 50|
 51|상당한 부상에서 사경을 헤매게 하더니, 이제는 죽이기까지 한다. 뒤늦게 정신을 차린 하오문도가 황급히 입을 열었다.
 52|
 53|“저기, 소가주님. 뭔가 엄청난 오해가 있는 모양이신데…….”
 54|
 55|“내 반드시 네놈의 사지를 갈기갈기 찢어 구주에 뿌리리라!”
 56|
 57|“…….”
 58|
 59|“…….”
 60|
 61|진위경의 분노는 다시 하루가 지난 다음에야 누그러졌다.
 62|
 63|“무경이와 태경이가 어제 항산검문에서 출발했다고?”
 64|
 65|“예. 그러니까 이제 적당히 좀 하십쇼.”
 66|
 67|“둘 다 무사한 건가?”
 68|
 69|“안 무사했으면 수레에 실려서 오지, 마차 타고 오겠습니까?”
 70|
 71|“그럼…….”
 72|
 73|“내일 정오 무렵에는 만나실 수 있을 겁니다.”
 74|
 75|비로소 쉴 수 있다고 생각하니 위팽은 속이 다 후련했다.
 76|
 77|자신이 누군가, 귀검(鬼劍)이라는 별호까지 붙은 절정 고수다. 당장 어디를 가도 한 자리 차지할 수 있는 실력자인데 주군을 잘못 섬기는 바람에 이런 극한의 노동에 시달리고 있었다.
 78|
 79|‘마지막으로 술을 마신 게 언제더라.’
 80|
 81|오늘은 드디어 오리 구이에 따끈한 술 한잔 걸칠 수 있겠다. 위팽의 입가에 흐뭇한 미소가 맺힌 그 순간이었다.
 82|
 83|“좋아. 그럼 빨리 준비하자고.”
 84|
 85|“예? 뭘 준비합니까?”
 86|
 87|“내 아우들이 수많은 역경을 딛고 임무를 성공적으로 마쳤으니 환영식을 열어야지.”
 88|
 89|“……저는 뭐, 보름이 넘도록 강호 유람하다가 온 겁니까?”
 90|
 91|“응? 누구? 아, 자네?”
 92|
 93|눈을 깜빡이며 위팽을 바라보던 진위경이 호탕하게 웃었다.
 94|
 95|“그거야 물론 자네도 포함이지! 설마 내가 잊고 있었겠나?”
 96|
 97|이 인간, 설마 했는데 잊고 있었던 게 분명하다.
 98|
 99|황당한 얼굴로 입만 벙긋거리는 위팽에게 진위경이 말했다.
100|
101|“아, 수하들 시켜서 인근 포목점에서 천 좀 사 오게나. 최대한 큼지막한 것으로.”
102|
103|“천을요? 갑자기 그건 또 왜요?”
104|
105|“생각해 놓은 게 있네.”
106|
107|
108|
109|* * *
110|
111|
112|
113|“……그렇게 된 겁니다.”
114|
115|못 본 사이 10년은 늙어 버린 위팽의 말을 들으며 주위를 둘러봤다.
116|
117|항산검문을 출발한 지 이틀 만에 도착한 삭주(朔州)에는 때아닌 인파가 바글거렸고, 입구에는 검은 글씨가 적힌 거대한 흰색 천이 나부꼈다.
118|
119|
120|
121|진무경, 진태경, 그리고 혁무진의 무사귀환을 축하합니다!
122|
123|- 태원진가 일동 -
124|
125|
126|
127|나도 모르게 신음이 흘러나왔다.
128|
129|“오메 시벌, 저게 뭐여…….”
130|
131|살다 살다 저런 건 처음 본다.
132|
133|가로 길이만 20여 장에 달하는 같은 현수막. 넓은 대로(大路)를 사이에 두고 마주 보는 두 전각의 꼭대기에 연결된 그것은 항산검문에서도 보일 것 같았다.
134|
135|‘쓸데없이 글씨체 용사비등한 것 보소.’
136|
137|자식 명문대 보낸 극성 부모도 이 정도는 아니겠다.
138|
139|나와 진무경, 혁무진은 약속이라도 한 듯 입을 벌리고 현수막을 바라봤다.
140|
141|“제 이름은 왜 작죠?”
142|
143|무슨 소린가 해서 다시 보니 아주 작은 글씨로 혁무진의 이름까지 들어가 있다.
144|
145|“글씨 크기 작아서 섭섭하냐? 난 기쁠 것 같은데.”
146|
147|“이상하잖아요. 아래에서 보면 잘 보이지도 않아요.”
148|
149|“그럼 내 이름 빼고 네 거 넣을래? 진심이야.”
150|
151|잠시 고민하던 혁무진이 대답했다.
152|
153|“생각해 보니까 지금도 괜찮은 것 같습니다.”
154|
155|“그럼 입 닥치고 있어.”
156|
157|“옙.”
158|
159|대화는 더 이상 이어지지 못했다. 극성 부모, 아니 진위경이 세상에서 가장 환한 웃음을 지으며 달려왔기 때문이다.
160|
161|“이 녀석들!”
162|
163|이게 사람이냐 불곰이냐.
164|
165|2m가 넘어 가는 거한이 솥뚜껑만 한 손으로 나와 진무경을 끌어당겼다. 이대로 으스러져도 이상하지 않을 만큼 우악스러운 힘이다.
166|
167|“무사해서 다행이다. 정말 다행이야!”
168|
169|무사했다. 진위경이 있는 힘껏 끌어안기 전까지는.
170|
171|우두둑.
172|
173|“커헉!”
174|
175|“헉, 무경아!”
176|
177|……지금은 별로 무사하지 않은 것 같군.
178|
179|고통에 몸을 부르르 떠는 피해자를 끌어안은 가해자가 소리쳤다.
180|
181|“의원! 의원!”
182|
183|“의원 불러야 할 것 같은데요? 진짜 아파 보이는데.”
184|
185|내 질문에 위팽이 피곤한 얼굴로 대답했다.
186|
187|“하루 이틀입니까? 이럴 줄 알고 미리 불러 놨습니다.”
188|
189|“오오오.”
190|
191|처음으로 위팽이 위대하게 느껴지는 순간이었다.
192|
193|
194|
195|* * *
196|
197|
198|
199|나를 포함한 태원진가의 삼 형제와 위팽이 한자리에 모인 것은 해가 떨어진 직후였다.
200|
201|진무경이 한층 두꺼워진 붕대 차림으로 나타나자 진위경이 눈치를 살폈다.
202|
203|“괜찮으냐?”
204|
205|“주군 같으면 괜찮으시겠습니까? 가뜩이나 다친 사람을 그렇게 막 다루시면 어떡합니까?”
206|
207|“나름 살살 한 건데…….”
208|
209|무공으로는 모르겠지만 신체 피지컬로 따지자면 진위경이 산서제일인이다.
210|
211|나는 슬그머니 의자를 옆으로 밀었고, 진무경은 초췌한 얼굴로 대답했다.
212|
213|“전 괜찮습니다.”
214|
215|“…….”
216|
217|전혀 안 괜찮아 보이는데.
218|
219|진무경이 절정 고수라 다행이지, 무공 한 수 익히지 못한 양민이었다면 걸어 다니지도 못했다.
220|
221|“이공자께서 부상을 입었다고 듣긴 했습니다만, 이 정도일 줄은 몰랐군요. 아직 내상도 다 낫지 않았던데…….”
222|
223|“정말 그 풍양이란 놈이 한 짓이냐?”
224|
225|두 사람의 물음에 진무경이 담담하게 수긍했다.
226|
227|“강하더군요. 생각 이상으로.”
228|
229|진무경이 누군가. 천하에서도 주목하는 촉망받는 후기지수다. 눈부신 천재성과 노력을 바탕으로 일찍이 절정의 경지에 오른 그가 일개 마적 우두머리에게 패배한 것이다.
230|
231|“놈이 그 정도의 강자라는 말씀이십니까?”
232|
233|“풍양이라, 고원의 마적 중에 제법 뛰어난 고수들이 있다고는 들었지만. 글쎄…….”
234|
235|문득 두 사람의 시선이 나를 향했다. 오리 구이는 그만 처먹고 말 좀 해 보라는 무언의 압박.
236|
237|입 안 가득 쑤셔 넣은 음식을 꿀꺽 삼키고 입을 열었다.
238|
239|“사실이에요. 항산호 대협 소식은 들어서 아시죠? 그 양반도 팔다리 아작 나서 요즘 휠체어 타고 다닙니다.”
240|
241|“휭최어가 뭡니까?”
242|
243|“아, 수레요, 수레.”
244|
245|진위경이 굵은 손가락으로 탁자를 두드렸다.
246|
247|“그 정도의 고수라면 진작 알려졌을 텐데. 혹 무경이 네가 방심한 것은 아니냐?”
248|
249|이번엔 진무경이 망설임 없이 고개를 저었다.
250|
251|“미처 예상치 못한 수에 당하긴 했지만 그게 변명이 될 수는 없습니다. 다시 싸운다 해도 결과는 같을 겁니다.”
252|
253|“……그 정도였더냐?”
254|
255|“호신강기(護身罡氣)를 사용하더군요. 압도적이었습니다.”
256|
257|진위경과 위팽이 동시에 눈을 부릅떴다.
258|
259|“호신강기!”
260|
261|“이공자, 그게 사실입니까?”
262|
263|굳이 대답은 필요 없었다. 진무경이 그런 뻔한 거짓말을 할 이유가 없으니까. 경악한 두 사람을 향해 진무경이 다시 말을 이었다.
264|
265|“지금까지 싸워 본 적 중 가장 강했습니다. 아니, 정확히는 강해졌다고 해야 맞을 것 같습니다.”
266|
267|“강해졌다니?”
268|
269|“그건 또 무슨…….”
270|
271|“피처럼 붉은 단환 한 알을 삼키자마자 무섭도록 강해지더군요.”
272|
273|드디어 잠력단에 관한 이야기가 나온다.
274|
275|나는 최대한 자연스럽게 행동하려 애썼다.
276|
277|‘내가 갖고 있다는 사실을 들키면 안 돼.’
278|
279|잠력단은 독이 든 성배다. 분명 불길하고 수상쩍은 물건이지만 엄청난 효력을 지니고 있음을 부정할 수는 없다.
280|
281|나는 이미 죽음이라는 최악(最惡)의 순간에 쓸 수 있는 차악(次惡)의 대비책으로 잠력단을 사용하기로 마음먹었다.
282|
283|“짧은 순간이었지만 놈이 단환을 복용하려 할 때 분명 목갑 안에 한 알이 남아 있는 걸 봤는데…….”
284|
285|진무경이 말꼬리를 흐리며 나를 바라본다.
286|
287|“혹시 나중에라도 풍양의 품에서 뭔가 발견하지 못했느냐?”
288|
289|“응? 뭐가.”
290|
291|“목갑이라든지. 내가 말한 붉은 단환이라든지.”
292|
293|나는 짐짓 눈살을 찌푸렸다.
294|
295|“잘 모르겠는데? 나중에 뭐 있나 싶어서 뒤져 봤는데 웬 나무 쪼가리만 우수수 쏟아지더라니, 그게 목갑 파편이었나?”
296|
297|“그럼 단환, 단환은?”
298|
299|“모르지. 당장 나도 힘들어서 죽겠는데 어떻게 그걸 다 뒤져 보겠어.”
300|
301|이 정도면 제법 그럴싸한 핑계다.
302|
303|사람이 한두 명 죽은 것도 아니고, 워낙 격렬한 전투였으니 지쳐서 못 찾아본 것도 어쩜 당연한 일인데 더 무슨 말을 하겠나.
304|
305|“그런가?”
306|
307|“항산검문 사람들이 발견했을 수도 있고, 아니면 널리고 널린 피 웅덩이에 그대로 녹아 버렸을 수도 있겠지.”
308|
309|“흠.”
310|
311|진무경이 약간 의구심 어린 눈빛으로 나를 응시했지만 그냥 어깨만 으쓱해 보였다.
312|
313|‘어차피 뒤져 봐도 안 나온다. 이놈아.’
314|
315|나만이 열고 닫을 수 있는 최고의 금고, 인벤토리 한구석에 고이 모셔 뒀으니 진무경이 아니라 천하의 어떤 대도(大盜)라고 해도 잠력단의 털끝 하나 건드릴 수 없다.
316|
317|‘참 편하단 말이지.’
318|
319|내가 다시 한번 시스템의 편리함에 감탄하고 있을 때, 진위경과 위팽은 잠력단의 정체에 대해 유추하기 시작했다.
320|
321|“볼 것도 없이 사마외도의 유산이겠군. 정마대전 당시에 비슷한 효력의 단환이 상당수 사용되었다고 들은 기억이 있다.”
322|
323|“한때 고원을 비롯한 산서 북부가 마교(魔敎)의 손아귀에 떨어진 적이 있었지요. 풍양이 그 흔적을 발견한 거라면 얼추 맞아떨어집니다.”
324|
325|귀를 쫑긋 세우고 듣다가 멈칫했다.
326|
327|‘잠깐만. 마교?’
328|
329|마교란 무협 소설에서 절대 빠지지 않는 단골손님이자 약방의 감초, 금잔디의 명예 소방관 같은 존재다.
330|
331|물론 세계 평화와 빈민 구제를 위해 힘쓰는 종교 단체는 아니고, 일종의 IS(이슬람 테러 단체)라고 할 수 있겠다.
332|
333|한 줄 요약하자면, 엮여서 좋은 점이 단 하나도 없는 광신도 집단이라는 거지.
334|
335|‘마교에서 잠력단을 만들었다면?’
336|
337|지옥에서 막 올라온 악마처럼 붉게 물들었던 풍양의 눈동자. 상상을 뛰어넘는 힘을 일시적으로나마 선사하던 비상식적인 효능.
338|
339|‘이거, 그림이 대충 그려지는데.’
340|
341|찝찝하다. 더럽게 찝찝하다!
342|
343|하지만 고통 없이 얻어지는 것은 없는 법. 부작용도 충분히 감당할 만한…….
344|
345|“그때 당시에 마교도들이 사용했던 대표적인 것이 폭혈단(爆血團)이었지, 아마.”
346|
347|“말로만 들어 봤습니다. 두 시진만 지나면 전신의 혈맥이 터져서 죽는다면서요?”
348|
349|“사술(詐術)로 힘을 얻으려 한 대가지.”
350|
351|“폭혈단이 그 정도인데 풍양이란 놈이 쓴 건 도대체 어느 정도일까요?”
352|
353|“글쎄, 모르긴 몰라도 부작용이 상상을 초월하겠지. 선천지기가 상하는 것은 물론이고 제한 시간이 끝나면 몸에 큰 무리가 갈 걸세. 결국, 제 몸을 장작 삼아 짧은 시간을 불태우는 역할이니까.”
354|
355|절로 마른침이 넘어간다. 나도 모르게 목소리가 튀어나왔다.
356|
357|“그다음은요?”
358|
359|“마교에서 만든 물건이니 오죽하겠느냐. 마기(魔氣)가 골수까지 치밀면…… 피밖에 모르는 살인귀가 되겠지.”
360|
361|“……살인귀요? 마기가 골수까지 치밀어요?”
362|
363|“그런 물건이 악인의 손에 들어가면 실로 큰일…… 태경아, 왜 그러느냐?”
364|
365|진위경이 걱정스러운 얼굴로 나를 바라본다. 슬쩍 이마를 문질러 보니 땀이 송골송골 맺혀 있었다.
366|
367|“그냥요, 좀 더워서.”
368|
369|진무경이 퉁명스럽게 대꾸했다.
370|
371|“무슨 소리야. 밖에 눈 오는데.”
372|
373|“소음인 주제에 뭘 알아. 난 태양인이라 그래…….”
374|
375|젠장. 이제 내가 무슨 말을 하는지도 모르겠다.
376|
377|나는 세 사람을 향해 어색하게 웃어 보였다.
378|
379|“저기. 아까 깜빡한 게 있는데요.”
380|
381|“……?”
382|
383|“……?”
384|
385|“……?”
386|
387|“그 환단. 생각해 보니까 제가 갖고 있네요. 허허, 허허허.”
388|
389|“……!”
390|
391|“……!”
392|
393|“……!”
```

## Assembled English

```markdown
[P1]
# Chapter 126

[P2]
Four days ago, after completing every mission and returning to the Jin Family of Taiyuan, Wipeng deeply regretted how efficiently he had handled things.

[P3]
*I should’ve come back a day later.*

[P4]
But it was already too late. Jin Wikyung had received a messenger eagle from the Lower District Sect and was flying into a rage, his eyes practically rolling back in his head.

[P5]
“Those goddamn mounted bandits dare!”

[P6]
“What is it this time?”

[P7]
“Pung Yang! The Red Wind Band! The Mount Heng Sword Sect! My brothers are in danger! Great danger! We leave at once!”

[P8]
“…I’ll assemble the guards.”

[P9]
Now that every obstacle had been swept aside, Jin Wikyung’s authority was absolute. Before even half a shichen had passed, the two left the family grounds with fifty elite guards and raced onward without rest.

[P10]
Two days later, they stopped at a Lower District Sect branch to change horses and received new information.

[P11]
“What? Pung Yang is dead, and the Red Wind Band has been annihilated?”

[P12]
“Yes! According to our sect’s intelligence, most of the enemy force—some three hundred men—was wiped out, and Young Master Jin Taekyung defeated Pung Yang himself.”

[P13]
“Oh. Ohhh! Taekyung!”

[P14]
Jin Wikyung’s laughter, as if he had gained the whole world, vanished without a trace at the next words.

[P15]
“Tell me again. What happened to Mukyung?”

[P16]
“W-well… he suffered a considerable injury during his life-and-death duel with Pung Yang. But his life isn’t in danger, and he’s recovering quickly, so there should be no need to worry.”

[P17]
It was already over. Jin Wikyung had probably heard nothing except *considerable injury*.

[P18]
When his younger brothers were children, if even a thorn pierced one of their fingers, he would raise such a commotion that you would have thought the finger had been severed.

[P19]
*And it wasn’t a minor injury. It was a considerable one. This is going to be a disaster.*

[P20]
Experience told Wipeng what would happen next.

[P21]
Sure enough, he was exactly right.

[P22]
“Mukyung is hovering between life and death?!”

[P23]
The Lower District Sect member blinked at Jin Wikyung’s roar.

[P24]
“Y-yes?”

[P25]
“Pung Yang! You dare kill my little brother!”

[P26]
First Jin Wikyung turned a considerable injury into hovering between life and death, and now he’d pronounced Mukyung dead outright. The Lower District Sect member finally came to his senses and hurriedly opened his mouth.

[P27]
“Lesser Family Head, I think there’s been a terrible misunderstanding…”

[P28]
“I’ll tear your limbs to shreds and scatter them across the Nine Provinces!”

[P29]
“…”

[P30]
“…”

[P31]
Jin Wikyung’s fury did not subside until another day had passed.

[P32]
“Mukyung and Taekyung left the Mount Heng Sword Sect yesterday?”

[P33]
“Yes. So please take it down a notch.”

[P34]
“Are they both safe?”

[P35]
“If they weren’t, they’d be carried here on a cart. Why would they be riding in a carriage?”

[P36]
“Then…”

[P37]
“You should see them around noon tomorrow.”

[P38]
The thought that he could finally rest filled Wipeng with relief.

[P39]
Who was he, after all? He was a Peak master known by the epithet Ghost Sword. He had the skill to secure an important position wherever he went, yet choosing the wrong lord had condemned him to this grueling labor.

[P40]
*When was the last time I had a drink?*

[P41]
Today, at last, he could enjoy some roast duck and a warm cup of liquor.

[P42]
A satisfied smile had just appeared around Wipeng’s lips when Jin Wikyung spoke.

[P43]
“Good. Then let’s hurry and get ready.”

[P44]
“Pardon? Get ready for what?”

[P45]
“My brothers overcame countless hardships and successfully completed their mission. We have to hold a welcoming ceremony.”

[P46]
“…And what about me? Did I spend more than half a month touring the martial world for pleasure?”

[P47]
“Hm? Who? Oh, you?”

[P48]
Jin Wikyung blinked at Wipeng, then burst into hearty laughter.

[P49]
“Of course that includes you! Surely you didn’t think I’d forgotten?”

[P50]
*I’d thought surely not, but this guy had definitely forgotten.*

[P51]
As Wipeng stared at him in disbelief, opening and closing his mouth without a word, Jin Wikyung continued.

[P52]
“Ah, have your men buy some cloth from a nearby fabric shop. As large as possible.”

[P53]
“Cloth? Why do we suddenly need that?”

[P54]
“I have something in mind.”

[P55]
* * *

[P56]
“…And that’s what happened.”

[P57]
I glanced around as I listened to Wipeng, who looked ten years older than the last time I’d seen him.

[P58]
We had reached Sakju two days after leaving the Mount Heng Sword Sect. The city was unexpectedly packed with people, and at the entrance, a gigantic white cloth bearing black writing fluttered in the wind.

[P59]
Congratulations on the safe return of Jin Mukyung, Jin Taekyung, and Hyuk Mujin!

[P60]
—Everyone in the Jin Family of Taiyuan—

[P61]
A groan escaped me before I knew it.

[P62]
“Oh, fuck. What the hell is that…?”

[P63]
I had never seen anything like it in my life.

[P64]
The banner’s width alone was more than twenty jang—over sixty meters.[^1] Strung between the tops of two pavilions facing each other across a broad avenue, it looked as though it might even be visible from the Mount Heng Sword Sect.

[P65]
*Look at that unnecessarily flamboyant calligraphy.*

[P66]
Even overbearing parents whose child had been accepted into a prestigious university wouldn’t go this far.

[P67]
Jin Mukyung, Hyuk Mujin, and I stared up at the banner with our mouths hanging open as if we had planned it.

[P68]
“Why is my name so small?”

[P69]
I looked again to see what he meant. Sure enough, even Hyuk Mujin’s name had been included in tiny letters.

[P70]
“Are you disappointed that the letters are small? I’d be happy if I were you.”

[P71]
“It looks strange. You can barely see my name from down here.”

[P72]
“Want to take my name out and put yours there instead? I mean it.”

[P73]
Hyuk Mujin considered the offer for a moment.

[P74]
“Now that I think about it, it seems fine as it is.”

[P75]
“Then shut up.”

[P76]
“Yes, sir.”

[P77]
That was as far as our conversation got. The overbearing parent—no, Jin Wikyung—came running toward us with the brightest smile in the world.

[P78]
“You rascals!”

[P79]
Was he a man or a brown bear?

[P80]
The giant, well over two meters tall, pulled Jin Mukyung and me close with hands the size of pot lids. His brute strength was so tremendous that it would not have been strange if he had crushed us to pieces.

[P81]
“I’m so glad you’re safe. Really, so glad!”

[P82]
We had been safe.

[P83]
Right up until Jin Wikyung hugged us with all his strength.

[P84]
*Crack.*

[P85]
“Guh!”

[P86]
“Mukyung!”

[P87]
...He doesn’t look very safe now.

[P88]
The perpetrator, still embracing his victim as he trembled in pain, shouted,

[P89]
“Doctor! Doctor!”

[P90]
“I think we should call a doctor. He looks like he’s in real pain.”

[P91]
Wipeng answered me wearily.

[P92]
“Is this your first day dealing with him? I knew this would happen, so I called one in advance.”

[P93]
“Ohhh.”

[P94]
It was the first time Wipeng had ever seemed magnificent.

[P95]
* * *

[P96]
The three Jin brothers of the Jin Family of Taiyuan, including me, and Wipeng gathered together shortly after sunset.

[P97]
When Jin Mukyung appeared wrapped in even thicker bandages, Jin Wikyung watched him apprehensively.

[P98]
“Are you all right?”

[P99]
“Would you be all right if it were you, my lord? How could you treat someone who was already injured so roughly?”

[P100]
“I thought I was being gentle…”

[P101]
Jin Wikyung might not have been the strongest in martial arts, but when it came to raw physical strength, he was Shanxi's Number One.

[P102]
I quietly slid my chair farther away as Jin Mukyung answered with a haggard expression.

[P103]
“I’m fine.”

[P104]
“…”

[P105]
He looked anything but fine.

[P106]
It was fortunate that Jin Mukyung was a Peak master. An ordinary civilian who had never learned a single martial art wouldn’t have been able to walk after that.

[P107]
“I heard the Second Young Master had been injured, but I didn’t realize it was this severe. Even his Internal Injury hasn’t fully healed…”

[P108]
“Did that Pung Yang bastard really do this to you?”

[P109]
Jin Mukyung calmly nodded in response to their questions.

[P110]
“He was strong. Stronger than I expected.”

[P111]
And who was Jin Mukyung? A promising young prodigy who had drawn the attention of the entire realm. Through dazzling talent and relentless effort, he had reached the Peak realm at an early age—yet he had been defeated by a mere mounted-bandit leader.

[P112]
“You mean he was truly that powerful?”

[P113]
“Pung Yang… I’ve heard that there are some fairly skilled masters among the mounted bandits of Gaoyuan. But still…”

[P114]
Their gazes suddenly turned toward me.

[P115]
The silent pressure told me to stop stuffing my face with roast duck and say something.

[P116]
I swallowed the food filling my mouth and opened it.

[P117]
“It’s true. You’ve heard what happened to the Great Hero known as the Tiger of Mount Heng, right? His arms and legs got wrecked too. He’s been getting around in a wheelchair lately.”

[P118]
“What is a wheelchair?”

[P119]
“Ah, a cart. A cart.”

[P120]
Jin Wikyung tapped the table with one thick finger.

[P121]
“A master of that caliber would have been known long ago. Mukyung, is it possible that you let your guard down?”

[P122]
This time, Jin Mukyung shook his head without hesitation.

[P123]
“I was caught by a move I hadn’t anticipated, but that cannot be an excuse. Even if we fought again, the result would be the same.”

[P124]
“…He was that strong?”

[P125]
“He used Body-Protecting Qi. It was overwhelming.”

[P126]
Jin Wikyung’s and Wipeng’s eyes widened simultaneously.

[P127]
“Body-Protecting Qi!”

[P128]
“Second Young Master, is that true?”

[P129]
There was no need for an answer. Jin Mukyung had no reason to tell such an obvious lie. Facing their shock, he continued.

[P130]
“He was the strongest opponent I’ve ever fought. No—to be precise, I should say he *became* that strong.”

[P131]
“Became?”

[P132]
“What do you mean by that...?”

[P133]
“The instant he swallowed a blood-red pill, he became terrifyingly powerful.”

[P134]
At last, the conversation had reached the Temporary Strength Pill.

[P135]
I tried to act as naturally as possible.

[P136]
*I can’t let them find out I have it.*

[P137]
The Temporary Strength Pill was a poisoned chalice. It was undeniably ominous and suspicious, but its tremendous effects couldn’t be ignored.

[P138]
I had already decided to use it as a second-worst contingency for the worst possible moment—when I was facing death.

[P139]
“It was only for a brief moment, but when he was about to take the pill, I clearly saw that one pill remained inside the wooden case...”

[P140]
Jin Mukyung trailed off and looked at me.

[P141]
“Did you happen to find anything on Pung Yang’s person afterward?”

[P142]
“Hm? Like what?”

[P143]
“A wooden case. Or the red pill I mentioned.”

[P144]
I deliberately furrowed my brow.

[P145]
“I’m not sure. I searched him afterward to see if he had anything, but a bunch of wooden splinters spilled out. Maybe those were pieces of the case?”

[P146]
“Then the pill? The pill?”

[P147]
“No idea. I was half-dead myself. How was I supposed to search through everything?”

[P148]
It was a fairly convincing excuse.

[P149]
It wasn’t as though only one or two people had died, and the battle had been brutally fierce. It was only natural that I’d been too exhausted to search properly. What more could he say?

[P150]
“Is that so?”

[P151]
“The people from the Mount Heng Sword Sect might have found it. Or it could have dissolved into one of the countless pools of blood scattered across the ground.”

[P152]
“Hmm.”

[P153]
Jin Mukyung stared at me with faint suspicion, but I merely shrugged.

[P154]
*You won’t find it even if you search, idiot.*

[P155]
I had tucked it safely into a corner of the greatest vault in existence—my Inventory, which only I could open and close. Neither Jin Mukyung nor the greatest thief under heaven could touch a hair of the Temporary Strength Pill.

[P156]
*It really is convenient.*

[P157]
While I marveled once more at the convenience of the System, Jin Wikyung and Wipeng began speculating about the pill’s origins.

[P158]
“It must be a relic of demonic, heterodox arts. I remember hearing that quite a few pills with similar effects were used during the Great Faction War.”

[P159]
“Northern Shanxi, including Gaoyuan, once fell into the hands of the Demonic Cult. If Pung Yang discovered some remnant they left behind, it would make sense.”

[P160]
I had been listening with my ears perked up when I suddenly froze.

[P161]
*Wait. The Demonic Cult?*

[P162]
The Demonic Cult was a regular fixture you could never leave out of a Murim novel, the licorice in every medicine shop, and Geum Jandi’s honorary firefighter.[^2]

[P163]
Of course, it wasn’t a religious organization devoted to world peace and helping the poor. It was more like IS—the Islamic terrorist group.

[P164]
In short, they were a bunch of fanatics you had absolutely nothing to gain from getting involved with.

[P165]
*What if the Demonic Cult made the Temporary Strength Pill?*

[P166]
Pung Yang’s eyes had been stained red, like a demon that had just climbed out of hell. The pill had granted him unimaginable power, even if only temporarily.

[P167]
*I’m starting to see the picture.*

[P168]
This felt wrong. Really fucking wrong!

[P169]
But nothing could be gained without suffering. The side effects should be something I could endure...

[P170]
“The best-known pill used by the Demonic Cult at the time was the Blood-Exploding Pill, if memory serves.”

[P171]
“I’ve only heard stories about it. Don’t all the blood vessels in the user’s body burst after two shichen, killing them?”

[P172]
“That was the price of trying to gain power through dark arts.”

[P173]
“If the Blood-Exploding Pill was that terrible, just how severe would the side effects of Pung Yang’s pill be?”

[P174]
“I don’t know, but they must be beyond imagination. It wouldn’t just damage his innate qi. Once the time limit ended, his body would suffer tremendous strain. In the end, the pill uses the body itself as kindling and burns it for a brief period.”

[P175]
I swallowed dryly. Before I knew it, my voice had jumped out.

[P176]
“And after that?”

[P177]
“It was made by the Demonic Cult. What else would you expect? Once the demonic qi surges into your very marrow… you’d become a murderous fiend who knows nothing but blood.”

[P178]
“...A murderous fiend? The demonic qi surges into his marrow?”

[P179]
“If an item like that fell into the hands of a villain, it would be a true disaster… Taekyung, what’s wrong?”

[P180]
Jin Wikyung looked at me with concern. I rubbed my forehead and found it covered in beads of sweat.

[P181]
“Nothing. I’m just a little hot.”

[P182]
“What are you talking about? It’s snowing outside.”

[P183]
“What would a Soeumin know? I’m a Taeyangin. That’s why…”[^3]

[P184]
Damn it. I didn’t even know what I was saying anymore.

[P185]
I gave the three of them an awkward smile.

[P186]
“There’s something I forgot earlier.”

[P187]
“…?”

[P188]
“…?”

[P189]
“…?”

[P190]
“That pill. Now that I think about it, I have it. Heh-heh. Heh-heh-heh.”

[P191]
“…!”

[P192]
“…!”

[P193]
“…!”

[P194]
[^1]: A jang is a traditional Korean unit of length measuring roughly three meters.

[P195]
[^2]: Geum Jandi is the heroine of the Korean drama *Boys Over Flowers*.

[P196]
[^3]: Soeumin and Taeyangin are two of the four constitutional types in traditional Korean Sasang medicine.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source, RULES.md, or the exact
glossary requires the change. Exact glossary English wins over an older baseline
synonym for the same Korean key.

```markdown
[P1]
# Chapter 126

[P2]
Four days ago, after completing every mission and returning to the Jin Family of Taiyuan, Wipeng deeply regretted how efficiently he had handled things.

[P3]
*I should have come back a day later.*

[P4]
But it was already too late. Jin Wikyung had received a messenger eagle from the Lower District Sect and was raging with his eyes bulging out of his head.

[P5]
“Those goddamned mounted bandits dare!”

[P6]
“What happened now?”

[P7]
“Pung Yang, the Red Wind Band, the Mount Heng Sword Sect, my brothers—they’re in danger! Great danger! We leave at once!”

[P8]
“...I’ll assemble the guards.”

[P9]
Now that every obstacle had been removed, Jin Wikyung’s authority was absolute. Before even half a shichen had passed, the two of them left the family with fifty elite guards and raced off without stopping.

[P10]
Two days later, while changing horses at a Lower District Sect branch, they received new information.

[P11]
“What? Pung Yang is dead, and the Red Wind Band has been annihilated?”

[P12]
“Yes! According to what our sect has learned, most of the enemy forces, numbering around three hundred, were slaughtered. Young Master Jin Taekyung defeated Pung Yang himself.”

[P13]
“Oh. Ohhh. Taekyung!”

[P14]
Jin Wikyung’s laughter, as if he had gained the whole world, vanished at the next words.

[P15]
“Tell me again. What happened to Mukyung?”

[P16]
“Th-that is... He suffered a considerable injury in his life-and-death duel with Pung Yang... But his life is not in danger, and he is recovering quickly, so you likely have nothing to worry about.”

[P17]
It was already over. Jin Wikyung had probably heard nothing except *considerable injury*.

[P18]
When his younger brothers were children, if even a thorn pierced one of their fingers, he would raise such a commotion that you would have thought the finger had been severed.

[P19]
*And it wasn’t a minor injury. It was a considerable one. This is going to be a disaster.*

[P20]
Based on his experience so far, Wipeng predicted what would happen next.

[P21]
Sure enough, he was exactly right.

[P22]
“Mukyung is hovering between life and death?!”

[P23]
At Jin Wikyung’s roar, the Lower District Sect member blinked.

[P24]
“Y-yes?”

[P25]
“Pung Yang! You dare kill my little brother!”

[P26]
First Jin Wikyung turned a considerable injury into hovering between life and death, and now he’d pronounced Mukyung dead outright. The Lower District Sect member finally came to his senses and hurriedly opened his mouth.

[P27]
“Lesser Family Head, I think there’s been a terrible misunderstanding...”

[P28]
“I’ll tear your limbs to shreds and scatter them across the Nine Provinces!”

[P29]
“...”

[P30]
“...”

[P31]
Jin Wikyung’s anger did not subside until another day had passed.

[P32]
“Mukyung and Taekyung left the Mount Heng Sword Sect yesterday?”

[P33]
“Yes. So please take it down a notch.”

[P34]
“Are they both safe?”

[P35]
“If they weren’t, would they be coming in a carriage instead of being carried in on a cart?”

[P36]
“Then...”

[P37]
“You should be able to see them around noon tomorrow.”

[P38]
The thought that he could finally rest brought Wipeng immense relief.

[P39]
*Who am I?*

[P40]
He was a Peak master, a skilled martial artist known by the epithet Ghost Sword. He had enough ability to claim an important position wherever he went, yet because he had chosen the wrong lord to serve, he was being subjected to this extreme labor.

[P41]
*When was the last time I had a drink?*

[P42]
Today, at last, he would be able to enjoy some roast duck with a warm glass of liquor.

[P43]
A satisfied smile had just appeared around Wipeng’s lips when Jin Wikyung spoke.

[P44]
“Good. Then let’s get ready.”

[P45]
“Pardon? Get ready for what?”

[P46]
“My brothers overcame countless hardships and successfully completed their mission. We have to hold a welcoming ceremony.”

[P47]
“...Did I spend more than half a month touring the martial world for fun?”

[P48]
“Hm? Who? Oh, you?”

[P49]
Jin Wikyung blinked at Wipeng, then let out a hearty laugh.

[P50]
“Of course that includes you! Surely you didn’t think I’d forgotten?”

[P51]
*I’d thought surely not, but this guy had definitely forgotten.*

[P52]
As Wipeng stared at him in disbelief, opening and closing his mouth without a word, Jin Wikyung continued.

[P53]
“Oh, have your subordinates buy some cloth from a nearby fabric shop. As large as possible.”

[P54]
“Cloth? Why do we suddenly need that?”

[P55]
“I have an idea.”

[P56]
* * *

[P57]
“...And that’s how it happened.”

[P58]
Listening to Wipeng, who looked ten years older than when I’d last seen him, I glanced around.

[P59]
We had reached Sakju two days after leaving the Mount Heng Sword Sect. The city was unexpectedly packed with people, and at the entrance, a gigantic white cloth bearing black writing fluttered in the wind.

[P60]
Congratulations on the safe return of Jin Mukyung, Jin Taekyung, and Hyuk Mujin!

[P61]
—Everyone in the Jin Family of Taiyuan—

[P62]
A groan escaped me before I could stop it.

[P63]
“Oh, fuck. What the hell is that...?”

[P64]
In all my life, I had never seen anything like it.

[P65]
The banner was more than twenty jang—over sixty meters—wide.[^1] Strung between the tops of two pavilions facing each other across a broad avenue, it looked as though it might even be visible from the Mount Heng Sword Sect.

[P66]
*Look at that unnecessarily flamboyant calligraphy.*

[P67]
Even overbearing parents whose child had been accepted into a prestigious university wouldn’t go this far.

[P68]
Jin Mukyung, Hyuk Mujin, and I all stared at the banner with our mouths hanging open, as if we had planned it.

[P69]
“Why is my name so small?”

[P70]
I looked again to see what he meant. Hyuk Mujin’s name had been included in tiny letters.

[P71]
“Are you disappointed that the letters are small? I’d be happy if I were you.”

[P72]
“It’s strange. You can barely see it from below.”

[P73]
“Want me to remove my name and put yours there instead? I’m serious.”

[P74]
Hyuk Mujin thought about it for a moment before answering.

[P75]
“Now that I think about it, this is fine as it is.”

[P76]
“Then shut up.”

[P77]
“Yes, sir.”

[P78]
The conversation could go no further. The overbearing parent—no, Jin Wikyung—came running toward us with the brightest smile in the world.

[P79]
“You little rascals!”

[P80]
Was he a man or a brown bear?

[P81]
The giant, well over two meters tall, dragged Jin Mukyung and me close with hands as large as pot lids. His brute strength was so tremendous that it would not have been strange if he had crushed us to pieces.

[P82]
“I’m so glad you’re safe. Really, so glad!”

[P83]
We had been safe.

[P84]
Right up until Jin Wikyung hugged us with all his strength.

[P85]
*Crack.*

[P86]
“Guh!”

[P87]
“Mukyung!”

[P88]
...He doesn’t look very safe now.

[P89]
The perpetrator, still embracing his victim as he trembled in pain, shouted,

[P90]
“Doctor! Doctor!”

[P91]
“I think we should call a doctor. He looks like he’s in real pain.”

[P92]
Wipeng answered my question with a weary expression.

[P93]
“Is this your first day dealing with him? I knew this would happen, so I called one in advance.”

[P94]
“Ohhh.”

[P95]
It was the first time I had ever thought Wipeng was magnificent.

[P96]
* * *

[P97]
The three Jin brothers of the Jin Family of Taiyuan, including me, and Wipeng gathered together shortly after sunset.

[P98]
When Jin Mukyung appeared wrapped in even thicker bandages, Jin Wikyung cautiously studied him.

[P99]
“Are you all right?”

[P100]
“Would you be all right if it were you, my lord? How could you handle someone who was already injured so roughly?”

[P101]
“I was being as gentle as I could...”

[P102]
Jin Wikyung might not have been the strongest in martial arts, but when it came to raw physical strength, he was number one in Shanxi.

[P103]
I quietly slid my chair farther away, while Jin Mukyung answered with a haggard expression.

[P104]
“I’m fine.”

[P105]
“...”

[P106]
He looked anything but fine.

[P107]
It was fortunate that Jin Mukyung was a Peak master. If he had been an ordinary civilian who had never learned martial arts, he would not have been able to walk.

[P108]
Wipeng spoke up.

[P109]
“I heard that the Second Young Master was injured, but I didn’t realize it was this severe. His Internal Injury hasn’t even healed completely yet...”

[P110]
“Was this really the work of that Pung Yang bastard?”

[P111]
In response to their questions, Jin Mukyung nodded calmly.

[P112]
“He was strong. Stronger than I expected.”

[P113]
Who was Jin Mukyung? He was a promising young prodigy who drew attention throughout the realm. Based on his dazzling talent and relentless effort, he had reached the Peak realm at a young age—yet he had been defeated by a mere mounted-bandit leader.

[P114]
“You mean he was truly that powerful?”

[P115]
“Pung Yang... I’ve heard that there are some fairly skilled masters among the mounted bandits of the plateau. But still...”

[P116]
Their gazes suddenly turned toward me.

[P117]
It was a silent demand that I stop stuffing my face with roast duck and say something.

[P118]
I swallowed the food filling my mouth and opened it.

[P119]
“It’s true. You’ve heard the news about the Great Hero known as the Tiger of Mount Heng, right? He got his arms and legs wrecked too. These days, he gets around in a wheelchair.”

[P120]
“What is a wheelchair?”

[P121]
“Ah, a cart. A cart.”

[P122]
Jin Wikyung tapped the table with one thick finger.

[P123]
“A master of that caliber would have been known long ago. Mukyung, is it possible that you let your guard down?”

[P124]
This time, Jin Mukyung shook his head without hesitation.

[P125]
“I was caught by a move I hadn’t anticipated, but that cannot be an excuse. Even if we fought again, the result would be the same.”

[P126]
“...Was he really that strong?”

[P127]
“He used Body-Protecting Qi. It was overwhelming.”

[P128]
Jin Wikyung and Wipeng both opened their eyes wide.

[P129]
“Body-Protecting Qi!”

[P130]
“Second Young Master, is that true?”

[P131]
There was no need for an answer. Jin Mukyung had no reason to tell such an obvious lie. Facing their shock, he continued.

[P132]
“He was the strongest opponent I’ve ever fought. No—in exact terms, it would be more accurate to say that he became stronger.”

[P133]
“Became stronger?”

[P134]
“What do you mean by that...?”

[P135]
“The moment he swallowed a crimson pill, he became terrifyingly powerful.”

[P136]
At last, the conversation had reached the Temporary Strength Pill.

[P137]
I tried to act as naturally as possible.

[P138]
*I can’t let them find out I have it.*

[P139]
The Temporary Strength Pill was a poisoned chalice. It was unquestionably ominous and suspicious, but there was no denying that it possessed tremendous power.

[P140]
I had already decided to use it as a second-worst contingency for the worst possible moment—when I was facing death.

[P141]
“It was only for a brief moment, but when he was about to take the pill, I clearly saw that one pill remained inside the wooden case...”

[P142]
Jin Mukyung let his voice trail off and looked at me.

[P143]
“Did you happen to find anything on Pung Yang’s person afterward?”

[P144]
“Something like what?”

[P145]
“A wooden case. Or the red pill I mentioned.”

[P146]
I deliberately furrowed my brow.

[P147]
“I’m not sure. I searched him later to see if he had anything, but all that came spilling out were piles of wooden scraps. Could those have been fragments of the case?”

[P148]
“Then the pill? The pill?”

[P149]
“No idea. I was exhausted enough to die myself. How was I supposed to search through everything?”

[P150]
It was a fairly convincing excuse.

[P151]
It wasn’t as if only one or two people had died, and the battle had been brutally fierce. It was only natural that I had been too exhausted to search properly. What more could he say?

[P152]
“Is that so?”

[P153]
“The people from the Mount Heng Sword Sect might have found it. Or it could have melted into one of the countless pools of blood scattered across the ground.”

[P154]
“Hmm.”

[P155]
Jin Mukyung stared at me with faint suspicion, but I merely shrugged.

[P156]
*You won’t find it even if you search, idiot.*

[P157]
I had tucked it safely into a corner of the greatest vault in existence—my Inventory, which only I could open and close. Neither Jin Mukyung nor the greatest thief under heaven could touch a hair of the Temporary Strength Pill.

[P158]
*It really is convenient.*

[P159]
As I marveled at the convenience of the system once again, Jin Wikyung and Wipeng began speculating about the pill’s origin.

[P160]
“It must be a relic of demonic, heterodox arts. I remember hearing that quite a few pills with similar effects were used during the Great Faction War.”

[P161]
“There was a time when the northern part of Shanxi, including Gaoyuan, fell into the hands of the Demonic Cult. If Pung Yang discovered traces of it, that would make sense.”

[P162]
I had been listening with my ears perked up when I suddenly froze.

[P163]
*Wait. The Demonic Cult?*

[P164]
The Demonic Cult was a regular fixture you could never leave out of a Murim novel, the licorice in every medicine shop, and Geum Jandi’s honorary firefighter.[^2]

[P165]
Of course, it wasn’t a religious organization devoted to world peace and helping the poor. It was more like IS—the Islamic terrorist group.

[P166]
In short, it was a fanatical organization with absolutely nothing to gain from getting involved with it.

[P167]
*If the Demonic Cult created the Temporary Strength Pill...*

[P168]
Pung Yang’s eyes had been stained red, like a demon that had just climbed out of hell. The pill had granted him an absurd amount of power, even if only temporarily.

[P169]
*I was starting to get the picture.*

[P170]
It felt bad. Really, really bad!

[P171]
But nothing could be gained without suffering. The side effects should be something I could endure...

[P172]
“The most famous thing the Demonic Cult used back then was the Blood-Exploding Pill, if I remember correctly.”

[P173]
“I’ve only heard of it. They say that once two shichen pass, all the blood vessels in the body burst and the user dies?”

[P174]
“That was the price of trying to gain power through dark arts.”

[P175]
“If the Blood-Exploding Pill was that bad, how severe would the side effects of the one Pung Yang used be?”

[P176]
“I don’t know, but they must be beyond imagination. It wouldn’t just damage his innate qi. Once the time limit ended, his body would suffer tremendous strain. In the end, the pill uses the body itself as kindling and burns it for a brief period.”

[P177]
I swallowed dryly. Before I knew it, my voice had jumped out.

[P178]
“What happens after that?”

[P179]
“It was made by the Demonic Cult. What else would you expect? Once the demonic qi surges into your very marrow… you’d become a murderous fiend who knows nothing but blood.”

[P180]
“...A murderous fiend? The demonic qi surges into his marrow?”

[P181]
“If such an object fell into the hands of a villain, it would be a truly terrible disaster... Taekyung, what’s wrong?”

[P182]
Jin Wikyung looked at me with concern. I rubbed my forehead and found it covered in beads of sweat.

[P183]
“Nothing. I’m just a little hot.”

[P184]
“What are you talking about? It’s snowing outside.”

[P185]
“What would a Soeumin know? I’m a Taeyangin.[^3] That’s why…”

[P186]
Damn it. I didn’t even know what I was saying anymore.

[P187]
I gave the other three an awkward smile.

[P188]
“There’s something I forgot earlier.”

[P189]
“...?”

[P190]
“...?”

[P191]
“...?”

[P192]
“That pill. Now that I think about it, I have it. Heh-heh. Heh-heh-heh.”

[P193]
“...!”

[P194]
“...!”

[P195]
“...!”

[P196]
[^1]: A jang is a traditional Korean unit of length measuring roughly three meters.

[P197]
[^2]: Geum Jandi is the heroine of the Korean drama *Boys Over Flowers*.

[P198]
[^3]: Soeumin and Taeyangin are two of the four constitutional types in traditional Korean Sasang medicine.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 삭주 | **Sakju** | Jin Family branch location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 평화 | **Peace Guild** | Guild name. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 폭혈단 | **Blood-Exploding Pill** | Demonic Cult pill said to kill the user after its time limit. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 산서제일인 | **Shanxi's Number One** | Jin Wikyung's reputation for physical strength. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 소음인 | **Soeumin** | One of the constitutional types in Sasang medicine. |
| 태양인 | **Taeyangin** | One of the constitutional types in Sasang medicine. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 126,
  "passed": true,
  "metrics": {
    "source_characters": 6325,
    "translation_characters": 14509,
    "length_ratio": 2.294,
    "source_paragraphs": 190,
    "translation_paragraphs": 196
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "귀가",
        "preferred": "your family"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "대협",
        "preferred": "Great Hero or Sir depending tone"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "평화",
        "preferred": "Peace Guild"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "갑자",
        "preferred": "jiazi"
      }
    }
  ]
}
```

## Binding editorial rules

# Translation Rules

## Fidelity

- Translate the Korean source—not the wiki, manhwa, fan translations, or expected plot.
- Semantic fidelity outranks elegance. Never improve rhythm, humor, or localization by changing a physical action, negation, relationship, hierarchy, mechanism, quantity, or causal detail.
- Preserve every fact, causal link, joke, emotional beat, repetition, and intentional omission. Add nothing.
- Preserve small action verbs and pragmatic cues exactly: nodding versus shaking one's head, pretending nothing happened, and mild or approachable impressions are characterization, not expendable texture.
- Preserve viewpoint and tense. Resolve omitted subjects only when context supports it; retain genuine ambiguity.
- Match each speaker's hierarchy, intimacy, humor, and profanity naturally. Do not mechanically retain every honorific or classical self-reference.
- Do not censor or soften content.

## Terminology

- `compendium.md` and `docs/NAMES.md` are binding for established names, titles, ranks, techniques, organizations, system terms, items, and locations. Profile headings and aliases join that ledger.
- Search only exact Korean terms already present in the current chapter; the compendium contains future-sensitive entries.
- Never re-romanize established names or invent grand names for uncertain terms. First use of an unlisted name or title almost always needs a footnote or a mapped ledger term.
- Use `qi` for Murim energy and `mana` for the modern Hunter system when the source distinguishes them. Preserve an established chapter-specific rendering such as `internal energy` when the exact glossary and surrounding Korean distinguish accumulated `공력` from resulting `기운`.
- In System panels, render `등급` as `**Grade:**` for quest, item, skill, and martial-art classifications. Reserve `rank` for Hunter classifications or ordinary prose; never replace a System `Grade` field with `Rank`.

## English and Markdown

- Use contemporary US English and natural action-comedy prose; avoid Korean syntax calques and generic cultivation MTL phrasing.
- File: `translations/NNNN.md`; heading: `# Chapter N`.
- Speech: curly double quotes. Direct thoughts: italics without quotes.
- Use em dashes without spaces, the ellipsis character `…`, and `* * *` for source scene breaks.
- Format each actual game System-message panel as one Markdown blockquote window headed `> **System**`. Keep all consecutive notices, fields, and lines inside that same blockquote; separate windows when prose intervenes. Do not enclose System notices or UI terms in square brackets; the `System` heading and framed blockquote identify the panel. Do not label manuals, ordinary quotations, warnings printed in a manual, or other non-System material as `System`; use a normal blockquote or a specific heading instead. Do not wrap each complete notice in outer `**`; retain bold only for meaningful labels or emphasis inside the panel.
- Keep the final file English-only reading copy: no audit notes, Korean text, summaries, or model metadata.

### Tone and Style

- Write like a polished commercial webnovel: brisk, vivid, accessible, and easy to read aloud.
- Preserve the series’ contrast between danger and comedy. Let absurdity, bad timing, blunt reactions, and grim situations create dark humor without adding jokes absent from the Korean.
- Jin Taekyung’s narration is conversational, observant, self-mocking, and occasionally profane. It may be irreverent even when the situation is serious.
- Keep deadpan punchlines short and well-timed. Do not explain a joke after delivering it.
- Preserve the source's level of explicitness. A euphemism may remain euphemistic even when its meaning is sexual or crude; do not replace it with more graphic English merely for impact.
- Make dialogue spontaneous and character-specific. Preserve hierarchy and intimacy through word choice, address, rhythm, and restraint—not archaic wuxia English.
- Use strong profanity when the Korean is strong, but neither intensify nor sanitize it. Do not make ordinary lines uniformly vulgar. Profanity should reveal mood or relationship.
- Keep action and injury vivid but clear rather than purple. Do not make violence funny unless the source’s framing does.
- Avoid stiff literalism, translator-added melodrama, dated internet slang, and quippy superhero-style banter.
- On the second pass, correct awkward English collocations and word choices without changing meaning or voice. Prefer ordinary, spoken English over stiff Latinate or ceremonial wording when the scene is brisk or comic: “goose bumps” rather than “gooseflesh,” and “laid into them” rather than “launched into a solemn denunciation.” Read the prose aloud and replace any phrase that sounds like a formal essay, legal document, or literal dictionary gloss unless the source deliberately calls for that register.

## Footnotes

Use `[^1]` Markdown footnotes when a brief, factual, spoiler-free explanation materially helps an English reader understand:

- a Korean institution, living arrangement, food, holiday, myth, historical reference, or local custom;
- a Korean word, phrase, idiom, wordplay, or culturally specific image that cannot be conveyed fully by the best natural English analogy;
- a deliberately literal rendering whose cultural or linguistic force would otherwise be lost.

For example, render `고시원` as “goshiwon” when the setting or connotations matter, with a concise footnote explaining that it is a very small, inexpensive room-for-rent housing arrangement. Prefer the best natural English analogy in the prose. Use a literal translation plus a concise footnote when the Korean wording itself matters. Define a term at its first meaningful occurrence and do not repeat the note unnecessarily. Footnotes must be rare, useful, and non-spoiling; do not footnote ordinary vocabulary, fully preserved jokes, or uncertainty. Record consequential uncertainty in `docs/STATE.md`.

## Spoilers and Scope

- Safe profiles contain only facts revealed through the latest completed chapter.
- Never read `characters/spoilers/` during drafting. Reviewers may consult one relevant sealed profile only for a specific unresolved continuity issue after the draft is complete.
- Future knowledge may prevent contradiction but may not add early names, pronouns, certainty, motives, or foreshadowing.
- Translate exactly one requested chapter unless the user explicitly requests a batch. Never modify Korean source files under `source/`.

# Master Editorial Brief

You are the final English-language editor of an existing Korean-to-English novel translation.

The Korean source is the authority for meaning. The existing English is the baseline you are editing, not a draft to discard. Your task is to make the chapter read like professionally written native English commercial fiction while preserving the author's exact story, characterization, humor, register, pacing, ambiguity, and cultural texture.

## Editorial authority

You may freely recast sentences and paragraphs when the English is stiff, literal, repetitive for accidental reasons, awkwardly collocated, over-explained, or syntactically shaped by Korean. You may tighten dialogue, improve rhythm, repair transitions, and make action easier to follow. A technically correct sentence may still need rewriting if a fluent English novelist would not naturally phrase it that way.

Do not change text merely to make it different. If the baseline is already strong, leave it alone.

The accepted baseline is also the project's style and terminology anchor. Do not
replace an established rendering, cultural term, System label, Markdown form, or
recurring phrase with a synonym merely because the synonym sounds smoother.
Make that change only when the Korean source, `RULES.md`, or the exact glossary
requires it. In particular, do not turn a source-specific image into a nearby
English image, or change a gold-spoon joke, item name, technique name, or UI
label into a different expression without source support.

## Fidelity constraints

Never invent, omit, explain away, generalize, intensify, soften, or reinterpret source-supported content. In particular, preserve:

- exact actions, subjects, objects, directionality, causality, quantities, and physical details;
- deliberate ambiguity, euphemism, implication, profanity level, repetition, and withheld information;
- jokes and comic specificity, even when a more generic English joke would sound smoother;
- hierarchy, kinship, forms of address, characterization, and speaker attitude;
- System mechanics, Murim concepts, names, ranks, techniques, items, organizations, and established terminology.
- chapter-level logical consistency: interpret labels, counters, notifications, and repeated facts from how they behave across the scene, not from an isolated surface gloss;
- idioms by their narrative function rather than their component words, and jokes with their setup, recognition, and punchline timing intact;
- cross-sentence implications: do not create a claim that contradicts “again,” an increasing value, an earlier action, or the explanation immediately around it;
- repeated terminology and formatting: once the baseline or glossary establishes a rendering, keep it consistent throughout the chapter unless the source clearly changes the sense;

Do not add jokes, metaphors, explanations, emotional conclusions, or colorful details that are absent from the Korean. Do not replace a specific source image with a generic equivalent merely because the generic version is smoother.

When natural English and literal form conflict, preserve the source meaning and pragmatic effect while changing the English form as much as necessary.

Before returning the chapter, perform a silent continuity pass: trace every
counter, quantity, repeated System label, item or technique name, joke setup and
payoff, and physical cause-and-effect sequence from the Korean through the
finished English. Correct any local sentence that contradicts the sequence.

## Relationship to project files

`RULES.md` is binding. `POLISH.md` describes known translation-English failure modes and should guide the edit. Exact glossary matches are binding unless the packet explicitly marks them otherwise. Character/continuity material is context only and must never override the chapter's Korean source.

## Output

Return only the complete edited English Markdown chapter. Preserve the required chapter heading and project Markdown conventions. Do not provide commentary, a change log, explanations, or a Markdown code fence.
