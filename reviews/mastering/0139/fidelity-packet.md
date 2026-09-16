# Fidelity Gate — Chapter 139

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
  1|＃139화
  2|
  3|
  4|
  5|진태경 일행을 태운 육두마차가 출발하고 채 한 시진도 되지 않아 태원 거리는 다시 한번 뜨겁게 달아올랐다.
  6|
  7|사두마차를 둘러싼 오십 기의 기마, 그리고 형형한 눈빛을 뿜어내는 무인들 때문이었다.
  8|
  9|“저건…….”
 10|
 11|“태원진가다!”
 12|
 13|“와아아아!”
 14|
 15|“아까는 산서잠룡이고 이제는 태원진가야? 오늘 눈 호강 제대로 하는구먼.”
 16|
 17|마차 안, 사방에서 쏟아지는 환호를 듣고 있던 진위경의 귀가 쫑긋 섰다.
 18|
 19|“무경아, 방금 들었느냐?”
 20|
 21|진무경이 하품을 하며 고개를 끄덕였다.
 22|
 23|“예. 들었습니다.”
 24|
 25|“위팽, 자네도?”
 26|
 27|위팽 역시 지긋지긋하다는 표정으로 대답했다.
 28|
 29|“제가 들었건 말건 신경 안 쓰시잖습니까. 그냥 말씀하십쇼.”
 30|
 31|“자넨 말을 왜 그렇게 하나? 그러면 속이 시원해?”
 32|
 33|“속이 시원하긴요, 지금도 화병 나게 생겼는데요. 그래서 하고 싶으신 말이 뭡니까?”
 34|
 35|“방금 사람들이 그러는데 태경이가…….”
 36|
 37|“와, 미치겠네.”
 38|
 39|진위경은 위팽의 중얼거림을 못 들은 척하며 말을 이었다.
 40|
 41|“성주와의 오찬에 참석하러 간 모양일세. 지금쯤이면 도착했을지도 모르고.”
 42|
 43|“도착했겠죠. 엎어지면 코 닿을 거린데.”
 44|
 45|“혹시 무슨 일이라도 생기는 건 아니겠지?”
 46|
 47|“삼공자가 무슨 물가에 내놓은 어린아이도 아니고. 상다리가 부러지도록 극진한 대접을 받고 있을 테니 걱정일랑 접어 두십시오.”
 48|
 49|“글쎄, 워낙 자유분방한 아이라.”
 50|
 51|위팽이 그게 무슨 개소리냐는 듯 눈을 동그랗게 떴다.
 52|
 53|“자유분방이라뇨. 이 경우는 천방지축 아닙니까?”
 54|
 55|“크흠.”
 56|
 57|“그냥 사고 칠 것 같아서 걱정된다고 말씀하시면 되지, 뭘 또 그렇게…….”
 58|
 59|“그 입 다물게.”
 60|
 61|“예. 그럼 아무 말도 안 할 테니까 정 걱정되시면 저기 있는 이공자한테 물어보십쇼.”
 62|
 63|심드렁한 대답에 진위경의 시선이 슬쩍 옆으로 옮겨 갔다.
 64|
 65|사실 위팽의 조언은 적절했다. 이 중에서 현 산서 성주와 한 번이라도 대면해 본 적이 있는 사람은 진무경뿐이니까.
 66|
 67|‘더 말을 안 해 줘서 문제지.’
 68|
 69|산서 성주와의 오찬을 그냥 ‘개 같았다’는 한마디로 일축한 진무경은 그 후로 입을 굳게 다물고 있었다.
 70|
 71|“무경아, 혹시…….”
 72|
 73|말이 채 이어지기도 전에 대답이 돌아왔다.
 74|
 75|“아무 문제 없을 겁니다.”
 76|
 77|단칼 같은 대답에 진위경이 안도의 한숨을 내쉴 때, 진무경이 한마디를 덧붙였다.
 78|
 79|“비위가 좋다면요.”
 80|
 81|“……비위라니? 갑자기 그게 무슨 소리냐?”
 82|
 83|황족이며 성주가 주최하는 식사 자리다. 성대한 연회에 구더기가 들끓는 음식이라도 나온단 말인가?
 84|
 85|순간 어리둥절해진 그의 시선에 서서히 일그러지는 진무경의 얼굴이 보였다.
 86|
 87|“있습니다. 벌레만큼 징그러운 놈이.”
 88|
 89|
 90|
 91|* * *
 92|
 93|
 94|
 95|성주가 머무른다는 이곳, 산서성부(山西城府)는 저택의 형태를 벗어난 지 오래였다.
 96|
 97|태원진가도, 얼마 전에 다녀왔던 항산검문도 상당한 규모였지만 이곳에 비하면 우스울 정도다.
 98|
 99|‘이걸 뭐라고 불러야 하나. 요새? 아니면 성?’
