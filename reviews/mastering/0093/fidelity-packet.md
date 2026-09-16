# Fidelity Gate — Chapter 93

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
  1|＃93화
  2|
  3|
  4|
  5|‘이런 아마추어 자식들.’
  6|
  7|홍우진은 분통이 터질 지경이었다. 지난번처럼 고양이의 몸에 들어갔다면 털을 바짝 세우고 하악질을 했을 것이다.
  8|
  9|하지만 지금 그는 손톱보다도 작은 쌀벌레. 냉장고 밑 틈새에 숨어 꿈틀거리는 게 할 수 있는 최대의 분노 표출이었다.
 10|
 11|왜애애앵.
 12|
 13|‘저 새끼 저거, 또 들어오네.’
 14|
 15|분노의 대상은 끊임없이 집 안으로 들어오는 파리였다.
 16|
 17|어느 놈인지는 몰라도 나름 조심한다고 한 마리씩만 슬금슬금 들어오긴 하는데, 오히려 진태경의 경계심만 돋우는 꼴이다.
 18|
 19|“아오, 이놈의 파리.”
 20|
 21|후웅. 찍!
 22|
 23|뻔한 최후. 홍우진은 혹시라도 진태경이 알아챌까 봐 몸이 달았다.
 24|
 25|‘꼭 저런 놈들이 상도덕도 없는 주제에 머리까지 나빠요.’
 26|
 27|어지간한 헌터들은 알아차리지 못하겠지만 그는 바로 알아봤다.
 28|
 29|저 파리는 마법사가 조종하는 패밀리어(Familiar)라는 사실을. 같은 마법사만이 느낄 수 있는 매우 미약한 마나가 그 증거다.
 30|
 31|‘누구한테 고용된 놈이지? 역시 상동 길드인가?’
 32|
 33|만약 그렇다면 이 의뢰는 당장 때려치워야 한다. 그는 자신의 실력에 엄청난 자부심을 갖고 있는 프로니까.
 34|
 35|신성한 업무 공간에 훼방꾼이 끼어드는 일은 참을 수 없었다.
 36|
 37|‘그렇게 신신당부했는데도…….’
 38|
 39|아무리 일을 잘 처리하더라도 결국 성질 급한 의뢰인이 풀어 놓은 미꾸라지 한 마리가 물을 흐릴 때가 있다. 바로 지금처럼.
 40|
 41|“요즘 파리들은 다 저러냐?”
 42|
 43|“그, 그럴 수도 있지 않을까? 아무튼 10만 원 줘.”
 44|
 45|“줘야지. 주긴 주는데…… 저 파리 좀 이상하지 않아?”
 46|
 47|젠장, 이렇게 될 줄 알았지.
 48|
 49|홍우진은 욕을 삼키며 열심히 몸을 움직였다. 꿈틀꿈틀, 사람의 시선이 닿지 않는 더 깊은 곳으로 기어가던 그때였다.
 50|
 51|찌릿.
 52|
 53|‘……어?’
 54|
 55|그는 몸이 붕 뜨는 듯한 낯선 감각에 사로잡혔다. 패밀리어 마법을 사용하기 시작한 이래 단 한 번도 없었던 일이다.
 56|
 57|‘뭐지? 이번 패밀리어가 너무 작아서 그런가?’
 58|
 59|찰나에 불과했지만 홍우진은 찝찝함을 감출 수 없었다. 순간 탐지 마법은 아닌지 하는 의심이 들었지만 이내 고개를 저었다.
 60|
 61|‘마법은 절대 아니야.’
 62|
 63|진태경이 비(非)마법 헌터이기 때문만은 아니다. 어차피 돈만 있으면 마법 장비를 구할 수 있는 세상 아닌가?
 64|
 65|하지만 동류는 동류를 알아보는 법. B급 마법사인 그가 탐지 마법을 구분하지 못할 리 없다.
 66|
 67|‘순간적으로 연결이 약해진 거겠지. 맞아. 분명히 그럴 거야.’
 68|
 69|단순한 착각이라고 생각하게 된 결정적인 계기는 진태경의 반응이었다.
 70|
 71|“날개를 다쳐서 그런가, 파리가 어째 비실비실하네.”
 72|
 73|짝!
 74|
 75|경쾌한 소리와 함께 다시 거실로 나온 진태경이 소파에 드러누웠다. 예능 프로그램을 보며 낄낄거리기를 잠시, 웃음소리 대신 요란한 코골이가 집 안을 가득 채웠다.
 76|
 77|드르렁. 드르렁.
 78|
 79|그제야 홍우진의 마음이 느슨하게 풀어졌다.
 80|
 81|‘그럼 그렇지. C급 헌터, 그것도 얼마 전까지 F급이었던 놈이 뭘 알겠어. 이틀 전에 있었던 일도 전부 우연이 분명해.’
 82|
 83|이틀 전, 고양이를 패밀리어 삼아 진태경을 관찰하다 놀랐던 일이 아직 마음 한편에 남아 있었다. 왠지 모르게 그 후로도 자꾸만 신경 쓰였는데 이제야 한시름 놓을 수 있을 것 같았다.
 84|
 85|‘저런 허접한 패밀리어도 못 알아챌 정도면, 뭐. 말 다 한 거지.’
 86|
 87|한 가지 문제가 있다면 저 게으른 놈이 도무지 움직일 생각이 없다는 건데…….
 88|
 89|‘이제는 조금 더 과감하게 감시해야겠어.’
 90|
 91|홍우진이 하고 많은 생명체 중 쌀벌레를 패밀리어로 골랐던 건 진태경에 대한 일말의 경계심 때문이었다.
 92|
 93|그러나 이제는 이 작고 느려 터진 벌레의 몸에서 빠져나가도 될 듯싶었다.
 94|
 95|‘내일은 다른 모습으로 만나자고, 진태경.’
 96|
 97|팟.
 98|
 99|홍우진은 링크를 해제했다. 냉장고 틈새에 숨어 있던 그것은 더 이상 패밀리어가 아니다. 그저 작고 연약한 쌀벌레에 불과했다.
