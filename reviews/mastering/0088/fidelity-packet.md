# Fidelity Gate — Chapter 88

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
  1|＃88화
  2|
  3|
  4|
  5|“아들?”
  6|
  7|나를 발견한 그녀의 눈이 크게 뜨인다. 음식점 상호명이 적힌 앞치마와 기름때 묻은 고무장갑을 낀 엄마. 우리 엄마.
  8|
  9|놀란 얼굴은 곧 당혹감으로 바뀌었다.
 10|
 11|“태, 태경이 네가 여긴 어떻게?”
 12|
 13|당황하는 엄마를 향해 씩 웃어 준 그때, 앙칼진 목소리가 귓가를 파고들었다.
 14|
 15|“그쪽이 김씨 아줌마 아들이야?”
 16|
 17|경계 어린 눈빛으로 나를 훑어보는 중년 여자.
 18|
 19|누군지, 뭐 하는 사람인지 물어볼 필요도 없다. 이미 이 여자의 정체를 알고 있으니까.
 20|
 21|“안녕하세요, 진태경이라고 합니다.”
 22|
 23|“어? 흠흠. 그래.”
 24|
 25|예의 바르게 허리까지 숙이는 내 모습에 괜한 헛기침을 내뱉은 사장이 물었다.
 26|
 27|“그런데 여기는 갑자기 어쩐 일로 왔어?”
 28|
 29|빙긋 웃으며 대답했다.
 30|
 31|“아들이 엄마 보러 오는데 이유가 필요한가요.”
 32|
 33|“이유?”
 34|
 35|사장의 눈매가 가늘어졌다.
 36|
 37|“젊은 사람이라 그런가 생각이 짧네. 이렇게 불쑥 찾아오면 사장인 내 기분은 어떻겠어?”
 38|
 39|“음. 기분 나쁘시겠죠.”
 40|
 41|“그래!”
 42|
 43|“점심시간이라 가게는 미어터지고, 주방이든 홀이든 눈코 뜰 새 없이 바쁘고.”
 44|
 45|“……그렇지.”
 46|
 47|“그런데 갑자기 직원 아들이 말도 없이 찾아왔다? 사장님 입장에서는 기분 나쁘실 수 있죠. 충분히 이해합니다.”
 48|
 49|“자, 잘 아네.”
 50|
 51|이 자식 뭐지? 지금 사장이 딱 그런 생각일 거다.
 52|
 53|혼란스러워하는 사장의 반응을 뒤로하고 엄마의 팔을 잡아당겼다.
 54|
 55|“그런 의미에서 저희는 이만 가 보겠습니다. 엄마, 옷 갈아입고 나가자.”
 56|
 57|“뭐?”
 58|
 59|“아, 아들?”
 60|
 61|당황하는 두 사람.
 62|
 63|나는 천연덕스러운 표정으로 물었다.
 64|
 65|“왜요?”
 66|
 67|“왜요라니, 왜요라니!”
 68|
 69|“혹시 무슨 문제라도?”
 70|
 71|“어린노무 자식이 어른을 갖고 놀아? 방금 했던 말은 다 까먹었어?”
 72|
 73|“아, 바쁜데 찾아오면 기분 나쁘실 거라고 한 거요?”
 74|
 75|“그래! 내 입장에서는 기분 나쁠 수도 있다고 네 입으로 말해 놓고 그걸 잊어? 너, 지금 사람 놀리는 거야?!”
 76|
 77|“어휴, 놀리긴요.”
 78|
 79|“그럼 뭐야?”
 80|
 81|“아까 했던 말은 진심입니다. 사장님 입장에서는 충분히 그럴 수 있죠. 그런데…….”
 82|
 83|나는 활짝 웃으며 말을 이었다.
 84|
 85|“우리 엄마, 이제 그쪽 직원 아니거든요.”
 86|
 87|“뭐?”
 88|
 89|“이해가 안 되세요? 때려치운다고요. 지금 이 순간부터.”
 90|
 91|무거운 침묵이 내려앉았다. 엄마는 멍하니 나만 바라봤고, 얼굴이 검붉은 색으로 변한 사장은 빽 소리쳤다.
 92|
 93|“누구 맘대로!”
 94|
 95|“우리 맘대로요.”
 96|
 97|“내가 이대로 보내 줄 줄 알아!”
 98|
 99|“안 보내 주면요?”