100|
101|대륙 스케일이 큰 건 진작 알고 있었지만, 상상 이상이다.
102|
103|나는 물론이고 청풍과 후기지수들도 입을 쩍 벌리고 주위를 둘러보았다. 그러자 관리가 슬며시 웃는다.
104|
105|“어떻소?”
106|
107|“넓네요. 엄청나게.”
108|
109|“능히 수천 명을 수용하고도 남으니 그럴 수밖에. 전시에 수성하게 된다면 십 년을 버틸 만한 곡식도 있다오.”
110|
111|관리는 거대한 창고 몇 개를 차례대로 가리켰다. 저 안에 식량이 가득 채워져 있다는 말도 덧붙였다.
112|
113|“저 많은 곳에 전부 다요?”
114|
115|“물론이오.”
116|
117|강남 아파트 입주민처럼 자부심 넘치는 미소를 띤 관리가 말을 이었다.
118|
119|“성부라는 곳은 전시를 대비하여 크고 단단하게 짓기 마련이지만, 본래 이 정도 크기는 아니라오.”
120|
121|“그럼……?”
122|
123|“이곳에 어떤 분이 사시는지 벌써 잊었소?”
124|
125|“아.”
126|
127|그랬지. 그냥 성주도 아니고 황족. 거기에 더해 정식으로 왕 작위도 가진 어엿한 임금님이 살고 있댔다.
128|
129|“그럼 여기가 왕궁?”
130|
131|“그런 셈이오.”
132|
133|우리는 촌놈처럼 주위를 두리번거리며 계속 이동했다.
134|
135|시선이 닿는 곳마다 하인과 시비들이 바쁘게 움직였고, 군기가 바짝 든 정예군들은 경계를 서거나 연무장에서 대련을 벌이고 있었다.
136|
137|‘수준이 제법인데?’
138|
139|가장 의외였던 점은 군사들의 질이 상당히 높다는 사실이었다.
140|
141|경계를 서는 인원 중 대부분이 레벨 20 전후였고, 제법 그럴싸한 갑주를 차려입은 장수들의 경우에는 일류를 가뿐히 넘겼다.
142|
143|‘하긴, 버젓이 있는 무공을 굳이 익히지 말라는 법은 없으니까.’
144|
145|오히려 군대가 강성해지는 거니 장려해야 할 일이다.
146|
147|나는 걸음을 옮기면서 계속 연무장을 곁눈질했다.
148|
149|둥! 둥! 둥!
150|
151|“찔러!”
152|
153|“악!”
154|
155|이미 해가 중천에 걸린 정오.
156|
157|북소리에 맞춰 수백의 창날이 빛나고, 군사들이 한 몸처럼 일사불란하게 모이고 흩어진다.
158|
159|전법과 전술, 대형을 훈련받는 그들을 보고 있자니 문득 한 단어가 떠올랐다.
160|
161|‘레이드 팀.’
162|
163|통일된 무기 종류. 체계적인 훈련을 통해 맞춘 합(合)은 대규모 집단전에서 무시무시한 위력을 발휘할 것이다.
164|
165|‘개개인의 실력은 무림인들보다 떨어지겠지만.’
166|
167|수십 대 수십의 싸움이라면 몰라도 수백 대 수백, 수천 대 수천의 전투가 벌어진다면 어지간한 절정 고수로는 전세를 뒤엎을 수 없다.
168|
169|그게 바로 훈련된 집단의 무서움이다.
170|
171|‘떨어지는 질은 물량과 훈련으로 메운다, 이건가.’
172|
173|지난 수백 년간 광활한 영토를 지배해 왔다는 통일 제국답다.
174|
175|그 자존심 강한 무림인들이 대국의 백성임을 인정하는 데에는 지금 같은 이유도 한몫하지 않았을까.
176|
177|그런데…….
178|
179|‘이거 뒀다가 어따 써. 엿 바꿔 먹나?’
180|
181|당장 눈에 보이는 군사들만 수백이 넘어간다. 저 중에 일부만이라도 산서 북부로 보냈으면 적풍단은 진작 빤쓰런 했을 거다.
182|
183|‘시벌, 누구는 죽을 고비 넘겨 가면서 그 고생을 했는데.’
184|
185|무능한 공권력의 실체를 보자 갑자기 현자 타임이 찾아온다.
186|
187|천하제일의 명검을 갖고 있으면 뭐 해. 검갑에서 뽑지 않으면 몽둥이나 다름없는데.
188|
189|내심 욕을 퍼붓고 있을 때 관리가 입을 열었다.
190|
191|“자, 이제 거의 다 도착했소.”
192|
193|그의 말대로였다. 수십여 개의 기둥이 늘어선 긴 회랑의 끝, 거대한 철문이 모습을 드러내자 양옆으로 긴장된 한숨이 흘러나온다.
194|
195|“휴우우.”
196|
197|“후우. 어떡해요, 정 소협? 나 너무 떨려요.”
198|
199|“걱정 마시오. 내가 있잖소.”
200|
201|“……지랄 염병하네.”
202|
203|될 놈은 된다더니 그 와중에 어떻게 눈이 맞은 건지 모르겠다.
204|
205|함께 빠따를 맞으면서 애정이 싹튼 건가?
206|
207|‘이게 나라냐.’
208|
209|솔로부대 투 스타로서 불편한 심기를 숨기지 못하는 내게 경쾌한 발걸음으로 걷고 있던 청풍이 밝은 목소리로 물었다.
210|
211|“저 안에 왕이 있는 건가요?”
212|
213|왕. 그 한 글자에 산서오문의 후기지수들이 입을 딱 벌렸고, 앞서 걷던 관리는 벌에라도 쏘인 것처럼 펄쩍 뛰었다.
214|
215|“와, 왕이라니! 무엄하오!”
216|
217|“어? 왕 아니에요?”
218|
219|“왕이 아니긴! 당연히 왕이지!”
220|
221|“그럼 왕 맞지 않아요?”
222|
223|“아니, 그게 아니고……!”
224|
225|이러다가는 둘 중 하나다. 관리가 고혈압으로 쓰러지거나, 역모죄를 들먹이면서 당장 연무장에서 훈련 중인 수백 명의 군사를 부르거나.
226|
227|둘 중 어느 것도 원하지 않는 내가 중재에 나섰다.
228|
229|“일단 좀 진정하시고, 그리고 청 공자.”
230|
231|“예, 은인.”
232|
233|“왕이라고 하면 안 됩니다. 전하라고 해야 돼요. 맞죠?”
234|
235|마지막 질문은 관리를 향한 거다. 그가 청풍을 노려보며 맹렬하게 고개를 끄덕였다.
236|
237|“반드시! 무조건 그래야 하오!”
238|
239|“아, 정말요?”
240|
241|“휴, 그렇소.”
242|
243|청풍이 맑은 눈동자를 깜빡였다.
244|
245|“왜요?”
246|
247|“……진 공자. 정말 이놈, 아니 이자를 데려가야겠소?”
248|
249|“전 빼도 상관없긴 한데. 괜찮으시겠어요?”
250|
251|관리는 잠깐 침묵했다.
252|
253|청풍을 빼고 다섯 명을 데려가면 상부의 문책과 함께 직장이 날아갈 것이고, 청풍이 혓바닥 한 번 잘못 놀렸다가는 목이 날아갈 것이다.
254|
255|잠시 후, 다시 입을 연 그의 얼굴은 십 년은 늙어 있었다.
256|
257|“……그냥 갑시다.”
258|
259|청풍이 활짝 웃었다.
260|
261|“감사합니다. 혹시 시간 되면 왕, 아니 전하한테 잘 말씀드려 볼게요.”
262|
263|“그쪽 양반은 제발 입만 다물고 있어 주시오.”
264|
265|관리가 간곡한 부탁과 함께 주의해야 할 점을 줄줄이 읊는 동안 우리는 마침내 철문 앞에 도착했다.
266|
267|척 봐도 엄청나게 크고 두꺼운 철문 뒤에서 두런두런 목소리가 흘러나오고 있었다.
268|
269|‘도지휘첨사, 화산파, 모욕?’
270|
271|단편적인 단어들만 들어서는 도저히 무슨 대화를 나누고 있는 건지 알 도리가 없다. 다만…….
272|
273|‘분위기는 영 아닌 것 같은데?’
274|
275|마주 보며 밥 먹기에는 썩 좋은 자리가 아닌 것 같다는 직감이 든 그때, 철문 앞에 시립해 있던 이가 크게 외쳤다.
276|
277|“산서 무림의 후기지수들이 뵙기를 청합니다!”
278|
279|그그긍.
280|
281|외침과 동시에 철문이 열리기 시작했다.
282|
283|관리가 걱정스러운 얼굴로 마지막 당부를 건넸다. 슬쩍 청풍을 곁눈질하면서.
284|
285|“저 인간 주둥이만 막아 주시오.”
286|
287|“……아, 예.”
288|
289|정말 어지간히 걱정되나 보다.
290|
291|
292|
293|* * *
294|
295|
296|
297|들어가자마자 눈앞이 환해지는 기분이었다.
298|
299|호화롭게 꾸며진 대전은 마법 학교를 배경으로 한 영화에서나 보던 넓은 탁자와 온갖 음식으로 가득했다.
300|
301|그리고 미리 와 있던 다섯 사람을 본 순간, 딱 한 가지 생각이 머릿속을 스쳤다.
302|
303|‘조졌군.’
304|
305|눈치 빠르기로는 둘째가라면 서러운 나다. F급 헌터로 눈칫밥을 하도 처먹다 보니 0.1초면 분위기 파악이 끝난다.
306|
307|바로 지금처럼.
308|
309|‘분위기 끝내주는데.’
310|
311|다섯 사람을 중심으로 팽팽하게 조여든 공기가 느껴진다. 밖에서부터 심상치 않음을 느끼긴 했지만 생각 이상이다.
312|
313|자리가 자리인지라 모두 빈손이기에 망정이지, 허리춤에 뭐라도 있었으면 당장 칼부림이 일어났을 거다.
314|
315|“이거…… 손님이 오셨으니 해후는 이쯤에서 마칠까요?”
316|
317|팽팽한 분위기를 흩어 놓은 것은 가냘픈 목소리의 사내였다.
318|
319|아니, 사내가 맞나? 여인이라고 생각될 정도로 가냘픈 체구에 얼굴은 희었고 입술은 염료라도 바른 듯 붉다.
320|
321|
322|
323|[Lv.22 홍진]
324|
325|
326|
327|그가 나를 향해 미소를 지어 보였다.
328|
329|“강호의 후기지수답게 훤칠한 미남이시네. 내 듣기로는 오늘 태원진가에서 젊은 영웅이 온다고 들었는데, 혹시……?”
330|
331|지금이 인사를 할 타이밍이다. 나는 다섯 사람을 향해 포권을 취했다.
332|
333|“태원진가의 진태경이라고 합니다.”
334|
335|순간 안 좋았던 분위기가 한결 누그러진다. 불쾌와 비웃음의 흔적이 남아 있던 네 사람의 얼굴 위로 놀라움이 덧칠해졌다.
336|
337|“태원진가의 진태경이라면…….”
338|
339|흑색 무복을 걸친 거한이 중얼거렸다.
340|
341|처음 봤을 때부터 상남자 냄새가 물씬 풍기던 그의 이름은 이풍, 머리 위에는 68레벨이라는 숫자가 떠다녔다.
342|
343|‘군문(軍門)에 소속된 사람인가?’
344|
345|첫 만남에서 모든 걸 판단할 수는 없지만 풍기는 냄새가 그렇다. 자존심 강하고 강직한 군인. 그것이 그의 첫인상이었다.
346|
347|‘이풍, 이풍이라. 68레벨이면…… 초일류 정도?’
348|
349|그의 이름과 레벨을 다시 한번 머릿속에 새겼을 때쯤 나머지 세 사람의 반응이 이어졌다.
350|
351|“흠. 저 친구가 산서잠룡이라고?”
352|
353|“젊은데? 아니, 어려.”
354|
355|“딱히 소문만큼 실력이 대단해 보이지는 않는데…….”
356|
357|신기한 듯 나를 바라보는 눈빛에는 놀라움과 약간의 질투, 그리고 미묘한 우월함이 담겨 있었다.
358|
359|대개 이런 경우에는 굳이 상대의 정체를 물어볼 필요가 없다. 자신을 자랑하기 위해 안달이 난 사람들이기 때문이다.
360|
361|“인사가 늦었군. 후배.”
362|
363|날카로운 눈매의 남자가 씩 웃으며 말을 걸어온다. 다른 두 명은 귀여운 병아리 보듯이 팔짱을 끼고 날 바라보는 중이었다.
364|
365|‘이거 묘하게 기분 나쁘네.’
366|
367|뭐 하는 놈들이기에 다짜고짜 선배 노릇일까?
368|
369|의문은 얼마 가지 않아 곧 풀렸다.
370|
371|“아, 아직 모르겠군. 우린 섬서에서 왔다네. 섬서 종남파(終南派), 들어 봤나?”
372|
373|나도 모르게 입이 벌어졌다.
374|
375|“조, 종남파? 그 종남파요?”
376|
377|세 사람의 얼굴에 한껏 웃음꽃이 피었다.
378|
379|“하하, 이 친구 너무 놀라는데?”
380|
381|“그러게 말이야.”
382|
383|“혹 우리 문파를 잘 아는가?”
384|
385|나는 잔뜩 흥분해서 외쳤다.
386|
387|“알죠! 잘 알죠! 얼마나 재밌게 봤는데!”
388|
389|“잘 안다니 기쁘…… 잠깐, 재밌게 보다니?”
390|
391|“뭐긴요. 그야 당연히 군림…….”
392|
393|대답하려다가 문득 깨달았다.
394|
395|아, 여긴 소설이 아니었지.
```

## Assembled English

```markdown
[P1]
# Chapter 139