100|
101|그리고 다음 순간.
102|
103|드르렁…….
104|
105|진태경의 코골이가 서서히 잦아들더니 이내 뚝 끊겼다.
106|
107|
108|
109|* * *
110|
111|
112|
113|미약한 기운 하나가 사라진다. 감각을 총동원하고 있기에 느낄 수 있었던 변화였다.
114|
115|‘갔나?’
116|
117|기지개를 켜는 척 눈을 떴다. 가장 먼저 눈길이 향한 곳은 냉장고 바닥 틈새였다.
118|
119|
120|
121|[Lv.1 쌀벌레]
122|
123|
124|
125|불과 10분 전만 하더라도 ‘패밀리어’라는 꼬리표가 붙어 있던 레벨창이다. 링크가 끊긴 지금은 아니지만.
126|
127|“흐아암. 뭐 먹을 거 없나…….”
128|
129|나는 소파에서 일어나 자연스럽게 집 안을 돌아다녔다. 그러고 나서야 확신할 수 있었다.
130|
131|‘더 이상 패밀리어는 없어.’
132|
133|[기감]에 걸려드는 건 평범한 날벌레 몇 마리뿐. 그중 패밀리어는 어디에도 없다.
134|
135|쉬지 않고 들려오던 파리 날갯짓 소리도 뚝 끊긴 후였다.
136|
137|방금 일로 놈들도 아마 뜨끔했을 테니 최소한 오늘 하루만큼은 얼씬도 못 하겠지.
138|
139|‘젠장, 패밀리어라니.’
140|
141|패밀리어(Familiar) 마법.
142|
143|마법사들이 사용하는 일종의 정신계 마법이다. 시전자는 패밀리어로 삼은 생물체와 정신이 연결되며 수준에 따라서는 자신의 뜻대로 조종할 수도 있다고 했다.
144|
145|‘실제로 경험해 본 건 처음인데.’
146|
147|근접 헌터라고 모든 무기의 달인이 아니듯 마법사도 마찬가지다. 그중에서도 정신계 마법은 꽤 어려운 축에 들어간다고 들었다.
148|
149|‘그런 놈들이 왜 나를?’
150|
151|놈, 이 아니라 놈들인 이유는 패밀리어가 두 마리였기 때문이다. 두 놈이 한패일 수도 있고, 아닐 수도 있다.
152|
153|그러나 누가 보냈는지는 대강 짐작 가는 구석이 있었다.
154|
155|‘상동 길드밖에 더 있나.’
156|
157|현실에서 모종의 원한 관계를 맺은 곳이라고는 상동 길드 한 군데뿐이다. 정확히는 임창수지만.
158|
159|‘자식을 건드리면 아버지가 뛰어나오는 법이지.’
160|
161|냉혹하고 성질 더럽다는 A급 헌터, 임춘수.
162|
163|오늘 벌어진 일이 그의 지시라면 쉽게 끝나진 않을 것이다.
164|
165|하지만…….
166|
167|‘이쪽에서도 당하고 있을 수만은 없지.’
168|
169|이틀 전 나를 미행한 것까지는 괜찮다. 참을 수 있다.
170|
171|그러나 오늘 일은 참을 수 없다. 이곳은 집이고, 사랑하는 가족이 사는 곳이니까. 놈들은 내 역린을 건드린 거다.
172|
173|‘이 새끼들을 어떻게 엿 먹여야 하나…….’
174|
175|고민하던 그때, 하연이의 방문이 벌컥 열렸다.
176|
177|딱딱하게 굳은 얼굴. 혹시 놈들이 나 모르게 패밀리어로 무슨 수작질을 벌였나? 마음이 다급해진다.
178|
179|“오빠.”
180|
181|“왜, 무슨 일이야? 방에 뭐 이상한 거라도 있어?”
182|
183|“아니, 그런 거 아냐.”
184|
185|“그럼 뭔데?”
186|
187|“10만 원 왜 안 줘?”
188|
189|“…….”
190|
191|그래. 내가 너를 너무 과소평가했구나.
192|
193|
194|
195|* * *
196|
197|
198|
199|다음 날 아침. 나는 날이 밝기가 무섭게 집을 나섰다.
200|
201|지난밤 내내 [기감]으로 패밀리어의 침입을 대비하느라 눈이 뻑뻑했지만 운기조식으로 피로를 풀었다.
202|
203|“어디로 모실까요?”
204|
205|“일산 라페스타요.”
206|
207|택시는 뻥 뚫린 도로를 막힘없이 달렸고, 생각했던 것보다 훨씬 빨리 목적지에 도착했다.
208|
209|‘스토어는 몇 년 전에 한 번 와 봤던 거 이후로 처음인가?’
210|
211|일산 중심가에 위치한 스토어(Store)는 멀리서 봐도 확연히 눈에 띄었다. 일단 근처의 다른 가게에 비해 압도적으로 컸고 화려했다.
212|
213|거기에 다른 가게들과 다른 점이 또 있다. 입구에서 정장을 입은 경비가 손님들을 걸러 내고 있었다.
214|
215|“아저씨, 우리 성인이라니까요?”
216|
217|“안 됩니다.”
218|
219|“성인인데 왜 출입 금지냐고요.”
220|
221|“지문 인식기가 성인이 아니라고 하니까요.”
222|
223|“그거 불량 아니에요?”
224|
225|“아닙니다.”
226|
227|“아 씨, 좀 들여보내 달라고요.”
228|
229|“뭔 씨?”
230|
231|경비의 말에 척 봐도 앳되어 보이는 10대 대여섯 명이 움찔하며 뒷걸음질 쳤다.
232|
233|“……뭐요.”
234|
235|“손님한테 이렇게 해도 되는 거예요?”
236|
237|“손님? 하, 이 어린노무 새끼들이 진짜.”
238|
239|경비가 피곤한 듯한 얼굴로 눈가를 문질렀다. 그는 평범한 성인 남성이 아니라 고용된 경비 헌터였다. 미성년자 대여섯이 아니라 격투기 선수가 떼거지로 와도 뚫을 수 없다.
240|
241|“나한테 손님은 헌터 아니면 회원증 발급받은 민간인 성인들이야. 너네 같은 고삐리가 아니라.”
242|
243|“…….”
244|
245|“좋게 말할 때 갈래, 아니면 경찰 부를까?”
246|
247|어딜 가나 저런 놈들이 꼭 있다. 일반인들은 접할 수 없는 온갖 물건들로 가득한 스토어에는 더더욱.
248|
249|“……야, 야. 가자.”
250|
251|앞에서 얼쩡거리던 놈들이 물러가고 나서야 나를 발견한 경비가 친절한 말씨로 물었다.
252|
253|“무슨 일로 오셨습니까?”
254|
255|“물건을 구입하려고요.”
256|
257|“회원권 혹은 헌터 자격증을 제시해 주시면 됩니다.”
258|
259|“여기요.”
260|
261|“확인 절차 좀 걸치겠습니다.”
262|
263|자격증 확인과 지문 인식을 거친 후에야 출입증이 주어졌다.
264|
265|“C급 헌터님이시니 3층까지 이용 가능하십니다.”
266|
267|스토어는 층마다 구비되어 있는 물품이 다르다. F급 헌터 시절에 딱 한 번 와 봤었는데, 당시 내 등급으로는 2층이 한계라 그 위로는 구경도 못 해 봤다.
268|
269|“즐거운 시간 되십시오.”
270|
271|“네, 고생하세요.”
272|
273|문을 통과하자 끝도 없이 늘어선 유리 진열대가 보인다.
274|
275|일반적인 가게와는 비교도 안 될 정도로 넓은 공간. 그러나 보이는 손님은 몇 되지 않는다.
276|
277|‘하긴, 붐비는 게 이상하지.’
278|
279|이곳을 이용할 수 있는 사람들은 극소수다. 대한민국 전체 인구의 0.1%에 불과한 헌터들, 그리고 회원권을 발급받을 수 있을 정도로 사회적 영향력이 있는 일반인들.
280|
281|그들이 스토어의 주 고객이다.
282|
283|“해당 상품은 국내 S사에서 제작하였으며 경보 마법이 내장되어 있어 보안에 유용…….”
284|
285|“해외 M사에서 제작한 브로치입니다. 아름답고 감각적인 디자인과 실드 마법이 내장되어 있어 사모님 호신용으로…….”
286|
287|열심히 고객들에게 제품을 설명 중인 직원들.
288|
289|맞다. 스토어는 민간에서 구하기 힘든 고가의 마법 물품을 구매할 수 있는 일종의 명품 백화점이다.
290|
291|“그럼 그거랑 이거랑. 저것도 줘 봐요.”
292|
293|“더 성능 좋은 거 없나? 가격은 신경 쓰지 말고 가져와 봐.”
294|
295|고객 숫자는 적을지 몰라도 구매력 하나는 최강이다.
296|
297|기본 수백만 원 대의 물건을 사들이는 사람들을 멍하니 바라보고 있는데 예쁘장하게 생긴 여직원이 다가와 고개를 숙였다.
298|
299|“안녕하십니까. 고객님의 안내를 도와드릴 일산 스토어 김선희 대리입니다.”
300|
301|“아, 예.”
302|
303|지난번에 왔을 때도 정중하게 대해 줬지만 이 정도는 아니었는데.
304|
305|C급 정도 되니까 손님 접대가 제법 극진하다.
306|
307|“혹시 찾으시는 제품이 있으십니까?”
308|
309|“레이드 장비를 좀 사려고요.”
310|
311|직원의 표정이 밝아졌다. 스토어에는 수많은 마법 물품이 있지만 그중에서도 가장 고가에 속하는 것이 헌터 장비다.
312|
313|더군다나 나는 C급 헌터. 중급 헌터 정도면 장비 하나만 골라도 억 소리가 나온다.
314|
315|그러니 판매 직원 입장에서는 실적 쌓을 생각에 기분이 좋을 수밖에.
316|
317|“3층으로 안내해 드리겠습니다.”
318|
319|에스컬레이터 쪽으로 몸을 튼 그녀에게 말했다.
320|
321|“아뇨, 2층으로 가 주세요.”
322|
323|“네? 하지만 C급 헌터 장비를 구매하시려면 3층으로…….”
324|
325|“괜찮아요. 제가 사려는 건 하급 헌터용 무기니까.”
326|
327|살짝 어두워지는 직원의 얼굴을 모른 척하고 먼저 에스컬레이터에 올랐다.
328|
329|‘쥐새끼 잡을 때 쓸 만한 게 있으려나.’
330|
331|인벤토리를 채워야 할 때가 왔다.
332|
333|
334|
335|* * *
336|
337|
338|
339|“괜찮아요. 제가 사려는 건 하급 헌터용 무기니까.”
340|
341|고객의 말에 김선희 대리는 몰래 한숨을 내쉬었다. 판매 실적에 유난히 신경 쓰고 있는 그녀로서는 영 달갑지 않은 소식이다.
342|
343|‘이번 달에 좋은 실적을 올려야 승진할 텐데.’
344|
345|서울 지점에 있는 입사 동기는 벌써 팀장을 달았다. 운이 좋은 건지, 수완이 좋은 건지 걸리는 손님마다 큰손이란다.
346|
347|그에 비하면 자신은…….
348|
349|“이거 괜찮네요.”
350|
351|“아, 네. 해당 제품은 F급 마정석으로 제작된…….”
352|
353|김선희는 퍼뜩 정신을 차리고 설명을 시작했다. 고객이 집어 든 것은 날이 검게 칠해진 단검이었다.
354|
355|다른 무기들에 비하면 특별한 것도, 그렇다고 마법이 내장된 것도 아닌 평범한 소모품.
356|
357|“가격은요?”
358|
359|“현재 여름 특가 할인 중이라 52만 원의 저렴한 가격으로 모시고 있습니다.”
360|
361|“음. 비싼데.”
362|
363|“…….”
364|
365|C급 헌터 연봉이 어떻게 되더라? 기본 수당만 몇억 아니었나? 김선희는 어이가 없었지만 묵묵히 고객의 선택을 기다렸다.
366|
367|“에이, 어쩔 수 없지. 살게요. 하나 주세요.”
368|
369|“……네.”
370|
371|돈 아까워 죽겠다는 얼굴이 밉상 그 자체다. 김선희가 내심 욕을 삼키며 단검을 집어 든 그때였다.
372|
373|“아뇨. 그거 말고요.”
374|
375|“네?”
376|
377|“옆에 있는 거요.”
378|
379|그녀의 시선이 옆을 향했다. 보관 박스에 가지런히 정렬된 100개의 단검이 보인다.
380|
381|“같은 제품입니다, 고객님.”
382|
383|“알아요. 저걸로 하나 주세요.”
384|
385|“……설마 저 보관 박스를 말씀하신 건가요?”
386|
387|“네. 저거 한 박스 주세요. 그리고 저것도 한 박스 주시고, 저것도…….”
388|
389|김선희 대리의 실적 걱정이 사라지는 순간이었다.
```

## Assembled English

```markdown
[P1]
# Chapter 93