100|
101|“이, 이!”
102|
103|“삼, 삼! 사, 사!”
104|
105|딱 거기까지가 한계였다. 사장의 인내심은.
106|
107|“야, 이 개새끼야!”
108|
109|쌍욕과 함께 치켜올라 간 손은 목적을 달성하지 못했다.
110|
111|덥석.
112|
113|단번에 사장의 손목을 낚아챈 한 사람이 눈을 부릅떴다.
114|
115|엄마가 일류 고수도 찔끔할 정도로 살벌한 기세를 내뿜으며 씹어뱉었다.
116|
117|“누구 새끼 몸에 손을 대려고 해, 이 썅년이.”
118|
119|세상에, 아까 홀에 있을 때 한 번 듣긴 했지만 엄마가 욕하는 모습은 난생처음 본다. 자식 앞에서는 다른 사람 뒷담화도 안 하시는 분인데…….
120|
121|“그리고 뭔 새끼? 개새끼는 네 아들이 개새끼고. 이 돼지 같은 여자야!”
122|
123|“저게 아까부터 진짜! 야!”
124|
125|엄마에게로 달려드는 사장을 내가 가로막았다.
126|
127|나도 어딜 가도 눈에 띌 만큼 한 체격 한다. 두 중년 여성 사이에 가만히 서 있기만 해도 충분했다.
128|
129|“어허. 진정하세요, 진정.”
130|
131|“비켜, 안 비켜? 너희가 이러고도 무사할 것 같아!”
132|
133|“네, 등 따시고 배부르게 살 것 같은데요?”
134|
135|“으이이익!”
136|
137|눈이 뒤집힌 사장이 괴성과 함께 마구잡이로 팔을 휘두르기 시작했다. 물론 내게는 하나도 위협이 되지 않는 공격이었다.
138|
139|‘공격이라고 부르기도 민망하네.’
140|
141|게이트나 무림에서 상대한 적들을 생각하면 파리 날갯짓이나 다름없다. 근골, 근맥에 맷집까지 엄청나게 상승한 지금은 어지간한 성인 남성이 때린다 해도 간지러운 정도다.
142|
143|“그만하세요. 지금 엄청 힘들어 보이시는데.”
144|
145|예상대로 사장의 발악은 금방 끝났다.
146|
147|50대에 접어든 나이와 고도 비만에 이른 몸뚱어리에는 한계가 분명했으니까.
148|
149|“헉, 허억, 헌터라는 놈이 민간인을 핍박해?”
150|
151|이런 멘트를 칠 줄이야. 나는 사장의 뇌구조에 감탄했다.
152|
153|“제가요? 그쪽을?”
154|
155|“나 다친 거 안 보여? 손톱 부러져서 피 나잖아!”
156|
157|“그거야 아줌마가 나 때리다가 혼자 다친 거고. 전 여기 가만히 서 있기만 했는데 왜 혼자 부들부들 하세요.”
158|
159|“어쨌든!”
160|
161|이 정도면 지랄이 풍작이다. 슬쩍 주위를 둘러보니 주방 직원들은 물론이고 홀의 손님들도 질린 얼굴로 사장의 스탠딩 코미디를 바라보고 있었다.
162|
163|“뭐 납득 못 하겠으면 경찰 부르시든가요. 여기 증인 한 50명은 되니까 딱 좋네.”
164|
165|“…….”
166|
167|“안 불러요? 헌터 때문에 다쳐서 피 났으니까 경찰서 가서 조서 쓰고 고소도 하고, 변호사도 고용하셔야지. 내일부터 바빠지시겠네.”
168|
169|좀 더 놀려 주려고 했는데, 얘기를 하면 할수록 시간이 아까워진다. 나는 혀를 쯧쯧 찼다.
170|
171|“사장이 무슨 시장이라도 됩니까? 주변 사람들 피곤하게 하지 말고 심보 좀 곱게 써요. 그럼 이만 갑니다.”
172|
173|돌아서려던 그때였다. 분한 얼굴을 하고 있던 사장의 입꼬리가 비틀렸다.
174|
175|“너, 부천 산다며?”
176|
177|“그런데요.”
178|
179|“부천 어디 길드야?”
180|
181|“말하면 압니까?”
182|
183|“내 아들이 알지. 우리 민수도 부천에서 헌터 하거든.”
184|
185|“아, 그래요?”
186|
187|“듣자 하니 헌터들끼리는 한두 다리 건너면 다 아는 사이라며? 그 바닥에서 소문 안 좋게 나면 얼마나 버틸지 모르겠네.”
188|
189|“저 성실하고 실력 좋다고 소문났으니까 오래 버틸 겁니다. 됐어요?”
190|
191|“김민수 알아? 우리 아들 부천에서 유명할 텐데.”
192|
193|김민수? 알지. 지난 7년 동안 스쳐 지나간 민수만 서른 명이 넘을 거다. 나는 심드렁하게 대꾸했다.
194|
195|“성진호 아세요? 우리 고시원에서 제일 유명한데.”
196|
197|“풋, 고시원? F급 헌터라 그런가, 수준 알 만하네. 벌이가 그 정도로 시원찮아?”
198|
199|“걱정해 주셔서 참 감사하긴 한데…… 나름 시원시원하게 법니다. 어제도 40억 벌었고요.”
200|
201|“얼마?”
202|
203|“40억이요.”
204|
205|유치하게 돈 자랑까지 하고 싶진 않았는데, 기어이 잠자는 사자의 코털을 건드리는구나.
206|
207|그러나 한 가지 깜빡한 사실이 있었다. 사람들은 항상 자신이 가진 상식에서 모든 판단을 내린다는 것.
208|
209|“40억? F급 헌터가 저렇게 많이 벌어?”
210|
211|“당연히 허세지. 아는 헌터가 그러는데, F급이면 진짜 빡세게 해야 1억 정도 번다더라. 그리고 방금 못 들었어? 연봉이 아니라 어제 하루 만에 40억 벌었다고 한 거. 로또도 아니고 그게 말이 되냐?”
212|
213|“에이, 난 또 진짜인 줄 알았네.”
214|
215|홀의 손님들은 물론이고 은근히 나를 응원하는 기색이던 주방 직원들도 떨떠름한 눈빛으로 변했다.
216|
217|하긴, 내가 생각해도 허무맹랑한 이야기긴 하다.
218|
219|“아들, 사실이야?”
220|
221|눈을 동그랗게 뜬 엄마의 물음에 사장이 코웃음 쳤다.
222|
223|“퍽이나 사실이겠다. 우리 민수도 그렇게는 못 벌어.”
224|
225|“아까부터 궁금했는데, 그 유명하다는 민수 씨 등급이 어떻게 되세요? A급?”
226|
227|“D급 헌터야.”
228|
229|“…….”
230|
231|“왜, 너무 높아서 당황스러워?”
232|
233|“아니, 뭐…… 솔직히 당황스럽긴 하네요.”
234|
235|워낙 당당하게 말해서 몽키.D.민수 정도는 되는 줄 알았네.
236|
237|‘부천에 유명한 D급 헌터가 어디 있어.’
238|
239|순간 말문이 막힌 내 모습을 오해했는지 사장이 피식피식 비웃음을 흘린다.
240|
241|“우리 아들처럼 D급 헌터는 돼야 어디 가서 대접받고 살지. F급은 부끄러워서 말이나 할 수 있겠어?”
242|
243|“그렇게 부끄럽지는 않았는데요. 말도 잘했고.”
244|
245|“그래도 무시는 받겠지. 헌터들 사이에서는 등급이 깡패잖아.”
246|
247|“아, 예. 등급이 깡패죠.”
248|
249|“내 전화 한 통이면 민수가…….”
250|
251|“예, 예.”
252|
253|내가 건성으로 대답하며 주머니를 뒤적거리자 사장이 눈썹을 치켜뜬다.
254|
255|“이게 어른이 말하고 있는데. 우리 민수한테 혼나고 싶어?”
256|
257|“잠깐 찾을 게 있어서요. 아, 여기 있다.”
258|
259|“이게 뭔데?”
260|
261|“궁금하면 직접 보세요.”
262|
263|지갑에 포인트 카드며 할인 쿠폰이 너무 많아서 찾는 것도 일이다. 내가 건넨 얇은 은색 카드를 확인한 사장이 입을 벌렸다.
264|
265|“……C급 헌터?”
266|
267|“개인적으로는 헌터는 등급이 깡패라고 생각하는데, 사장님 생각은 어떠세요?”
268|
269|“마, 말도 안 돼. 분명히 F급이라고 들었는데…….”
270|
271|“F급이었죠. 지금은 C급이고. 정보 업데이트가 많이 느리시네.”
272|
273|“이, 이거 가짜 아니야? 우리 민수 자격증이랑 색깔이 완전히 다르잖아!”
274|
275|“그 자격증, 황동색이죠?”
276|
277|“…….”
278|
279|“저도 예전에 그거 썼어요. 하급 헌터들은 황동색, 중급 헌터들은 은색. 이건 모르셨나 보네.”
280|
281|곳곳에서 숨죽인 웃음이 터져 나왔다.
282|
283|한순간에 반전된 분위기. 엄마는 뿌듯한 미소를 지으며 내 팔짱을 꼈고, 사장은 벌겋게 달아오른 얼굴로 변명을 시작했다.
284|
285|“허, 헌터 등급이 중요해? C급이나 D급이나 겨우 한 단계 차이인데 거기서 거기지.”
286|
287|이게 말이야, 방구야. 말도 안 되는 발악을 보고 있자니 헛웃음밖에 안 나온다.
288|
289|“헌터 등급 가지고 사람 무시하던 사람이 할 말은 아닌 것 같은데.”
290|
291|“사람이 직급만 중요해? 회사가 어디인지가 더 중요하지. 중소기업 과장보다는 대기업 대리를 더 쳐주잖아. 내 말이 틀려?”
292|
293|“그건 모르겠고…… 일단 여기 계신 손님들은 동의 못 하시는 것 같은데요?”
294|
295|나는 홀을 꽉 채운 손님들을 가리켰다. 중소기업의 직장인 수십 명이 기분 나쁘다는 표정을 숨기지 않은 채로 사장을 노려보고 있었다.
296|
297|“저 아줌마 뭐야?”
298|
299|“아, 입맛 확 떨어지네.”
300|
301|“아직 음식도 안 나왔는데 그냥 갈까?”
302|
303|“그래, 가자. 가.”
304|
305|“다들 자리 옮기지. 요 앞에 백반집 괜찮은 곳 있어. 내가 대기업 대리는 못 돼도 중소기업 과장이니까 한 턱 쏜다.”
306|
307|드르륵.
308|
309|중년 아저씨의 한마디에 대여섯 명의 부하 직원들이 뒤따라 일어났다. 그런 광경이 홀 곳곳에서 벌어지고 있었다.
310|
311|“손님, 그게 아니고요. 손님!”
312|
313|“아니긴 뭐가 아닙니까. 내가 여기 다신 오나 봐라.”
314|
315|“지금 주문 들어갔는데 이렇게 가시면…….”
316|
317|“주방 꼴 보니까 한 시간은 걸릴 텐데, 뭘. 됐고, 저희도 이만 갑니다.”
318|
319|홀 직원들의 만류에도 사람들이 썰물처럼 빠져나갔다. 1분 남짓한 시간이 흐르자 홀에 남아 있는 손님은 열 명도 채 되지 않았다.
320|
321|‘크, 가게 망하는 소리가 벌써부터 들리는구나.’
322|
323|사장은 이미 분노와 당황으로 몸을 부들부들 떨고 있었다.
324|
325|“너, 너희들…….”
326|
327|“그래서 아드님이 어느 길드시라고요?”
328|
329|“우리 민수가 상동 길드에서도 아주 잘나가는 헌터야! 너 하나쯤은…….”
330|
331|“네? 어디요?”
332|
333|“상동 길드! 거기서 집도 주고 차도 주고.”
334|
335|“아, 상동 길드. 잠시만 기다려 보시겠어요?”
336|
337|이런 기막힌 우연이 있나. 웃음을 꾹꾹 참으며 스마트폰을 꺼내어 전화를 걸었다.
338|
339|뚜, 뚜, 뚜. 달칵.
340|
341|- 어, 어쩐 일로?
342|
343|“어쩐 일이긴, 우리가 일 있어야 연락하는 사이였어?”
344|
345|- ……약속한 40억은 보내 드렸는데요.
346|
347|“아, 그거 확인했지. 잘 받았어.”
348|
349|스피커 모드를 통해 이어지는 대화를 모든 사람이 들었다.
350|
351|40억. 앞서 했던 말이 사실임이 밝혀지자 하나같이 눈이 툭 튀어나온다. 나는 쏟아지는 시선을 무시하고 용건을 꺼냈다.
352|
353|“너 혹시 김민수라고 아냐?”
354|
355|- 김민수요? 처음 듣는 이름인데.
356|
357|“상동 길드 팀장이라는 놈이 그것도 몰라? 너희 길드 소속 D급 헌터래.”
358|
359|- ……널리고 널린 게 D급 헌턴데 제가 어떻게 압니까. 이것 때문에 전화하신 거예요?
360|
361|“응, 끊어.”
362|
363|돈 떼일까 봐 임창수의 명함을 받아 놓은 게 신의 한 수다.
364|
365|뚝, 전화를 끊자 사장이 더듬거리는 목소리로 묻는다.
366|
367|“누, 누구라고?”
368|
369|“못 들으셨어요? 상동 길드 팀장이에요. 쉽게 말하면 민수 씨 직장 상사.”
370|
371|“……팀장? 상사?”
372|
373|“아, 하나 더 추가하자면 민수 씨가 잘 보여야 할 미래의 고용주기도 하죠. 이 친구 아버지가 상동 길드 길드장이거든요.”
374|
375|“…….”
376|
377|백지장처럼 새하얘진 얼굴. 더 이상 말 섞을 이유도, 필요도 없다. 나는 엄마를 향해 고개를 돌렸다.
378|
379|“이제 가요.”
380|
381|“그럴까? 아들.”
382|
383|우리 엄마, 김정희 여사는 활짝 웃으며 작업복을 싱크대에 처박았다. 아, 물론 사장을 향한 한마디도 잊지 않았다.
384|
385|“부모면 부모답게 똑바로 살아. 이 아줌마야. 어디서 남의 귀한 자식을 함부로 입에 담아?”
386|
387|마지막 한 방.
388|
389|사장은 대답 대신 고개를 푹 숙였고, 우리는 가벼운 발걸음으로 가게를 빠져나왔다.
390|
391|“아들, 밥 먹었어? 집에 청국장이랑 김치전 있는데.”
392|
393|“이야, 진수성찬이네.”
394|
395|날씨 참 좋다.
```

## Assembled English

```markdown
[P1]
# Chapter 88