[P2]
Less than a shichen after the six-horse carriage carrying Jin Taekyung and his group departed, the streets of Taiyuan heated up once again.

[P3]
This time, it was because of the fifty mounted soldiers surrounding the four-horse carriage, as well as the martial artists radiating sharp, piercing gazes.

[P4]
“That’s…”

[P5]
“It’s the Jin Family of Taiyuan!”

[P6]
“Woooooah!”

[P7]
“First the Sleeping Dragon of Shanxi, and now the Jin Family of Taiyuan? What a feast for the eyes today!”

[P8]
Inside the carriage, Jin Wikyung’s ears pricked up at the cheers pouring in from every direction.

[P9]
“Mukyung, did you hear that just now?”

[P10]
Jin Mukyung yawned and nodded.

[P11]
“Yes. I heard it.”

[P12]
“Wipeng, you too?”

[P13]
Wipeng answered with an exasperated expression.

[P14]
“You don’t care whether I heard it or not. Just say what you want to say.”

[P15]
“Why do you always speak like that? Does it make you feel better?”

[P16]
“Feel better? I’m about to give myself an ulcer as it is. So what did you want to say?”

[P17]
“Those people just said Taekyung…”

[P18]
“Wow. This is driving me insane.”

[P19]
Jin Wikyung pretended not to hear Wipeng’s muttering and continued.