[P2]
*What a bunch of amateurs.*

[P3]
Hong Woojin was furious enough to burst. If he had entered the cat’s body like last time, he would have puffed up its fur and hissed.

[P4]
But right now, he was a rice weevil smaller than a fingernail. The most he could do to express his anger was hide in the gap beneath the refrigerator and wriggle.

[P5]
Bzzzzzz.

[P6]
*That bastard’s coming in again.*

[P7]
The target of his anger was the flies that kept entering the house.

[P8]
Woojin did not know who was behind them, but whoever it was seemed to think they were being careful by sneaking the flies in one at a time. Instead, they were only putting Jin Taekyung further on guard.

[P9]
“Ugh, these damn flies.”

[P10]
Whoosh. Smack!

[P11]
A predictable end. Hong Woojin grew anxious, worried that Jin Taekyung might notice him.

[P12]
*Bastards like that have no professional courtesy, and they’re stupid on top of it.*

[P13]
Most Hunters would never have noticed, but he recognized it immediately.

[P14]
That fly was a Familiar being controlled by a mage. The proof was the incredibly faint mana that only another mage could sense.

[P15]
*Who hired the bastard? Was it Sangdong Guild after all?*

[P16]
If that was the case, he would have to quit this assignment right away. He was a professional with immense pride in his abilities.