[P2]
“Son?”

[P3]
Her eyes widened when she saw me.

[P4]
She wore an apron printed with the restaurant’s name and rubber gloves smeared with grease.

[P5]
My mother.

[P6]
Her surprise quickly turned to bewilderment.

[P7]
“Ta-Taekyung, what are you doing here?”

[P8]
I flashed my flustered mother a broad grin. Just then, a shrill voice pierced my ear.

[P9]
“So you’re Kim ajumma’s[^1] son?”

[P10]
A middle-aged woman looked me over warily.

[P11]
There was no need to ask who she was or what she did. I already knew.

[P12]
“Hello. My name is Jin Taekyung.”

[P13]
“Huh? Ahem. Yes.”

[P14]
The owner gave an unnecessary cough after seeing me bow politely from the waist.

[P15]
“But what brings you here all of a sudden?”

[P16]
I answered with a pleasant smile.

[P17]
“Does a son need a reason to visit his mother?”

[P18]
“A reason?”

[P19]
The owner narrowed her eyes.

[P20]
“Maybe it’s because you’re young, but you’re awfully thoughtless. If someone showed up out of the blue like this, how do you think I’d feel as the owner?”

[P21]
“Hmm. I suppose you’d be upset.”

[P22]
“Exactly!”

[P23]
“It’s lunchtime, the restaurant is packed, and everyone in the kitchen and dining area is so busy they can barely see straight.”