[P20]
“It seems he’s on his way to attend a luncheon with the City Lord. He might even have arrived by now.”

[P21]
“He probably has. It’s just a stone’s throw away.”

[P22]
“You don’t think anything will happen, do you?”

[P23]
“The Third Young Master isn’t some little child left by the water. He’s probably being treated to such a lavish meal that the table legs are breaking. Stop worrying.”

[P24]
“I don’t know. He’s such a free-spirited child.”

[P25]
Wipeng’s eyes went round as though he were asking what the hell that was supposed to mean.

[P26]
“Free-spirited? Isn’t this more a case of him being reckless and out of control?”

[P27]
“Ahem.”

[P28]
“You could just say you’re worried he’ll cause trouble. Why dress it up like that…?”

[P29]
“Shut your mouth.”

[P30]
“Yes, my lord. I won’t say another word. If you’re really that worried, ask the Second Young Master over there.”

[P31]
At Wipeng’s indifferent reply, Jin Wikyung’s gaze shifted slightly to the side.

[P32]
In truth, Wipeng’s advice was appropriate. Jin Mukyung was the only person among them who had ever met Shanxi’s current City Lord, even once.

[P33]
*The problem is that he won’t tell us anything else.*

[P34]
Jin Mukyung had dismissed his luncheon with the Shanxi City Lord with a single phrase—*It was fucking awful*—and had firmly kept his mouth shut ever since.

[P35]
“Mukyung, by any chance…”

[P36]
The answer came before he could finish.

[P37]
“There shouldn’t be any problems.”

[P38]
Jin Wikyung let out a sigh of relief at the decisive answer, but Jin Mukyung added one more thing.

[P39]
“As long as he has a strong stomach.”

[P40]
“…A strong stomach? What are you talking about all of a sudden?”

[P41]
This was a meal hosted by a member of the imperial family and the City Lord. Was he saying they might serve food crawling with maggots at such a grand banquet?

[P42]
As Jin Wikyung stared at him in confusion, Jin Mukyung’s face slowly twisted.

[P43]
“There’s someone there as revolting as a bug.”

[P44]
* * *

[P45]
The Shanxi Provincial Office, where the City Lord resided, had long since ceased to resemble an ordinary estate.

[P46]
The Jin Family of Taiyuan and the Mount Heng Sword Sect, which I had visited not long ago, were both enormous, but they looked laughably small compared to this place.

[P47]
*What am I supposed to call this? A fortress? Or a castle?*

[P48]
I had known for a long time that the continent operated on a massive scale, but this was beyond anything I had imagined.

[P49]
Cheongpung, the other young prodigies, and I all gaped as we looked around. The official smiled faintly.

[P50]
“What do you think?”

[P51]
“It’s big. Extremely big.”

[P52]
“It can easily accommodate several thousand people, so it has to be. If we had to defend it during wartime, we even have enough grain to last ten years.”

[P53]
The official pointed to several enormous warehouses one after another. He added that they were filled with food.

[P54]
“All of those?”

[P55]
“Of course.”

[P56]
The official continued with a proud smile, like a resident of a Gangnam apartment showing off his building.

[P57]
“Provincial offices are generally built large and sturdy in preparation for wartime, but they aren’t normally this large.”

[P58]
“Then…?”

[P59]
“Have you already forgotten who lives here?”

[P60]
“Oh.”

[P61]
Right. He wasn’t merely the City Lord. He was a member of the imperial family. On top of that, he possessed an official royal title—a proper prince in his own right.

[P62]
“Then is this the royal palace?”

[P63]
“In a manner of speaking.”

[P64]
We continued moving, looking around like country bumpkins.

[P65]
Everywhere we looked, servants and maidservants hurried about their business, while elite soldiers with razor-sharp discipline stood guard or sparred in the training grounds.

[P66]
*They’re pretty good.*

[P67]
The most surprising thing was the remarkably high quality of the soldiers.

[P68]
Most of the soldiers standing guard were around Level 20, while the commanders wearing fairly impressive armor were comfortably above First Rate.

[P69]
*Well, it’s not as if there’s any reason soldiers shouldn’t learn martial arts when they’re readily available.*

[P70]
If anything, it would make the army stronger. It was something that ought to be encouraged.

[P71]
I kept walking while stealing glances at the training grounds.

[P72]
*Boom! Boom! Boom!*

[P73]
“Thrust!”

[P74]
“Argh!”

[P75]
It was noon, with the sun already high overhead.