[P17]
He could not tolerate an intruder interfering with his sacred workspace.

[P18]
*I warned them over and over…*

[P19]
No matter how well you handled a job, there were times when a single loach released by an impatient client muddied the water. Just like now.

[P20]
“Are all flies like that these days?”

[P21]
“Th-They could be, couldn’t they? Anyway, give me the hundred thousand won.”

[P22]
“I will. I’ll give it to you, but… don’t you think that fly’s a little strange?”

[P23]
Damn it. He knew this would happen.

[P24]
Swallowing his curses, Hong Woojin wriggled with all his might. He was crawling deeper into a place no human eyes could reach when—

[P25]
A jolt.

[P26]
*…Huh?*

[P27]
A strange sensation seized him, as though his body had suddenly floated into the air. It had never happened once since he began using Familiar magic.

[P28]
*Is it because this Familiar is too small?*

[P29]
The sensation lasted only an instant, but Hong Woojin could not shake off his unease. For a moment, he wondered whether it had been some kind of detection spell, but he soon shook his head.

[P30]
*It definitely wasn’t magic.*

[P31]
That was not merely because Jin Taekyung was a non-mage Hunter. After all, this was a world where anyone could obtain magical equipment if they had enough money.

[P32]
But mages recognized their own kind. As a B-rank mage, there was no way he could fail to distinguish a detection spell.

[P33]
*The connection must have weakened for a moment. Yes. That has to be it.*

[P34]
What finally convinced him that he had imagined it was Jin Taekyung’s reaction.

[P35]
“Maybe its wing’s injured. This fly’s looking pretty weak.”

[P36]
Smack!

[P37]
With a crisp sound, Jin Taekyung returned to the living room and sprawled out on the sofa. He chuckled at a variety show for a while, but soon the house was filled with loud snoring instead of laughter.

[P38]
Hrrrnk. Hrrrnk.

[P39]
Only then did Hong Woojin relax.

[P40]
*Of course. What could a C-rank Hunter who was an F-rank until recently possibly know? What happened two days ago must have been a complete coincidence, too.*

[P41]
The incident from two days ago still lingered in the back of his mind. He had been watching Jin Taekyung through a cat Familiar and had been startled by what happened. For some reason, it had continued to bother him ever since. Now, at last, he felt he could breathe a little easier.

[P42]
*If he can’t even recognize a shoddy Familiar like that, then that says it all.*

[P43]
There was only one problem: the lazy bastard had no intention of moving at all…

[P44]
*I’ll have to monitor him a little more boldly from now on.*

[P45]
Hong Woojin had chosen a rice weevil from among all the living creatures in the world because he still harbored a sliver of caution toward Jin Taekyung.

[P46]
But now, it seemed safe to leave the body of this tiny, painfully slow insect.

[P47]
*Let’s meet in a different form tomorrow, Jin Taekyung.*

[P48]
Pop.

[P49]
Hong Woojin severed the Link. The creature hiding beneath the refrigerator was no longer a Familiar. It was nothing more than a small, fragile rice weevil.

[P50]
And then—

[P51]
Hrrrnk…

[P52]
Jin Taekyung’s snoring gradually faded before stopping altogether.

[P53]
* * *

[P54]
A faint presence disappeared. I could sense the change only because I was focusing every one of my senses.

[P55]
*Did he leave?*

[P56]
I opened my eyes while pretending to stretch. The first place I looked was the gap beneath the refrigerator.

[P57]
> **System**
>
> Lv. 1 Rice Weevil

[P58]
Only ten minutes ago, its Level window had carried the tag “Familiar.” Not anymore, now that the Link had been severed.

[P59]
“Yaaawn. Is there anything to eat…?”

[P60]
I got up from the sofa and casually wandered around the house. Only then could I be certain.

[P61]
*There aren’t any Familiars left.*

[P62]
The only things caught by my Qi Sense were a few ordinary flying insects. There was not a Familiar among them.