[P24]
“…That’s right.”

[P25]
“And then an employee’s son suddenly shows up without saying a word? From your perspective, Boss, I can understand why you’d be upset. Completely.”

[P26]
“Y-you do understand.”

[P27]
*What the hell is with this kid?*

[P28]
That was probably exactly what the owner was thinking.

[P29]
Ignoring her confused reaction, I pulled my mother by the arm.

[P30]
“In that case, we’ll be going now. Mom, go change so we can leave.”

[P31]
“What?”

[P32]
“S-son?”

[P33]
The two of them stared at me in bewilderment.

[P34]
I asked with an innocent expression,

[P35]
“Why?”

[P36]
“What do you mean, why? Why?!”

[P37]
“Is there some kind of problem?”

[P38]
“You little punk, are you making fun of an adult? Did you already forget everything you just said?”

[P39]
“Oh, you mean when I said you might be upset if someone came by while you were busy?”

[P40]
“Yes! You said yourself that I might be upset, and now you’ve forgotten already? Are you making fun of me right now?!”

[P41]
“Oh, come on. I’m not making fun of you.”

[P42]
“Then what is this?”

[P43]
“I meant every word. From your perspective, Boss, you have every right to feel that way. But…”

[P44]
I continued with a bright smile.

[P45]
“My mother isn’t your employee anymore.”

[P46]
“What?”

[P47]
“Is that hard to understand? She’s quitting. Starting right now.”

[P48]
A heavy silence descended.

[P49]
My mother stared blankly at me, while the owner’s face turned dark red before she shrieked.

[P50]
“Who said you could do that?!”

[P51]
“We did.”

[P52]
“You think I’ll just let you take her away?”

[P53]
“What happens if you don’t?”

[P54]
“Y-you!”

[P55]
“Th-three, three! F-four, four!”

[P56]
That was as far as the owner’s patience went.

[P57]
“Hey, you fucking son of a bitch!”

[P58]
The hand she raised along with her vicious curse never reached its target.

[P59]
Grab!

[P60]
Someone caught the owner’s wrist in a single motion and glared at her.

[P61]
My mother spat the words out, radiating an aura fierce enough to make even a First Rate master flinch.

[P62]
“Whose son do you think you’re laying a hand on, you fucking bitch?”

[P63]
Good Lord.

[P64]
I had heard her swear once earlier in the dining area, but this was the first time in my life I had seen my mother curse like this. She never even spoke ill of other people in front of her children, and yet…

[P65]
“And who are you calling a son of a bitch? Your son is the son of a bitch, you pig!”

[P66]
“You’ve been getting on my nerves from the start! Hey!”

[P67]
The owner charged at my mother, but I stepped between them.

[P68]
I was big enough to stand out wherever I went. Simply standing between the two middle-aged women was more than enough.

[P69]
“Now, now. Calm down. Please calm down.”

[P70]
“Move! Are you going to move or not? Do you think you’ll get away with this?”

[P71]
“Yes. I think we’ll live quite comfortably.”

[P72]
“Gaaaah!”

[P73]
The owner’s eyes rolled back as she began wildly swinging her arms with a scream.

[P74]
Of course, none of her attacks posed the slightest threat to me.

[P75]
*It’s embarrassing to even call that an attack.*

[P76]
Compared to the enemies I had faced inside Gates and in the Murim, it was no more dangerous than a fly beating its wings. Now that my bones and muscles, Sinews and Meridians, and Toughness had all improved dramatically, even a punch from an ordinary adult man would only tickle.

[P77]
“Please stop. You look like you’re having a really hard time.”

[P78]
As expected, the owner’s struggle ended quickly.

[P79]
She was in her fifties and morbidly obese. Her body clearly had its limits.

[P80]
“Huff, huff! You Hunter bastard, are you bullying a civilian?”

[P81]
That she could come out with a line like that—I had to marvel at how the owner’s brain worked.

[P82]
“Me? Bullying you?”

[P83]
“Can’t you see I’m hurt? My fingernail broke, and it’s bleeding!”

[P84]
“You hurt yourself hitting me. I’ve just been standing here, so why are you trembling all by yourself?”

[P85]
“Whatever!”

[P86]
This was a bumper crop of bullshit.

[P87]
I glanced around. The kitchen staff and the customers in the dining area were all watching the owner’s stand-up routine with disgusted expressions.

[P88]
“If you can’t accept what happened, call the police. There must be about fifty witnesses here, so that works out nicely.”

[P89]
“…”

[P90]
“Not going to call? Since you were injured and bled because of a Hunter, you should go to the police station, give a statement, file a complaint, and hire a lawyer. You’ll be busy starting tomorrow.”

[P91]
I had intended to tease her a little longer, but the more we talked, the more I felt I was wasting my time. I clicked my tongue.

[P92]
“What are you, the mayor? You’re only the owner. Don’t make everyone around you miserable, and try to have a better attitude. We’re leaving.”

[P93]
I was about to turn away when the corners of the owner’s mouth twisted with resentment.

[P94]
“You live in Bucheon, don’t you?”