[P76]
Hundreds of spearheads flashed in time with the drums, and the soldiers gathered and scattered in perfect unison, moving as one body.

[P77]
Watching them train in formations, tactics, and battle strategies, one word suddenly came to mind.

[P78]
*Raid team.*

[P79]
Uniform weapons. Coordination drilled into them through systematic training. In a large-scale battle, that kind of teamwork would display terrifying power.

[P80]
*Their individual skills might be inferior to those of Murim martial artists.*

[P81]
A battle of dozens against dozens might be another story, but if hundreds fought hundreds, or thousands fought thousands, even an ordinary Peak master couldn’t turn the tide by himself.

[P82]
That was the terrifying strength of a trained group.

[P83]
*Make up for inferior quality with numbers and training. Is that it?*

[P84]
It was exactly what one would expect from a unified empire that had ruled a vast territory for centuries.

[P85]
Wasn’t that part of the reason those proud Murim martial artists acknowledged that they were subjects of a Great Nation?

[P86]
And yet…

[P87]
*What the hell are they keeping all this for? To trade it in for candy?*

[P88]
There were already more than several hundred soldiers in sight. If even a portion of them had been sent to northern Shanxi, the Red Wind Band would have run so fast they’d have left their pants behind.

[P89]
*Fuck. Some of us nearly died going through all that trouble.*

[P90]
Seeing the true face of incompetent public authority suddenly plunged me into a spell of hollow enlightenment.

[P91]
What good was owning the finest sword under heaven? If you didn’t draw it from its scabbard, it was no different from a club.

[P92]
Just as I was cursing them inwardly, the official spoke.

[P93]
“Well, we’re almost there.”

[P94]
He was right. A massive iron gate came into view at the end of a long corridor lined with dozens of pillars, drawing anxious sighs from both sides.

[P95]
“Phew…”

[P96]
“Whew. What do I do, Young Hero Jeong? I’m so nervous.”

[P97]
“Don’t worry. You have me.”

[P98]
“…What a fucking load of bullshit.”

[P99]
They say people destined to succeed will succeed, but I had no idea how those two had managed to hit it off in the middle of all this.

[P100]
*Maybe getting beaten together made them fall for each other?*

[P101]
*What kind of country is this?*

[P102]
Unable to hide my discomfort as a two-star general of the Singles Brigade, I heard Cheongpung ask brightly as he walked along with a light step.

[P103]
“Is the king in there?”

[P104]
King.

[P105]
At that single word, the young prodigies of the Five Gates of Shanxi gaped, while the official leading us leaped as though he had been stung by a bee.

[P106]
“A king? How impudent!”

[P107]
“Huh? Isn’t he a king?”

[P108]
“Of course he’s a king!”

[P109]
“Then I was right, wasn’t I?”

[P110]
“No, that’s not what I mean…!”

[P111]
At this rate, one of two things would happen. The official would collapse from high blood pressure, or he would invoke treason and immediately summon the hundreds of soldiers training in the grounds.

[P112]
I wanted neither, so I stepped in to mediate.

[P113]
“First, calm down. And, Young Master Cheongpung.”

[P114]
“Yes, Benefactor.”

[P115]
“You can’t call him the king. You have to say ‘His Highness.’ Right?”

[P116]
I directed the last question at the official. He glared at Cheongpung and nodded furiously.

[P117]
“Absolutely! You must!”

[P118]
“Oh, really?”

[P119]
“Phew. Yes.”

[P120]
Cheongpung blinked his clear eyes.

[P121]
“Why?”

[P122]
“…Young Master Jin. Do we really have to take this bastard—I mean, this person—with us?”

[P123]
“I don’t mind leaving him out. But are you sure you’ll be all right?”

[P124]
The official fell silent for a moment.

[P125]
If he took five people without Cheongpung, he would be reprimanded by his superiors and lose his job. But if Cheongpung let his tongue slip just once, he might lose his head.

[P126]
A moment later, when he spoke again, his face looked ten years older.

[P127]
“…Let’s just go.”

[P128]
Cheongpung beamed.

[P129]
“Thank you. If there’s time, I’ll put in a good word with the king—I mean, His Highness.”

[P130]
“Please, just keep that gentleman’s mouth shut.”

[P131]
While the official rattled off every precaution we needed to take, along with his earnest pleas, we finally reached the iron gate.

[P132]
The gate was enormous and incredibly thick. Quiet voices drifted from behind it.

[P133]
*Assistant Military Commissioner, Huashan, insult?*

[P134]
Those fragments alone gave me no clue what they were discussing. Still…

[P135]
*The atmosphere doesn’t seem very good.*

[P136]
I had a feeling this wasn’t the best place for people to sit across from one another over a meal.

[P137]
At that moment, a man standing at attention before the gate shouted loudly,

[P138]
“The young prodigies of Shanxi Murim request an audience!”

[P139]
*Groooan.*

[P140]
The iron gate began to open at the same time.

[P141]
The official gave me one final warning with a worried expression, stealing a sidelong glance at Cheongpung.

[P142]
“Please just keep that man’s mouth shut.”

[P143]
“…Ah. Yes.”

[P144]
He must have been seriously worried.

[P145]
* * *

[P146]
The moment we entered, it felt as though my eyes had brightened.

[P147]
The lavishly decorated grand hall was filled with a long table like the ones I had only seen in movies set in magic schools, along with all kinds of food.

[P148]
And the moment I saw the five people who had arrived ahead of us, only one thought crossed my mind.

[P149]
*We’re screwed.*

[P150]
When it came to reading the room, I was second to none. After scraping by as an F-rank Hunter for so long, always watching everyone’s mood, I could size up an atmosphere in 0.1 seconds.

[P151]
Like right now.

[P152]
*What a wonderful atmosphere.*

[P153]
The air around the five people was pulled taut. I had sensed something was wrong from outside, but it was even worse than I had expected.

[P154]
It was fortunate everyone was empty-handed given the occasion. If they’d had anything hanging from their waists, swords would already have been drawn.

[P155]
“Well… Now that our guests have arrived, shall we end this reunion here?”

[P156]
A man’s delicate voice broke the tension.