[P63]
The incessant buzzing of wings had stopped, too.

[P64]
They had probably gotten spooked by what just happened, so at least they would not show their faces for the rest of the day.

[P65]
*Damn it. A Familiar?*

[P66]
Familiar magic.

[P67]
It was a kind of mental magic used by mages. The caster formed a mental connection with the creature chosen as a Familiar and, depending on the caster’s skill, could even control it at will.

[P68]
*That was my first time experiencing it firsthand.*

[P69]
A melee Hunter was not automatically a master of every weapon, and mages were the same. Mental magic, in particular, was said to be among the more difficult branches.

[P70]
*Why would people like that come after me?*

[P71]
The reason I thought of them as “people” rather than “someone” was that there had been two Familiars. The two could have been working together, or they might not have been.

[P72]
Still, I had a rough idea of who had sent them.

[P73]
*Who else could it be but Sangdong Guild?*

[P74]
The only place I had formed some kind of grudge against in the real world was Sangdong Guild. More precisely, Im Changsoo.

[P75]
*When you mess with someone’s child, the father comes running.*

[P76]
Im Chunsoo, the A-rank Hunter known for being cold-blooded and foul-tempered.

[P77]
If what happened today was his order, this would not end easily.

[P78]
But…

[P79]
*I can’t just sit back and take it.*

[P80]
I could let the fact that they had followed me two days ago go. I could tolerate that.

[P81]
But I could not tolerate what happened today. This was my home, the place where my beloved family lived. They had crossed my one inviolable boundary.

[P82]
*How should I screw these bastards over…?*

[P83]
I was thinking about it when Hayeon’s bedroom door flew open.

[P84]
Her face was stiff. Had they used a Familiar to pull something behind my back? My thoughts grew frantic.

[P85]
“Oppa.”

[P86]
“What is it? What happened? Is there something strange in your room?”

[P87]
“No, it’s not that.”

[P88]
“Then what is it?”

[P89]
“Why haven’t you given me the hundred thousand won?”

[P90]
“…”

[P91]
Right. I had been underestimating you far too much.

[P92]
* * *

[P93]
The next morning, I left the house as soon as dawn broke.

[P94]
My eyes felt gritty from staying alert with Qi Sense all night in case another Familiar intruded, but I shook off the fatigue by circulating my qi.

[P95]
“Where should I take you?”

[P96]
“Ilsan Lafesta, please.”

[P97]
The taxi sped along the wide-open roads without a hitch, reaching the destination much faster than I had expected.

[P98]
*Is this my first time coming to the Store since I visited once a few years ago?*

[P99]
The Store, located in the center of Ilsan, stood out clearly even from a distance. For one thing, it was overwhelmingly larger and more splendid than the shops around it.

[P100]
There was another thing that set it apart from ordinary stores. At the entrance, guards in suits were screening the customers.

[P101]
“Sir, we’re adults, I’m telling you!”

[P102]
“No.”

[P103]
“We’re adults, so why aren’t we allowed inside?”

[P104]
“Because the fingerprint scanner says you’re not adults.”

[P105]
“Isn’t it broken?”

[P106]
“No.”

[P107]
“Ah, shit, just let us in!”

[P108]
“‘Shit’?”

[P109]
Five or six teenagers who looked obviously young flinched and took a step back.

[P110]
“…What?”

[P111]
“Is that any way to treat customers?”

[P112]
“Customers? Ha. You little shits, seriously.”

[P113]
The guard rubbed the corners of his eyes with a weary expression. He was not an ordinary adult man but a hired guard Hunter. Even if a whole crowd of professional fighters came instead of five or six minors, they would not be able to force their way in.

[P114]
“My customers are Hunters or civilian adults who’ve been issued membership cards. Not high school punks like you.”

[P115]
“…”

[P116]
“Are you leaving while I’m asking nicely, or should I call the police?”

[P117]
People like that existed everywhere. Especially in a Store filled with all kinds of goods ordinary people could never access.

[P118]
“…Hey, hey. Let’s go.”

[P119]
Only after the kids loitering out front had left did the guard notice me. He addressed me politely.

[P120]
“What brings you here?”

[P121]
“I’d like to purchase something.”

[P122]
“Please present your membership card or Hunter certification.”

[P123]
“Here.”

[P124]
“I’ll need to complete the verification process.”

[P125]
Only after my certification had been checked and my fingerprints scanned was I given an admission pass.

[P126]
“As a C-rank Hunter, you may access up to the third floor.”

[P127]
The Store stocked different items on each floor. I had visited once when I was an F-rank Hunter, but the second floor had been the highest I could access at the time. I had never even gotten to look around above it.

[P128]
“Have a pleasant time.”

[P129]
“Thanks. Take care.”

[P130]
Once I passed through the doors, I saw endless rows of glass display cases.

[P131]
The space was incomparably larger than an ordinary shop, yet there were only a handful of customers in sight.

[P132]
*Well, it would be strange if this place were crowded.*

[P133]
Only a tiny minority could shop here: Hunters, who made up just 0.1 percent of Korea’s population, and civilians with enough social influence to be issued membership cards.

[P134]
They were the Store’s main customers.

[P135]
“This item was manufactured by domestic S Company and has a built-in alarm spell, making it useful for security…”

[P136]
“This brooch was made by overseas M Company. With its beautiful, tasteful design and built-in shield spell, it’s perfect for your wife’s personal protection…”

[P137]
The employees were busy explaining their products to customers.

[P138]
That was right. The Store was a kind of luxury department store where people could buy expensive magical goods that were difficult to obtain through ordinary channels.

[P139]
“Then I’ll take that one and this one. Bring me that, too.”

[P140]
“Don’t you have anything with better performance? Don’t worry about the price. Bring me some options.”

[P141]
There might not have been many customers, but their purchasing power was unmatched.

[P142]
I was staring blankly at people buying goods that cost at least several million won when a pretty female employee approached and bowed.

[P143]
“Hello. I’m Assistant Manager Kim Seonhee from the Ilsan Store. I’ll be assisting you today.”

[P144]
“Ah, yes.”

[P145]
They had treated me politely the last time I visited, too, but not to this extent.