[P95]
“So?”

[P96]
“Which Guild in Bucheon are you with?”

[P97]
“Would you know it if I told you?”

[P98]
“My son would. Our Minsu is a Hunter in Bucheon, too.”

[P99]
“Oh, really?”

[P100]
“I hear Hunters all know one another after only a degree or two. I wonder how long you’ll last if you get a bad reputation in that line of work.”

[P101]
“I have a reputation for being hardworking and skilled, so I’ll be around for a long time. Happy?”

[P102]
“Do you know Kim Minsu? My son must be famous in Bucheon.”

[P103]
Kim Minsu?

[P104]
Sure. Over the past seven years, I had probably crossed paths with more than thirty people named Minsu.

[P105]
I answered indifferently.

[P106]
“Do you know Seong Jinho? He’s the most famous person in our goshiwon.[^2]”

[P107]
“Pfft, a goshiwon? I suppose that’s the level you’d expect from an F-rank Hunter. Is your income really that bad?”

[P108]
“It’s kind of you to worry, but I make a decent living. I made four billion won just yesterday.”

[P109]
“How much?”

[P110]
“Four billion won.”

[P111]
I hadn’t wanted to boast about money like a child, but she just had to tug on a sleeping lion’s nose hairs.

[P112]
There was one thing I had forgotten, though.

[P113]
People always judged everything according to their own common sense.

[P114]
“Four billion won? An F-rank Hunter made that much?”

[P115]
“Obviously, he’s bluffing. A Hunter I know said an F-rank Hunter has to work like hell to make even a hundred million won. And didn’t you hear him? He said he made four billion won in a single day, not in a year. It’s not like he won the lottery. Does that make any sense?”

[P116]
“Geez, I almost thought he was telling the truth.”

[P117]
The customers in the dining area and even the kitchen staff, who had quietly seemed to be rooting for me, began looking at me doubtfully.

[P118]
Well, even I had to admit it sounded absurd.

[P119]
“Son, is that true?”

[P120]
My mother’s eyes went round.

[P121]
The owner snorted.

[P122]
“As if it’s true. Even my Minsu can’t make that much.”

[P123]
“I’ve been wondering. What rank is this famous Minsu of yours? A-rank?”

[P124]
“He’s a D-rank Hunter.”

[P125]
“…”

[P126]
“What? Are you stunned because it’s so high?”

[P127]
“No, well… I’ll admit I’m a little surprised.”

[P128]
She had sounded so confident that I thought her son was at least Monkey D. Minsu.

[P129]
*Where is there a famous D-rank Hunter in Bucheon?*

[P130]
Perhaps she mistook my momentary silence for shock. The owner let out a series of derisive chuckles.

[P131]
“You have to be a D-rank Hunter like my son to get respect wherever you go. An F-rank Hunter must be too embarrassed to even admit what he does for a living.”

[P132]
“I wasn’t that embarrassed. I spoke just fine.”

[P133]
“You still get looked down on. Among Hunters, rank is everything.”

[P134]
“Ah, yes. Rank is everything.”

[P135]
“If I make one phone call, Minsu will…”

[P136]
“Yes, yes.”

[P137]
As I answered halfheartedly and rummaged through my pocket, the owner raised her eyebrows.

[P138]
“An adult is talking to you. Do you want my Minsu to teach you a lesson?”

[P139]
“I’m just looking for something. Ah, here it is.”

[P140]
“What is that?”

[P141]
“If you’re curious, take a look.”

[P142]
I had so many point cards and discount coupons in my wallet that finding anything was a chore. When the owner examined the thin silver card I handed her, her mouth fell open.

[P143]
“…C-rank Hunter?”

[P144]
“Personally, I think rank is everything for Hunters. What do you think, Boss?”

[P145]
“N-no way. I heard you were F-rank…”

[P146]
“I was F-rank. I’m C-rank now. You’re pretty slow about updating your information.”

[P147]
“I-isn’t this fake? The color is completely different from my Minsu’s license!”

[P148]
“His license is brass-colored, right?”

[P149]
“…”

[P150]
“I used one of those myself in the past. Lower-rank Hunters have brass-colored licenses, while mid-rank Hunters have silver ones. You didn’t know that?”

[P151]
Suppressed laughter erupted from all around us.

[P152]
The atmosphere had flipped in an instant.

[P153]
My mother slipped her arm through mine with a proud smile, while the owner’s face turned bright red and she began making excuses.

[P154]
“D-does a Hunter’s rank really matter? C-rank and D-rank are only one step apart. They’re practically the same.”

[P155]
*Was that supposed to be an argument or a fart?*

[P156]
All I could do was laugh hollowly at her absurd struggle.

[P157]
“That’s not something a person who looked down on someone for their Hunter rank should be saying.”

[P158]
“Is a person’s title all that matters? The company they work for matters more. People respect an Assistant Manager at a major corporation more than a section manager at a small company. Am I wrong?”

[P159]
“I don’t know about that, but the customers here don’t seem to agree with you.”

[P160]
I gestured toward the customers filling the dining area.

[P161]
Dozens of office workers from small and midsize companies were glaring at the owner without bothering to hide their displeasure.

[P162]
“What’s with that ajumma?”

[P163]
“My appetite’s completely gone.”

[P164]
“The food hasn’t even come out yet. Should we just leave?”

[P165]
“Yeah. Let’s go.”

[P166]
“Everyone, let’s eat somewhere else. There’s a decent set-meal place right up ahead. I may not be an Assistant Manager at a major corporation, but I’m a section manager at a small company, so lunch is on me.”

[P167]
Scrape.

[P168]
At the middle-aged man’s words, five or six of his subordinates stood and followed him.

[P169]
Similar scenes began unfolding throughout the dining area.

[P170]
“Customers, that’s not what I meant. Customers!”

[P171]
“What do you mean, it’s not? Just watch me never come back here.”

[P172]
“But your orders have already gone in. If you leave like this…”

[P173]
“Looking at that kitchen, it’ll take an hour anyway. Forget it. We’re leaving too.”

[P174]
Despite the dining staff’s attempts to stop them, the customers streamed out like the receding tide.

[P175]
Barely a minute later, fewer than ten customers remained in the dining area.

[P176]
*Damn. I can already hear the sound of this place going under.*

[P177]
The owner was trembling with anger and bewilderment.

[P178]
“You… You people…”

[P179]
“So which Guild did you say your son was with?”