[P157]
Though was he really a man? He was slender enough to seem like a woman, with a pale face and lips as red as though they had been painted with dye.

[P158]
> **System**
>
> Level 22: Hong Jin

[P159]
He smiled at me.

[P160]
“What a strikingly handsome young man, just as one would expect of a young prodigy of the martial world. I heard a young hero from the Jin Family of Taiyuan would be joining us today. Might that be you…?”

[P161]
Now was the time for introductions. I performed a fist-and-palm salute toward the five men.

[P162]
“My name is Jin Taekyung of the Jin Family of Taiyuan.”

[P163]
The unpleasant atmosphere immediately eased somewhat. Surprise painted over the traces of displeasure and ridicule lingering on the other four faces.

[P164]
“If you’re Jin Taekyung of the Jin Family of Taiyuan…”

[P165]
A huge man dressed in black martial robes muttered.

[P166]
From the moment I first saw him, he had radiated tough-guy energy. His name was Li Feng, and the number 68 hovered above his head.

[P167]
*Is he affiliated with the military?*

[P168]
I couldn’t judge everything from a first meeting, but that was the impression he gave. A proud and upright soldier. That was my first impression of him.

[P169]
*Li Feng, Li Feng… At Level 68, he’s probably an advanced First Rate?*

[P170]
Just as I was engraving his name and Level into my mind, the other three men reacted.

[P171]
“Hm. That’s the Sleeping Dragon of Shanxi?”

[P172]
“He’s young. No, he’s a child.”

[P173]
“He doesn’t particularly look as impressive as the rumors claim…”

[P174]
Their curious gazes held surprise, a hint of jealousy, and a subtle sense of superiority.

[P175]
In situations like this, there was usually no need to ask about the other person’s identity. They were the sort of people desperate to show off.

[P176]
“Apologies for the late introduction, Junior.”

[P177]
A sharp-eyed man grinned as he spoke to me. The other two stood with their arms folded, looking at me like I was a cute little chick.

[P178]
*This is weirdly irritating.*

[P179]
Who the hell were they to act like my Seniors right off the bat?

[P180]
My question was answered soon enough.

[P181]
“Oh, you don’t know yet, do you? We came from Shaanxi. The Zhongnan Sect of Shaanxi—have you heard of it?”

[P182]
My mouth fell open before I knew it.

[P183]
“Th-the Zhongnan Sect? *That* Zhongnan Sect?”

[P184]
The three men’s faces blossomed with smiles.

[P185]
“Haha! Look how surprised he is.”

[P186]
“Exactly.”

[P187]
“Perhaps you know our sect well?”

[P188]
I shouted, suddenly brimming with excitement.

[P189]
“I do! I know it very well! I had so much fun reading about it!”

[P190]
“We’re glad to hear you know us… Wait. What do you mean, ‘reading about it’?”

[P191]
“What else? Obviously, *The Reign…*”

[P192]
I stopped halfway through my answer.

[P193]
*Ah. This wasn’t a novel.*
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
# Chapter 139

[P2]
The six-horse carriage carrying Jin Taekyung and his group had been on the road for less than a shichen when the streets of Taiyuan heated up once again.

[P3]
This time, it was because of the fifty mounted soldiers surrounding the four-horse carriage, as well as the martial artists radiating sharp, piercing gazes.

[P4]
“That’s…”

[P5]
“It’s the Jin Family of Taiyuan!”

[P6]
“Woooooah!”

[P7]
“First the Sleeping Dragon of Shanxi, and now the Jin Family of Taiyuan? My eyes are getting spoiled today.”

[P8]
Inside the carriage, Jin Wikyung’s ears pricked up at the cheers pouring in from every direction.

[P9]
“Mukyung, did you hear that just now?”

[P10]
Jin Mukyung yawned and nodded.

[P11]
“Yes. I heard it.”

[P12]
“Wipeng, you too?”

[P13]
Wipeng answered with an exasperated expression.

[P14]
“You don’t care whether I heard it or not. Just say what you wanted to say.”

[P15]
“Why do you always speak like that? Does it make you feel better?”

[P16]
“Feel better? I’m about to give myself an ulcer as it is. So what did you want to say?”

[P17]
“People were saying that Taekyung…”

[P18]
“Wow. This is driving me insane.”

[P19]
Jin Wikyung pretended not to hear Wipeng’s muttering and continued.

[P20]
“It seems he’s on his way to attend a luncheon with the City Lord. He might even have arrived by now.”

[P21]
“He probably has. It’s close enough to touch if you fall over.”

[P22]
“I hope nothing happens.”

[P23]
“The Third Young Master isn’t some little child you’ve left beside a pond. He’s probably being treated to such an extravagant meal that the table legs are breaking. Stop worrying.”

[P24]
“I don’t know. He’s such a free-spirited child.”

[P25]
Wipeng’s eyes went round as though he were asking what the hell that was supposed to mean.

[P26]
“Free-spirited? Isn’t this more a case of him being reckless and out of control?”

[P27]
“Ahem.”

[P28]
“You could just say you’re worried he’ll cause trouble. Why do you have to dress it up like that…?”

[P29]
“Shut your mouth.”

[P30]
“Yes, my lord. Then I won’t say anything. If you’re really that worried, ask the Second Young Master over there.”

[P31]
At Wipeng’s indifferent reply, Jin Wikyung’s gaze shifted slightly to the side.

[P32]
In truth, Wipeng’s advice was appropriate. Jin Mukyung was the only person among them who had ever met Shanxi’s current City Lord, even once.

[P33]
*The problem is that he won’t tell us anything else.*

[P34]
Jin Mukyung had dismissed his luncheon with the Shanxi City Lord with a single phrase—*It was fucking awful*—and had firmly kept his mouth shut ever since.

[P35]
“Mukyung, by any chance…”

[P36]
Before he could finish, an answer came flying back.

[P37]
“There shouldn’t be any problems.”

[P38]
Jin Wikyung let out a relieved sigh at the decisive answer, but Jin Mukyung added one more thing.

[P39]
“If his stomach can handle it.”

[P40]
“…His stomach? What are you talking about all of a sudden?”

[P41]
It was a meal hosted by royalty and the City Lord. Was he saying they might serve food crawling with maggots at such a grand banquet?