[P146]
Now that I was a C-rank Hunter, the customer service was considerably more attentive.

[P147]
“Is there a particular product you’re looking for?”

[P148]
“I’d like to buy some raid equipment.”

[P149]
The employee’s expression brightened. The Store carried countless magical goods, but Hunter equipment was among the most expensive of them all.

[P150]
And I was a C-rank Hunter. Even a mid-level Hunter could spend hundreds of millions of won on a single piece of equipment.

[P151]
Naturally, a sales employee would be delighted at the thought of adding that kind of sale to her record.

[P152]
“I’ll show you to the third floor.”

[P153]
As she turned toward the escalators, I spoke.

[P154]
“No, please take me to the second floor.”

[P155]
“Pardon? But to purchase C-rank Hunter equipment, you’ll need to go to the third floor…”

[P156]
“It’s fine. I’m looking for weapons for low-rank Hunters.”

[P157]
I pretended not to notice her expression darkening and stepped onto the escalator first.

[P158]
*I wonder if they have anything useful for killing rats.*

[P159]
The time had come to fill my Inventory.

[P160]
* * *

[P161]
“It’s fine. I’m looking for weapons for low-rank Hunters.”

[P162]
Assistant Manager Kim Seonhee secretly sighed at the customer’s words. As someone unusually concerned about her sales numbers, this was far from welcome news.

[P163]
*I need a good sales record this month if I want to get promoted.*

[P164]
The colleague who had joined the company at the same time as her and worked at the Seoul branch was already a Team Leader. Whether it was luck or business savvy, every customer she encountered was apparently a big spender.

[P165]
Compared to her…

[P166]
“This one looks good.”

[P167]
“Ah, yes. This product was manufactured using an F-rank Magic Gem…”

[P168]
Kim Seonhee quickly pulled herself together and began her explanation. The customer had picked up a dagger with a black-painted blade.

[P169]
Compared to the other weapons, it was nothing special. It did not even have magic embedded in it. It was just an ordinary consumable.

[P170]
“How much is it?”

[P171]
“It’s currently on sale as part of our summer promotion, so we’re offering it at the low price of 520,000 won.”

[P172]
“Hmm. That’s expensive.”

[P173]
“…”

[P174]
How much did a C-rank Hunter make a year again? Didn’t their basic allowances alone amount to several hundred million won? Kim Seonhee found it ridiculous, but silently waited for the customer to make his choice.

[P175]
“Ah, well, I guess it can’t be helped. I’ll buy it. Give me one.”

[P176]
“…Yes.”

[P177]
The look on his face, as if parting with the money were killing him, was utterly obnoxious. Kim Seonhee swallowed a curse as she picked up the dagger when—

[P178]
“No. Not that one.”

[P179]
“Excuse me?”

[P180]
“The one next to it.”

[P181]
Her gaze shifted to the side. One hundred daggers were neatly arranged inside a storage box.

[P182]
“They’re the same product, sir.”

[P183]
“I know. Give me one of those.”

[P184]
“…Are you referring to that storage box?”

[P185]
“Yes. Give me one box of those. And one box of that, too. And that one…”

[P186]
That was the moment Assistant Manager Kim Seonhee’s worries about her sales numbers disappeared.
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
# Chapter 93

[P2]
*What a bunch of amateurs.*

[P3]
Hong Woojin was furious enough to burst. If he had entered the cat’s body like last time, he would have puffed up its fur and hissed.

[P4]
But right now, he was a rice weevil smaller than a fingernail. The most he could do to express his anger was hide in the gap beneath the refrigerator and wriggle.

[P5]
Bzzzzzz.

[P6]
*That bastard’s coming in again.*

[P7]
The target of his anger was the fly that kept entering the house.

[P8]
Woojin did not know who was behind them, but whoever it was seemed to think they were being careful by sneaking the flies in one at a time. Instead, they were only putting Jin Taekyung further on guard.

[P9]
“Ugh, these damn flies.”

[P10]
Whoosh. Smack!

[P11]
A predictable end. Hong Woojin grew anxious, worried that Jin Taekyung might notice him.

[P12]
*Bastards like that have no professional courtesy, and they’re stupid on top of it.*

[P13]
Most Hunters would never have noticed, but he recognized it immediately.

[P14]
That fly was a Familiar being controlled by a mage. The proof was the incredibly faint mana that only another mage could sense.

[P15]
*Who hired the bastard? Sangdong Guild, after all?*

[P16]
If that was the case, he would have to quit this assignment right away. He was a professional with immense pride in his abilities.

[P17]
He could not tolerate an intruder interfering with his sacred workspace.

[P18]
*I told them over and over…*

[P19]
No matter how well you handled a job, there were times when a single loach released by an impatient client muddied the water. Just like now.

[P20]
“Are all flies like that these days?”

[P21]
“Th-They could be, couldn’t they? Anyway, give me the hundred thousand won.”

[P22]
“I will. I’ll give it to you, but… don’t you think that fly’s a little strange?”

[P23]
Damn it. He knew this would happen.

[P24]
Swallowing his curses, Hong Woojin hurriedly moved his body. He was wriggling deeper into a place no human eyes could reach when—

[P25]
A jolt.

[P26]
*…Huh?*

[P27]
He was seized by a strange sensation, as if his body had suddenly floated into the air. It had never happened once since he began using Familiar magic.

[P28]
*Is it because this Familiar is too small?*

[P29]
The sensation lasted only an instant, but Hong Woojin could not shake off his unease. For a moment, he wondered whether it had been some kind of detection spell, but he soon shook his head.

[P30]
*It definitely wasn’t magic.*

[P31]
That was not merely because Jin Taekyung was a non-mage Hunter. After all, this was a world where anyone could obtain magical equipment if they had enough money.

[P32]
But mages recognized their own kind. As a B-rank mage, there was no way he could fail to distinguish a detection spell.

[P33]
*The connection must have weakened for a moment. Yes. That has to be it.*

[P34]
The decisive reason he convinced himself it had been a simple illusion was Jin Taekyung’s reaction.

[P35]
“Maybe its wing’s injured. This fly’s looking pretty weak.”

[P36]
Smack!