[P180]
“Our Minsu is a real hotshot Hunter in Sangdong Guild! Someone like you…”

[P181]
“What? Which Guild?”

[P182]
“Sangdong Guild! They even gave him a house and a car.”

[P183]
“Oh, Sangdong Guild. Could you wait just a moment?”

[P184]
What an incredible coincidence.

[P185]
Holding back my laughter, I pulled out my smartphone and made a call.

[P186]
Beep. Beep. Beep. Click.

[P187]
“Uh, what is it?”

[P188]
“What do you mean, what is it? Are we only supposed to call each other when we have business?”

[P189]
“…I sent you the promised four billion won, though.”

[P190]
“Ah, I checked that. It came through fine.”

[P191]
The conversation continued over speakerphone, loud enough for everyone to hear.

[P192]
Four billion won.

[P193]
The moment it became clear that what I had said earlier was true, everyone’s eyes nearly popped out of their heads. I ignored all the stares and got to the point.

[P194]
“Do you happen to know a Kim Minsu?”

[P195]
“Kim Minsu? That’s the first I’ve heard of him.”

[P196]
“You’re a Team Leader in Sangdong Guild, and you don’t even know him? Apparently, he’s a D-rank Hunter in your Guild.”

[P197]
“D-rank Hunters are a dime a dozen. How am I supposed to know all of them? Is that why you called?”

[P198]
“Yeah. Bye.”

[P199]
Getting Im Changsoo’s business card in case he tried to stiff me had been a stroke of genius.

[P200]
Click.

[P201]
As soon as I hung up, the owner asked in a faltering voice.

[P202]
“W-who was that?”

[P203]
“Didn’t you hear? He’s a Team Leader in Sangdong Guild. Put simply, he’s Mr. Minsu’s boss.”

[P204]
“…Team Leader? His boss?”

[P205]
“Oh, and one more thing. He’s also a future employer Mr. Minsu will want to impress. His father is the Guild Master of Sangdong Guild.”

[P206]
“…”

[P207]
Her face went white as a sheet.

[P208]
There was no longer any reason or need to exchange another word with her. I turned toward my mother.

[P209]
“Let’s go now.”

[P210]
“Shall we, son?”

[P211]
My mother, Kim Jeonghee, flashed a broad smile and shoved her work clothes into the sink.

[P212]
Of course, she didn’t forget to leave the owner with one final remark.

[P213]
“If you’re a parent, act like one and live right, you ajumma. Where do you get off casually running your mouth about someone else’s precious child?”

[P214]
The final blow.

[P215]
The owner lowered her head without answering, and we left the restaurant with light steps.

[P216]
“Son, have you eaten? There’s cheonggukjang and kimchi pancakes at home.”

[P217]
“Wow. What a feast.”

[P218]
The weather was beautiful.

[P219]
[^1]: *Ajumma* is a familiar Korean term for a married or middle-aged woman, commonly used by customers or employers to address service workers.

[P220]
[^2]: A *goshiwon* is a tiny, inexpensive room-for-rent housing arrangement, often with shared facilities.
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
# Chapter 88

[P2]
“Son?”

[P3]
Her eyes widened when she saw me.

[P4]
My mother was wearing an apron with the restaurant’s name printed on it and a pair of rubber gloves smeared with grease.

[P5]
My mother.

[P6]
Her surprised expression soon turned to bewilderment.

[P7]
“Ta-Taekyung, what are you doing here?”

[P8]
I gave my flustered mother a broad grin. That was when a shrill voice pierced my ear.

[P9]
“So you’re the son of Kim ajumma[^2]?”

[P10]
A middle-aged woman was looking me over warily.

[P11]
There was no need to ask who she was or what she did. I already knew.

[P12]
“Hello. My name is Jin Taekyung.”

[P13]
“Huh? Ahem. Yes.”

[P14]
The owner gave an unnecessary cough after seeing me bow politely from the waist.

[P15]
“But what brings you here all of a sudden?”

[P16]
I answered with a pleasant smile.

[P17]
“Does a son need a reason to visit his mother?”

[P18]
“A reason?”

[P19]
The owner narrowed her eyes.

[P20]
“Maybe it’s because you’re young, but you’re awfully thoughtless. If someone showed up out of the blue like this, how would you feel if you were the owner?”

[P21]
“Hmm. I suppose I’d be upset.”

[P22]
“Exactly!”

[P23]
“It’s lunchtime, the restaurant is packed, and everyone in the kitchen and dining area is so busy they can barely see straight.”

[P24]
“…That’s right.”

[P25]
“And then an employee’s son suddenly shows up without saying a word? From your perspective, Boss, I can understand why you’d be upset. Completely.”

[P26]
“Y-you do understand.”

[P27]
*What the hell is this kid?*

[P28]
That was probably exactly what the owner was thinking.

[P29]
Ignoring her confused reaction, I grabbed my mother by the arm.

[P30]
“In that case, we’ll be going now. Mom, go change so we can leave.”

[P31]
“What?”

[P32]
“S-son?”

[P33]
The two of them stared at me in bewilderment.

[P34]
I asked with an innocent expression,

[P35]
“Why?”

[P36]
“What do you mean, why? Why?!”

[P37]
“Is there some kind of problem?”

[P38]
“You little punk, are you making fun of an adult? Did you already forget everything you just said?”

[P39]
“Oh, you mean when I said you might be upset if someone came by while you were busy?”

[P40]
“Yes! You said yourself that I might be upset, and now you’ve forgotten already? Are you making fun of me right now?!”

[P41]
“Oh, come on. I’m not making fun of you.”

[P42]
“Then what is this?”

[P43]
“What I said before was sincere. From your perspective, Boss, you had every right to feel that way. But…”

[P44]
I continued with a bright smile.

[P45]
“My mother isn’t your employee anymore.”

[P46]
“What?”

[P47]
“Is that hard to understand? She’s quitting. Starting right now.”

[P48]
A heavy silence settled over the restaurant.

[P49]
My mother stared at me blankly, while the owner’s face turned dark red before she shrieked,

[P50]
“Who said you could do that?!”

[P51]
“We did.”

[P52]
“You think I’ll just let you take her away?”

[P53]
“What happens if you don’t?”

[P54]
“Y-you!”

[P55]
“T-three, three! F-four, four!”

[P56]
That was as far as the owner’s patience went.

[P57]
“Hey, you fucking son of a bitch!”

[P58]
The hand she raised along with her vicious curse never reached its target.