[P42]
As confusion filled Jin Wikyung’s gaze, he saw Jin Mukyung’s face slowly twist.

[P43]
“There’s someone here as disgusting as a bug.”

[P44]
* * *

[P45]
The Shanxi Provincial Office, where the City Lord resided, had long since outgrown the shape of an ordinary estate.

[P46]
The Jin Family of Taiyuan and the Mount Heng Sword Sect, which I had visited not long ago, were both enormous, but compared to this place, they seemed laughably small.

[P47]
*What should I call this? A fortress? No, a castle?*

[P48]
I had known for a long time that the continent operated on a massive scale, but this was beyond anything I had imagined.

[P49]
Cheongpung and the other young prodigies gaped as they looked around. The official gave a small smile.

[P50]
“What do you think?”

[P51]
“It’s big. Extremely big.”

[P52]
“It can easily accommodate several thousand people, so it has to be. If we had to defend it during wartime, we even have enough grain to last ten years.”

[P53]
The official pointed to several enormous warehouses one after another. He added that they were filled with food.

[P54]
“All of those?”

[P55]
“Of course.”

[P56]
The official continued with a proud smile, like a resident of a Gangnam apartment showing off his building.

[P57]
“Provincial offices are generally built large and sturdy in preparation for wartime, but they aren’t normally this large.”

[P58]
“Then…?”

[P59]
“Have you already forgotten who lives here?”

[P60]
“Oh.”

[P61]
Right. He wasn’t merely the City Lord. He was a member of the imperial family. On top of that, he possessed an official royal title—a proper prince in his own right.

[P62]
“Then is this the royal palace?”

[P63]
“In a manner of speaking.”

[P64]
We continued moving, looking around like country bumpkins.

[P65]
Everywhere we looked, servants and maidservants hurried about their business, while elite soldiers with razor-sharp discipline stood guard or sparred in the training grounds.

[P66]
*They’re pretty good.*

[P67]
The most surprising thing was the remarkably high quality of the soldiers.

[P68]
Most of the soldiers standing guard were around Level 20, while the commanders wearing fairly impressive armor were comfortably above First Rate.

[P69]
*Well, it’s not as if there’s any reason they shouldn’t learn martial arts when they’re readily available.*

[P70]
If anything, it would make the army stronger. It was something that ought to be encouraged.

[P71]
I kept walking while glancing toward the training grounds.

[P72]
*Boom! Boom! Boom!*

[P73]
“Thrust!”

[P74]
“Argh!”

[P75]
It was noon, with the sun already high overhead.

[P76]
Hundreds of spearheads flashed in time with the drums, and the soldiers gathered and scattered in perfect unison, moving as one body.

[P77]
Watching them train in formations, tactics, and battle strategies, one word suddenly came to mind.

[P78]
*Raid team.*

[P79]
Uniform weapons. Coordination drilled into them through systematic training. In a large-scale battle, that kind of teamwork would display terrifying power.

[P80]
*Their individual skills might be inferior to those of Murim martial artists.*

[P81]
A battle of dozens against dozens might be another story, but if hundreds fought hundreds, or thousands fought thousands, even an ordinary Peak master couldn’t turn the tide by himself.

[P82]
That was the terrifying strength of a trained group.

[P83]
*Make up for inferior quality with numbers and training. Is that it?*

[P84]
It was just as one would expect from a unified empire that had ruled a vast territory for hundreds of years.

[P85]
Wasn’t that part of the reason those proud Murim martial artists acknowledged that they were subjects of a great nation?

[P86]
And yet…

[P87]
*What the hell are they keeping all this for? To trade it in for candy?*

[P88]
There were already more than several hundred soldiers in sight. If even a portion of them had been sent to northern Shanxi, the Red Wind Band would have made a run for it long ago.

[P89]
*Fuck. Some of us nearly died going through all that trouble.*

[P90]
Seeing the true face of incompetent public authority suddenly plunged me into a spell of hollow enlightenment.

[P91]
What good was owning the finest sword under heaven? If you didn’t draw it from its scabbard, it was no different from a club.

[P92]
Just as I was cursing them inwardly, the official spoke.

[P93]
“Well, we’re almost there.”

[P94]
He was right. At the end of a long corridor lined with dozens of pillars, a massive iron gate came into view, and anxious sighs escaped from both sides.

[P95]
“Phew…”

[P96]
“Whew. What do I do, Young Hero Jeong? I’m so nervous.”

[P97]
“Don’t worry. You have me.”

[P98]
“…What a fucking load of bullshit.”

[P99]
They say people destined to succeed will succeed, but I had no idea how those two had managed to hit it off in the middle of all this.

[P100]
*Maybe getting beaten together made them fall for each other?*

[P101]
*What kind of country is this?*

[P102]
Unable to hide my discomfort as a two-star general of the Singles Brigade, I heard Cheongpung ask brightly as he walked along with a light step.

[P103]
“Is the king inside?”

[P104]
King.

[P105]
At that single word, the young prodigies of the Five Gates of Shanxi gaped, while the official leading us leaped as though he had been stung by a bee.

[P106]
“A king? How impudent!”

[P107]
“Huh? Isn’t he a king?”

[P108]
“Of course he’s a king!”

[P109]
“Then wasn’t I right?”

[P110]
“No, that’s not what I mean…!”

[P111]
At this rate, one of two things would happen. The official would collapse from high blood pressure, or he would invoke treason and immediately summon the hundreds of soldiers training in the grounds.

[P112]
I wanted neither, so I stepped in to mediate.

[P113]
“First, calm down. And, Young Master Cheongpung.”

[P114]
“Yes, Benefactor.”

[P115]
“You can’t call him a king. You have to say ‘His Highness.’ Right?”

[P116]
The final question was directed at the official. He glared at Cheongpung and nodded furiously.

[P117]
“Absolutely! You must!”

[P118]
“Oh, really?”

[P119]
“Phew. Yes.”

[P120]
Cheongpung blinked his clear eyes.

[P121]
“Why?”

[P122]
“…Young Master Jin. Do we really have to take this fellow—or rather, this person—with us?”