[P37]
With a crisp sound, Jin Taekyung returned to the living room and sprawled out on the sofa. He chuckled at a variety show for a while, but soon the house was filled with loud snoring instead of laughter.

[P38]
Grrrrr. Grrrrr.

[P39]
Only then did Hong Woojin relax.

[P40]
*Of course. What could a C-rank Hunter who was an F-rank until recently possibly know? What happened two days ago must have been a complete coincidence, too.*

[P41]
The incident from two days ago still lingered in the back of his mind. He had been watching Jin Taekyung through a cat Familiar and had been startled by what happened. For some reason, it had continued to bother him ever since. Now, at last, he felt he could breathe a little easier.

[P42]
*If he can’t even recognize a shoddy Familiar like this, then that says it all.*

[P43]
There was only one problem: the lazy bastard had no intention of moving at all…

[P44]
*I’ll have to monitor him a little more boldly from now on.*

[P45]
Hong Woojin had chosen a rice weevil from among all the living creatures in the world because he had retained a sliver of caution toward Jin Taekyung.

[P46]
But now, it seemed safe to leave the body of this tiny, painfully slow insect.

[P47]
*Let’s meet in a different form tomorrow, Jin Taekyung.*

[P48]
Pop.

[P49]
Hong Woojin severed the Link. The creature hiding beneath the refrigerator was no longer a Familiar. It was nothing more than a small, fragile rice weevil.

[P50]
And then—

[P51]
Grrrrr…

[P52]
Jin Taekyung’s snoring gradually faded before stopping altogether.

[P53]
* * *

[P54]
A faint presence disappeared. I could sense the change only because I was using every one of my senses.

[P55]
*Did he leave?*

[P56]
I opened my eyes while pretending to stretch. The first place I looked was the gap beneath the refrigerator.

[P57]
> **System**
>
> Lv. 1 Rice Weevil

[P58]
Only ten minutes ago, its Level window had carried the tag “Familiar.” Not anymore—not with the Link severed.

[P59]
“Yaaawn. Is there anything to eat…?”

[P60]
I got up from the sofa and casually walked around the house. Only then could I be certain.

[P61]
*There aren’t any Familiars left.*

[P62]
The only things caught by my Qi Sense were a few ordinary flying insects. There was no Familiar anywhere.

[P63]
The buzzing of wings that had continued without pause had stopped, too.

[P64]
They had probably gotten spooked by what just happened, so at least they would not show their faces for the rest of the day.

[P65]
*Damn it. A Familiar?*

[P66]
Familiar magic.

[P67]
It was a kind of mental magic used by mages. The caster formed a mental connection with the creature chosen as a Familiar and, depending on the caster’s skill, could even control it at will.

[P68]
*That was my first time experiencing it firsthand.*

[P69]
A melee Hunter was not automatically a master of every weapon, and mages were the same. Mental magic, in particular, was said to be among the more difficult branches.

[P70]
*Why would people like that come after me?*

[P71]
The reason I thought of them as “people” rather than “someone” was that there had been two Familiars. The two could have been working together, or they might not have been.

[P72]
Still, I had a rough idea of who had sent them.

[P73]
*Who else could it be but Sangdong Guild?*

[P74]
The only place I had formed some kind of grudge against in the real world was Sangdong Guild. More precisely, Im Changsoo.

[P75]
*When you mess with someone’s child, the father comes running.*

[P76]
Im Chunsoo, the A-rank Hunter known for being cold-blooded and foul-tempered.

[P77]
If what happened today was his order, this would not end easily.

[P78]
But…

[P79]
*I can’t just sit back and take it.*

[P80]
I could let the fact that they had followed me two days ago go. I could tolerate that.

[P81]
But I could not tolerate what happened today. This was my home, the place where my beloved family lived. They had touched my one inviolable boundary.

[P82]
*How should I screw these bastards over…?*

[P83]
I was thinking about it when Hayeon’s bedroom door flew open.

[P84]
Her face was stiff. Had they used a Familiar to pull something behind my back? My thoughts grew frantic.

[P85]
“Oppa.”

[P86]
“What is it? What happened? Is there something strange in your room?”

[P87]
“No, it’s not that.”

[P88]
“Then what is it?”

[P89]
“Why haven’t you given me the hundred thousand won?”

[P90]
“…”

[P91]
Right. I had been underestimating you far too much.

[P92]
* * *

[P93]
The next morning, I left the house as soon as dawn broke.

[P94]
My eyes felt gritty from staying alert all night in preparation for another Familiar’s intrusion with Qi Sense, but I shook off the fatigue by circulating my qi.

[P95]
“Where should I take you?”

[P96]
“Ilsan Lafesta, please.”

[P97]
The taxi sped along the wide-open roads without a hitch, reaching the destination much faster than I had expected.

[P98]
*Is this my first time coming to the Store since I visited once a few years ago?*

[P99]
The Store, located in the center of Ilsan, stood out clearly even from a distance. For one thing, it was overwhelmingly larger and more splendid than the shops around it.

[P100]
There was another thing that set it apart from ordinary stores. At the entrance, guards in suits were screening the customers.

[P101]
“Sir, we’re adults, I’m telling you!”

[P102]
“No.”

[P103]
“We’re adults, so why aren’t we allowed inside?”

[P104]
“Because the fingerprint scanner says you’re not adults.”

[P105]
“Isn’t it defective?”

[P106]
“No.”

[P107]
“Ah, shit, just let us in!”

[P108]
“‘Shit’?”

[P109]
Five or six teenagers who looked obviously young flinched and took a step back.

[P110]
“…What?”

[P111]
“Is that any way to treat customers?”

[P112]
“Customers? Ha. You little shits, seriously.”

[P113]
The guard rubbed the corners of his eyes with a weary expression. He was not an ordinary adult man but a hired guard Hunter. Even if a whole crowd of professional fighters came instead of five or six minors, they would not be able to force their way in.

[P114]
“Customers to me are Hunters or civilian adults who’ve been issued membership cards. Not high school punks like you.”

[P115]
“…”

[P116]
“Are you leaving while I’m asking nicely, or should I call the police?”