[P59]
Grab!

[P60]
Someone caught the owner’s wrist in a single motion and glared at her.

[P61]
My mother spat the words out with an aura fierce enough to make even a First Rate master flinch.

[P62]
“Whose son do you think you’re laying a hand on, you fucking bitch?”

[P63]
Good Lord.

[P64]
I had heard her swear once earlier in the dining area, but this was the first time in my life I had seen my mother curse like this. She never even spoke ill of other people in front of her children, and yet…

[P65]
“And who are you calling a son of a bitch? Your son is the son of a bitch, you pig!”

[P66]
“You’ve been getting on my nerves from the start! Hey!”

[P67]
The owner charged at my mother, but I stepped in front of her.

[P68]
I was big enough to stand out wherever I went. Simply standing between the two middle-aged women was more than enough.

[P69]
“Now, now. Calm down. Please calm down.”

[P70]
“Move! Are you going to move or not? Do you think you’ll get away with this?”

[P71]
“Yes. I think we’ll live quite comfortably.”

[P72]
“Gaaaah!”

[P73]
The owner’s eyes rolled back as she began wildly swinging her arms with a scream.

[P74]
Of course, none of her attacks posed the slightest threat to me.

[P75]
*Calling that an attack is embarrassing.*

[P76]
Compared to the enemies I had faced in Gates and the Murim, her attacks were no more dangerous than the fluttering of a fly’s wings. With my bones, muscles, tendons, and ability to take a hit all dramatically enhanced, even a punch from an ordinary adult man would only tickle.

[P77]
“Please stop. You look like you’re having a really hard time.”

[P78]
As expected, the owner’s struggle ended quickly.

[P79]
She was now in her fifties and morbidly obese; her body clearly had its limits.

[P80]
“Huff, huff! You Hunter bastard, are you bullying a civilian?”

[P81]
That she could come out with a line like that—I had to marvel at how the owner’s brain worked.

[P82]
“Me? Bullying you?”

[P83]
“Can’t you see that I’m hurt? My fingernail broke and it’s bleeding!”

[P84]
“You hurt yourself hitting me. I’ve just been standing here, so why are you shaking all by yourself?”

[P85]
“Whatever!”

[P86]
This was a bumper crop of bullshit.

[P87]
I glanced around. The kitchen employees, along with the customers in the dining area, were watching the owner’s stand-up routine with exhausted expressions.

[P88]
“If you can’t accept what happened, call the police. There must be about fifty witnesses here, so that should work out nicely.”

[P89]
“…”

[P90]
“Not going to call? Since you were injured and bled because of a Hunter, you should go to the police station, give a statement, file a complaint, and hire a lawyer. You’ll be busy starting tomorrow.”

[P91]
I had intended to tease her a little longer, but the more we talked, the more I felt my time slipping away. I clicked my tongue.

[P92]
“What are you, the mayor? You’re only the owner. Don’t make everyone around you miserable, and try to have a better attitude. We’re leaving.”

[P93]
I was about to turn around when the owner, her face twisted with resentment, crooked her lips.

[P94]
“You live in Bucheon, don’t you?”

[P95]
“So?”

[P96]
“Which Guild in Bucheon are you with?”

[P97]
“Would it mean anything if I told you?”

[P98]
“My son would know. Our Minsu is a Hunter in Bucheon, too.”

[P99]
“Oh, really?”

[P100]
“I hear Hunters all know one another after only a degree or two. I wonder how long you’ll last if you get a bad reputation in that line of work.”

[P101]
“I have a reputation for being hardworking and skilled, so I’ll be around for a long time. Happy?”

[P102]
“Do you know Kim Minsu? My son must be famous in Bucheon.”

[P103]
Kim Minsu?

[P104]
Of course I knew him. Over the past seven years, I had probably crossed paths with more than thirty people named Minsu.

[P105]
I answered indifferently,

[P106]
“Do you know Seong Jinho? He’s the most famous person in our goshiwon.[^1]”

[P107]
“Pfft, a goshiwon? I suppose that’s the level you’d expect from an F-rank Hunter. Is business really that bad?”

[P108]
“It’s kind of you to worry, but I make a decent living. I made four billion won just yesterday.”

[P109]
“How much?”

[P110]
“Four billion won.”

[P111]
I hadn’t wanted to boast about money like a child, but she just had to tug on a sleeping lion’s nose hairs.

[P112]
There was one thing I had forgotten, though.

[P113]
People always made their judgments based on the common sense they possessed.

[P114]
“Four billion won? An F-rank Hunter made that much?”

[P115]
“Obviously, he’s bluffing. A Hunter I know said an F-rank Hunter has to work like hell to make even a hundred million won. And did you hear him? He said he made four billion won in a single day, not in a year. It’s not like he won the lottery. Does that make any sense?”

[P116]
“Geez, I almost thought he was telling the truth.”

[P117]
The customers in the dining area, along with the kitchen employees who had quietly seemed to be rooting for me, began looking at me doubtfully.

[P118]
Well, even I had to admit it sounded absurd.

[P119]
“Son, is that true?”

[P120]
My mother’s eyes went round.

[P121]
The owner snorted.

[P122]
“As if it’s true. Even my Minsu can’t make that much.”

[P123]
“I’ve been wondering. What rank is this famous Minsu of yours? A-rank?”

[P124]
“He’s a D-rank Hunter.”

[P125]
“…”

[P126]
“What? Is that too high for you to believe?”

[P127]
“No, well… I’ll admit I’m a little surprised.”

[P128]
She had sounded so confident that I had thought her son was at least Monkey D. Minsu.

[P129]
*Where is there a famous D-rank Hunter in Bucheon?*

[P130]
Perhaps she mistook my momentary silence for shock. The owner let out a series of derisive chuckles.

[P131]
“A D-rank Hunter like my son is the kind of person who gets respect wherever he goes. An F-rank Hunter must be too embarrassed to even admit what he does for a living.”

[P132]
“I wasn’t that embarrassed. I spoke just fine.”

[P133]
“You still get looked down on. Among Hunters, rank is everything.”

[P134]
“Ah, yes. Rank is everything.”

[P135]
“If I make one phone call, Minsu will…”

[P136]
“Yes, yes.”

[P137]
As I answered halfheartedly and rummaged through my pocket, the owner raised her eyebrows.

[P138]
“An adult is talking to you. Do you want my Minsu to teach you a lesson?”

[P139]
“I’m just looking for something. Ah, here it is.”