[P123]
“I don’t mind leaving him out. But are you sure you’ll be all right?”

[P124]
The official fell silent for a moment.

[P125]
If he took five people without Cheongpung, he would be reprimanded by his superiors and lose his job. But if Cheongpung let his tongue slip just once, he might lose his head.

[P126]
A moment later, when he spoke again, his face looked ten years older.

[P127]
“…Let’s just go.”

[P128]
Cheongpung beamed.

[P129]
“Thank you. If we have time, I’ll put in a good word with the king—or rather, His Highness.”

[P130]
“Please, just keep that gentleman’s mouth shut.”

[P131]
The official proceeded to list every precaution we needed to take, along with his earnest pleas, and we finally reached the iron gate.

[P132]
The gate was so enormous and thick that it was almost absurd. From behind it came the sound of quiet voices.

[P133]
*Assistant Military Commissioner, Huashan, insult?*

[P134]
Those fragmentary words alone gave me no clue what kind of conversation was taking place. Still…

[P135]
*The atmosphere doesn’t seem very good.*

[P136]
I had a feeling this wasn’t the best place for people to sit across from one another over a meal.

[P137]
At that moment, a man standing at attention before the gate shouted loudly,

[P138]
“The young prodigies of Shanxi Murim request an audience!”

[P139]
*Groooan.*

[P140]
The iron gate began to open at the same time.

[P141]
The official gave me one final warning with a worried expression, stealing a sidelong glance at Cheongpung.

[P142]
“Please just keep that man’s mouth shut.”

[P143]
“…Ah. Yes.”

[P144]
He must have been extremely worried.

[P145]
* * *

[P146]
The moment we entered, it felt as though my eyes had brightened.

[P147]
The lavishly decorated grand hall was filled with a long table like the ones I had only seen in movies set in magic schools, along with every kind of dish imaginable.

[P148]
And the moment I saw the five people who had arrived ahead of us, only one thought crossed my mind.

[P149]
*We’re screwed.*

[P150]
When it came to reading the room, I was second to none. After spending so long scraping by as an F-rank Hunter, always watching everyone’s mood, I could read the room in 0.1 seconds.

[P151]
Just like now.

[P152]
*What a wonderful atmosphere.*

[P153]
The air around the five people was pulled taut.

[P154]
I had sensed that something was wrong from outside, but the reality was worse than I had expected.

[P155]
It was fortunate that everyone had come empty-handed because of the occasion. If anyone had been carrying so much as a weapon at their waist, someone would have drawn steel on the spot.

[P156]
“Well… Since we have guests, shall we end this reunion here?”

[P157]
The tense atmosphere was dispersed by a man’s delicate voice.

[P158]
Though was he really a man? His slender build was delicate enough to make him seem like a woman. His face was pale, and his lips were red as though they had been painted with dye.

[P159]
> **System**
>
> Level 22: Hong Jin

[P160]
He smiled at me.

[P161]
“You’re a strikingly handsome young prodigy, just as one would expect from the martial world. I heard a young hero from the Jin Family of Taiyuan was coming today. Might that be you…?”

[P162]
Now was the time for introductions. I performed a fist-and-palm salute toward the five men.

[P163]
“My name is Jin Taekyung of the Jin Family of Taiyuan.”

[P164]
The unpleasant atmosphere immediately eased somewhat. Surprise painted over the traces of displeasure and ridicule lingering on the other four faces.

[P165]
“If you’re Jin Taekyung of the Jin Family of Taiyuan…”

[P166]
A huge man dressed in black martial robes muttered.

[P167]
From the moment I first saw him, he had radiated tough-guy energy. His name was Li Feng, and the number 68 hovered above his head.

[P168]
*Is he affiliated with the military?*

[P169]
I couldn’t judge everything from a first meeting, but that was the impression he gave. A proud and upright soldier. That was my first impression of him.

[P170]
*Li Feng, Li Feng… At Level 68, he’s probably an advanced First Rate?*

[P171]
Just as I was engraving his name and Level into my mind, the other three men reacted.

[P172]
“Hm. That’s the Sleeping Dragon of Shanxi?”

[P173]
“He’s young. No, he’s a child.”

[P174]
“He doesn’t look particularly as incredible as the rumors claim…”

[P175]
The gazes fixed on me with apparent curiosity contained surprise, a hint of jealousy, and a subtle sense of superiority.

[P176]
In situations like this, there was usually no need to ask about the other person’s identity. They were the sort of people desperate to show off.

[P177]
“Apologies for the late introduction, Junior.”

[P178]
A sharp-eyed man grinned as he spoke to me. The other two had their arms folded as they looked at me like a cute little chick.

[P179]
*This is weirdly irritating.*

[P180]
What kind of people acted like my Seniors right off the bat?

[P181]
My question was answered soon enough.

[P182]
“Oh, you don’t know yet, do you? We came from Shaanxi. The Zhongnan Sect of Shaanxi—have you heard of it?”

[P183]
My mouth fell open before I knew it.

[P184]
“The Zhongnan Sect? *That* Zhongnan Sect?”

[P185]
The three men’s faces blossomed with smiles.

[P186]
“Haha! Look how surprised he is.”

[P187]
“Exactly.”

[P188]
“Perhaps you know our sect well?”

[P189]
I shouted, suddenly brimming with excitement.

[P190]
“I do! I know it very well! I had so much fun reading about it!”

[P191]
“We’re glad to hear you know us… Wait. What do you mean, ‘reading about it’?”

[P192]
“What else? Obviously, *The Reign…*”

[P193]
I stopped halfway through my answer.

[P194]
*Ah. This wasn’t a novel.*
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 139,
  "passed": true,
  "metrics": {
    "source_characters": 5994,
    "translation_characters": 13660,
    "length_ratio": 2.279,
    "source_paragraphs": 191,
    "translation_paragraphs": 193
  },
  "errors": [],
  "warnings": [
    {
      "code": "numbers",
      "message": "Arabic numerals from the source are absent",
      "details": {
        "values": [
          "0"
        ]
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "단전",
        "preferred": "dantian"
      }
    },
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
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "전세",
        "preferred": "jeonse lease"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "산서성",
        "preferred": "Shanxi Province"
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