[P117]
People like that existed everywhere. Especially in a Store filled with all kinds of goods ordinary people could never access.

[P118]
“…Hey, hey. Let’s go.”

[P119]
Only after the kids loitering in front had left did the guard notice me. He addressed me politely.

[P120]
“What brings you here?”

[P121]
“I’d like to purchase something.”

[P122]
“Please present your membership card or Hunter certification.”

[P123]
“Here.”

[P124]
“I’ll need to complete the verification process.”

[P125]
Only after my certification had been checked and my fingerprints scanned was I given an admission pass.

[P126]
“As a C-rank Hunter, you may access up to the third floor.”

[P127]
The items stocked on each floor of the Store were different. I had visited once when I was an F-rank Hunter, but the second floor had been the highest I could access at the time. I had never even gotten to look around above it.

[P128]
“Have a pleasant time.”

[P129]
“Thank you. Have a good one.”

[P130]
Once I passed through the doors, I saw endless rows of glass display cases.

[P131]
The space was incomparably larger than an ordinary shop. Yet there were only a handful of customers in sight.

[P132]
*Well, it would be strange if this place were crowded.*

[P133]
The people who could use this place were an extremely small minority: Hunters, who made up only 0.1 percent of Korea’s total population, and civilians with enough social influence to be issued membership cards.

[P134]
They were the Store’s main customers.

[P135]
“This item was manufactured by domestic S Company and has a built-in alarm spell, making it useful for security…”

[P136]
“This brooch was made by overseas M Company. With its beautiful, tasteful design and built-in shield spell, it’s perfect for your wife’s personal protection…”

[P137]
The employees were busy explaining their products to customers.

[P138]
That was right. The Store was a kind of luxury department store where people could buy expensive magical goods that were difficult to obtain through ordinary channels.

[P139]
“Then I’ll take that one and this one. Bring me that, too.”

[P140]
“Don’t you have anything with better performance? Don’t worry about the price. Bring me some options.”

[P141]
There might not have been many customers, but their purchasing power was unmatched.

[P142]
I was staring blankly at people buying goods that cost at least several million won when a pretty female employee approached and bowed.

[P143]
“Hello. I’m Assistant Manager Kim Seonhee from the Ilsan Store. I’ll be assisting you today.”

[P144]
“Ah, yes.”

[P145]
She had treated me politely the last time I visited, too, but not to this extent.

[P146]
Now that I was a C-rank Hunter, the customer service was considerably more lavish.

[P147]
“Is there a particular product you’re looking for?”

[P148]
“I’d like to buy some raid equipment.”

[P149]
The employee’s expression brightened. The Store carried countless magical goods, but Hunter equipment was among the most expensive of them all.

[P150]
And I was a C-rank Hunter. Even a mid-level Hunter could spend hundreds of millions of won on a single piece of equipment.

[P151]
Naturally, a sales employee would be delighted at the thought of adding that kind of sale to her record.

[P152]
“I’ll show you to the third floor.”

[P153]
As she turned toward the escalators, I spoke.

[P154]
“No, please take me to the second floor.”

[P155]
“Pardon? But to purchase C-rank Hunter equipment, you’ll need to go to the third floor…”

[P156]
“It’s fine. I’m looking for weapons for low-rank Hunters.”

[P157]
I pretended not to notice her expression darkening and stepped onto the escalator first.

[P158]
*I wonder if they have anything useful for killing rats.*

[P159]
The time had come to fill my Inventory.

[P160]
* * *

[P161]
“It’s fine. I’m looking for weapons for low-rank Hunters.”

[P162]
Assistant Manager Kim Seonhee secretly sighed at the customer’s words. As someone who was unusually concerned with her sales numbers, this was far from welcome news.

[P163]
*I need a good sales record this month if I want to get promoted.*

[P164]
The colleague who had joined the company at the same time as her, but worked at the Seoul branch, was already a Team Leader. Whether it was because of luck or business savvy, every customer she encountered was apparently a big spender.

[P165]
Compared to her…

[P166]
“This one looks good.”

[P167]
“Ah, yes. This product was manufactured using an F-rank Magic Gem…”

[P168]
Kim Seonhee quickly pulled herself together and began her explanation. The customer had picked up a dagger with a black-painted blade.

[P169]
Compared to the other weapons, it was nothing special. It did not even have magic embedded in it. It was just an ordinary consumable.

[P170]
“How much is it?”

[P171]
“It’s currently on sale as part of our summer promotion, so we’re offering it at the reasonable price of 520,000 won.”

[P172]
“Hmm. That’s expensive.”

[P173]
“…”

[P174]
What was the annual salary of a C-rank Hunter again? Didn’t their basic allowances alone amount to several hundred million won? Kim Seonhee found it ridiculous, but silently waited for the customer to make his choice.

[P175]
“Ah, well, I guess it can’t be helped. I’ll buy it. Give me one.”

[P176]
“…Yes.”

[P177]
The look on his face, as if parting with the money were killing him, was utterly obnoxious. Kim Seonhee was silently cursing him to herself as she picked up the dagger when—

[P178]
“No. Not that one.”

[P179]
“Excuse me?”

[P180]
“The one next to it.”

[P181]
Her gaze shifted to the side. One hundred daggers were neatly arranged inside a storage box.

[P182]
“They’re the same product, sir.”

[P183]
“I know. Give me one of those.”

[P184]
“…Are you referring to that storage box?”

[P185]
“Yes. Give me one box of those. And one box of that, too. And that one…”

[P186]
That was the moment Assistant Manager Kim Seonhee’s worries about her sales numbers disappeared.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진태경    | **Jin Taekyung**   |
| 임춘수    | **Im Chunsoo**    |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 레벨               | **Level**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 대한민국 | **Korea** | Country reference. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 93,
  "passed": true,
  "metrics": {
    "source_characters": 6243,
    "translation_characters": 13980,
    "length_ratio": 2.239,
    "source_paragraphs": 186,
    "translation_paragraphs": 186
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "운기조식",
        "preferred": "circulate one's qi"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "등급",
        "preferred": "Grade"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "매력",
        "preferred": "Charm"
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
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "상동",
        "romanization": "sangdong"
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