[P140]
“What is that?”

[P141]
“If you’re curious, take a look.”

[P142]
I had so many point cards and discount coupons in my wallet that finding anything was a chore. When the owner examined the thin silver card I handed her, her mouth fell open.

[P143]
“…C-rank Hunter?”

[P144]
“Personally, I think rank is everything for Hunters. What do you think, Boss?”

[P145]
“N-no way. I heard you were F-rank…”

[P146]
“I was F-rank. I’m C-rank now. You’re pretty slow when it comes to getting updated information.”

[P147]
“I-isn’t this fake? The color is completely different from my Minsu’s license!”

[P148]
“His license is brass-colored, right?”

[P149]
“…”

[P150]
“I used one of those myself in the past. Lower-rank Hunters have brass-colored licenses, while mid-rank Hunters have silver ones. You didn’t know that?”

[P151]
Suppressed laughter erupted from all around us.

[P152]
The atmosphere had flipped in an instant.

[P153]
My mother slipped her arm through mine with a proud smile, while the owner’s face turned bright red and she began making excuses.

[P154]
“D-does a Hunter’s rank really matter? C-rank and D-rank are only one step apart. They’re practically the same.”

[P155]
*What kind of logic was that supposed to be?*

[P156]
All I could do was give a hollow laugh at her absurd struggle.

[P157]
“That’s not something a person who looked down on someone for their Hunter rank should be saying.”

[P158]
“Are titles all that matter? The company you work for matters more. People respect an assistant manager at a major corporation more than a section manager at a small company. Am I wrong?”

[P159]
“I don’t know about that, but the customers here don’t seem to agree with you.”

[P160]
I gestured toward the customers filling the dining area.

[P161]
Dozens of office workers from small and midsize companies were glaring at the owner without bothering to hide their displeasure.

[P162]
“What’s with that ajumma?”

[P163]
“My appetite’s completely gone.”

[P164]
“The food hasn’t even come out yet. Should we just leave?”

[P165]
“Yeah. Let’s go.”

[P166]
“Everyone, move tables. There’s a decent set-meal place right up ahead. I may not be an assistant manager at a major corporation, but I’m a section manager at a small business, so lunch is on me.”

[P167]
Scrape.

[P168]
At the middle-aged man’s words, five or six of his subordinates stood and followed him.

[P169]
Similar scenes began unfolding throughout the dining area.

[P170]
“Customers, that’s not what happened. Customers!”

[P171]
“What do you mean, it’s not? Just watch me never come back here.”

[P172]
“But your orders have already gone in. If you leave like this…”

[P173]
“Looking at that kitchen, it’ll take an hour anyway. Enough. We’re leaving.”

[P174]
Despite the dining staff’s attempts to stop them, the customers streamed out like the tide going out.

[P175]
After barely a minute had passed, fewer than ten customers remained in the dining area.

[P176]
*Damn. I can already hear the sound of this place going under.*

[P177]
The owner was trembling with anger and bewilderment.

[P178]
“You… You people…”

[P179]
“So which Guild did your son say he was with?”

[P180]
“Our Minsu is one of the top Hunters in Sangdong Guild! Someone like you…”

[P181]
“What? Which Guild?”

[P182]
“Sangdong Guild! They even gave him a house and a car.”

[P183]
“Oh, Sangdong Guild. Could you wait just a moment?”

[P184]
What an incredible coincidence.

[P185]
Holding back my laughter, I pulled out my smartphone and made a call.

[P186]
Beep. Beep. Beep. Click.

[P187]
“Uh, what is it?”

[P188]
“Were we only supposed to call each other when we had business?”

[P189]
“…I sent you the promised four billion won, though.”

[P190]
“Ah, I checked that. It came through fine.”

[P191]
The entire conversation continued over speakerphone, loud enough for everyone to hear.

[P192]
Four billion won.

[P193]
The moment it became clear that what I had said earlier was true, everyone’s eyes seemed ready to pop out of their heads. I ignored all the attention and got to the point.

[P194]
“Do you happen to know a Kim Minsu?”

[P195]
“Kim Minsu? That’s the first I’ve heard of him.”

[P196]
“You’re a Team Leader in Sangdong Guild and you don’t even know that? They say he’s a D-rank Hunter in your Guild.”

[P197]
“D-rank Hunters are a dime a dozen. How would I know all of them? Is that why you called?”

[P198]
“Yeah. Bye.”

[P199]
Taking Im Changsoo’s business card in case he tried to stiff me had been a stroke of genius.

[P200]
Click.

[P201]
As soon as I hung up, the owner asked in a faltering voice,

[P202]
“W-who was that?”

[P203]
“Didn’t you hear? He’s the Team Leader of Sangdong Guild. In simple terms, he’s Mr. Minsu’s boss.”

[P204]
“…Team Leader? His boss?”

[P205]
“Oh, and one more thing. He’s also a future employer Mr. Minsu will want to impress. His father is the Guild Master of Sangdong Guild.”

[P206]
“…”

[P207]
Her face went white as a sheet.

[P208]
There was no longer any reason or need to exchange another word with her. I turned toward my mother.

[P209]
“Let’s go now.”

[P210]
“Should we, son?”

[P211]
My mother, Kim Jeonghee, flashed a broad smile and shoved her work clothes into the sink.

[P212]
Of course, she didn’t forget to leave the owner with one final remark.

[P213]
“Live like a parent should, you ajumma. Where do you get off casually running your mouth about someone else’s precious child?”

[P214]
That was the final blow.

[P215]
The owner lowered her head without answering, and we left the restaurant with light steps.

[P216]
“Son, have you eaten? There’s cheonggukjang and kimchi pancakes at home.”

[P217]
“Wow. What a feast.”

[P218]
The weather was beautiful.

[P219]
[^1]: A *goshiwon* is a tiny, inexpensive room-for-rent housing arrangement, often with shared facilities.

[P220]
[^2]: *Ajumma* is a familiar Korean term for a married or middle-aged woman, commonly used by customers or employers to address service workers.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 임창수    | **Im Changsoo**   |
| 일류     | **First Rate**    |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 성진호 | **Seong Jinho** |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 88,
  "passed": true,
  "metrics": {
    "source_characters": 6205,
    "translation_characters": 14015,
    "length_ratio": 2.259,
    "source_paragraphs": 197,
    "translation_paragraphs": 220
  },
  "errors": [],
  "warnings": [
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
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "갑자",
        "preferred": "jiazi"
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
